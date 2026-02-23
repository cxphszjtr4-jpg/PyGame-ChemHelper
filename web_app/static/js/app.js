// State Management
let currentScreen = 'menu';
let currentLanguage = 'English';
let calcInput = '';
let currentQuizElement = null;
let quizAnswered = false;
let blinkFrame = 0;

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
    showScreen('menu');
    loadTranslations();
});

// Screen Navigation
function showScreen(screenName) {
    // Hide all screens
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
    });
    
    // Show selected screen
    const screenId = screenName + '-screen';
    const screen = document.getElementById(screenId);
    if (screen) {
        screen.classList.add('active');
        currentScreen = screenName;
        
        // Screen-specific initialization
        if (screenName === 'quiz') {
            nextQuizQuestion();
        } else if (screenName === 'calculator') {
            calcReset();
        } else if (screenName === 'chemhelper') {
            document.getElementById('element-search').focus();
        }
    }
}

// ========== ChemHelper Functions ==========
function searchElement() {
    const searchInput = document.getElementById('element-search');
    const searchTerm = searchInput.value.trim();
    
    if (!searchTerm) {
        document.getElementById('element-info').style.display = 'none';
        document.getElementById('enter-element').style.display = 'block';
        return;
    }
    
    fetch('/api/search_element', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ search: searchTerm })
    })
    .then(response => response.json())
    .then(data => {
        if (data.found) {
            displayElement(data.element);
        } else {
            document.getElementById('element-info').style.display = 'none';
            document.getElementById('enter-element').textContent = 'Element not found. Try searching by name, symbol, or atomic number.';
            document.getElementById('enter-element').style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
}

function displayElement(element) {
    document.getElementById('element-name').textContent = element.name + ' (' + element.symbol + ')';
    document.getElementById('element-atomic').textContent = 'Atomic Number: ' + element.atomic_number;
    document.getElementById('element-protons').textContent = 'Protons: ' + element.protons;
    document.getElementById('element-neutrons').textContent = 'Neutrons: ' + element.neutrons;
    document.getElementById('charge-input').value = '0';
    document.getElementById('element-info').style.display = 'block';
    document.getElementById('enter-element').style.display = 'none';
    
    // Store element for electron calculation
    window.currentElement = element;
}

function updateElectrons() {
    if (!window.currentElement) return;
    
    const charge = parseInt(document.getElementById('charge-input').value) || 0;
    const electrons = window.currentElement.electrons - charge;
    
    // Update display
    const info = document.querySelector('.element-box');
    let electronLine = info.querySelector('.electron-line');
    if (!electronLine) {
        electronLine = document.createElement('p');
        electronLine.className = 'electron-line';
        info.insertBefore(electronLine, info.querySelector('.charge-section'));
    }
    electronLine.textContent = 'Electrons: ' + electrons;
}

function clearSearch() {
    document.getElementById('element-search').value = '';
    document.getElementById('element-info').style.display = 'none';
    document.getElementById('enter-element').style.display = 'block';
    document.getElementById('element-search').focus();
}

// ========== Calculator Functions ==========
function calcInput(value) {
    const display = document.getElementById('calc-display');
    
    if (value === '=') {
        try {
            const result = Function('"use strict"; return (' + calcInput + ')')();
            display.textContent = result;
            calcInput = '';
        } catch (e) {
            display.textContent = 'Error';
            calcInput = '';
        }
    } else if (value === 'C') {
        calcReset();
    } else {
        calcInput += value;
        display.textContent = calcInput || '0';
    }
}

function calcClear() {
    calcReset();
}

function calcReset() {
    calcInput = '';
    document.getElementById('calc-display').textContent = '0';
}

// ========== Quiz Functions ==========
function nextQuizQuestion() {
    quizAnswered = false;
    document.getElementById('quiz-answer').value = '';
    document.getElementById('quiz-feedback').style.display = 'none';
    document.getElementById('quiz-submit').style.display = 'inline-block';
    document.getElementById('quiz-next').style.display = 'none';
    
    fetch('/api/get_quiz_question')
        .then(response => response.json())
        .then(data => {
            currentQuizElement = data;
            document.getElementById('quiz-question').textContent = 
                'What is the atomic number of ' + data.name + '?';
            document.getElementById('quiz-answer').focus();
        })
        .catch(error => console.error('Error:', error));
}

function submitQuizAnswer() {
    if (quizAnswered) return;
    
    const answerInput = document.getElementById('quiz-answer');
    const answer = parseInt(answerInput.value);
    
    if (isNaN(answer)) {
        document.getElementById('quiz-feedback').textContent = 'Please enter a valid number';
        document.getElementById('quiz-feedback').style.display = 'block';
        return;
    }
    
    fetch('/api/check_quiz_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            answer: answer,
            atomic_number: currentQuizElement.atomic_number
        })
    })
    .then(response => response.json())
    .then(data => {
        quizAnswered = true;
        const feedback = document.getElementById('quiz-feedback');
        feedback.style.display = 'block';
        
        if (data.correct) {
            feedback.textContent = '✓ Correct! The atomic number of ' + currentQuizElement.name + ' is ' + currentQuizElement.atomic_number;
            feedback.className = 'quiz-feedback correct';
        } else {
            feedback.textContent = '✗ Incorrect. The correct answer is ' + currentQuizElement.atomic_number;
            feedback.className = 'quiz-feedback incorrect';
        }
        
        document.getElementById('quiz-submit').style.display = 'none';
        document.getElementById('quiz-next').style.display = 'inline-block';
    })
    .catch(error => console.error('Error:', error));
}

// ========== Settings Functions ==========
function setLanguage(language) {
    currentLanguage = language;
    
    // Update button highlighting
    document.querySelectorAll('.language-buttons .btn').forEach(btn => {
        btn.classList.remove('active-lang');
    });
    event.target.classList.add('active-lang');
    
    // Update UI text
    updateUIText();
}

function loadTranslations() {
    fetch('/api/translations')
        .then(response => response.json())
        .then(data => {
            window.translations = data;
            updateUIText();
        })
        .catch(error => console.error('Error:', error));
}

function updateUIText() {
    if (!window.translations) return;
    
    // Update menu buttons
    const menuButtons = document.querySelectorAll('#menu-screen .btn');
    const menuLabels = ['ChemHelper', 'Calculator', 'Quiz', 'Settings'];
    
    // Update all text based on language
    const transDict = window.translations[currentLanguage] || window.translations['English'];
    
    // This would need translation keys in your backend
    // For now, keeping English labels visible
}

// ========== Utility Functions ==========
function blinkCursor(elementId) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    blinkFrame++;
    if (blinkFrame % 30 < 15) {
        element.style.borderColor = '#FF69B4';
    } else {
        element.style.borderColor = '#193782';
    }
}

// Animation loop for blinking cursors
setInterval(() => {
    blinkCursor('element-search');
    blinkCursor('quiz-answer');
}, 100);
