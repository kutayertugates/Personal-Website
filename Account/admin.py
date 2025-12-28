from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Admin listesinde görünecek sütunlar
    list_display = UserAdmin.list_display + ('biography',)
    
    # Kullanıcı detayına girince görünen alan grupları
    # Varsayılan "Personal info" kısmına kendi alanlarımızı ekliyoruz
    fieldsets = UserAdmin.fieldsets + (
        ('Portfolio Bilgileri', {'fields': ('biography',)}),
    )