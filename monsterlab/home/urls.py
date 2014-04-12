from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib import admin
from login.views import register,login,logout,forget_password,changepassword
from ordinaryUser.views import ordinaryuser
admin.autodiscover()
from news.models import News
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monsterlab.views.home', name='home'),
    # url(r'^monsterlab/', include('monsterlab.foo.urls')),
    url(r'^$',TemplateView.as_view(template_name="index.html")),
    url(r'^contact',TemplateView.as_view(template_name="contact.html")),
    url(r'^member',TemplateView.as_view(template_name="member.html")),
    url(r'^about',TemplateView.as_view(template_name="about.html")),
    url(r'^index',TemplateView.as_view(template_name="index.html")),
    url(r'^honor',TemplateView.as_view(template_name="honor.html")),
    url(r'^news.html',ListView.as_view(
        queryset=News.objects.order_by('-id')[:5],
        context_object_name='newslist',
        template_name="news.html"),
        ),
    url(r'^(?P<pk>\d+)$',
        DetailView.as_view(
            model=News,
            template_name='show_news.html'),
            name='show'),
    url(r'^login',login),
    url(r'^register',register),
    url(r'^logout',logout),
    url(r'^forget',forget_password),
    url(r'^changpassword',changepassword),
    url(r'^user',ordinaryuser),
    
   # (r'^site_static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
)
