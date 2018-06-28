from __future__ import absolute_import, print_function, unicode_literals
# from django.conf import settings
from django.conf.urls import url, patterns
from .views import DestinationListView, DestinationDetailView

urlpatterns = patterns('',
                       url(r'^$', DestinationListView.as_view(),
                           name='destinations'),
                       url(r'^(?P<slug>[^/]+)/$', DestinationDetailView.as_view(),
                           name='destination_detail'),
                       )
