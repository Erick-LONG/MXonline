from django.conf.urls import url,include
from .views import CourseView,CourseDetailView,CourseInfoView

urlpatterns = [
    url(r'^list/$',CourseView.as_view(),name='course_list'),
    url(r'^detail/(?P<course_id>\d+)/$',CourseDetailView.as_view(),name='course_detail'),
    url(r'^info/(?P<course_id>\d+)/$',CourseInfoView.as_view(),name='course_info'),

]