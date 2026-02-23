from flask import Flask, render_template, request, jsonify
import random
import os

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
            static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# Element database - All 118 Elements
ELEMENTS = [
    {"atomic_number": 1, "name": "Hydrogen", "symbol": "H", "protons": 1, "neutrons": 0, "electrons": 1},
    {"atomic_number": 2, "name": "Helium", "symbol": "He", "protons": 2, "neutrons": 2, "electrons": 2},
    {"atomic_number": 3, "name": "Lithium", "symbol": "Li", "protons": 3, "neutrons": 4, "electrons": 3},
    {"atomic_number": 4, "name": "Beryllium", "symbol": "Be", "protons": 4, "neutrons": 5, "electrons": 4},
    {"atomic_number": 5, "name": "Boron", "symbol": "B", "protons": 5, "neutrons": 6, "electrons": 5},
    {"atomic_number": 6, "name": "Carbon", "symbol": "C", "protons": 6, "neutrons": 6, "electrons": 6},
    {"atomic_number": 7, "name": "Nitrogen", "symbol": "N", "protons": 7, "neutrons": 7, "electrons": 7},
    {"atomic_number": 8, "name": "Oxygen", "symbol": "O", "protons": 8, "neutrons": 8, "electrons": 8},
    {"atomic_number": 9, "name": "Fluorine", "symbol": "F", "protons": 9, "neutrons": 10, "electrons": 9},
    {"atomic_number": 10, "name": "Neon", "symbol": "Ne", "protons": 10, "neutrons": 10, "electrons": 10},
    {"atomic_number": 11, "name": "Sodium", "symbol": "Na", "protons": 11, "neutrons": 12, "electrons": 11},
    {"atomic_number": 12, "name": "Magnesium", "symbol": "Mg", "protons": 12, "neutrons": 12, "electrons": 12},
    {"atomic_number": 13, "name": "Aluminum", "symbol": "Al", "protons": 13, "neutrons": 14, "electrons": 13},
    {"atomic_number": 14, "name": "Silicon", "symbol": "Si", "protons": 14, "neutrons": 14, "electrons": 14},
    {"atomic_number": 15, "name": "Phosphorus", "symbol": "P", "protons": 15, "neutrons": 16, "electrons": 15},
    {"atomic_number": 16, "name": "Sulfur", "symbol": "S", "protons": 16, "neutrons": 16, "electrons": 16},
    {"atomic_number": 17, "name": "Chlorine", "symbol": "Cl", "protons": 17, "neutrons": 18, "electrons": 17},
    {"atomic_number": 18, "name": "Argon", "symbol": "Ar", "protons": 18, "neutrons": 22, "electrons": 18},
    {"atomic_number": 19, "name": "Potassium", "symbol": "K", "protons": 19, "neutrons": 20, "electrons": 19},
    {"atomic_number": 20, "name": "Calcium", "symbol": "Ca", "protons": 20, "neutrons": 20, "electrons": 20},
    {"atomic_number": 21, "name": "Scandium", "symbol": "Sc", "protons": 21, "neutrons": 24, "electrons": 21},
    {"atomic_number": 22, "name": "Titanium", "symbol": "Ti", "protons": 22, "neutrons": 26, "electrons": 22},
    {"atomic_number": 23, "name": "Vanadium", "symbol": "V", "protons": 23, "neutrons": 28, "electrons": 23},
    {"atomic_number": 24, "name": "Chromium", "symbol": "Cr", "protons": 24, "neutrons": 28, "electrons": 24},
    {"atomic_number": 25, "name": "Manganese", "symbol": "Mn", "protons": 25, "neutrons": 30, "electrons": 25},
    {"atomic_number": 26, "name": "Iron", "symbol": "Fe", "protons": 26, "neutrons": 30, "electrons": 26},
    {"atomic_number": 27, "name": "Cobalt", "symbol": "Co", "protons": 27, "neutrons": 32, "electrons": 27},
    {"atomic_number": 28, "name": "Nickel", "symbol": "Ni", "protons": 28, "neutrons": 31, "electrons": 28},
    {"atomic_number": 29, "name": "Copper", "symbol": "Cu", "protons": 29, "neutrons": 34, "electrons": 29},
    {"atomic_number": 30, "name": "Zinc", "symbol": "Zn", "protons": 30, "neutrons": 35, "electrons": 30},
    {"atomic_number": 31, "name": "Gallium", "symbol": "Ga", "protons": 31, "neutrons": 39, "electrons": 31},
    {"atomic_number": 32, "name": "Germanium", "symbol": "Ge", "protons": 32, "neutrons": 41, "electrons": 32},
    {"atomic_number": 33, "name": "Arsenic", "symbol": "As", "protons": 33, "neutrons": 42, "electrons": 33},
    {"atomic_number": 34, "name": "Selenium", "symbol": "Se", "protons": 34, "neutrons": 45, "electrons": 34},
    {"atomic_number": 35, "name": "Bromine", "symbol": "Br", "protons": 35, "neutrons": 45, "electrons": 35},
    {"atomic_number": 36, "name": "Krypton", "symbol": "Kr", "protons": 36, "neutrons": 48, "electrons": 36},
    {"atomic_number": 37, "name": "Rubidium", "symbol": "Rb", "protons": 37, "neutrons": 48, "electrons": 37},
    {"atomic_number": 38, "name": "Strontium", "symbol": "Sr", "protons": 38, "neutrons": 50, "electrons": 38},
    {"atomic_number": 39, "name": "Yttrium", "symbol": "Y", "protons": 39, "neutrons": 50, "electrons": 39},
    {"atomic_number": 40, "name": "Zirconium", "symbol": "Zr", "protons": 40, "neutrons": 51, "electrons": 40},
    {"atomic_number": 41, "name": "Niobium", "symbol": "Nb", "protons": 41, "neutrons": 52, "electrons": 41},
    {"atomic_number": 42, "name": "Molybdenum", "symbol": "Mo", "protons": 42, "neutrons": 54, "electrons": 42},
    {"atomic_number": 43, "name": "Technetium", "symbol": "Tc", "protons": 43, "neutrons": 55, "electrons": 43},
    {"atomic_number": 44, "name": "Ruthenium", "symbol": "Ru", "protons": 44, "neutrons": 57, "electrons": 44},
    {"atomic_number": 45, "name": "Rhodium", "symbol": "Rh", "protons": 45, "neutrons": 58, "electrons": 45},
    {"atomic_number": 46, "name": "Palladium", "symbol": "Pd", "protons": 46, "neutrons": 60, "electrons": 46},
    {"atomic_number": 47, "name": "Silver", "symbol": "Ag", "protons": 47, "neutrons": 61, "electrons": 47},
    {"atomic_number": 48, "name": "Cadmium", "symbol": "Cd", "protons": 48, "neutrons": 64, "electrons": 48},
    {"atomic_number": 49, "name": "Indium", "symbol": "In", "protons": 49, "neutrons": 66, "electrons": 49},
    {"atomic_number": 50, "name": "Tin", "symbol": "Sn", "protons": 50, "neutrons": 69, "electrons": 50},
    {"atomic_number": 51, "name": "Antimony", "symbol": "Sb", "protons": 51, "neutrons": 71, "electrons": 51},
    {"atomic_number": 52, "name": "Tellurium", "symbol": "Te", "protons": 52, "neutrons": 76, "electrons": 52},
    {"atomic_number": 53, "name": "Iodine", "symbol": "I", "protons": 53, "neutrons": 74, "electrons": 53},
    {"atomic_number": 54, "name": "Xenon", "symbol": "Xe", "protons": 54, "neutrons": 77, "electrons": 54},
    {"atomic_number": 55, "name": "Cesium", "symbol": "Cs", "protons": 55, "neutrons": 78, "electrons": 55},
    {"atomic_number": 56, "name": "Barium", "symbol": "Ba", "protons": 56, "neutrons": 81, "electrons": 56},
    {"atomic_number": 57, "name": "Lanthanum", "symbol": "La", "protons": 57, "neutrons": 82, "electrons": 57},
    {"atomic_number": 58, "name": "Cerium", "symbol": "Ce", "protons": 58, "neutrons": 82, "electrons": 58},
    {"atomic_number": 59, "name": "Praseodymium", "symbol": "Pr", "protons": 59, "neutrons": 82, "electrons": 59},
    {"atomic_number": 60, "name": "Neodymium", "symbol": "Nd", "protons": 60, "neutrons": 84, "electrons": 60},
    {"atomic_number": 61, "name": "Promethium", "symbol": "Pm", "protons": 61, "neutrons": 84, "electrons": 61},
    {"atomic_number": 62, "name": "Samarium", "symbol": "Sm", "protons": 62, "neutrons": 88, "electrons": 62},
    {"atomic_number": 63, "name": "Europium", "symbol": "Eu", "protons": 63, "neutrons": 89, "electrons": 63},
    {"atomic_number": 64, "name": "Gadolinium", "symbol": "Gd", "protons": 64, "neutrons": 93, "electrons": 64},
    {"atomic_number": 65, "name": "Terbium", "symbol": "Tb", "protons": 65, "neutrons": 94, "electrons": 65},
    {"atomic_number": 66, "name": "Dysprosium", "symbol": "Dy", "protons": 66, "neutrons": 97, "electrons": 66},
    {"atomic_number": 67, "name": "Holmium", "symbol": "Ho", "protons": 67, "neutrons": 98, "electrons": 67},
    {"atomic_number": 68, "name": "Erbium", "symbol": "Er", "protons": 68, "neutrons": 99, "electrons": 68},
    {"atomic_number": 69, "name": "Thulium", "symbol": "Tm", "protons": 69, "neutrons": 100, "electrons": 69},
    {"atomic_number": 70, "name": "Ytterbium", "symbol": "Yb", "protons": 70, "neutrons": 103, "electrons": 70},
    {"atomic_number": 71, "name": "Lutetium", "symbol": "Lu", "protons": 71, "neutrons": 104, "electrons": 71},
    {"atomic_number": 72, "name": "Hafnium", "symbol": "Hf", "protons": 72, "neutrons": 106, "electrons": 72},
    {"atomic_number": 73, "name": "Tantalum", "symbol": "Ta", "protons": 73, "neutrons": 108, "electrons": 73},
    {"atomic_number": 74, "name": "Tungsten", "symbol": "W", "protons": 74, "neutrons": 110, "electrons": 74},
    {"atomic_number": 75, "name": "Rhenium", "symbol": "Re", "protons": 75, "neutrons": 111, "electrons": 75},
    {"atomic_number": 76, "name": "Osmium", "symbol": "Os", "protons": 76, "neutrons": 114, "electrons": 76},
    {"atomic_number": 77, "name": "Iridium", "symbol": "Ir", "protons": 77, "neutrons": 115, "electrons": 77},
    {"atomic_number": 78, "name": "Platinum", "symbol": "Pt", "protons": 78, "neutrons": 117, "electrons": 78},
    {"atomic_number": 79, "name": "Gold", "symbol": "Au", "protons": 79, "neutrons": 118, "electrons": 79},
    {"atomic_number": 80, "name": "Mercury", "symbol": "Hg", "protons": 80, "neutrons": 121, "electrons": 80},
    {"atomic_number": 81, "name": "Thallium", "symbol": "Tl", "protons": 81, "neutrons": 123, "electrons": 81},
    {"atomic_number": 82, "name": "Lead", "symbol": "Pb", "protons": 82, "neutrons": 126, "electrons": 82},
    {"atomic_number": 83, "name": "Bismuth", "symbol": "Bi", "protons": 83, "neutrons": 126, "electrons": 83},
    {"atomic_number": 84, "name": "Polonium", "symbol": "Po", "protons": 84, "neutrons": 125, "electrons": 84},
    {"atomic_number": 85, "name": "Astatine", "symbol": "At", "protons": 85, "neutrons": 125, "electrons": 85},
    {"atomic_number": 86, "name": "Radon", "symbol": "Rn", "protons": 86, "neutrons": 136, "electrons": 86},
    {"atomic_number": 87, "name": "Francium", "symbol": "Fr", "protons": 87, "neutrons": 136, "electrons": 87},
    {"atomic_number": 88, "name": "Radium", "symbol": "Ra", "protons": 88, "neutrons": 138, "electrons": 88},
    {"atomic_number": 89, "name": "Actinium", "symbol": "Ac", "protons": 89, "neutrons": 138, "electrons": 89},
    {"atomic_number": 90, "name": "Thorium", "symbol": "Th", "protons": 90, "neutrons": 142, "electrons": 90},
    {"atomic_number": 91, "name": "Protactinium", "symbol": "Pa", "protons": 91, "neutrons": 140, "electrons": 91},
    {"atomic_number": 92, "name": "Uranium", "symbol": "U", "protons": 92, "neutrons": 146, "electrons": 92},
    {"atomic_number": 93, "name": "Neptunium", "symbol": "Np", "protons": 93, "neutrons": 144, "electrons": 93},
    {"atomic_number": 94, "name": "Plutonium", "symbol": "Pu", "protons": 94, "neutrons": 150, "electrons": 94},
    {"atomic_number": 95, "name": "Americium", "symbol": "Am", "protons": 95, "neutrons": 148, "electrons": 95},
    {"atomic_number": 96, "name": "Curium", "symbol": "Cm", "protons": 96, "neutrons": 151, "electrons": 96},
    {"atomic_number": 97, "name": "Berkelium", "symbol": "Bk", "protons": 97, "neutrons": 150, "electrons": 97},
    {"atomic_number": 98, "name": "Californium", "symbol": "Cf", "protons": 98, "neutrons": 153, "electrons": 98},
    {"atomic_number": 99, "name": "Einsteinium", "symbol": "Es", "protons": 99, "neutrons": 157, "electrons": 99},
    {"atomic_number": 100, "name": "Fermium", "symbol": "Fm", "protons": 100, "neutrons": 157, "electrons": 100},
    {"atomic_number": 101, "name": "Mendelevium", "symbol": "Md", "protons": 101, "neutrons": 157, "electrons": 101},
    {"atomic_number": 102, "name": "Nobelium", "symbol": "No", "protons": 102, "neutrons": 157, "electrons": 102},
    {"atomic_number": 103, "name": "Lawrencium", "symbol": "Lr", "protons": 103, "neutrons": 159, "electrons": 103},
    {"atomic_number": 104, "name": "Rutherfordium", "symbol": "Rf", "protons": 104, "neutrons": 161, "electrons": 104},
    {"atomic_number": 105, "name": "Dubnium", "symbol": "Db", "protons": 105, "neutrons": 163, "electrons": 105},
    {"atomic_number": 106, "name": "Seaborgium", "symbol": "Sg", "protons": 106, "neutrons": 165, "electrons": 106},
    {"atomic_number": 107, "name": "Bohrium", "symbol": "Bh", "protons": 107, "neutrons": 163, "electrons": 107},
    {"atomic_number": 108, "name": "Hassium", "symbol": "Hs", "protons": 108, "neutrons": 169, "electrons": 108},
    {"atomic_number": 109, "name": "Meitnerium", "symbol": "Mt", "protons": 109, "neutrons": 167, "electrons": 109},
    {"atomic_number": 110, "name": "Darmstadtium", "symbol": "Ds", "protons": 110, "neutrons": 171, "electrons": 110},
    {"atomic_number": 111, "name": "Roentgenium", "symbol": "Rg", "protons": 111, "neutrons": 171, "electrons": 111},
    {"atomic_number": 112, "name": "Copernicium", "symbol": "Cn", "protons": 112, "neutrons": 173, "electrons": 112},
    {"atomic_number": 113, "name": "Nihonium", "symbol": "Nh", "protons": 113, "neutrons": 173, "electrons": 113},
    {"atomic_number": 114, "name": "Flerovium", "symbol": "Fl", "protons": 114, "neutrons": 175, "electrons": 114},
    {"atomic_number": 115, "name": "Moscovium", "symbol": "Mc", "protons": 115, "neutrons": 173, "electrons": 115},
    {"atomic_number": 116, "name": "Livermorium", "symbol": "Lv", "protons": 116, "neutrons": 176, "electrons": 116},
    {"atomic_number": 117, "name": "Tennessine", "symbol": "Ts", "protons": 117, "neutrons": 176, "electrons": 117},
    {"atomic_number": 118, "name": "Oganesson", "symbol": "Og", "protons": 118, "neutrons": 176, "electrons": 118},
]

