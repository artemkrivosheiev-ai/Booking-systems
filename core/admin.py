from django.contrib import admin
from .models import RoomCategory, Room, Booking

# Реєструємо моделі, щоб вони з'явилися в панелі керування
admin.site.register(RoomCategory)
admin.site.register(Room)
admin.site.register(Booking)
