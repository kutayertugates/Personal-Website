// UX Logic: Sayfa yenilemeden formlar arası geçiş
function switchTab(tab) {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const btnLogin = document.getElementById('btn-login');
    const btnRegister = document.getElementById('btn-register');

    if (tab === 'login') {
        // Fade out effect
        registerForm.style.opacity = '0';
        setTimeout(() => {
            registerForm.classList.add('d-none');
            loginForm.classList.remove('d-none');
            // Fade in effect start
            setTimeout(() => {
                loginForm.style.opacity = '1';
            }, 50);
        }, 300); // CSS transition süresiyle uyumlu bekleme

        btnLogin.classList.add('active');
        btnRegister.classList.remove('active');
    } else {
        loginForm.style.opacity = '0';
        setTimeout(() => {
            loginForm.classList.add('d-none');
            registerForm.classList.remove('d-none');
            setTimeout(() => {
                registerForm.style.opacity = '1';
            }, 50);
        }, 300);

        btnRegister.classList.add('active');
        btnLogin.classList.remove('active');
    }
}


const togglePassword = document.querySelector('#togglePassword');
const passwordInput = document.querySelector('#loginPassword');

togglePassword.addEventListener('click', function (e) {
    // 1. Mevcut tipi al (password mü, text mi?)
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    
    // 2. Tipi değiştir
    passwordInput.setAttribute('type', type);

    // 3. İkonu değiştir (Göz açık <-> Göz kapalı)
    // Bootstrap icon sınıfını değiştiriyoruz
    this.classList.toggle('bi-eye');
    this.classList.toggle('bi-eye-slash');
});


const phoneInput = document.getElementById('regPhoneNumber');
phoneInput.addEventListener('input', function (e) {
    // 1. Girilen değerden rakam olmayan her şeyi sil
    // (Kullanıcı harf veya sembol giremesin, sadece temiz data kalsın)
    let value = this.value.replace(/\D/g, '');

    // 2. Eğer kullanıcı yanlışlıkla başına 90 yazarsa onu temizle
    // (Zaten biz +90 ekleyeceğiz)
    if (value.startsWith('90')) {
        value = value.substring(2);
    }

    // 3. Maksimum 10 haneye izin ver (5xx xxx xx xx)
    value = value.substring(0, 10);

    // 4. Formatı adım adım oluştur
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

    // 5. Input değerini güncelle
    this.value = formattedValue;
});

// Ufak bir UX iyileştirmesi:
// Kullanıcı silme tuşuna basıp her şeyi silerse +90 da gitsin diye kontrol
phoneInput.addEventListener('keydown', function(e) {
    const key = e.key;
    if (key === 'Backspace' && this.value.length <= 6) {
            this.value = '';
    }
});