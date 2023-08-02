from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from .views import xEduInstDetaile,courseDetail,semisterUpdate,InstCourseUdate,eduStorageMeter,eduInstUpdate,create_semister,createBooks,createInstetude,create_InstCourse

urlpatterns = [
    path('form/',createInstetude.as_view(),name="createEdu"),
    path('course/<str:pk_key>/',create_InstCourse.as_view(),name="createcourse"),
    path('<str:pk_key>/course/<str:name>/<int:pk>/semister/',create_semister.as_view(),name="createsemister"),
    path('<str:pk_key>/',xEduInstDetaile.as_view(),name="eduD"),
    path('<str:pk_key>/course/<str:name>/<pk>/',courseDetail.as_view(),name="courseD"),
    path('<str:pk_key>/addbook/',createBooks.as_view(),name="createBooks"),
    path('<str:pk_key>/update/',eduInstUpdate.as_view(),name="eduUpdate"),
    path('<str:pk_key>/update/<str:name>/<int:pk>/',InstCourseUdate.as_view(),name="courseUpdate"),
    path('<str:pk_key>/<str:name>/update_semister/<int:pk>/',semisterUpdate.as_view(),name="semisterUpdate"),
    path('storage/<pk_key>/',eduStorageMeter.as_view(), name="eduStorage" )
]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)