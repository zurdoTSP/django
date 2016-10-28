from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView, CreateView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rebsocial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^control/',include('control.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)
