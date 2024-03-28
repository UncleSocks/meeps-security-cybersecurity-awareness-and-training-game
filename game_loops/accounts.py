import pygame
import pygame_gui
import init
import queries
import elements.accounts_elements as accounts_elements


def accounts_management(connect, cursor):

    window_surface, clock, background = init.pygame_init()
    manager = init.pygame_gui_init()

    account_list = queries.accounts(cursor)

    back_button = accounts_elements.back_button_func(manager)
    create_button, delete_button = accounts_elements.create_delete_button_func(manager)
    account_entry_title_tbox = accounts_elements.account_entry_slist_misc_func(manager)
    account_entry_slist = accounts_elements.account_entry_slist_func(manager, account_list)


    running = True
    while running:
        
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                    running = False


            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0,0))
        manager.draw_ui(window_surface)
        pygame.display.update()