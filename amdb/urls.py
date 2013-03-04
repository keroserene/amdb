from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'amdb.views.index', name='index'),

  # Uncomment the admin/doc line below to enable admin documentation:
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/$', include(admin.site.urls), name='admin'),

  # Data examination pages
  url(r'^observation/(?P<id>\d+)/$', 'amdb.views.examine', {'cls': 'observation'}, name='observation'),
  url(r'^assertion/(?P<id>\d+)/$', 'amdb.views.examine', {'cls': 'assertion'},  name='assertion'),
  url(r'^capability/(?P<id>\d+)/$', 'amdb.views.examine', {'cls': 'capability'}, name='capability'),

  # Data editing / creation pages
  url(r'^(?P<cls>\w+)/(?P<id>\d+)/edit$', 'amdb.views.edit', name='edit'),
  url(r'^(?P<cls>\w+)/new$', 'amdb.views.new', name='new'),

  url(r'^nuke/$', 'amdb.views.nuke', name='nuke'),
  url(r'^nuke/yes$', 'amdb.views.nuke_fo_realz', name='nuke_fo_realz'),
)
