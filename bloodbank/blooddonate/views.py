from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import BloodBank, Donor

def home(request):
    context = {
        'user': request.user,  # Pass the current user to the template
        'message': 'Welcome to the Blood Bank Management System',
    }
    return render(request, 'home.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def register_blood_bank(request):
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        BloodBank.objects.create(name=name, location=location, contact_number=contact_number, email=email)
        return redirect('login')  # Redirect to login after registration
    return render(request, 'register_blood_bank.html')

def register_donor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        blood_group = request.POST.get('blood_group')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        last_donation_date = request.POST.get('last_donation_date')
        Donor.objects.create(name=name, blood_group=blood_group, contact_number=contact_number, email=email, last_donation_date=last_donation_date)
        return redirect('login')  # Redirect to login after registration
    return render(request, 'register_donor.html')
