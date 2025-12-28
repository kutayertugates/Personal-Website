const profilePhoneInput = document.getElementById('profilePhone');

    profilePhoneInput.addEventListener('input', function (e) {
        // 1. Rakam olmayan her şeyi temizle
        let value = this.value.replace(/\D/g, '');

        // 2. Başlangıçtaki 90'ı temizle (Biz zaten ekleyeceğiz)
        if (value.startsWith('90')) {
            value = value.substring(2);
        }

        // 3. Uzunluğu sınırla (10 hane: 5XX...)
        value = value.substring(0, 10);

        // 4. Formatı oluştur
        let formattedValue = '';

        if (value.length > 0) {
            formattedValue = '+90 (' + value.substring(0, 3);
        }
        if (value.length >= 4) {
            formattedValue += ') ' + value.substring(3, 6);
        }
        if (value.length >= 7) {
            formattedValue += ' ' + value.substring(6, 8);
        }
        if (value.length >= 9) {
            formattedValue += ' ' + value.substring(8, 10);
        }

        // 5. Değeri güncelle
        this.value = formattedValue;
    });

    // Silme tuşu (Backspace) kontrolü - +90'ın takılı kalmaması için
    profilePhoneInput.addEventListener('keydown', function(e) {
        const key = e.key;
        if (key === 'Backspace' && this.value.length <= 6) {
             this.value = '';
        }
    });