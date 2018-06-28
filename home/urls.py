from __future__ import absolute_import, print_function, unicode_literals
from django.conf.urls import url, patterns
from .views import HomeView

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='Home'),
                       # url(r'^send_mail/$', HomeView.as_view(), name='send_mail'),
                       )
