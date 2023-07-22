from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateAdmission,CreateJobRecruitry,JobRecruitryDetailView,admissionDV

urlpatterns = [
    path('admission',CreateAdmission.as_view(),name="admission"),
    path('jobvacancy',CreateJobRecruitry.as_view(),name="jobvacancy"),
    path('job/<int:pk>/<str:name>/',JobRecruitryDetailView.as_view(),name="jobd"),
    path('admission/<int:pk>/<str:name>/',admissionDV.as_view(),name="admissionD"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

