from django.contrib.auth import authenticate , login , logout
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from welcome.models import Visitor
from django.db import IntegrityError


def list_visitors ( request ) :
    visitors = Visitor.objects.filter()

    context = {
         'visitors':visitors
    }

    return render ( request , "welcome/list_visitors.html" , context )


def home ( request ) :
    if request.method == "POST" :
        userName = request.POST [ 'userName' ]

        try:
            newVisitor=Visitor.objects.create(name_visitor=userName)
            newVisitor.save()
            messages.success ( request , "Hello {0}!!!".format(userName) )
        except IntegrityError as e:
            messages.success ( request , "I have seen you already, {0}!!!".format(userName) )

    return render ( request , "welcome/index.html" )


def signup ( request ) :
    if request.method == "POST" :

        userName = request.POST [ 'userName' ]
        firstName = request.POST [ 'firstName' ]
        lastName = request.POST [ 'lastName' ]
        emailUser = request.POST [ 'emailUser' ]
        password1 = request.POST [ 'password1' ]
        password2 = request.POST [ 'password2' ]

        try:
            newUser = User.objects.create_user ( userName , emailUser , password1 )
            newUser.first_name = firstName
            newUser.last_name = lastName
            newUser.save ()
            messages.success ( request , "Your account has been created!" )
            return redirect ( 'signin' )
        except IntegrityError as e:
             messages.success ( request , "User name:{0} or email {1} is used!!!\n"
                                          "Please enter something else.".format(userName,emailUser) )


    return render ( request , "welcome/signup.html" )


def signin ( request ) :
    if request.method == 'POST' :
        userName = request.POST [ 'userName' ]
        password1 = request.POST [ 'password1' ]

        user = authenticate ( username=userName , password=password1 )

        if user is not None :
            login ( request , user )
            firstName = user.first_name
            return render ( request , "welcome/index.html" , {'firstName' : firstName} )
        else :
            messages.error ( request , "Bad login!" )
            return redirect ( 'home' )

    return render ( request , "welcome/signin.html" )


def signout ( request ) :
    logout ( request )
    messages.success ( request , "Logged out!" )
    return redirect ( 'home' )




