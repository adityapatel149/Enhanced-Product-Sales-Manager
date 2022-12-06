from django.contrib import admin

# Register your models here.
from .models import Customer,Vendor,Pro

admin.site.register(Customer)
admin.site.register(Vendor)


class ProAdmin(admin.ModelAdmin):
    list_display = ['name','price','des','review']
    list_filter = ['name','price','des','review']

    readonly_fields = ('id',)


admin.site.register(Pro, ProAdmin)