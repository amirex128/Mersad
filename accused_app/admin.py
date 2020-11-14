from django.contrib import admin

# Register your models here.
from accused_app.models import Accused, Crime


class CrimeInline(admin.TabularInline):
    extra = 1
    model = Crime


@admin.register(Accused)
class AccusedAdmin(admin.ModelAdmin):
    inlines = [CrimeInline]


@admin.register(Crime)
class CrimeAdmin(admin.ModelAdmin):
    pass
