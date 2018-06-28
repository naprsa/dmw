from __future__ import absolute_import, print_function, unicode_literals
# from django.conf import settings
from django.conf.urls import url, patterns
from .views import HotelListView, HotelDetailView

urlpatterns = patterns('',
                       url(r'^$', HotelListView.as_view(), name='hotels'),
                       url(r'^(?P<slug>[^/]+)/$', HotelDetailView.as_view(), name='hotel_detail'),
                       )
