from django.urls import path 
from . import views

urlpatterns = [
    path('',views.Tasklist.as_view(),name= 'tasks'),

]