from django.urls import path

from .views import AboutPageView, RulesPageView

app_name = 'pages'

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('rules/', RulesPageView.as_view(), name='rules'),
]
