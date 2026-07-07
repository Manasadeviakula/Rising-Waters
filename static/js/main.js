document.addEventListener('DOMContentLoaded', function() {
    console.log('🌊 Flood Prediction System loaded');
    initFormValidation();
    initHamburgerMenu();
    initFormSubmission();
    initInputAnimations();
});
function initHamburgerMenu() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');  
    if (!hamburger || !navMenu) return;    
    hamburger.addEventListener('click', function() {
        navMenu.classList.toggle('active');
        this.classList.toggle('active');
    });
}
function initFormValidation() {
    const form = document.getElementById('predictionForm');
    if (!form) return;    
    const inputs = form.querySelectorAll('input[type="number"]');
    const validationRules = {
        rainfall: { min: 0, max: 500, label: 'Rainfall' },
        river_level: { min: 0, max: 20, label: 'River Level' },
        humidity: { min: 0, max: 100, label: 'Humidity' },
        temperature: { min: -20, max: 50, label: 'Temperature' },
        wind_speed: { min: 0, max: 200, label: 'Wind Speed' },
        soil_moisture: { min: 0, max: 100, label: 'Soil Moisture' },
        pressure: { min: 900, max: 1100, label: 'Pressure' }
    };
    inputs.forEach(input => {
        const fieldName = input.id;
        const errorElement = document.getElementById(fieldName + 'Error');
        input.addEventListener('input', function() {
            validateField(this, validationRules[fieldName]);
        });
        input.addEventListener('blur', function() {
            validateField(this, validationRules[fieldName]);
        });
        input.addEventListener('change', function() {
            validateField(this, validationRules[fieldName]);
        });
    });
}
function validateField(input, rules) {
    if (!rules) return true;   
    const value = parseFloat(input.value);
    const errorElement = document.getElementById(input.id + 'Error');    
    if (!errorElement) return true;
    if (input.value === '') {
        errorElement.textContent = `${rules.label} is required`;
        errorElement.style.display = 'block';
        input.classList.remove('valid');
        input.classList.add('error');
        return false;
    }
    if (isNaN(value)) {
        errorElement.textContent = `Please enter a valid number for ${rules.label}`;
        errorElement.style.display = 'block';
        input.classList.remove('valid');
        input.classList.add('error');
        return false;
    }
    if (value < rules.min || value > rules.max) {
        errorElement.textContent = `${rules.label} must be between ${rules.min} and ${rules.max}`;
        errorElement.style.display = 'block';
        input.classList.remove('valid');
        input.classList.add('error');
        return false;
    }
    errorElement.style.display = 'none';
    input.classList.remove('error');
    input.classList.add('valid');
    return true;
}
function initFormSubmission() {
    const form = document.getElementById('predictionForm');
    if (!form) return; 
    const submitBtn = document.getElementById('predictBtn');
    const loadingSpinner = document.getElementById('loadingSpinner');   
    if (!submitBtn || !loadingSpinner) return;   
    form.addEventListener('submit', function(e) {
        const inputs = this.querySelectorAll('input[type="number"]');
        let isValid = true;
        let firstError = null;       
        inputs.forEach(input => {
            const event = new Event('blur');
            input.dispatchEvent(event);
            if (input.classList.contains('error')) {
                isValid = false;
                if (!firstError) firstError = input;
            }
        });    
        if (!isValid) {
            e.preventDefault();
            if (firstError) {
                firstError.focus();
                firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
            alert(' Please fix all validation errors before submitting.');
            return;
        }
        submitBtn.disabled = true;
        submitBtn.textContent = ' Processing with XGBoost...';
        loadingSpinner.style.display = 'block';
        setTimeout(() => {
            submitBtn.disabled = false;
            submitBtn.textContent = ' Predict Flood Risk';
            loadingSpinner.style.display = 'none';
        }, 5000);
    });
}
function initInputAnimations() {
    const inputs = document.querySelectorAll('.form-group input');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
            if (this.value !== '') {
                this.parentElement.classList.add('has-value');
            } else {
                this.parentElement.classList.remove('has-value');
            }
        });
    });
}
async function fetchPrediction(data) {
    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const result = await response.json();
        return result;
    } catch (error) {
        console.error(' API Error:', error);
        throw error;
    }
}
function showToast(message, type = 'info') {
    // Create toast container if it doesn't exist
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 9999;
            max-width: 400px;
        `;
        document.body.appendChild(container);
    } 
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.style.cssText = `
        background: ${type === 'error' ? '#e74c3c' : type === 'success' ? '#2ecc71' : '#3498db'};
        color: white;
        padding: 15px 20px;
        border-radius: 8px;
        margin-bottom: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        animation: slideIn 0.3s ease;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
    `;
    toast.textContent = message;
    container.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 5000);
}
const styleSheet = document.createElement('style');
styleSheet.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
`;
document.head.appendChild(styleSheet);
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        fetchPrediction,
        showToast,
        validateField
    };
}
console.log(' main.js loaded successfully');