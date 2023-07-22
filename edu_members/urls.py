from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import view_file,CreateStudentAdmission,CreateEmpolyJoinning,DataileOfEduFaculty,DatileOfEduStudent,ListOfEduFaculties,ListOfEduStudents,viewStudentApplication,viewEmpolyCv

urlpatterns = [
    path('view-file/<path:file_url>/', view_file, name='view_file'),
    path('<int:pk>/StudentAdmission',CreateStudentAdmission.as_view(),name="studentAdmit"),
    path('<int:pk>/job_cv/',CreateEmpolyJoinning.as_view(),name="empolyForm"),
    path('listOfapplications/',viewStudentApplication.as_view(),name="LOA"),
    path('listOfCvs/',viewEmpolyCv.as_view(),name="CVs"),
    path('f/faculties-list/',ListOfEduFaculties.as_view(),name="facultiesList"),
    path('st/students-list/',ListOfEduStudents.as_view(),name="studentsList"),
    path('st/<str:eduID>/',DatileOfEduStudent.as_view(),name="eduStudentP"),
    path('f/<str:eduID>/',DataileOfEduFaculty.as_view(),name="eduFacultyP"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

