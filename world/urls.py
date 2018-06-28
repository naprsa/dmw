from __future__ import absolute_import, print_function, unicode_literals
# from django.conf import settings
from django.conf.urls import url, patterns
from .views import PlatformListView, PlatformDetailView

urlpatterns = patterns('',
                       url(r'^$', PlatformListView.as_view(), name='platforms'),
                       url(r'^(?P<slug>[^/]+)/$', PlatformDetailView.as_view(),
                           name='platform_detail'),
                       )
