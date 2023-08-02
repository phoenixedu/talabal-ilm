from django.urls import path
from .views import registerGenUser,customUserLogin,index,GenUserProfile,profileUpdateGenUser,profileSetting,emailVerification,ChangePasswordView
from django.contrib.auth.views import LogoutView 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index.as_view() , name='home'),
    path('register/', registerGenUser.as_view() , name='register'),
    path('login/',customUserLogin.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
    path('u/<str:username>',GenUserProfile.as_view(),name="genProfile"),
    path('u/update/<str:username>',profileUpdateGenUser.as_view(),name="profileupdate"),
    path('u/setting/<str:username>',profileSetting.as_view(),name="profileSetting"),
    path('u/reset-pw/<str:username>', ChangePasswordView.as_view(), name='pwreset'),
    path('u/confirm_email/<str:token>/', emailVerification.as_view(), name='confirm_email'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)