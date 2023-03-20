from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse
from .forms import StudentForm
from django.contrib import messages

def home(request):
    std=Student.objects.all()
    return render(request,'index.html',{'std':std})




def add_student(request, id=None):
    std = None
    if id:
        std = Student.get_by_id(pk=id)
    form = StudentForm(instance=std)
    if request.method == 'POST':
        print(request.POST)
        form = StudentForm(request.POST, instance=std)
        if form.is_valid():
            form.save()
            messages.info(request, "Student_data saved successfully.")
            return redirect('home')
    return render(request, 'add_student.html', {'form': form})




def edit_student(request,roll):
    std=Student.objects.get(pk=roll)

    return render(request,"edit_student.html",{'std':std})




def delete_student(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    messages.info(request, "delete_student saved successfully.")
    return redirect("home")


def do_edit_student(request,roll):
        roll=request.POST.get("roll")
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        phone=request.POST.get("phone")
        address=request.POST.get("address")

        s=Student()
        s.roll=roll
        s.name=name
        s.email=email
        s.password=password
        s.phone=phone
        s.address=address


        s.save()
        messages.info(request, "edit_student saved successfully.")
        return redirect("home")
