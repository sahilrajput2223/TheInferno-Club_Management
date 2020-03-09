from django.shortcuts import render, redirect, get_object_or_404
from .forms import Profile_form, edit_Profile_form, Bookclub_from, ContactForm, FeedbackForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Bookclub
from django.views.generic.list import ListView
import os
import sqlite3
from django.core.mail import send_mail
from TheInferno import settings

# Create your views here.
def home(request):
    template= 'Home/index.html'
    return render(request, template, {})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            content = form.cleaned_data['message']
            print(contact_name)
            form.save()
            subject = 'Hello ' + contact_name + ' from TheInferno!'
            message = 'Stay Connected. We would love to hear you!'
            email_from = settings.EMAIL_HOST_USER
            email_to = [contact_email, ]
            send_mail(subject, message, email_from, email_to)

            return redirect('Home:home')
    else:
        form = ContactForm()
    template = 'Home/contact_us.html'
    return render(request, template, {'form': form})


def profile_view(request):
    temp = "Home/add_profile.html"
    if request.method == 'POST':
        p_form = Profile_form(request.POST or None, request.FILES or None)
        if p_form.is_valid():

            profile_form = p_form.save(commit = False)
            profile_form.email = request.POST.get('email')
            profile_form.save()
            # email for welcome
            subject = "TheInferno : Invoice Details"
            message = "Welcome To TheInferno Club. You are Verified Member for next 1 year and charges will be 20,000/-(per member - Offline Payment)       ...  if you want to upgrade your membership or add new member then contact on this email zeel3212@gmail.com"
            email_from = settings.EMAIL_HOST_USER
            email_to = [request.user.email, ]
            send_mail(subject, message, email_from, email_to)
            # email logic complate
            return redirect('Home:home')
    else:
        p_form = Profile_form()
    return render(request, temp, {'p_form':p_form})


def Show_profile_view(request):
    temp = "Home/profile.html"
    email = request.user.email
    if Profile.objects.filter(email__iexact=email).exists():
        data = Profile.objects.get(email = email)
        print(data)
    else:
        data = {}
    return render(request,temp, {'data':data})


def Edit_profile_view(request, pk):
    temp = "Home/edit_profile.html"
    profile = get_object_or_404(Profile,pk=pk)
    form = edit_Profile_form(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect("Home:profile")
    return render(request,temp, {'p_form':form})




@login_required
def Bookclub_view(request):
    temp = "Home/booking.html"
    db = sqlite3.connect(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Final Project', 'Admin', 'db_admin.sqlite3'))
    db.row_factory = sqlite3.Row
    data_cursor = db.execute('select name from Home_Amenities')
    print(data_cursor)
    data  = data_cursor.fetchall()

    if request.method == 'POST':
        print("In post")
        form = Bookclub_from(request.POST or None)
        print(request.POST.get('email'))
        print(request.POST.get('Amenitie'))
        print(request.POST.get('Date'))
        if form.is_valid():
            print("is valid")
            email = request.POST.get('email')
            Amenitie = request.POST.get('Amenitie')
            print("Form valid")
            booking_form = form.save(commit=False)
            booking_form.email = email
            booking_form.Amenities = Amenitie
            print(Amenitie)
            booking_form.save()
            return redirect('Home:home') #need to complete
    else:
        form = Bookclub_from()

    return render(request, temp, {'BookClub_from':form, 'data':data})



class show_booking(ListView):
    paginate_by = 15
    template_name = 'Home/show_bookings.html'

    def get_queryset(self):
        data = Bookclub.objects.all()

        return data


def Feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            email = request.POST.get('email')
            form.save()
            return redirect('Home:home')
    else:
        form = FeedbackForm
    template = 'Home/Feedback.html'
    return render(request, template, {'form': form})
