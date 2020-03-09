from django.shortcuts import render

# Create your views here.
def router(request):
    temp = "router/main_router.html"
    return render(request,temp)