from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from member.models import *
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username','email','first_name','last_name','membership_date','is_staff','is_active',)

    # user detail page এ extra field add
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {
            'fields': ('membership_date', 'phone_number', 'address'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {
            'fields': ('membership_date', 'phone_number', 'address'),
        }),
    )
# admin.site.register(Member,CustomUser)