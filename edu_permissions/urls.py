from django.urls import path
from .views import groupsView

urlpatterns = [
    path('groups/<str:pk_key>',groupsView.as_view(),name="allGroups")
]
