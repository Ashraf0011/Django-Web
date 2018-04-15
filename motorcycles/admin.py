from django.contrib import admin

# Register your models here.
from .models import Bike,Brand

class BikeAdmin(admin.ModelAdmin):
    list_display = ('name','id','topSpeed','releaseDate',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brandName',)


admin.site.register(Bike, BikeAdmin)
admin.site.register(Brand,BrandAdmin)
