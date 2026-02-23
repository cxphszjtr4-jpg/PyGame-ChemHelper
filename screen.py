import pygame
from enum import Enum
import random

class ScreenState(Enum):
    """Enum for different screen states"""
    MENU = 1
    PERIODIC_TABLE = 2
    CALCULATOR = 3
    SETTINGS = 4
    QUIZ = 5

# Element database
ELEMENTS = [
    {"atomic_number": 1, "name": "Hydrogen", "symbol": "H", "electrons": 1, "protons": 1, "neutrons": 0},
    {"atomic_number": 2, "name": "Helium", "symbol": "He", "electrons": 2, "protons": 2, "neutrons": 2},
    {"atomic_number": 3, "name": "Lithium", "symbol": "Li", "electrons": 3, "protons": 3, "neutrons": 4},
    {"atomic_number": 4, "name": "Beryllium", "symbol": "Be", "electrons": 4, "protons": 4, "neutrons": 5},
    {"atomic_number": 5, "name": "Boron", "symbol": "B", "electrons": 5, "protons": 5, "neutrons": 6},
    {"atomic_number": 6, "name": "Carbon", "symbol": "C", "electrons": 6, "protons": 6, "neutrons": 6},
    {"atomic_number": 7, "name": "Nitrogen", "symbol": "N", "electrons": 7, "protons": 7, "neutrons": 7},
    {"atomic_number": 8, "name": "Oxygen", "symbol": "O", "electrons": 8, "protons": 8, "neutrons": 8},
    {"atomic_number": 9, "name": "Fluorine", "symbol": "F", "electrons": 9, "protons": 9, "neutrons": 10},
    {"atomic_number": 10, "name": "Neon", "symbol": "Ne", "electrons": 10, "protons": 10, "neutrons": 10},
    {"atomic_number": 11, "name": "Sodium", "symbol": "Na", "electrons": 11, "protons": 11, "neutrons": 12},
    {"atomic_number": 12, "name": "Magnesium", "symbol": "Mg", "electrons": 12, "protons": 12, "neutrons": 12},
    {"atomic_number": 13, "name": "Aluminum", "symbol": "Al", "electrons": 13, "protons": 13, "neutrons": 14},
    {"atomic_number": 14, "name": "Silicon", "symbol": "Si", "electrons": 14, "protons": 14, "neutrons": 14},
    {"atomic_number": 15, "name": "Phosphorus", "symbol": "P", "electrons": 15, "protons": 15, "neutrons": 16},
    {"atomic_number": 16, "name": "Sulfur", "symbol": "S", "electrons": 16, "protons": 16, "neutrons": 16},
    {"atomic_number": 17, "name": "Chlorine", "symbol": "Cl", "electrons": 17, "protons": 17, "neutrons": 18},
    {"atomic_number": 18, "name": "Argon", "symbol": "Ar", "electrons": 18, "protons": 18, "neutrons": 22},
    {"atomic_number": 19, "name": "Potassium", "symbol": "K", "electrons": 19, "protons": 19, "neutrons": 20},
    {"atomic_number": 20, "name": "Calcium", "symbol": "Ca", "electrons": 20, "protons": 20, "neutrons": 20},
    {"atomic_number": 21, "name": "Scandium", "symbol": "Sc", "electrons": 21, "protons": 21, "neutrons": 24},
    {"atomic_number": 22, "name": "Titanium", "symbol": "Ti", "electrons": 22, "protons": 22, "neutrons": 26},
    {"atomic_number": 23, "name": "Vanadium", "symbol": "V", "electrons": 23, "protons": 23, "neutrons": 28},
    {"atomic_number": 24, "name": "Chromium", "symbol": "Cr", "electrons": 24, "protons": 24, "neutrons": 28},
    {"atomic_number": 25, "name": "Manganese", "symbol": "Mn", "electrons": 25, "protons": 25, "neutrons": 30},
    {"atomic_number": 26, "name": "Iron", "symbol": "Fe", "electrons": 26, "protons": 26, "neutrons": 30},
    {"atomic_number": 27, "name": "Cobalt", "symbol": "Co", "electrons": 27, "protons": 27, "neutrons": 32},
    {"atomic_number": 28, "name": "Nickel", "symbol": "Ni", "electrons": 28, "protons": 28, "neutrons": 30},
    {"atomic_number": 29, "name": "Copper", "symbol": "Cu", "electrons": 29, "protons": 29, "neutrons": 34},
    {"atomic_number": 30, "name": "Zinc", "symbol": "Zn", "electrons": 30, "protons": 30, "neutrons": 35},
    {"atomic_number": 31, "name": "Gallium", "symbol": "Ga", "electrons": 31, "protons": 31, "neutrons": 38},
    {"atomic_number": 32, "name": "Germanium", "symbol": "Ge", "electrons": 32, "protons": 32, "neutrons": 40},
    {"atomic_number": 33, "name": "Arsenic", "symbol": "As", "electrons": 33, "protons": 33, "neutrons": 42},
    {"atomic_number": 34, "name": "Selenium", "symbol": "Se", "electrons": 34, "protons": 34, "neutrons": 44},
    {"atomic_number": 35, "name": "Bromine", "symbol": "Br", "electrons": 35, "protons": 35, "neutrons": 44},
    {"atomic_number": 36, "name": "Krypton", "symbol": "Kr", "electrons": 36, "protons": 36, "neutrons": 48},
    {"atomic_number": 37, "name": "Rubidium", "symbol": "Rb", "electrons": 37, "protons": 37, "neutrons": 48},
    {"atomic_number": 38, "name": "Strontium", "symbol": "Sr", "electrons": 38, "protons": 38, "neutrons": 50},
    {"atomic_number": 39, "name": "Yttrium", "symbol": "Y", "electrons": 39, "protons": 39, "neutrons": 50},
    {"atomic_number": 40, "name": "Zirconium", "symbol": "Zr", "electrons": 40, "protons": 40, "neutrons": 50},
    {"atomic_number": 41, "name": "Niobium", "symbol": "Nb", "electrons": 41, "protons": 41, "neutrons": 52},
    {"atomic_number": 42, "name": "Molybdenum", "symbol": "Mo", "electrons": 42, "protons": 42, "neutrons": 54},
    {"atomic_number": 43, "name": "Technetium", "symbol": "Tc", "electrons": 43, "protons": 43, "neutrons": 55},
    {"atomic_number": 44, "name": "Ruthenium", "symbol": "Ru", "electrons": 44, "protons": 44, "neutrons": 57},
    {"atomic_number": 45, "name": "Rhodium", "symbol": "Rh", "electrons": 45, "protons": 45, "neutrons": 58},
    {"atomic_number": 46, "name": "Palladium", "symbol": "Pd", "electrons": 46, "protons": 46, "neutrons": 60},
    {"atomic_number": 47, "name": "Silver", "symbol": "Ag", "electrons": 47, "protons": 47, "neutrons": 60},
    {"atomic_number": 48, "name": "Cadmium", "symbol": "Cd", "electrons": 48, "protons": 48, "neutrons": 64},
    {"atomic_number": 49, "name": "Indium", "symbol": "In", "electrons": 49, "protons": 49, "neutrons": 66},
    {"atomic_number": 50, "name": "Tin", "symbol": "Sn", "electrons": 50, "protons": 50, "neutrons": 69},
    {"atomic_number": 51, "name": "Antimony", "symbol": "Sb", "electrons": 51, "protons": 51, "neutrons": 70},
    {"atomic_number": 52, "name": "Tellurium", "symbol": "Te", "electrons": 52, "protons": 52, "neutrons": 76},
    {"atomic_number": 53, "name": "Iodine", "symbol": "I", "electrons": 53, "protons": 53, "neutrons": 74},
    {"atomic_number": 54, "name": "Xenon", "symbol": "Xe", "electrons": 54, "protons": 54, "neutrons": 77},
    {"atomic_number": 55, "name": "Cesium", "symbol": "Cs", "electrons": 55, "protons": 55, "neutrons": 78},
    {"atomic_number": 56, "name": "Barium", "symbol": "Ba", "electrons": 56, "protons": 56, "neutrons": 82},
    {"atomic_number": 57, "name": "Lanthanum", "symbol": "La", "electrons": 57, "protons": 57, "neutrons": 82},
    {"atomic_number": 58, "name": "Cerium", "symbol": "Ce", "electrons": 58, "protons": 58, "neutrons": 82},
    {"atomic_number": 59, "name": "Praseodymium", "symbol": "Pr", "electrons": 59, "protons": 59, "neutrons": 82},
    {"atomic_number": 60, "name": "Neodymium", "symbol": "Nd", "electrons": 60, "protons": 60, "neutrons": 84},
    {"atomic_number": 61, "name": "Promethium", "symbol": "Pm", "electrons": 61, "protons": 61, "neutrons": 84},
    {"atomic_number": 62, "name": "Samarium", "symbol": "Sm", "electrons": 62, "protons": 62, "neutrons": 88},
    {"atomic_number": 63, "name": "Europium", "symbol": "Eu", "electrons": 63, "protons": 63, "neutrons": 88},
    {"atomic_number": 64, "name": "Gadolinium", "symbol": "Gd", "electrons": 64, "protons": 64, "neutrons": 90},
    {"atomic_number": 65, "name": "Terbium", "symbol": "Tb", "electrons": 65, "protons": 65, "neutrons": 94},
    {"atomic_number": 66, "name": "Dysprosium", "symbol": "Dy", "electrons": 66, "protons": 66, "neutrons": 97},
    {"atomic_number": 67, "name": "Holmium", "symbol": "Ho", "electrons": 67, "protons": 67, "neutrons": 98},
    {"atomic_number": 68, "name": "Erbium", "symbol": "Er", "electrons": 68, "protons": 68, "neutrons": 99},
    {"atomic_number": 69, "name": "Thulium", "symbol": "Tm", "electrons": 69, "protons": 69, "neutrons": 100},
    {"atomic_number": 70, "name": "Ytterbium", "symbol": "Yb", "electrons": 70, "protons": 70, "neutrons": 103},
    {"atomic_number": 71, "name": "Lutetium", "symbol": "Lu", "electrons": 71, "protons": 71, "neutrons": 104},
    {"atomic_number": 72, "name": "Hafnium", "symbol": "Hf", "electrons": 72, "protons": 72, "neutrons": 106},
    {"atomic_number": 73, "name": "Tantalum", "symbol": "Ta", "electrons": 73, "protons": 73, "neutrons": 108},
    {"atomic_number": 74, "name": "Tungsten", "symbol": "W", "electrons": 74, "protons": 74, "neutrons": 110},
    {"atomic_number": 75, "name": "Rhenium", "symbol": "Re", "electrons": 75, "protons": 75, "neutrons": 111},
    {"atomic_number": 76, "name": "Osmium", "symbol": "Os", "electrons": 76, "protons": 76, "neutrons": 114},
    {"atomic_number": 77, "name": "Iridium", "symbol": "Ir", "electrons": 77, "protons": 77, "neutrons": 115},
    {"atomic_number": 78, "name": "Platinum", "symbol": "Pt", "electrons": 78, "protons": 78, "neutrons": 117},
    {"atomic_number": 79, "name": "Gold", "symbol": "Au", "electrons": 79, "protons": 79, "neutrons": 118},
    {"atomic_number": 80, "name": "Mercury", "symbol": "Hg", "electrons": 80, "protons": 80, "neutrons": 120},
    {"atomic_number": 81, "name": "Thallium", "symbol": "Tl", "electrons": 81, "protons": 81, "neutrons": 123},
    {"atomic_number": 82, "name": "Lead", "symbol": "Pb", "electrons": 82, "protons": 82, "neutrons": 125},
    {"atomic_number": 83, "name": "Bismuth", "symbol": "Bi", "electrons": 83, "protons": 83, "neutrons": 126},
    {"atomic_number": 84, "name": "Polonium", "symbol": "Po", "electrons": 84, "protons": 84, "neutrons": 125},
    {"atomic_number": 85, "name": "Astatine", "symbol": "At", "electrons": 85, "protons": 85, "neutrons": 125},
    {"atomic_number": 86, "name": "Radon", "symbol": "Rn", "electrons": 86, "protons": 86, "neutrons": 136},
    {"atomic_number": 87, "name": "Francium", "symbol": "Fr", "electrons": 87, "protons": 87, "neutrons": 136},
    {"atomic_number": 88, "name": "Radium", "symbol": "Ra", "electrons": 88, "protons": 88, "neutrons": 138},
    {"atomic_number": 89, "name": "Actinium", "symbol": "Ac", "electrons": 89, "protons": 89, "neutrons": 138},
    {"atomic_number": 90, "name": "Thorium", "symbol": "Th", "electrons": 90, "protons": 90, "neutrons": 142},
    {"atomic_number": 91, "name": "Protactinium", "symbol": "Pa", "electrons": 91, "protons": 91, "neutrons": 140},
    {"atomic_number": 92, "name": "Uranium", "symbol": "U", "electrons": 92, "protons": 92, "neutrons": 146},
    {"atomic_number": 93, "name": "Neptunium", "symbol": "Np", "electrons": 93, "protons": 93, "neutrons": 144},
    {"atomic_number": 94, "name": "Plutonium", "symbol": "Pu", "electrons": 94, "protons": 94, "neutrons": 150},
    {"atomic_number": 95, "name": "Americium", "symbol": "Am", "electrons": 95, "protons": 95, "neutrons": 148},
    {"atomic_number": 96, "name": "Curium", "symbol": "Cm", "electrons": 96, "protons": 96, "neutrons": 151},
    {"atomic_number": 97, "name": "Berkelium", "symbol": "Bk", "electrons": 97, "protons": 97, "neutrons": 150},
    {"atomic_number": 98, "name": "Californium", "symbol": "Cf", "electrons": 98, "protons": 98, "neutrons": 153},
    {"atomic_number": 99, "name": "Einsteinium", "symbol": "Es", "electrons": 99, "protons": 99, "neutrons": 153},
    {"atomic_number": 100, "name": "Fermium", "symbol": "Fm", "electrons": 100, "protons": 100, "neutrons": 157},
    {"atomic_number": 101, "name": "Mendelevium", "symbol": "Md", "electrons": 101, "protons": 101, "neutrons": 157},
    {"atomic_number": 102, "name": "Nobelium", "symbol": "No", "electrons": 102, "protons": 102, "neutrons": 157},
    {"atomic_number": 103, "name": "Lawrencium", "symbol": "Lr", "electrons": 103, "protons": 103, "neutrons": 159},
    {"atomic_number": 104, "name": "Rutherfordium", "symbol": "Rf", "electrons": 104, "protons": 104, "neutrons": 161},
    {"atomic_number": 105, "name": "Dubnium", "symbol": "Db", "electrons": 105, "protons": 105, "neutrons": 163},
    {"atomic_number": 106, "name": "Seaborgium", "symbol": "Sg", "electrons": 106, "protons": 106, "neutrons": 163},
    {"atomic_number": 107, "name": "Bohrium", "symbol": "Bh", "electrons": 107, "protons": 107, "neutrons": 163},
    {"atomic_number": 108, "name": "Hassium", "symbol": "Hs", "electrons": 108, "protons": 108, "neutrons": 165},
    {"atomic_number": 109, "name": "Meitnerium", "symbol": "Mt", "electrons": 109, "protons": 109, "neutrons": 165},
    {"atomic_number": 110, "name": "Darmstadtium", "symbol": "Ds", "electrons": 110, "protons": 110, "neutrons": 171},
    {"atomic_number": 111, "name": "Roentgenium", "symbol": "Rg", "electrons": 111, "protons": 111, "neutrons": 171},
    {"atomic_number": 112, "name": "Copernicium", "symbol": "Cn", "electrons": 112, "protons": 112, "neutrons": 173},
    {"atomic_number": 113, "name": "Nihonium", "symbol": "Nh", "electrons": 113, "protons": 113, "neutrons": 173},
    {"atomic_number": 114, "name": "Flerovium", "symbol": "Fl", "electrons": 114, "protons": 114, "neutrons": 175},
    {"atomic_number": 115, "name": "Moscovium", "symbol": "Mc", "electrons": 115, "protons": 115, "neutrons": 173},
    {"atomic_number": 116, "name": "Livermorium", "symbol": "Lv", "electrons": 116, "protons": 116, "neutrons": 177},
    {"atomic_number": 117, "name": "Tennessine", "symbol": "Ts", "electrons": 117, "protons": 117, "neutrons": 177},
    {"atomic_number": 118, "name": "Oganesson", "symbol": "Og", "electrons": 118, "protons": 118, "neutrons": 176}
]

