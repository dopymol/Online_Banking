from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect("e_bank:newpage")
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')


def register(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password1']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'register.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return render(request,"login.html")
        else:
            return render (request,'register.html', {'error':'Password does not match!'})
    else:
        return render(request,'register.html')


# logout
def logout(request):
    auth.logout(request)
    return redirect('/')

def newpage(request):
    if request.user.is_authenticated and request.user.is_user:
        render(request,'newpage.html')
    else:
        return redirect('Credentials:register')