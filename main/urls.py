from django.urls import path 
from . import views

urlpatterns = [
    path('',views.Tasklist.as_view(),name= 'tasks'),
    path('base/',views.Feach.as_view(),name='base'),
    path('display',views.Feach2.as_view(),name='display'),
    

]