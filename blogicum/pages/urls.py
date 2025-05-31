from django.urls import include, path
from django.views.generic.base import TemplateView
import debug_toolbar

app_name = 'pages'


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('about/', TemplateView.as_view(template_name='pages/about.html'),
         name='about'),
    path('rules/', TemplateView.as_view(template_name='pages/rules.html'),
         name='rules'),
]
