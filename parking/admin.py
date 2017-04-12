from django.contrib import admin
from .models import Spots, Parked

# Register your models here.
class SpotsAdmin(admin.ModelAdmin):
    list_display = ["id", "lng", "lat", "occupied"]
    class Meta:
        model = Spots
admin.site.register(Spots, SpotsAdmin)

class ParkedAdmin(admin.ModelAdmin):
    list_display = ["id", "parking_spot", "time_range"]
    class Meta:
        model = Parked
admin.site.register(Parked, ParkedAdmin)