from django.shortcuts import render

# Create your views here.
def login(request):
    template = 'account/login.html'
    return render(request, template, {})