from django.contrib import admin
from .models import RoomCategory, Room, Booking
from .models import Review


admin.site.register(RoomCategory)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Review)
 