from django.contrib import admin

# Register your models here.
from accused_app.models import Accused, Crime


@admin.register(Accused)
class AccusedAdmin(admin.ModelAdmin):
    pass


@admin.register(Crime)
class CrimeAdmin(admin.ModelAdmin):
    pass

