from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', ),
    url(r'^$', 'subs.views.timeline', name='timeline'),
    url(r'^user/(?P<username>[a-zA-Z0-9_.-]+)/', 'subs.views.user_timeline', name='user_timeline'),
    url(r'^unfollow/(?P<username>[a-zA-Z0-9_.-]+)/', 'subs.views.unfollow_user', name='unfollow'),
    url(r'^follow/(?P<username>[a-zA-Z0-9_.-]+)/', 'subs.views.follow_user', name='follow'),
    ('^activity/', include('actstream.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
