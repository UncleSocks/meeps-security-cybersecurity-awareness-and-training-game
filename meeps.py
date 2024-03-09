import pygame
import pygame_gui
import init
import elements.main_menu as main_menu
from game_loop import meeps_game_loop
from tickets import ticket_management
from threats import threat_database_management_func


if __name__ == "__main__":

    database = 'data.db'
    window_surface, clock, background = init.pygame_init()
    manager = init.pygame_gui_init()

    start_button = main_menu.start_button_func(manager)
    ticket_management_button = main_menu.ticket_management_button_func(manager)
    threat_entries_button = main_menu.threat_entries_button_func(manager)
    quit_button = main_menu.quit_button_func(manager)

    title_image_path = "Assets/title.png"
    main_title_image = main_menu.main_title_image_func(manager, title_image_path)
    main_title_slogan = main_menu.main_title_slogan_label_func(manager)

    current_version = "MS v2024.0.1"
    version_label = main_menu.version_label_func(manager, current_version)
    github_label = main_menu.github_label_func(manager)


    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    meeps_game_loop(database)

                elif event.ui_element == ticket_management_button:
                    ticket_management(database)

                elif event.ui_element == threat_entries_button:
                    print("Under Development")
                    threat_database_management_func(database)

                elif event.ui_element == quit_button:
                    running = False

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()

    pygame.quit()