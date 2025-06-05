from blog.models import Post
from django.core.paginator import Paginator
from django.db.models import Count
from django.utils import timezone


def get_page_from_paginator(paginator, page_number):
    return paginator.get_page(page_number)


def posts_pagination(request, query_set, per_page=10):
    paginator = Paginator(query_set, per_page)
    page_number = request.GET.get('page')
    return get_page_from_paginator(paginator, page_number)


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
    return queryset


def annotate(queryset):
    """Аннотации количества комментариев к постам"""
    return queryset.annotate(
        comment_count=Count('comments')
    ).order_by('-pub_date')
