from django.db import models
from django.core.exceptions import ValidationError

class DynamicContent(models.Model):
    # Bu alan bizim anahtarımız olacak (Örn: 'navbar_logo', 'footer_text')
    title = models.CharField(max_length=100, unique=True, verbose_name="Anahtar (Key)")
    
    # Yönetici için not alanı (Zorunlu değil)
    description = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    
    # İçerik alanları
    html_content = models.TextField(blank=True, null=True, verbose_name="HTML/Yazı İçeriği")
    image = models.ImageField(upload_to='dynamic_contents/', blank=True, null=True, verbose_name="Görsel")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Dinamik İçerik"
        verbose_name_plural = "Dinamik İçerikler"

    def __str__(self):
        return self.title

    def clean(self):
        # Admin panelinde kaydet butonuna basınca çalışır
        if self.html_content and self.image:
            raise ValidationError("Hem HTML içerik hem de Resim aynı anda olamaz! Lütfen birini seçin.")
        
        if not self.html_content and not self.image:
            raise ValidationError("En az bir içerik (HTML veya Resim) girmelisiniz.")

    def save(self, *args, **kwargs):
        self.full_clean() # Kodla kayıt yapılırsa da validation çalışsın
        super().save(*args, **kwargs)