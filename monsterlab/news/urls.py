from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView,ListView,DetailView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from news.models import News
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monsterlab.views.home', name='home'),
    # url(r'^monsterlab/', include('monsterlab.foo.urls')),
    # url(r'^$',TemplateView.as_view(template_name="index.html")),
#     url(r'login',views.login),
 #      url(r'index',views.index)
    url(r'html$',
        ListView.as_view(
            queryset=News.objects.order_by('-id')[:3],
            context_object_name='newslist',
            template_name='news.html'),
         ),
    url(r'^(?P<pk>\d+)$',
        DetailView.as_view(
            model=News,
            template_name='show_news.html'),
        name='show'),

  #    url(r'^home$',TemplateView.as_view(template_name="text_app/home.html")),
    # (r'^site_static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
)
