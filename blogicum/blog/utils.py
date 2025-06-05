from blog.constants import DEFAULT_NUM_PAGE, POSTS_ON_PAGE
from blog.models import Post
from django.core.paginator import Paginator, Page
from django.db.models import Count
from django.utils import timezone
from django.http import HttpRequest
from django.db import models


def posts_pagination(
    request: HttpRequest,
    queryset: models.QuerySet,
    per_page: int = POSTS_ON_PAGE,
    page_key: str = 'page',
    default_page: int = DEFAULT_NUM_PAGE
) -> Page:
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get(page_key, default_page)
    return paginator.get_page(page_number)


def query_post(
        manager=Post.objects,
        filters=True,
        with_comments=True
):
    queryset = manager.select_related('author', 'location', 'category')
    if filters:
        queryset = queryset.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        )
    if with_comments:
        queryset = annotate(queryset)
    return queryset.order_by('-pub_date')


def annotate(queryset):
    """Аннотации количества комментариев к постам"""
    return queryset.annotate(comment_count=Count('comments'))
