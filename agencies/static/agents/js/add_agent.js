document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.querySelector('input[type="file"]');
    const preview = document.createElement('img');
    preview.className = 'image-preview';
    
    fileInput.after(preview);

    fileInput.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            
            reader.onload = function(e) {
                preview.src = e.target.result;
                preview.style.display = 'block';
            }
            
            reader.readAsDataURL(file);
        } else {
            preview.style.display = 'none';
            preview.src = '';
        }
    });

    // Создаем кастомный элемент для загрузки файла
    const customUpload = document.createElement('label');
    customUpload.className = 'custom-file-upload';
    customUpload.innerHTML = '<i class="fas fa-cloud-upload-alt"></i> Выберите фото агента';
    fileInput.before(customUpload);

    // Обновляем текст при выборе файла
    fileInput.addEventListener('change', function() {
        const fileName = this.files[0] ? this.files[0].name : 'Выберите фото агента';
        customUpload.innerHTML = `<i class="fas fa-file-image"></i> ${fileName}`;
    });

    // Валидация формы
    const form = document.querySelector('.add-agent-form');
    form.addEventListener('submit', function(e) {
        let isValid = true;
        const requiredFields = form.querySelectorAll('[required]');
        
        requiredFields.forEach(field => {
            if (!field.value) {
                isValid = false;
                showError(field, 'Это поле обязательно для заполнения');
            } else {
                clearError(field);
            }
        });

        if (!isValid) {
            e.preventDefault();
        }
    });

    // Функции для отображения/скрытия ошибок
    function showError(field, message) {
        clearError(field);
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = message;
        field.parentNode.appendChild(errorDiv);
        field.classList.add('error');
    }

    function clearError(field) {
        const errorDiv = field.parentNode.querySelector('.error-message');
        if (errorDiv) {
            errorDiv.remove();
        }
        field.classList.remove('error');
    }

    // Анимация при наведении на поля
    const formInputs = form.querySelectorAll('input, select, textarea');
    formInputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentNode.classList.add('focused');
        });

        input.addEventListener('blur', function() {
            if (!this.value) {
                this.parentNode.classList.remove('focused');
            }
        });
    });

    // Добавляем подсказки при заполнении
    const nameInput = form.querySelector('input[name="name"]');
    if (nameInput) {
        nameInput.addEventListener('input', function() {
            const value = this.value;
            if (value && !/^[а-яА-ЯёЁ\s-]+$/.test(value)) {
                showError(this, 'Используйте только русские буквы, пробелы и дефис');
            } else {
                clearError(this);
            }
        });
    }

    // Маска для телефона (если есть поле телефона)
    const phoneInput = form.querySelector('input[name="credit"]');
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            let value = this.value.replace(/\D/g, '');
            if (value.length > 0) {
                if (value[0] === '7' || value[0] === '8') {
                    value = value.substring(1);
                }
                const matches = value.match(/(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
                this.value = '+7 ' + 
                    (matches[1] ? '(' + matches[1] + ') ' : '') +
                    (matches[2] ? matches[2] : '') +
                    (matches[3] ? '-' + matches[3] : '') +
                    (matches[4] ? '-' + matches[4] : '');
            }
        });
    }

    // Добавляем анимацию при успешной отправке
    form.addEventListener('submit', function(e) {
        if (form.checkValidity()) {
            const submitButton = form.querySelector('.submit-button');
            submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Отправка...';
            submitButton.disabled = true;
        }
    });
});

// Добавляем красивые эффекты при скролле
window.addEventListener('scroll', function() {
    const formContainer = document.querySelector('.form-container');
    const rect = formContainer.getBoundingClientRect();
    
    if (rect.top < window.innerHeight && rect.bottom >= 0) {
        formContainer.classList.add('visible');
    }
});