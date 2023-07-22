from django.urls import path
from .views import ClassOfStudentsListView,ClassOfStudentsViewForm,ClassOfStudentsDetailView,createElecture,addStudentList,eLactureDatile,eLactureAttendence,listOfElectures
urlpatterns = [
    path('class-form/',ClassOfStudentsViewForm.as_view(),name='classCForm'),
    path('class-list/',ClassOfStudentsListView.as_view(),name='classCList'),
    path('<int:pk>/<str:name>',ClassOfStudentsDetailView.as_view(),name='classCD'),
    path('<int:pk>/<str:name>/Add-Students/',addStudentList.as_view(),name='addStudent'),
    path('<int:pk>/<str:name>/Leture-form/',createElecture.as_view(),name='ElectureForm'),
    path('<str:cls_key>/<int:pk>/<str:name>/',eLactureDatile.as_view(),name='electureD'),
    path('<str:cls_key>/list-of-lectures/',listOfElectures.as_view(),name='list_Lectures'),
    path('<int:pk>/attendance-sheet/',eLactureAttendence.as_view(),name='atSheet'),
]



