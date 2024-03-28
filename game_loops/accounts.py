import pygame
import pygame_gui
import init
import queries
import elements.accounts_elements as accounts_elements


def accounts_management(connect, cursor):

    window_surface, clock, background = init.pygame_init()
    manager = init.pygame_gui_init()

    id_list, account_list = queries.accounts(cursor)
    ticket_list = []

    back_button = accounts_elements.back_button_func(manager)
    create_button, delete_button = accounts_elements.create_delete_button_func(manager)
    account_entry_title_tbox = accounts_elements.account_entry_slist_misc_func(manager)
    account_entry_slist = accounts_elements.account_entry_slist_func(manager, account_list)
    assigned_ticket_label = accounts_elements.assigned_ticket_label_func(manager)
    assigned_ticket_slist = accounts_elements.assigned_tickets(manager, ticket_list)

    account_details_label, selected_account_description_tbox = accounts_elements.account_details(manager)


    running = True
    while running:
        
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                    running = False

            if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == account_entry_slist:
                    assigned_ticket_slist.kill()
                    selected_account = event.text

                    id_index_find = account_list.index(selected_account)
                    selected_account_id = id_list[id_index_find]
                    print(selected_account_id)

                    cursor.execute('SELECT name, organization, email, contact, picture FROM accounts WHERE id=?', [selected_account_id])
                    name, organization, email, contact, picture_path = cursor.fetchone()
                    selected_account_description_tbox.set_text(f"<b>Name:</b> {name}\n<b>Organization:</b> {organization}\n<b>Emai:</b> {email}\n<b>Contact:</b> {contact}\n<b>Picture Path:</b> {picture_path}")

                    cursor.execute('SELECT title FROM tickets WHERE caller_id=?', [selected_account_id])
                    assigned_tickets_results = cursor.fetchall()
                    ticket_list = [assigned_tickets_result[0] for assigned_tickets_result in assigned_tickets_results]
                    print(ticket_list)
                    assigned_ticket_slist = accounts_elements.assigned_tickets(manager, ticket_list)

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0,0))
        manager.draw_ui(window_surface)
        pygame.display.update()