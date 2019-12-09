from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User
import apps.the_wall_app.views

def index(request):
    return render(request, "login_app/index.html")

def registration(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())    
        print(pw_hash)
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], pw_hash=pw_hash)
        request.session['email'] = new_user.email
        request.session['id'] = new_user.id
        return redirect("/add_new_user")

def welcome_new_user(request):
    if (request.session.has_key('id')):
        context = {
            'user' : User.objects.get(id=request.session['id'])
        }
        messages.success(request, "Successfully registered!")
        return render(request, "login_app/welcome.html", context)
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    elif request.method == "POST":
        try:
            user = User.objects.get(email = request.POST['email'])
            request.session['email'] = user.email
            request.session['id'] = user.id
            return redirect('/logged_in')
        except:
            return HttpResponse('Invalid email or password')
            # return redirect('/')

def success(request):
    if (request.session.has_key('id')):
        context = {
            'user' : User.objects.get(id = request.session['id'])
        }
        return render(request, "login_app/welcome.html", context)
    return redirect('/')

def logout(request):
    try:
        del request.session['email']
        del request.session['id']
    except KeyError:
        pass
    return redirect('/')


