from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def register(request):
    if request.method == 'POST':   # POST = POST => True
        username = request.POST['username'] # vijaya
        email = request.POST['email']  # vijayakhandavalli13@gmail.com
        password1 = request.POST['password']   # vijaya123
        password2 = request.POST['password2']    # vijaya123

        if password1 == password2:
            if User.objects.filter(username= username).exists():
                print('username Exists...! Try with another name')
                return redirect('register')
            else:
                if User.objects.filter(email= email).exists():
                    print("Email is already taken, Try another one")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save() # send the data to the database : Table : User
                    return redirect('login')
        else:
            print('Password did not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':   # if the condition is true it should enter in to the if condition
        username = request.POST['username']   # vijaya
        password = request.POST['password']   # vijaya123

        user = auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request,user)
            print("Login Successful..!")
            return redirect('showProducts')
        else:
            print('Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        print("Logout From Website...")
        return redirect('login')




