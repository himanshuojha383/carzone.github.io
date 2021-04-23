from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    search_fields = Car.objects.values('model','city','year','body_style')
    data = {
        'teams': teams,
        'featured_cars' : featured_cars,
        'all_cars' : all_cars,
        'search_fields': search_fields,
    }
    return render(request, 'pages/home.html',data)

def about(request):
    teams = Team.objects.all
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html',data)    

def services(request):
    return render(request, 'pages/services.html')      

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
    return render(request, 'pages/contact.html')    