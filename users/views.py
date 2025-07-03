from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import Profile
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email


def loginUser(request):
    errors = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # returns boolean value if any value matching username exists in model User
        check_user = User.objects.filter(username=username).exists() 
        if check_user:
            # for authenticating user with username and password
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user:
                login(request, authenticated_user) # saves the user data in session 
                messages.success(request, "You have successfully logged in")
                return redirect("/") # redirects to /home route
            else:
                errors['password'] = "Invalid Password!" #stores error in key 'password'
        else:
            errors['username'] = "User doesnot exist."
        
        if errors:
            return render(request, 'pages/auth/login.html', {'errors': errors}) # renders login.html with errors
        
def signupUser(request):
    errors = {}
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        profile_image = request.FILES.get('profile_image')
        nationality = request.POST.get('nationality')
        
        
        # profile = Profile.objects.create(user=user, address=address, phone=phone, gender=gender, dob=dob, nationality=nationality)
        # if profile_image:
        #     profile.profile_image = profile_image
        # else:
        # profile.profile_image = "user/default_user.png"
        # profile.save()

        user_exists = User.objects.filter(username=username).exists()
        email_exists = User.objects.filter(email=email).exists()
        phone_exists = Profile.objects.filter(phone=phone).exists()
        
        if user_exists:
            errors['username'] = "Username already exists."
        if phone_exists:
            errors['phone'] = "Phone number already exists."
        if len(username) < 3 :
            errors['username'] = "Username must be at least 3 characters long."
        if password != confirm_password:
            errors['confirm_password'] = "Passwords do not match."
        if len(password) < 8:
            errors['password'] = "Password must be at least 8 characters long."
        if len(first_name) < 2:
            errors['first_name'] = "First name must be at least 2 characters long."
        if len(phone)< 10 or len(phone)> 10:
            errors['phone'] = "Phone Number Should be 10 Digits Long"
        try:
            validate_password(password)
        except Exception as e:
            errors['password'] = e
        
        try:
            if email_exists:
                errors['email'] = ["Email already exists."]
            validate_email(email)
        except Exception as e:
            errors['email'] = e
        
        if errors:
            return render(request, 'pages/auth/signup.html', {'errors': errors,})
        
        else:  
        
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            Profile.objects.create( user = user, address=address, phone=phone, gender=gender, dob=dob, nationality=nationality, profile_image=profile_image)
            
            messages.success(request, "You have successfully signed up")
            return redirect('/auth/log-in')

def logoutUser(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('/auth/log-in')