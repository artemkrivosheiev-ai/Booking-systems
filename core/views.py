from django.shortcuts import render
from .models import Room

def room_list(request):
    rooms = Room.objects.all()  # Витягуємо всі кімнати з бази даних
    return render(request, 'core/room_list.html', {'rooms': rooms})

