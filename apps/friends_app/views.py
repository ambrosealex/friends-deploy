from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from datetime import datetime
import re

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        request.session['user_id'] = ''
    if 'page' not in request.session:
        request.session['page'] = ''
    context = {
        'page' : request.session['page']
    }
    print request.session['page']
    print models.Users.objects.all().values('email')
    return render(request, 'friends_app/index.html', context)

def login(request):
    user_login = request.POST['user_login']
    print user_login
    print models.Users.objects.all().values('email')
    pass_login = request.POST['pass_login']
    current_user = models.Users.objects.filter(email = user_login)
    request.session['page'] = 'login'
    if not current_user:
        messages.add_message(request, messages.INFO, 'Username is not valid')
        return redirect('/')
    if current_user[0].password != pass_login:
        messages.add_message(request, messages.INFO, 'Incorrect Password')
        return redirect('/')
    request.session['user_id'] = current_user[0].id
    return redirect('/home')

def register(request):
    name = request.POST['name']
    alias = request.POST['alias']
    email = request.POST['email']
    pass_init = request.POST['pass_init']
    pass_confirm = request.POST['pass_confirm']
    birthdate = request.POST['birthdate']
    user_check = models.Users.objects.filter(email = email)
    request.session['page'] = 'register'
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    print "THE BIRTHDATE LOOKS LIKE: ", birthdate
    if not birthdate:
        messages.add_message(request, messages.INFO, 'Date of Birth field must be filled out')
        return redirect('/')
    nowYr = int(datetime.now().strftime('%Y'))
    check = int(birthdate.split('-')[0]) + 12
    if check > nowYr:
        messages.add_message(request, messages.INFO, 'You must be at least 12 years old to create a profile')
        return redirect('/')
    if len(name) < 3 or len(alias) < 3:
        messages.add_message(request, messages.INFO, 'Name and Alias must be at least 3 characters')
        return redirect('/')
    if not match:
        messages.add_message(request, messages.INFO, 'Not a valid email address')
        return redirect('/')
    if user_check:
        messages.add_message(request, messages.INFO, 'That email is already in use')
        return redirect('/')
    if len(pass_init) < 8:
        messages.add_message(request, messages.INFO, 'Please make password at least 8 characters')
        return redirect('/')
    if pass_init != pass_confirm:
        messages.add_message(request, messages.INFO, 'Password and Confirmation must match')
        return redirect('/')
    models.Users.objects.create(name = name, alias = alias, email = email, password = pass_init, birthdate = birthdate)
    return redirect('/')

def home(request):
    user = models.Users.objects.get(id = request.session['user_id'])
    myFriends = models.Friends.objects.filter(user_id = user)
    imFriends = models.Friends.objects.filter(friend_id = user)

    look = models.Friends.objects.filter(user_id = user)
    look2 = models.Friends.objects.filter(friend_id = user)

    notFriends = models.Users.objects.exclude(id = request.session['user_id']).exclude(id__in = look.values('friend_id')).exclude(id__in = look2.values('user_id')).order_by('alias')

    context = {
        'user' : user,
        'myFriends' : myFriends,
        'imFriends' : imFriends,
        'notFriends' : notFriends,
        'look' : look
    }
    return render(request, 'friends_app/home.html', context)

def add(request,id):
    friend = models.Users.objects.get(id=id)
    current_user = models.Users.objects.get(id = request.session['user_id'])
    result = models.Friends.objects.create(user_id = current_user, friend_id = friend)

    return redirect('/home')

def profile(request,id):
    page_user = models.Users.objects.get(id=id)
    context = {
        'user' : page_user
    }
    return render(request, 'friends_app/profile.html', context)

def remove(request,id):
    models.Friends.objects.get(id=id).delete()
    return redirect('/home')

def logout(request):
    if 'user_id' in request.session:
        request.session['user_id'] = 0
    return redirect('/')
