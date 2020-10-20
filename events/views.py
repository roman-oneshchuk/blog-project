from django.shortcuts import render
from .models import Event
# Create your views here.
def home(request):
	events = Event.objects # отримуємо усі об'єкта класу Івент
	return render(request, 'events/home.html', {'events': events})