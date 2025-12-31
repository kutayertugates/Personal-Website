document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const activeTags = urlParams.getAll("tag");

    // 1. Durum Kontrolü (State Check): URL'deki tagleri bul ve butonları boya
    if (activeTags.length === 0) {
        // Hiç filtre yoksa "Tümü" aktiftir
        document.getElementById("btn-reset").classList.add("active");
    } else {
        activeTags.forEach(tag => {
            // data-tag değeri eşleşen butonu bul
            const btn = document.querySelector(`.filter-pill[data-tag="${tag}"]`);
            if (btn) {
                btn.classList.add("active");
            }
        });
    }
});

// 2. Tıklama Mantığı (Interaction Logic)
function handleTagClick(tagSlug) {
    const urlParams = new URLSearchParams(window.location.search);
    let currentTags = urlParams.getAll("tag");
    const currentQuery = urlParams.get("q"); // Arama metnini koru

    if (currentTags.includes(tagSlug)) {
        // Varsa çıkar (Toggle Off)
        currentTags = currentTags.filter(t => t !== tagSlug);
    } else {
        // Yoksa ekle (Toggle On)
        currentTags.push(tagSlug);
    }

    // Yeni URL'yi inşa et
    const newParams = new URLSearchParams();
    currentTags.forEach(t => newParams.append("tag", t));
    if (currentQuery) newParams.set("q", currentQuery);

    // Sayfayı yönlendir (Performans için aynı sekmede)
    window.location.search = newParams.toString();
}

// Filtreleri Sıfırla
function resetFilters() {
    // window.location.search'i boş bir stringe eşitlemek, 
    // URL'deki tüm parametreleri (?q=...&tag=...) siler ve sayfayı yeniler.
    window.location.search = "";
}