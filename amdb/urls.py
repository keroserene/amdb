from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # Examples:
  url(r'^$', 'amdb.views.index', name='index'),
  # url(r'^amdb/', include('amdb.foo.urls')),
  # Uncomment the admin/doc line below to enable admin documentation:
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  # Uncomment the next line to enable the admin:
  url(r'^admin/$', include(admin.site.urls), name='admin'),

  url(r'^observation/(?P<observation_id>\d+)/edit$', 'amdb.views.observation', {'edit': 'True'}, name='edit-obs'),

  url(r'^(?P<edit_type>\w+)/(?P<edit_id>\d+)/edit$', 'amdb.views.edit', name='edit'),

  url(r'^observation/(?P<observation_id>\d+)$', 'amdb.views.observation', name='done'),

  url(r'^observation/(?P<observation_id>\d+)/$', 'amdb.views.observation', name='observation'),
  url(r'^assertion/(?P<assertion_id>\d+)/$', 'amdb.views.assertion', name='assertion'),
  url(r'^capability/(?P<capability_id>\d+)/$', 'amdb.views.capability', name='capability'),

  url(r'^nuke/$', 'amdb.views.nuke', name='nuke'),
)
