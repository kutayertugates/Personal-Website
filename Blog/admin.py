from django.contrib import admin
from django.utils.html import mark_safe
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Blog, Tag

# --- 1. ETİKET YÖNETİMİ ---
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    # Başlık girilirken slug otomatik oluşsun (UX için şart)
    prepopulated_fields = {'slug': ('name',)}


# --- 2. BLOG YÖNETİMİ ---
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # CKEditor'ü Content alanına bağla
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    class Media:
        css = {
            'all': ('css/components/_ckeditor.css',) 
        }

    # Liste Görünümü (Sütunlar)
    list_display = ('title', 'author', 'get_thumbnail_button', 'created_at', 'updated_at')
    
    # Tıklanabilir linkler
    list_display_links = ('get_thumbnail_button', 'title')
    
    # Sağ taraftaki filtre kutusu
    list_filter = ('created_at', 'author', 'tags')
    
    # Arama çubuğu (Hangi alanlarda arayacak?)
    search_fields = ('title', 'content')
    
    # Slug otomasyonu
    prepopulated_fields = {'slug': ('title',)}
    
    # *** İŞTE O KRİTİK UX AYARI (Many-to-Many için) ***
    # Etiketleri seçmek için gelişmiş ikili kutu yapısı
    filter_horizontal = ('tags',)
    
    # Değiştirilemez alanlar (Bilgi amaçlı)
    readonly_fields = ('created_at', 'updated_at')

    # Detay sayfasındaki alan gruplandırması (Fieldsets)
    # Formu bölümlere ayırarak bilişsel yükü azaltıyoruz.
    fieldsets = (
        ('Genel Bilgiler', {
            'fields': ('title', 'slug', 'author', 'thumbnail', 'thumbnail_alt', 'thumbnail_owner', 'content')
        }),
        ('SEO Ayarları', {
            'fields': ('meta_title', 'meta_description', 'tags'),
            'classes': ('collapse',),
        }),
        ('Geliştirici / Tasarımcı', {
            'fields': ('page_css',),
            'classes': ('collapse',),
        }),
        ('Zaman Bilgileri', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    # Listede Görsel Önizleme Metodu
    def get_thumbnail_button(self, obj):
        if obj.thumbnail:
            # HTML: Ufak resim + Yanına Django stili buton
            html = f"""
                <div style="display: flex; align-items: center; gap: 10px;">
                    <a href="{obj.thumbnail.url}" target="_blank" class="button" style="font-size: 11px; font-weight: bold; text-decotation: none;">
                        Göster
                    </a>
                </div>
            """
            return mark_safe(html)
        
        # Resim yoksa silik bir tire
        return mark_safe('<span style="color: #ccc;">-</span>')

    get_thumbnail_button.short_description = "Kapak Görseli"