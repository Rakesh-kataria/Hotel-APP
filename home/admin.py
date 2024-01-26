from django.contrib import admin
from .models import Hotel, HotelImages, Amenities, HotelBooking

admin.site.register(Hotel)
admin.site.register(HotelImages)
admin.site.register(Amenities)
admin.site.register(HotelBooking)
