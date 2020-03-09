from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .forms import Amenities_form
import sqlite3
from django.contrib.auth.decorators import login_required
import os
# Create your views here.

@login_required
def Home_view(request):
    temp = "index.html"
    db = sqlite3.connect(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Final Project', 'TheInferno', 'db_user.sqlite3'))
    db.row_factory = sqlite3.Row
    data_cursor = db.execute('select * from Home_profile')
    print(data_cursor)
    data  = data_cursor.fetchall()
    return render(request,temp,{'data':data})

@login_required
def all_user_view(request):
    temp = "all_user.html"
    db = sqlite3.connect(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Final Project', 'TheInferno', 'db_user.sqlite3'))
    db.row_factory = sqlite3.Row
    data_cursor = db.execute('select * from Home_profile')
    print(data_cursor)
    data  = data_cursor.fetchall()
    print(data[0])
    for i in data_cursor:
        print(i.email)
    return render(request,temp,{'data':data})


@login_required
def contact_user_view(request):
    temp = "contact_details.html"
    db = sqlite3.connect(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Final Project', 'TheInferno', 'db_user.sqlite3'))
    db.row_factory = sqlite3.Row
    data_cursor = db.execute('select * from Home_Contact')
    print(data_cursor)
    data  = data_cursor.fetchall()
    return render(request,temp,{'data':data})

@login_required
def Booking_view(request):
    temp = "booking.html"
    db = sqlite3.connect(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Final Project', 'TheInferno', 'db_user.sqlite3'))
    db.row_factory = sqlite3.Row
    data_cursor = db.execute('select * from Home_Bookclub')
    print(data_cursor)
    data  = data_cursor.fetchall()
    print(data[0])
    for i in data_cursor:
        print(i.email)
    return render(request,temp,{'data':data})

@login_required
def New_Amenities_view(request):
    temp = 'new_amenitie.html'
    if request.method == "POST":
        form = Amenities_form(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('Admin:home')
    else:
        form = Amenities_form()

    return render(request, temp, {'new_Amenities_form':form})



@login_required
def show_feedback_view(request):
    temp = 'feedback.html'
    db = sqlite3.connect(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Final Project', 'TheInferno', 'db_user.sqlite3'))
    db.row_factory = sqlite3.Row
    data_cursor = db.execute('select * from Home_Feedback')
    print(data_cursor)
    data  = data_cursor.fetchall()
    for i in data_cursor:
        print(i.email)
    return render(request,temp,{'data':data})