# Translations
TRANSLATIONS = {
    "English": {
        "title": "ChemHelper",
        "subtitle": "Chemistry Assistant",
        "periodic": "ChemHelper",
        "calculator": "Calculator",
        "quiz": "Quiz",
        "settings": "Settings",
        "back": "Back",
        "search_label": "Search by name, symbol, or atomic number:",
        "type_here": "Type here...",
        "element": "Element",
        "atomic_number": "Atomic Number",
        "protons": "Protons",
        "electrons": "Electrons (neutral)",
        "neutrons": "Neutrons",
        "electrons_ionic": "Electrons (ionic)",
        "charge": "Charge",
        "clear": "Clear",
        "language": "Language",
        "enter_element": "Enter an element to search!",
        "quiz_title": "Chemistry Quiz",
        "question": "What is the atomic number of",
        "correct": "Correct!",
        "wrong": "Wrong! The answer is",
        "next_question": "Next Question",
        "submit": "Submit",
    },
    "Spanish": {
        "title": "ChemHelper",
        "subtitle": "Asistente de Química",
        "periodic": "ChemHelper",
        "calculator": "Calculadora",
        "quiz": "Quiz",
        "settings": "Configuración",
        "back": "Atrás",
        "search_label": "Buscar por nombre, símbolo o número atómico:",
        "type_here": "Escribe aquí...",
        "element": "Elemento",
        "atomic_number": "Número Atómico",
        "protons": "Protones",
        "electrons": "Electrones (neutral)",
        "neutrons": "Neutrones",
        "electrons_ionic": "Electrones (iónico)",
        "charge": "Carga",
        "clear": "Limpiar",
        "language": "Idioma",
        "enter_element": "¡Ingresa un elemento para buscar!",
        "quiz_title": "Quiz de Química",
        "question": "¿Cuál es el número atómico de",
        "correct": "¡Correcto!",
        "wrong": "¡Incorrecto! La respuesta es",
        "next_question": "Siguiente Pregunta",
        "submit": "Enviar",
    },
    "French": {
        "title": "ChemHelper",
        "subtitle": "Assistant Chimie",
        "periodic": "ChemHelper",
        "calculator": "Calculatrice",
        "quiz": "Quiz",
        "settings": "Paramètres",
        "back": "Retour",
        "search_label": "Rechercher par nom, symbole ou numéro atomique:",
        "type_here": "Tapez ici...",
        "element": "Élément",
        "atomic_number": "Numéro Atomique",
        "protons": "Protons",
        "electrons": "Électrons (neutre)",
        "neutrons": "Neutrons",
        "electrons_ionic": "Électrons (ionique)",
        "charge": "Charge",
        "clear": "Effacer",
        "language": "Langue",
        "enter_element": "Entrez un élément à rechercher!",
        "quiz_title": "Quiz de Chimie",
        "question": "Quel est le numéro atomique de",
        "correct": "Correct!",
        "wrong": "Faux! La réponse est",
        "next_question": "Question Suivante",
        "submit": "Envoyer",
    }
}

