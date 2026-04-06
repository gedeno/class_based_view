from django.urls import path 
from . import views

urlpatterns = [
    path('',views.Tasklist.as_view(),name= 'tasks'),
    path('base/',views.Feach.as_view(),name='base'),
    path('display/',views.Feach2.as_view(),name='display'),
    path('disp/',views.Feach3.as_view(),name="disp"),
    path('forms/',views.ContactFormview.as_view() ,name='forms'),
    path('check/<int:pk>',views.Dataupdate.as_view(), name='check')


]