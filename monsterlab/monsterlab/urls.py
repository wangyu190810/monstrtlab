from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from news.models import News
admin.autodiscover()
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monsterlab.views.home', name='home'),
    # url(r'^monsterlab/', include('monsterlab.foo.urls')),
 #   url(r'^$',TemplateView.as_view(template_name="index.html")),
 #   url(r'^login',TemplateView.as_view(template_name="login.html")),
 #   url(r'^contact.html$',TemplateView.as_view(template_name="contact.html")),
 #   url(r'^member',TemplateView.as_view(template_name="member.html")),
 #   url(r'^register',TemplateView.as_view(template_name="register.html")),
 #   url(r'^about',TemplateView.as_view(template_name="about.html")),
 #   url(r'^index.html$',TemplateView.as_view(template_name="index.html")),
 #   url(r'^honor',TemplateView.as_view(template_name="honor.html")),
 #   url(r'^news',ListView.as_view(queryset=News.objects.order_by('-id')[:3]
 #                                   ,context_object_name='news_list',
 #                              template_name="news.html"),
 #                               name='news'),
   #Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#   url(r'^new/$',include('news.urls',namespace='new',app_name='news')),
   url(r'^',include('home.urls',namespace='home',app_name='home')),

  #  url(r'^news',"news.views.news"),
  #ng@mint ~/workspace/web/monstrelab $ 
  # url(r'^(?P<pk>\d+)$',
   #     DetailView.as_view(
   #         model=News,
    #        template_name='show_news.html'),
    #        name='show_news'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'weblog/',include('zinnia.urls')),
    url(r'comments/',include('django.contrib.comments.urls')),

   #url(r'^news',include('news.urls')),
  # url(r'^$',)
  # url(r'text_app2/',include('text_app2.urls')),
     (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
)

