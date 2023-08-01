from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from .views import creatDept,creatClass,creatLab,creatRole,createSociety,eduAdmin,eduDeptView,eduClassDeView

urlpatterns = [
    path('admin/',eduAdmin.as_view(),name='eduAdmin'),
    path('add-department',creatDept.as_view(),name='addept'),
    path('create-class',creatClass.as_view(),name='createclass'),
    path('create-lab',creatLab.as_view(),name='createlab'),
    path('add-role',creatRole.as_view(),name='addRole'),
    path('create-society',createSociety.as_view(),name='createSociety'),
    path('department/<str:name>/<int:pk>',eduDeptView.as_view(),name='departmentD'),
    path('e-class/<str:name>/<int:pk>',eduClassDeView.as_view(),name='e_classD'),

]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