@app.route('/')
def index():
    with open('templates/index.html', 'r') as f:
        html_content = f.read()
    return html_content

@app.route('/api/search_element', methods=['POST'])
def search_element():
    data = request.json
    search_term = data.get('search', '').strip()
    
    if not search_term:
        return jsonify({"found": False})
    
    # Try to match by atomic number
    try:
        atomic_num = int(search_term)
        for element in ELEMENTS:
            if element["atomic_number"] == atomic_num:
                return jsonify({"found": True, "element": element})
    except ValueError:
        pass
    
    # Search by name or symbol
    search_lower = search_term.lower()
    for element in ELEMENTS:
        if element["name"].lower() == search_lower or element["symbol"].lower() == search_lower:
            return jsonify({"found": True, "element": element})
    
    return jsonify({"found": False})

@app.route('/api/get_quiz_question', methods=['GET'])
def get_quiz_question():
    element = random.choice(ELEMENTS)
    return jsonify({"element": element})

@app.route('/api/check_quiz_answer', methods=['POST'])
def check_quiz_answer():
    data = request.json
    answer = data.get('answer')
    atomic_number = data.get('atomic_number')
    
    try:
        answer = int(answer)
        if answer == atomic_number:
            return jsonify({"correct": True})
        else:
            return jsonify({"correct": False, "answer": atomic_number})
    except ValueError:
        return jsonify({"correct": False, "answer": atomic_number})

@app.route('/api/translations')
def get_translations():
    return jsonify(TRANSLATIONS)

if __name__ == '__main__':
    # Run without the debugger/reloader to avoid background suspension issues
    # Port 5000 may be occupied on some macOS systems (AirPlay / Control Center).
    # Use 5001 to avoid conflicts.
    app.run(host='127.0.0.1', port=5001, debug=False)
