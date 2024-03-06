import pygame
import pygame_gui
import init
import elements
from game_loop import meeps_game_loop
from ticket_creation import ticket_creation


if __name__ == "__main__":

    database = 'data.db'
    window_surface, clock, background = init.pygame_init()
    manager = init.pygame_gui_init()

    start_button = elements.start_button_func(manager)
    ticket_creation_button = elements.ticket_creation_button_func(manager)
    quit_button = elements.quit_button_func(manager)


    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    meeps_game_loop(database)

                if event.ui_element == ticket_creation_button:
                    print("Under Development")
                    ticket_creation(database)

                if event.ui_element == quit_button:
                    running = False

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()

    pygame.quit()