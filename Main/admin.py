from django.contrib import admin
from django.utils.html import mark_safe  # <--- 1. BU IMPORT ÖNEMLİ
from .models import DynamicContent

@admin.register(DynamicContent)
class DynamicContentAdmin(admin.ModelAdmin):
    # 2. 'view_image_button' metodunu listeye ekledik
    list_display = ('title', 'content_type_preview', 'view_image_button', 'updated_at')
    search_fields = ('title', 'description')
    
    # Mevcut metodun duruyor
    def content_type_preview(self, obj):
        if obj.image:
            return "Görsel"
        elif obj.html_content:
            return f"HTML: {obj.html_content[:30]}..."
        return "-"
    content_type_preview.short_description = "İçerik Tipi"

    def view_image_button(self, obj):
        if obj.image:
            # target="_blank": Yeni sekmede açılmasını sağlar.
            # Ufak bir CSS ile Django admin butonlarına benzetelim.
            html_link = f"""
                <a href="{obj.image.url}" target="_blank" 
                   style="background-color: #79aec8; color: white; padding: 5px 10px; border-radius: 4px; text-decoration: none; font-weight: bold; font-size: 11px;">
                   Görüntüle ↗
                </a>
            """
            # Django'ya bu string'in güvenli HTML olduğunu söylüyoruz.
            return mark_safe(html_link)
        
        # Görsel yoksa soluk bir tire işareti koyalım
        return mark_safe('<span style="color: #ccc;">-</span>')

    # Admin tablosundaki sütun başlığı
    view_image_button.short_description = "Görsel Linki"
    # Bu bir veritabanı alanı olmadığı için sıralamayı kapatalım
    view_image_button.admin_order_field = None