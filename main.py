import pygame
import sys
from screen import Screen, ScreenState

# Initialize Pygame
pygame.init()

# Create screen manager
screen_manager = Screen(width=1200, height=800)

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Store button rects globally
menu_buttons = {}
current_buttons = {}

# Main game loop
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle keyboard input for ChemHelper
        elif event.type == pygame.KEYDOWN:
            if screen_manager.get_screen_state() == ScreenState.PERIODIC_TABLE:
                if event.key == pygame.K_BACKSPACE:
                    screen_manager.chem_search_input = screen_manager.chem_search_input[:-1]
                elif event.key == pygame.K_RETURN:
                    screen_manager.search_element(screen_manager.chem_search_input)
                elif event.unicode.isprintable():
                    screen_manager.chem_search_input += event.unicode
            
            # Handle quiz keyboard input
            elif screen_manager.get_screen_state() == ScreenState.QUIZ:
                if event.key == pygame.K_BACKSPACE:
                    screen_manager.quiz_answer_input = screen_manager.quiz_answer_input[:-1]
                elif event.key == pygame.K_RETURN:
                    if screen_manager.quiz_feedback:
                        # Move to next question
                        screen_manager.start_quiz()
                    else:
                        # Check answer
                        screen_manager.check_quiz_answer()
                elif event.unicode.isdigit():
                    screen_manager.quiz_answer_input += event.unicode
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            # Handle menu buttons
            if screen_manager.get_screen_state() == ScreenState.MENU:
                if menu_buttons['periodic_table'].collidepoint(mouse_pos):
                    screen_manager.set_screen_state(ScreenState.PERIODIC_TABLE)
                elif menu_buttons['calculator'].collidepoint(mouse_pos):
                    screen_manager.set_screen_state(ScreenState.CALCULATOR)
                elif menu_buttons['quiz'].collidepoint(mouse_pos):
                    screen_manager.quiz_current_element = None
                    screen_manager.set_screen_state(ScreenState.QUIZ)
                elif menu_buttons['settings'].collidepoint(mouse_pos):
                    screen_manager.set_screen_state(ScreenState.SETTINGS)
            
            # Handle ChemHelper buttons
            elif screen_manager.get_screen_state() == ScreenState.PERIODIC_TABLE:
                if current_buttons['search_box'].collidepoint(mouse_pos):
                    screen_manager.chem_search_input = ""
                if current_buttons['clear'].collidepoint(mouse_pos):
                    screen_manager.chem_search_input = ""
                    screen_manager.chem_found_element = None
                elif current_buttons['back'].collidepoint(mouse_pos):
                    screen_manager.set_screen_state(ScreenState.MENU)
            
            # Handle settings buttons
            elif screen_manager.get_screen_state() == ScreenState.SETTINGS:
                for button_label, button_rect in current_buttons.items():
                    if button_rect.collidepoint(mouse_pos):
                        if button_label == 'back':
                            screen_manager.set_screen_state(ScreenState.MENU)
                        elif button_label.startswith('lang_'):
                            lang = button_label.replace('lang_', '')
                            screen_manager.current_language = lang
                        break
            
            # Handle quiz buttons
            elif screen_manager.get_screen_state() == ScreenState.QUIZ:
                for button_label, button_rect in current_buttons.items():
                    if button_rect.collidepoint(mouse_pos):
                        if button_label == 'back':
                            screen_manager.set_screen_state(ScreenState.MENU)
                        elif button_label == 'next':
                            screen_manager.start_quiz()
                        break
            
            # Handle calculator buttons
            elif screen_manager.get_screen_state() == ScreenState.CALCULATOR:
                for button_label, button_rect in current_buttons.items():
                    if button_rect.collidepoint(mouse_pos):
                        if button_label == 'back':
                            screen_manager.set_screen_state(ScreenState.MENU)
                        else:
                            screen_manager.calculator_input(button_label)
                        break
            
            # Handle back button for other screens
            elif 'back' in current_buttons and current_buttons['back'].collidepoint(mouse_pos):
                screen_manager.set_screen_state(ScreenState.MENU)
    
    # Draw current screen based on state
    if screen_manager.get_screen_state() == ScreenState.MENU:
        menu_buttons = screen_manager.draw_menu()
    elif screen_manager.get_screen_state() == ScreenState.PERIODIC_TABLE:
        current_buttons = screen_manager.draw_periodic_table()
    elif screen_manager.get_screen_state() == ScreenState.CALCULATOR:
        current_buttons = screen_manager.draw_calculator()
    elif screen_manager.get_screen_state() == ScreenState.SETTINGS:
        current_buttons = screen_manager.draw_settings()
    elif screen_manager.get_screen_state() == ScreenState.QUIZ:
        current_buttons = screen_manager.draw_quiz()
    
    # Update display
    screen_manager.update()

pygame.quit()
sys.exit()
