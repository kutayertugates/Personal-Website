from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Admin listesinde görünecek sütunlar
    list_display = UserAdmin.list_display + ('biography', 'get_avatar_button')
    
    # Kullanıcı detayına girince görünen alan grupları
    # Varsayılan "Personal info" kısmına kendi alanlarımızı ekliyoruz
    fieldsets = UserAdmin.fieldsets + (
        ('Portfolio Bilgileri', {'fields': ('biography', 'avatar')}),
    )

    def get_avatar_button(self, obj):
        if obj.avatar:
            # HTML: Ufak resim + Yanına Django stili buton
            html = f"""
                <div style="display: flex; align-items: center; gap: 10px;">
                    <a href="{obj.avatar.url}" target="_blank" class="button" style="font-size: 11px; font-weight: bold; text-decotation: none;">
                        Göster
                    </a>
                </div>
            """
            return mark_safe(html)
        
        # Resim yoksa silik bir tire
        return mark_safe('<span style="color: #ccc;">-</span>')

    get_avatar_button.short_description = "Profil Resmi"