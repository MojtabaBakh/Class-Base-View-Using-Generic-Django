from django.shortcuts import render
from . models import Student
from django.http import HttpResponse
import datetime
from django.views import generic
from django.urls import reverse_lazy









class StudentListView(generic.ListView):
    model=Student

class StudentCreateView(generic.CreateView):
    model=Student
    fields="__all__"
    success_url=reverse_lazy("studentsclass")
    
    
class StudentUpdateView(generic.UpdateView):
    model=Student
    fields="__all__"
    success_url=reverse_lazy("studentsclass")   
    
    
class StudentDeleteView(generic.DeleteView):
    model=Student 
    success_url=reverse_lazy("studentsclass") 
    
    
    

def student_details( request , pk) :
    student=Student.objects.get(id = pk)
    return render(request , 'myapp/studentdetails.html' , {'student':student})