class Screen:
    """Main screen manager for the application"""
    
    def __init__(self, width=1200, height=800):
        self.width = width
        self.height = height
        self.current_state = ScreenState.MENU
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.DARK_GRAY = (40, 40, 40)
        self.LIGHT_GRAY = (200, 200, 200)
        self.BLUE = (0, 100, 255)
        self.GREEN = (0, 200, 0)
        self.RED = (255, 0, 0)
        self.GRAY = (100, 100, 100)
        
        # New vibrant colors
        self.PURPLE = (147, 51, 234)
        self.CYAN = (0, 200, 255)
        self.ORANGE = (255, 140, 0)
        self.PINK = (255, 105, 180)
        self.LIME = (50, 205, 50)
        self.DARK_BLUE = (25, 55, 130)
        self.LIGHT_PURPLE = (200, 100, 255)
        self.TURQUOISE = (64, 224, 208)
        self.GOLD = (255, 215, 0)
        
        # Create the display
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("ChemHelper - Chemistry Assistant")
        
        # Font setup
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        
        # Calculator state
        self.calc_display = "0"
        self.calc_first_num = None
        self.calc_operation = None
        self.calc_new_number = True
        
        # ChemHelper state
        self.chem_search_input = ""
        self.chem_search_active = False
        self.chem_found_element = None
        self.chem_charge = 0
        self.cursor_visible = True
        self.cursor_timer = 0
        self.cursor_blink_speed = 30  # frames
        
        # Language setting
        self.current_language = "English"  # English, Spanish, French
        
        # Quiz state
        self.quiz_current_element = None
        self.quiz_answer_input = ""
        self.quiz_feedback = ""
        self.quiz_feedback_timer = 0
        self.quiz_cursor_visible = True
        self.quiz_cursor_timer = 0
        
        # Language translations
        self.translations = {
            "English": {
                "title": "ChemHelper",
                "subtitle": "Chemistry Assistant",
                "periodic": "ChemHelper",
                "calculator": "Calculator",
                "settings": "Settings",
                "back": "Back",
                "search_label": "Search by name, symbol, or #:",
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
                "quiz": "Quiz",
                "quiz_title": "Chemistry Quiz",
                "question": "What is the atomic number of",
                "correct": "Correct!",
                "wrong": "Wrong! The answer is",
                "next_question": "Next Question",
                "exit_quiz": "Exit Quiz",
            },
            "Spanish": {
                "title": "ChemHelper",
                "subtitle": "Asistente de Química",
                "periodic": "ChemHelper",
                "calculator": "Calculadora",
                "settings": "Configuración",
                "back": "Atrás",
                "search_label": "Buscar por nombre, símbolo o #:",
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
                "quiz": "Quiz",
                "quiz_title": "Quiz de Química",
                "question": "¿Cuál es el número atómico de",
                "correct": "¡Correcto!",
                "wrong": "¡Incorrecto! La respuesta es",
                "next_question": "Siguiente Pregunta",
                "exit_quiz": "Salir del Quiz",
            },
            "French": {
                "title": "ChemHelper",
                "subtitle": "Assistant Chimie",
                "periodic": "ChemHelper",
                "calculator": "Calculatrice",
                "settings": "Paramètres",
                "back": "Retour",
                "search_label": "Rechercher par nom, symbole ou #:",
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
                "quiz": "Quiz",
                "quiz_title": "Quiz de Chimie",
                "question": "Quel est le numéro atomique de",
                "correct": "Correct!",
                "wrong": "Faux! La réponse est",
                "next_question": "Question Suivante",
                "exit_quiz": "Quitter le Quiz",
            }
        }
    
    def get_text(self, key):
        """Get translated text for a given key"""
        return self.translations[self.current_language].get(key, key)
    
    def draw_background(self, color=None):
        """Fill screen with background color"""
        bg_color = color or self.WHITE
        self.display.fill(bg_color)
    
    def draw_text(self, text, font, color, x, y):
        """Draw text on screen"""
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.display.blit(text_surface, text_rect)
        return text_rect
    
    def draw_button(self, x, y, width, height, text, bg_color=None, text_color=None):
        """Draw a button and return its rect"""
        bg = bg_color or self.BLUE
        txt_color = text_color or self.WHITE
        
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.display, bg, button_rect)
        pygame.draw.rect(self.display, self.BLACK, button_rect, 2)
        
        self.draw_text(text, self.font_medium, txt_color, 
                      x + 10, y + height // 2 - 16)
        
        return button_rect
    
    def draw_menu(self):
        """Draw the main menu screen"""
        # Create gradient background
        for y in range(self.height):
            color_ratio = y / self.height
            r = int(40 + (147 - 40) * color_ratio)
            g = int(40 + (100 - 40) * color_ratio)
            b = int(100 + (200 - 100) * color_ratio)
            pygame.draw.line(self.display, (r, g, b), (0, y), (self.width, y))
        
        # Title with glow effect
        title_text = self.get_text("title")
        self.draw_text(title_text, self.font_large, self.CYAN, 
                      self.width // 2 - 150, 40)
        self.draw_text(title_text, self.font_large, self.WHITE, 
                      self.width // 2 - 148, 42)
        
        # Subtitle
        self.draw_text(self.get_text("subtitle"), self.font_small, self.GOLD,
                      self.width // 2 - 100, 120)
        
        # Menu buttons with vibrant colors
        buttons = {
            'periodic_table': self.draw_button(
                self.width // 2 - 100, 250, 200, 60, self.get_text("periodic"), self.CYAN, self.WHITE),
            'calculator': self.draw_button(
                self.width // 2 - 100, 330, 200, 60, self.get_text("calculator"), self.ORANGE, self.WHITE),
            'quiz': self.draw_button(
                self.width // 2 - 100, 410, 200, 60, self.get_text("quiz"), self.LIME, self.WHITE),
            'settings': self.draw_button(
                self.width // 2 - 100, 490, 200, 60, self.get_text("settings"), self.PINK, self.WHITE),
        }
        
        return buttons
    
    def draw_periodic_table(self):
        """Draw the ChemHelper element lookup screen"""
        # Colorful background
        self.draw_background(self.WHITE)
        
        # Add decorative header
        pygame.draw.rect(self.display, self.DARK_BLUE, (0, 0, self.width, 80))
        self.draw_text("ChemHelper - Element Lookup", self.font_large, self.CYAN,
                      self.width // 2 - 250, 20)
        
        # Update cursor blink
        self.cursor_timer += 1
        if self.cursor_timer >= self.cursor_blink_speed:
            self.cursor_timer = 0
            self.cursor_visible = not self.cursor_visible
        
        # Search input box with colored border
        input_box = pygame.Rect(150, 120, 400, 50)
        pygame.draw.rect(self.display, self.CYAN, input_box, 3)
        pygame.draw.rect(self.display, self.LIGHT_GRAY, input_box)
        
        self.draw_text(self.get_text("search_label"), self.font_small, self.DARK_BLUE, 160, 100)
        
        # Draw input text with cursor
        display_text = self.chem_search_input
        if self.cursor_visible:
            display_text += "|"
        
        if self.chem_search_input or self.cursor_visible:
            self.draw_text(display_text, self.font_medium, self.BLACK, 160, 130)
        else:
            self.draw_text(self.get_text("type_here"), self.font_medium, (150, 150, 150), 160, 130)
        
        # Load and display Flask.png image on the right
        try:
            flask_image = pygame.image.load("Flask.png")
            # Scale image to fit the right side
            flask_image = pygame.transform.scale(flask_image, (310, 310))
            flask_rect = flask_image.get_rect(topright=(self.width - 80, 160))
            self.display.blit(flask_image, flask_rect)
        except pygame.error:
            pass  # If image doesn't load, continue without it
        
        # Display element information if found
        if self.chem_found_element:
            elem = self.chem_found_element
            adjusted_electrons = elem["protons"] - self.chem_charge
            if adjusted_electrons < 0:
                adjusted_electrons = 0
            
            y_pos = 220
            # Element info box background
            pygame.draw.rect(self.display, (240, 248, 255), (130, y_pos - 10, 550, 160))
            pygame.draw.rect(self.display, self.ORANGE, (130, y_pos - 10, 550, 160), 3)
            
            self.draw_text(f"{self.get_text('element')}: {elem['name']} ({elem['symbol']})", self.font_medium, self.PURPLE, 150, y_pos)
            self.draw_text(f"{self.get_text('atomic_number')}: {elem['atomic_number']}", self.font_small, self.DARK_BLUE, 150, y_pos + 40)
            self.draw_text(f"{self.get_text('protons')}: {elem['protons']}  |  {self.get_text('electrons')}: {elem['electrons']}", self.font_small, self.DARK_BLUE, 150, y_pos + 70)
            self.draw_text(f"{self.get_text('neutrons')}: {elem['neutrons']}  |  {self.get_text('electrons_ionic')}: {adjusted_electrons}", self.font_small, self.DARK_BLUE, 150, y_pos + 100)
            
            # Charge input
            charge_box = pygame.Rect(150, y_pos + 150, 200, 40)
            pygame.draw.rect(self.display, self.LIME, charge_box, 2)
            pygame.draw.rect(self.display, self.LIGHT_GRAY, charge_box)
            self.draw_text(f"{self.get_text('charge')}: {self.chem_charge}", self.font_small, self.BLACK, 160, y_pos + 160)
            
            # Clear button
            clear_button = self.draw_button(400, y_pos + 150, 120, 40, self.get_text("clear"), self.RED, self.WHITE)
        else:
            self.draw_text(self.get_text("enter_element"), self.font_small, self.ORANGE, 150, 220)
            clear_button = pygame.Rect(0, 0, 0, 0)
        
        # Back button
        back_button = self.draw_button(50, self.height - 80, 150, 60, self.get_text("back"), self.PINK, self.WHITE)
        
        buttons = {'search_box': input_box, 'clear': clear_button, 'back': back_button}
        return buttons
    
    def search_element(self, search_term):
        """Search for an element by name, symbol, or atomic number"""
        self.chem_found_element = None
        self.chem_charge = 0
        
        if not search_term:
            return
        
        # Try to match by atomic number
        try:
            atomic_num = int(search_term)
            for element in ELEMENTS:
                if element["atomic_number"] == atomic_num:
                    self.chem_found_element = element
                    return
        except ValueError:
            pass
        
        # Search by name or symbol
        search_lower = search_term.lower()
        for element in ELEMENTS:
            if element["name"].lower() == search_lower or element["symbol"].lower() == search_lower:
                self.chem_found_element = element
                return
    
    def draw_calculator(self):
        """Draw the calculator screen"""
        # Colorful gradient background
        for y in range(self.height):
            color_ratio = y / self.height
            r = int(255 * (1 - color_ratio))
            g = int(140 * color_ratio)
            b = int(200)
            pygame.draw.line(self.display, (r, g, b), (0, y), (self.width, y))
        
        self.draw_text(self.get_text("calculator"), self.font_large, self.WHITE,
                      self.width // 2 - 100, 30)
        
        # Calculator display with colored border
        display_rect = pygame.Rect(200, 120, 300, 80)
        pygame.draw.rect(self.display, self.CYAN, display_rect, 4)
        pygame.draw.rect(self.display, (30, 30, 30), display_rect)
        self.draw_text(self.calc_display, self.font_medium, self.CYAN, 220, 140)
        
        # Button layout: 4x5 grid
        buttons = {}
        button_width = 70
        button_height = 60
        start_x = 180
        start_y = 240
        
        # Button data: (label, row, col)
        button_data = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
            ("C", 4, 0),
        ]
        
        for label, row, col in button_data:
            x = start_x + col * (button_width + 10)
            y = start_y + row * (button_height + 10)
            
            if label == "C":
                color = self.RED
            elif label in ["+", "-", "*", "/", "="]:
                color = self.ORANGE
            else:
                color = self.CYAN
            
            rect = self.draw_button(x, y, button_width, button_height, label, color, self.WHITE)
            buttons[label] = rect
        
        # Back button
        back_button = self.draw_button(50, self.height - 80, 150, 60, self.get_text("back"), self.PINK, self.WHITE)
        buttons['back'] = back_button
        
        return buttons
    
    def calculator_input(self, button_label):
        """Process calculator input"""
        if button_label == "C":
            self.calc_display = "0"
            self.calc_first_num = None
            self.calc_operation = None
            self.calc_new_number = True
        elif button_label in ["+", "-", "*", "/"]:
            if self.calc_first_num is None:
                self.calc_first_num = float(self.calc_display)
            else:
                # Calculate intermediate result
                second_num = float(self.calc_display)
                self.calc_first_num = self.calculate(self.calc_first_num, second_num, self.calc_operation)
                self.calc_display = str(self.calc_first_num)
            self.calc_operation = button_label
            self.calc_new_number = True
        elif button_label == "=":
            if self.calc_first_num is not None and self.calc_operation is not None:
                second_num = float(self.calc_display)
                result = self.calculate(self.calc_first_num, second_num, self.calc_operation)
                self.calc_display = str(result)
                self.calc_first_num = None
                self.calc_operation = None
                self.calc_new_number = True
        elif button_label == ".":
            if "." not in self.calc_display:
                self.calc_display += "."
                self.calc_new_number = False
        else:  # Number
            if self.calc_new_number:
                self.calc_display = button_label
                self.calc_new_number = False
            else:
                if self.calc_display == "0":
                    self.calc_display = button_label
                else:
                    self.calc_display += button_label
    
    def calculate(self, first, second, operation):
        """Perform calculation"""
        if operation == "+":
            return first + second
        elif operation == "-":
            return first - second
        elif operation == "*":
            return first * second
        elif operation == "/":
            return first / second if second != 0 else 0
        return 0
    
    def draw_quiz(self):
        """Draw the quiz screen"""
        # Colorful gradient background
        for y in range(self.height):
            color_ratio = y / self.height
            r = int(50 + (100 * color_ratio))
            g = int(205 + (50 * color_ratio))
            b = int(50 * (1 - color_ratio))
            pygame.draw.line(self.display, (r, g, b), (0, y), (self.width, y))
        
        # Header
        pygame.draw.rect(self.display, self.DARK_BLUE, (0, 0, self.width, 80))
        self.draw_text(self.get_text("quiz_title"), self.font_large, self.GOLD,
                      self.width // 2 - 150, 20)
        
        # Initialize quiz if not started
        if self.quiz_current_element is None:
            self.start_quiz()
        
        # Update cursor blink
        self.quiz_cursor_timer += 1
        if self.quiz_cursor_timer >= self.cursor_blink_speed:
            self.quiz_cursor_timer = 0
            self.quiz_cursor_visible = not self.quiz_cursor_visible
        
        buttons = {}
        
        # Display question in a box
        elem = self.quiz_current_element
        question_text = f"{self.get_text('question')} {elem['name']} ({elem['symbol']})?"
        
        # Question box
        pygame.draw.rect(self.display, self.TURQUOISE, (100, 120, 1000, 80))
        pygame.draw.rect(self.display, self.WHITE, (100, 120, 1000, 80), 3)
        self.draw_text(question_text, self.font_medium, self.WHITE,
                      self.width // 2 - 300, 150)
        
        # Answer input box with colored border
        input_box = pygame.Rect(300, 250, 300, 60)
        pygame.draw.rect(self.display, self.GOLD, input_box, 3)
        pygame.draw.rect(self.display, (240, 248, 255), input_box)
        self.draw_text("Enter answer:", self.font_small, self.DARK_BLUE, 320, 230)
        
        # Draw input text with cursor
        display_text = self.quiz_answer_input
        if self.quiz_cursor_visible:
            display_text += "|"
        
        if self.quiz_answer_input or self.quiz_cursor_visible:
            self.draw_text(display_text, self.font_medium, self.BLACK, 320, 260)
        else:
            self.draw_text("0", self.font_medium, (150, 150, 150), 320, 260)
        
        # Display feedback
        if self.quiz_feedback:
            if "Correct" in self.quiz_feedback or self.get_text("correct") in self.quiz_feedback:
                feedback_color = self.LIME
            else:
                feedback_color = self.RED
            self.draw_text(self.quiz_feedback, self.font_medium, feedback_color,
                          self.width // 2 - 200, 350)
            
            # Show next question button
            next_button = self.draw_button(self.width // 2 - 100, 420, 200, 60, 
                                          self.get_text("next_question"), self.LIME, self.WHITE)
            buttons['next'] = next_button
        else:
            self.draw_text("Press Enter to submit your answer", self.font_small, self.GOLD,
                          self.width // 2 - 250, 350)
        
        # Back button
        back_button = self.draw_button(50, self.height - 80, 150, 60, self.get_text("back"), self.PINK, self.WHITE)
        buttons['back'] = back_button
        buttons['answer_box'] = input_box
        
        return buttons
    
    def start_quiz(self):
        """Start a new quiz question"""
        self.quiz_current_element = random.choice(ELEMENTS)
        self.quiz_answer_input = ""
        self.quiz_feedback = ""
    
    def check_quiz_answer(self):
        """Check the quiz answer"""
        try:
            answer = int(self.quiz_answer_input)
            if answer == self.quiz_current_element["atomic_number"]:
                self.quiz_feedback = self.get_text("correct")
            else:
                self.quiz_feedback = f"{self.get_text('wrong')} {self.quiz_current_element['atomic_number']}"
        except ValueError:
            self.quiz_feedback = f"{self.get_text('wrong')} {self.quiz_current_element['atomic_number']}"
    
    def draw_settings(self):
        """Draw the settings screen"""
        # Colorful background
        for y in range(self.height):
            color_ratio = y / self.height
            r = int(200 + (55 * color_ratio))
            g = int(100 + (155 * color_ratio))
            b = int(255 - (100 * color_ratio))
            pygame.draw.line(self.display, (r, g, b), (0, y), (self.width, y))
        
        # Header
        pygame.draw.rect(self.display, self.DARK_BLUE, (0, 0, self.width, 80))
        self.draw_text(self.get_text("settings"), self.font_large, self.GOLD,
                      self.width // 2 - 100, 20)
        
        # Language section
        pygame.draw.rect(self.display, (255, 255, 240), (100, 130, 1000, 200))
        pygame.draw.rect(self.display, self.CYAN, (100, 130, 1000, 200), 3)
        self.draw_text(f"{self.get_text('language')}:", self.font_medium, self.DARK_BLUE, 150, 150)
        
        buttons = {}
        
        # Language buttons
        languages = ["English", "Spanish", "French"]
        button_width = 120
        button_height = 50
        start_x = 150
        y_pos = 210
        
        for i, lang in enumerate(languages):
            x = start_x + i * (button_width + 20)
            # Highlight current language
            if lang == self.current_language:
                color = self.LIME
                text_color = self.BLACK
            else:
                color = self.TURQUOISE
                text_color = self.WHITE
            
            rect = self.draw_button(x, y_pos, button_width, button_height, lang, color, text_color)
            buttons[f"lang_{lang}"] = rect
        
        # Back button
        back_button = self.draw_button(50, self.height - 80, 150, 60, self.get_text("back"), self.PINK, self.WHITE)
        buttons['back'] = back_button
        
        return buttons
    
    def update(self):
        """Update the display"""
        pygame.display.flip()
    
    def get_screen_state(self):
        """Return current screen state"""
        return self.current_state
    
    def set_screen_state(self, state):
        """Set the current screen state"""
        if isinstance(state, ScreenState):
            self.current_state = state
