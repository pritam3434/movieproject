from django.contrib import admin
from testapp.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display=['rdate','moviename','hero','heroine','rating','platform']
admin.site.register(Movie,MovieAdmin) 
# Register your models here.


