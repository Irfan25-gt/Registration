from django.shortcuts import render
from django.http import HttpResponse
from . models import student
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about_form(request):
    return render(request, 'about.html')

def registration_form(request):
    return render(request, 'registration.html')

def save(request):
    myname = request.POST['name']
    caption = request.POST['status']
    if myname == "" and caption == "":
        return render (request, 'confirm.html',{'has_error':True})
    newstd = student(name = myname, status = caption )
    newstd.save()
    return render(request, 'confirm.html' )

def std_list(request):
    students = student.objects.all()
    context = {'data':students}
    return render(request, 'displaystd.html', context)