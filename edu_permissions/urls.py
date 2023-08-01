from django.urls import path
from .views import AllGroupsView,addListOfFlty,listForHOD
urlpatterns = [
    path('groups/<str:pk_key>', AllGroupsView.as_view(),name="allGroups" ),
    path('g/add-to/<str:name>/<str:pk_key>', addListOfFlty.as_view(),name="add_to_group" ),
    path('g/add/<str:name>/<str:pk_key>', listForHOD.as_view(),name="add_to_hod" ),
]
