from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Etiket Adı")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "Etiket"
        verbose_name_plural = "Etiketler"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Etiketleri her zaman küçük harfe çevirelim (UX standartı)
        # "Python" girilse bile "python" kaydedilsin.
        self.name = self.name.lower()
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Yazar')
    thumbnail = models.ImageField(upload_to='blog_thumbnail/', blank=True, null=True, verbose_name="Kapak Görseli")
    meta_title = models.CharField(max_length=60, verbose_name='Meta Başlık')
    title = models.CharField(max_length=70, verbose_name='Başlık')
    meta_description = models.CharField(max_length=160, verbose_name='Meta Açıklama')
    slug = models.SlugField(max_length=256, unique=True, db_index=True, blank=True, editable=True, verbose_name='URL')
    page_css = models.TextField(blank=True, verbose_name='Özel CSS')
    content = models.TextField(
        help_text="Makale içeriğini buraya girin. Görselleri, başlıkları (H2, H3) editör araçlarıyla ekleyin.",
        validators=[
        MinLengthValidator(
                limit_value=300, 
                message="SEO standardı gereği içerik en az 300 karakter olmalıdır."
            )
        ],
        blank=False,
        null=False,
        verbose_name='İçerik Gövdesi'
    )
    tags = models.ManyToManyField('Blog.Tag', blank=True, related_name='posts', verbose_name="Etiketler")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncelleme")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    class Meta:
        verbose_name = 'Blog Yazısı'
        verbose_name_plural = 'Blog Yazıları'
        ordering = ['-created_at']

    def __str__(self):
        # Slug yerine Title daha okunabilir
        return f'{self.title} ({self.author.username})'

    def save(self, *args, **kwargs):
        # Eğer slug girilmediyse title'dan üret
        if not self.slug:
            self.slug = slugify(self.title.replace('ı', 'i')) # Türkçe karakter fix
        super().save(*args, **kwargs)
