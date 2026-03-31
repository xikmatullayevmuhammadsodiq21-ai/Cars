from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('car_list') 
        else:
            return render(request, 'login.html', {"error": "parol yoki username xato"})

    return render(request, 'login.html')

def register_view(request):
    if request.method == "POST":
        
        
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")  
        confirm_password = request.POST.get("password2") 

        # Basic validation
        if password != confirm_password:
            return render(request, "register.html", {"error": "Parollar yoki username mos emas ❌"})

        # Check if username already exists to prevent a crash
        

        # Create user and log them in
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request, user)

        return redirect("car_list") # Ensure "car_list" exists in your car/urls.py

    # 2. This handles the initial page load (GET request)
    return render(request, 'register.html')

def profile(request):
    return render(request, 'profile.html')


