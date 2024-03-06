import pygame
import pygame_gui
import random
import sqlite3
import init
import elements
from sqlite import ticket_ids, threats


def meeps_game_loop(database):
    
    connect = sqlite3.connect(database, timeout=10)
    cursor = connect.cursor()

    window_surface, clock, background = init.pygame_init()
    manager = init.pygame_gui_init()

    ticket_ids_list = ticket_ids(cursor)
    total_tickets = len(ticket_ids_list)
    threat_list = threats(cursor)

    back_button, title_label, main_sla_timer_label, caller_profile_tbox, submit_button, threat_entry_title_tbox, threat_entry_slist, threat_description_tbox, ticket_entry_tbox = init.meeps_background_init(manager, threat_list)
    ticket_timer, randomized_ticket_entry, popup_window_close_timer, popup_window_sla_countdown, main_sla_timer, main_sla_countdown = init.meeps_timers_init()
    running, ticket_presence, caller_popup_window, popup_button_accepted, total_score, missed_calls, missed_tickets   = init.meeps_loop_init()


    while running:

        time_delta = clock.tick(60) / 1000.0
        ticket_timer += time_delta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == threat_entry_slist:
                    selected_threat = event.text
                    print(selected_threat)

                    cursor.execute('SELECT description, impact, mitigation FROM threats WHERE name=?', [selected_threat])
                    description, impact, mitigation = cursor.fetchone()
                    threat_description_tbox.set_text(f'<b>{selected_threat.upper()}</b>\n<b>Description</b>:\n{description}\n<b>Impact:\n</b>{impact}\n<b>Mitigation:</b>\n{mitigation}')
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                
                if event.ui_element == back_button:
                    running = False
                
                if event.ui_element == submit_button and ticket_presence:
                    ticket_entry_tbox.kill()
                    caller_profile_image.kill()
                    caller_profile_tbox.kill()
                    ticket_presence = False
                    ticket_timer = 0

                    main_sla_timer_label.set_text("SLA: ")

                    if selected_threat == answer:
                        print("Correct")
                        total_score += 1
                    else:
                        print("Wrong!")
                    
            manager.process_events(event)
        
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))


        if ticket_timer >= randomized_ticket_entry and not ticket_presence and caller_popup_window is None:
            caller_popup_window, accept_button, popup_window_countdown = elements.caller_popup_window_func(manager)
            popup_window_close_timer = 0

        if not ticket_ids_list and not ticket_presence:
            shift_report(total_score, total_tickets, missed_calls, 
                            missed_tickets, window_surface, clock, background, manager)
            running = False
        
        else:
            if caller_popup_window:
                caller_popup_window.show()
                manager.draw_ui(window_surface)
                popup_window_sla_countdown_difference = popup_window_sla_countdown - popup_window_close_timer

                popup_window_countdown.set_text("SLA: {:.1f}".format(max(0, popup_window_sla_countdown_difference)))
                popup_window_close_timer += time_delta

                if popup_window_sla_countdown_difference <= 0:
                    caller_popup_window.hide()
                    caller_popup_window = None
                    selected_id = random.choice(ticket_ids_list)
                    ticket_ids_list.remove(selected_id)
                    ticket_timer = 0
                    missed_calls += 1

                for event in pygame.event.get():
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == accept_button:
                            main_sla_timer = 0

                            selected_id = random.choice(ticket_ids_list)
                            cursor.execute('SELECT entry, answer, caller, picture_path FROM tickets WHERE id=?', [selected_id])
                            current_ticket, answer, caller, path = cursor.fetchone()
                            selected_threat = None

                            ticket_entry_tbox = elements.ticket_entry_tbox_func(manager, current_ticket)
                            caller_profile_image = elements.caller_profile_image_func(manager, path)
                            caller_profile_tbox = elements.caller_profile_tbox_func(manager, caller)
                            
                            ticket_presence = True
                            ticket_ids_list.remove(selected_id)

                            caller_popup_window.hide()
                            caller_popup_window = None
                    
                    manager.process_events(event)

            else:
                manager.draw_ui(window_surface)

            if ticket_presence and caller_popup_window is None:
                main_sla_countdown_difference = main_sla_countdown - main_sla_timer
                main_sla_timer_label.set_text("SLA: {:.1f}".format(max(0, main_sla_countdown_difference)))

                main_sla_timer += time_delta

                if main_sla_countdown_difference <= 0:

                    ticket_entry_tbox.kill()
                    caller_profile_image.kill()
                    caller_profile_tbox.kill()
                    ticket_presence = False
                    ticket_timer = 0
                    missed_tickets += 1

                    main_sla_timer_label.set_text("SLA: ")

        manager.draw_ui(window_surface)
        pygame.display.update()

    connect.close()


def shift_report(total_score, total_tickets, missed_calls,
                    missed_tickets, window_surface, clock, background, manager):
    
    manager.clear_and_reset()
    shift_report_tbox = elements.shift_report_tbox_func(manager, total_score, total_tickets, 
                                                        missed_calls, missed_tickets)
    end_shift_title_label = elements.end_shift_title_label_func(manager)
    end_shift_button = elements.end_shift_button_func(manager)

    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == end_shift_button:
                    running = False

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()