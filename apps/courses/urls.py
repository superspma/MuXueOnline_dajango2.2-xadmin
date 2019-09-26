# coding:utf-8

from django.conf.urls import url
from django.urls import path

from apps.courses.views import CourseListView, CourseDetailView
from apps.organizations.views import OrgView, AddAskView, OrgHomeView, OrgTeacherView, OrgCourseView, OrgDescView

urlpatterns = [
    url(r'list/$', CourseListView.as_view(), name='list'),
    url(r'(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='detail'),

]
