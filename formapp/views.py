from django.shortcuts import render,redirect
from formapp.models import employee
from formapp.forms import employeeforms
from django.core.mail import send_mail
from django.conf import settings

def add(request):
    form=employeeforms()
    return render(request,"add_employee.html",{'form':form})
def addemp(request):
    if request.method == 'POST':
        form = employeeforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_employees')
        return render(request,"add_employee.html")
def show_employees(request):
     emp=employee.objects.all()
     return render(request,'showemployee.html',{'employees':emp})
def update(request,id):
    empl=employee.objects.get(id=id)
    form=employeeforms(instance=empl)
    if request.method == 'POST':
        form=employeeforms(request.POST,instance=empl)
        if form.is_valid():
           form.save()
           return redirect('show_employees')
    return render(request,'update.html',{'form':form})
    
def delete(request,id):
    empl=employee.objects.get(id=id)
    empl.delete()
    return redirect("show_employees")

def sendmail(request):

    if request.method=='POST':
        form=employeeforms(request.POST)
        if form.is_valid():
            form.save()
            subject="Application"
            message="received your application"
            recipient=form.cleaned_data.get('email')
            send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient])
            return redirect("show_employees")

