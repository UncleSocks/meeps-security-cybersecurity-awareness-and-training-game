import pygame
import pygame_gui
import init
import queries
import elements.accounts_elements as accounts_elements


def accounts_management(connect, cursor):

    def account_management_init(connect, cursor):
    
        window_surface, clock, background = init.pygame_init()
        manager = init.pygame_gui_init()

        id_list, account_list = queries.accounts(cursor)
        ticket_list = []

        image_path = "assets/images/general/account_manager.png"

        back_button = accounts_elements.back_button_func(manager)
        create_button, delete_button = accounts_elements.create_delete_button_func(manager)
        account_entry_title_tbox = accounts_elements.account_entry_slist_misc_func(manager)
        account_entry_slist = accounts_elements.account_entry_slist_func(manager, account_list)
        assigned_ticket_label = accounts_elements.assigned_ticket_label_func(manager)
        assigned_ticket_slist = accounts_elements.assigned_tickets(manager, ticket_list)
        account_manager_image = accounts_elements.account_manager_image_func(manager, image_path)

        account_details_label, selected_account_description_tbox = accounts_elements.account_details(manager)

        return account_management_loop(window_surface, clock, background, manager, id_list, account_list, ticket_list,
                                       back_button, create_button, delete_button, account_entry_title_tbox, account_entry_slist, 
                                       assigned_ticket_label, assigned_ticket_slist, account_manager_image,
                                       account_details_label, selected_account_description_tbox)

    def account_management_loop(window_surface, clock, background, manager, id_list, account_list, ticket_list,
                                back_button, create_button, delete_button, account_entry_title_tbox, account_entry_slist, 
                                assigned_ticket_label, assigned_ticket_slist, account_manager_image,
                                account_details_label, selected_account_description_tbox):
        
        selected_account = None
        
        running = True
        while running:
            
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        running = False

                    elif event.ui_element == create_button:
                        id_list, account_list = account_creation(connect, cursor)
                        account_entry_slist.kill()
                        account_entry_slist = accounts_elements.account_entry_slist_func(manager, account_list)

                    elif event.ui_element == delete_button and selected_account is not None:
                        cursor.execute('DELETE FROM accounts WHERE id=?', [selected_account_id])
                        connect.commit()
                        id_list, account_list = queries.accounts(cursor)
                        account_entry_slist.kill()
                        account_entry_slist = accounts_elements.account_entry_slist_func(manager, account_list)


                if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                    if event.ui_element == account_entry_slist:
                        assigned_ticket_slist.kill()
                        selected_account = event.text

                        id_index_find = account_list.index(selected_account)
                        selected_account_id = id_list[id_index_find]
                        print(selected_account_id)

                        cursor.execute('SELECT name, organization, email, contact, picture FROM accounts WHERE id=?', [selected_account_id])
                        name, organization, email, contact, picture_path = cursor.fetchone()
                        selected_account_description_tbox.set_text(f"<b>Name:</b> {name}\n<b>Organization:</b> {organization}\n<b>Email:</b> {email}\n<b>Contact:</b> {contact}\n<b>Picture Filename:</b> {picture_path}")

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


    def account_creation(connect, cursor):

        window_surface, clock, background = init.pygame_init()
        manager = init.pygame_gui_init()

        back_button = accounts_elements.back_button_func(manager)

        account_name_label, new_account_name_tentry = accounts_elements.new_account_name_tentry_func(manager)
        organization_label, organization_tentry = accounts_elements.new_account_organization_func(manager)
        account_email, account_email_tentry = accounts_elements.new_account_email_func(manager)
        account_contact, account_contact_tentry = accounts_elements.new_account_contact_func(manager)
        account_picture_path_label, account_picture_path_tentry = accounts_elements.new_account_picture_path_func(manager)

        add_account_button = accounts_elements.add_new_account_button_func(manager)

        new_name = None
        new_organization = None
        new_email = None
        new_contact = None
        new_picture_path = None

        account_confirm_window = None

        running = True
        while running:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        updated_id_list, updated_account_list = queries.accounts(cursor)
                        print("back button")
                        return updated_id_list, updated_account_list
                    
                new_name = new_account_name_tentry.get_text()
                new_organization = organization_tentry.get_text()
                new_email = account_email_tentry.get_text()
                new_contact = account_contact_tentry.get_text()
                new_picture_path = account_picture_path_tentry.get_text()

                if new_name is not None and new_organization is not None and new_email is not None and new_contact is not None and new_picture_path is not None:
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == add_account_button:

                            cursor.execute('SELECT MAX(id) FROM accounts')
                            last_id = cursor.fetchone()[0]
                            new_id = last_id + 1

                            new_account = (new_id, new_name, new_organization, new_email, new_contact, new_picture_path)
                            cursor.execute('INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?)', new_account)
                            connect.commit()

                            account_confirm_window, account_confirm_close_button = accounts_elements.account_confirm_window_func(manager)

                    
                manager.process_events(event)
            
            manager.update(time_delta)

            window_surface.blit(background, (0,0))

            if account_confirm_window:
                account_confirm_window.show()
                manager.draw_ui(window_surface)

                for event in pygame.event.get():
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == account_confirm_close_button:
                            new_account_name_tentry.set_text("")
                            organization_tentry.set_text("")
                            account_email_tentry.set_text("")
                            account_contact_tentry.set_text("")
                            account_picture_path_tentry.set_text("")

                            account_confirm_window.hide()

                            new_name = None
                            new_organization = None
                            new_email = None
                            new_contact = None
                            new_picture_path = None
                            account_confirm_window = None
                    
                    manager.process_events(event)

            manager.update(time_delta)

            window_surface.blit(background, (0,0))
            manager.draw_ui(window_surface)
            pygame.display.update()

    account_management_init(connect, cursor)