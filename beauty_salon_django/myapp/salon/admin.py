from django.contrib import admin
from .models import Person

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ('name', 'num_tel')
    list_display = ('name', 'num_tel')
    search_fields = ('num_tel',)
    list_per_page = 30