from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
def homepage(request):
    return render(request, "home.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def registration(request):
    return render(request,"registration.html")

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        # Checking if student with given name already exists
        if Student.objects.filter(name=name).exists():
            error = "Name already exists in the database. Please enter a new name."
            return render(request, 'add.html', {'error': error})
        else:
            Student.objects.create(name=name, age=age)
            # Redirect to the specified URL
            redirect_url = request.POST.get('redirect_url')
            if redirect_url:
                return redirect(redirect_url)
    return render(request, 'add.html')

def view_students(request):
    students = Student.objects.all()
    return render(request, 'view.html', {'students': students})

def apply(request):
    return render(request,"apply.html")

def practice(request):
    return render(request,"pratice.html")

def profile(request):
    return render(request,"profile.html")

def jobs(request):
    return render(request,"jobs.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Perform validation (e.g., check if passwords match)

        # Create user object and save to database
        user = User(username=username, email=email, password=password)
        user.save()

        return JsonResponse({'message': 'User created successfully'})

    return render(request, 'signup.html')