from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from Home.models import Contact, Student
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def course(request):
    return render(request, 'course.html')


def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    if request.method == 'POST':
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        massege = request.POST.get("massege")
        
        # Corrected to use Contact.objects.get_or_create()
        contact=Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            massege=massege
        )
        contact.save()
        messages.success(request, "Your Form has been sent")
    return render(request, 'contact.html')

def student(request):
    if request.method == 'POST':
        Course_Name = request.POST.get("Course_Name")
        usn = request.POST.get("usn")
        name = request.POST.get("name")
        # Gender = request.POST.get("G")
        email = request.POST.get("email")
        Phone = request.POST.get("Phone")
        DOB = request.POST.get("DOB")
        Branch = request.POST.get("Branch")
        
        # Check if a student with the same USN already exists
        if Student.objects.filter(usn=usn).exists():
            messages.error(request, "A student with this USN already exists.")
            return redirect('student')  # Redirect back to the student page
        
        # Corrected to use Contact.objects.get_or_create()
        student=Student.objects.create(
            Course_Name = Course_Name,
            usn=usn,
            name=name,
            # Gender=Gender,
            email=email,
            Phone=Phone,
            DOB=DOB,
            Branch=Branch
        )
        student.save()
        messages.success(request, "Your Form has been submitted")
    return render(request, 'student.html')