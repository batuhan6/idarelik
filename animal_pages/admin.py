from django.contrib import admin

from animal_pages.models import Animal


# Register your models here.
@admin.register(Animal)
class AnimalsAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal_name','created_date', 'updated_date')
