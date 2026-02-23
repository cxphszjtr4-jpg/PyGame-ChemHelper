# ChemHelper Web Application

A web-based chemistry education assistant with element lookup, calculator, and quiz features.

## Features

- **ChemHelper**: Search and display information about all 118 chemical elements
- **Calculator**: Full arithmetic calculator with support for basic operations
- **Quiz**: Random element trivia questions testing atomic number knowledge
- **Settings**: Language selection (English, Spanish, French)
- **Multi-language Support**: Complete UI translation in 3 languages

## Installation

1. **Install Flask** (if not already installed):
```bash
pip install flask
```

2. **Run the Flask server**:
```bash
cd /Users/kalebfowler/Desktop/"PyGame ChemHelper"/web_app
python app.py
```

3. **Open in browser**:
```
http://localhost:5000
```

## Project Structure

```
web_app/
├── app.py                    # Flask backend with API routes
├── templates/
│   └── index.html           # Main HTML template
└── static/
    ├── css/
    │   └── style.css        # Styling and layout
    └── js/
        └── app.js           # JavaScript for interactivity
```

## API Routes

- `GET /` - Serves the main web interface
- `POST /api/search_element` - Search for an element by name, symbol, or atomic number
- `GET /api/get_quiz_question` - Get a random element for quiz
- `POST /api/check_quiz_answer` - Check quiz answer
- `GET /api/translations` - Get all translation dictionaries

## Usage

### ChemHelper
1. Click "ChemHelper" from the menu
2. Enter an element name, symbol, or atomic number
3. View element information (protons, neutrons, electrons)
4. Adjust charge to see ionic electrons

### Calculator
1. Click "Calculator" from the menu
2. Use buttons to perform calculations
3. Supports: +, -, *, /, =, and decimal points

### Quiz
1. Click "Quiz" from the menu
2. A random element will be displayed
3. Enter the atomic number
4. Get instant feedback
5. Move to the next question

### Settings
1. Click "Settings" from the menu
2. Choose your preferred language
3. UI will update immediately

## Browser Compatibility

Works on modern browsers (Chrome, Firefox, Safari, Edge)

## Notes

- The app uses Jinja2 templating for Flask
- All 118 elements from the periodic table are available
- Fully responsive design for different screen sizes
