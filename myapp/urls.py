
from django.contrib import admin
from django.urls import path , include
from .views import  StudentListView , StudentCreateView , StudentUpdateView , StudentDeleteView , student_details

name='myapp'

urlpatterns = [
 
    path('studentlist/', StudentListView.as_view() , name="studentlist"),
    path('createstudent/', StudentCreateView.as_view() , name="createstudent"),
    path('updatestudent/<pk>', StudentUpdateView.as_view() , name="updatestudent"),
    path('deletestudent/<pk>', StudentDeleteView.as_view() , name="deletestudent"),
    
    
    
    path('studentdetails/<pk>', student_details , name="studentdetails"),

    
]
