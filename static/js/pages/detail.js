document.addEventListener('DOMContentLoaded', function() {
    // Elemanları seç
    const galleryItems = document.querySelectorAll('.gallery-item');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.querySelector('.lightbox-close');

    // Her galeri öğesine tıklama olayı ekle
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const imgSource = this.querySelector('img').src;
            
            // Resmi yükle
            lightboxImg.src = imgSource;
            
            // Lightbox'ı aç
            lightbox.classList.add('active');
            
            // Scroll'u kilitle (Arkada sayfa kaymasın)
            document.body.style.overflow = 'hidden';
        });
    });

    // Kapatma fonksiyonu
    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = 'auto'; // Scroll'u geri aç
        
        // Animasyon bitince resmi temizle (kısa bir gecikme ile)
        setTimeout(() => {
            lightboxImg.src = '';
        }, 300);
    }

    // X butonuna basınca kapat
    closeBtn.addEventListener('click', closeLightbox);

    // Siyah alana (resim dışına) basınca kapat
    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    // ESC tuşuna basınca kapat
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
            closeLightbox();
        }
    });
});