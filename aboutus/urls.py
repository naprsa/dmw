from __future__ import absolute_import, print_function, unicode_literals
# from django.conf import settings
from django.conf.urls import url, patterns
from .views import TeamView, StoryView, MissionVisionView

urlpatterns = patterns('',
                       url(r'^d-team/$', TeamView.as_view(), name='about_team'),
                       url(r'^d-story/$', StoryView.as_view(), name='about_story'),
                       url(r'^mission-vision/$',
                           MissionVisionView.as_view(), name='about_story'),
                       )
