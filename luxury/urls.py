from __future__ import absolute_import, print_function, unicode_literals
# from django.conf import settings
from django.conf.urls import url, patterns
from .views import LuxuryListView, LuxuryDetailView

urlpatterns = patterns('',
                       url(r'^$', LuxuryListView.as_view(), name='luxury'),
                       url(r'^(?P<slug>[^/]+)/$', LuxuryDetailView.as_view(),
                           name='luxury_detail'),
                       )
