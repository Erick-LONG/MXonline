from django.conf.urls import url
from .views import UserInfoView,UpLoadImgView,UpDatePwdView,SendEmailCodeView,UpdateEmailView


urlpatterns = [
    #用户信息
    url(r'^info/$',UserInfoView.as_view(),name='user_info'),

    #用户头像上传
    url(r'^img_upload/$',UpLoadImgView.as_view(),name='img_upload'),

    #用户个人中心修改密码
    url(r'^update/pwd/$',UpDatePwdView.as_view(),name='update_pwd'),

    #发送邮箱验证码
    url(r'^sendemail_code/$',SendEmailCodeView.as_view(),name='sendemail_code$'),

    #修改邮箱
    url(r'^update_email/$',UpdateEmailView.as_view(),name='update_email$'),
]