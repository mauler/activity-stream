from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'act.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^activity/', include('actstream.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
