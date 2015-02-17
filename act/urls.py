from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', ),
    url(r'^user/(?P<username>[a-zA-Z0-9_.-]+)/', 'subs.views.user_timeline', name='user_timeline'),
    ('^activity/', include('actstream.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
