from django.conf.urls import url
from .views import UserInfoView,UpLoadImgView,UpDatePwdView


urlpatterns = [
    #用户信息
    url(r'^info/$',UserInfoView.as_view(),name='user_info'),

    #用户头像上传
    url(r'^img_upload/$',UpLoadImgView.as_view(),name='img_upload'),

    #用户个人中心修改密码
    url(r'^update/pwd/$',UpDatePwdView.as_view(),name='update_pwd'),
]