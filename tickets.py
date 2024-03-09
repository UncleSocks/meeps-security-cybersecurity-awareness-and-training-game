import pygame
import pygame_gui
import random
import sqlite3
import init
import sqlite
import elements.ticket_loop as ticket_loop


def ticket_init():

    selected_threat = None
    ticket_title = None
    ticket_entry = None
    ticket_confirm_window = None

    return selected_threat, ticket_title, ticket_entry, ticket_confirm_window


def ticket_management(database):

    connect = sqlite3.connect(database, timeout=10)
    cursor = connect.cursor()

    window_surface, clock, background = init.pygame_init()
    manager = init.pygame_gui_init()

    id_list, ticket_list = sqlite.tickets(cursor)

    back_button = ticket_loop.back_button_func(manager)
    create_button = ticket_loop.create_ticket_button_func(manager)
    delete_button, ticket_entry_title_tbox = ticket_loop.ticket_entry_slist_misc_func(manager)
    ticket_entry_slist = ticket_loop.ticket_entry_slist_func(manager, ticket_list)
    selected_ticket_title_tbox, selected_ticket_description_tbox = ticket_loop.selected_ticket_tbox_func(manager)

    selected_ticket_id = None

    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                    running = False
                
                if event.ui_element == create_button:
                    id_list, ticket_list = ticket_creation(database)
                    ticket_entry_slist.kill()
                    ticket_entry_slist = ticket_loop.ticket_entry_slist_func(manager, ticket_list)

            if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == ticket_entry_slist:
                    selected_ticket = event.text
                    
                    id_index_find = ticket_list.index(selected_ticket)
                    selected_ticket_id = id_list[id_index_find]
                    
                    cursor.execute('SELECT title, entry, caller_id FROM tickets WHERE id=?', [selected_ticket_id])
                    title, entry, caller_id = cursor.fetchone()
                    selected_ticket_title_tbox.set_text(f"{title}")
                    selected_ticket_description_tbox.set_text(f"{entry}")

            if selected_ticket_id is not None:
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == delete_button:
                        cursor.execute('DELETE FROM tickets WHERE id=?', [selected_ticket_id])
                        connect.commit()

                        id_list, ticket_list = sqlite.tickets(cursor)
                        ticket_entry_slist.kill()
                        ticket_entry_slist = ticket_loop.ticket_entry_slist_func(manager, ticket_list)


            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()



def ticket_creation(database):

    connect = sqlite3.connect(database, timeout=10)
    cursor = connect.cursor()

    window_surface, clock, background = init.pygame_init()
    manager = init.pygame_gui_init()

    threat_list = sqlite.threats(cursor)

    back_button = ticket_loop.back_button_func(manager)
    title_label, title_text_entry = ticket_loop.title_text_entry_func(manager)
    ticket_label, ticket_text_entry = ticket_loop.ticket_text_entry_func(manager)
    create_button, threat_entry_title_tbox, threat_entry_slist = ticket_loop.threat_entry_slist_func(manager, threat_list)
    threat_description_tbox = ticket_loop.threat_description_tbox_func(manager)
    
    selected_threat, ticket_title, ticket_entry, ticket_confirm_window = ticket_init()

    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                   updated_id_list, updated_ticket_list = sqlite.tickets(cursor)
                   return updated_id_list, updated_ticket_list

            if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == threat_entry_slist:
                    selected_threat = event.text
                    print(selected_threat)

                    cursor.execute('SELECT description, indicators, countermeasures FROM threats WHERE name=?', [selected_threat])
                    description, indicators, countermeasures = cursor.fetchone()
                    threat_description_tbox.set_text(f'<b>{selected_threat.upper()}</b>\n<b>Description</b>:\n{description}\n<b>Indicators:\n</b>{indicators}\n<b>Countermeasures:</b>\n{countermeasures}')

            ticket_title = title_text_entry.get_text()
            ticket_entry = ticket_text_entry.get_text()

            if selected_threat is not None and ticket_title is not None and ticket_entry is not None and ticket_confirm_window is None:
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == create_button:

                        cursor.execute('SELECT MAX(id) FROM tickets')
                        last_id = cursor.fetchone()[0]
                        new_id = last_id + 1

                        new_ticket = (new_id, ticket_title, ticket_entry, selected_threat, 1)
                        cursor.execute('INSERT INTO tickets VALUES (?, ?, ?, ?, ?)', new_ticket)
                        connect.commit()

                        ticket_confirm_window, ticket_confirm_close_button = ticket_loop.ticket_confirm_window_func(manager)
        
            manager.process_events(event)

        manager.update(time_delta)
        window_surface.blit(background, (0, 0))

        if ticket_confirm_window:
            ticket_confirm_window.show()
            manager.draw_ui(window_surface)
            
            for event in pygame.event.get():
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == ticket_confirm_close_button:

                        title_text_entry.set_text("")
                        ticket_text_entry.set_text("")
                        threat_description_tbox.set_text("SELECT A THREAT")

                        ticket_confirm_window.hide()
                        selected_threat, ticket_title, ticket_entry, ticket_confirm_window = ticket_init()

                manager.process_events(event)


        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()