import pygame
import pygame_gui
import init
import elements
from game import meeps_game_loop


window_surface, clock, background = init.pygame_init()
manager = init.pygame_gui_init()
start_button = elements.start_button_func(manager)
settings_button = elements.settings_button_func(manager)


running = True
while running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                meeps_game_loop()

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()

pygame.quit()