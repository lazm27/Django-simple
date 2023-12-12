from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def loginUser(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request, user) 
            return render(request,'home.html')
        else:
            return redirect('/')
    return render(request,'login.html')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first')  
        last_name = request.POST.get('last')  
        username = request.POST.get('username')  
        email = request.POST.get('email')  
        password = request.POST.get('password')  
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        print(User.objects.all())
        return redirect('/')
    return render(request,'signup.html')
def logout_user(request):
    logout(request)
    return render(request, 'login.html')
# Create your views here.
