import pygame
import pygame_gui


def back_button_func(manager):
    
    back_button_rect = pygame.Rect(5, 5, 30, 30)
    back_button = pygame_gui.elements.UIButton(relative_rect=back_button_rect,
                                                 text="<", manager=manager)
    return back_button


def create_delete_button_func(manager):

    create_button_rect = pygame.Rect(0, 0, 45, 30)
    create_button_rect.bottomleft = (320, -470)
    create_button = pygame_gui.elements.UIButton(relative_rect=create_button_rect,
                                                 text="+", manager=manager,
                                                 anchors={'bottom':'bottom', 'left':'left'})
    
    delete_button_rect = pygame.Rect(0, 0, 45, 30)
    delete_button_rect.bottomleft = (280, -470)
    delete_button = pygame_gui.elements.UIButton(relative_rect=delete_button_rect,
                                                 text="-", manager=manager,
                                                 anchors={'bottom':'bottom', 'left':'left'})
    
    return create_button, delete_button


def account_entry_slist_misc_func(manager):

    account_entry_title_tbox_rect = pygame.Rect(0, 0, 265, 30)
    account_entry_title_tbox_rect.bottomleft = (15, -470)
    account_entry_title_tbox = pygame_gui.elements.UITextBox(relative_rect=account_entry_title_tbox_rect, 
                                                             html_text="ACCOUNT LIST", manager=manager,
                                                             anchors={'left':'left', 'bottom':'bottom'})
    return account_entry_title_tbox


def account_entry_slist_func(manager, account_list):

    account_entry_slist_rect = pygame.Rect(0, 0, 350, 460)
    account_entry_slist_rect.bottomleft = (15, -10)
    account_entry_slist = pygame_gui.elements.UISelectionList(item_list=account_list,
                                                              relative_rect=account_entry_slist_rect,
                                                              manager=manager,
                                                              anchors={'left':'left', 'bottom':'bottom'})

    return account_entry_slist


def account_details(manager):

    account_details_label_rect = pygame.Rect(360, 10, 150, 30)
    account_details_label = pygame_gui.elements.UILabel(relative_rect=account_details_label_rect,
                                                           text="ACCOUNT DETAILS", manager=manager)
    
    selected_account_description_tbox_rect = pygame.Rect(375, 40, 405, 160)
    selected_account_description_tbox = pygame_gui.elements.UITextBox(relative_rect=selected_account_description_tbox_rect,
                                                                     html_text="SELECT AN ACCOUNT", manager=manager)
    
    return account_details_label, selected_account_description_tbox


def assigned_ticket_label_func(manager):

    assigned_ticket_label_rect = pygame.Rect(365, 220, 150, 30)
    assigned_ticket_label = pygame_gui.elements.UILabel(relative_rect=assigned_ticket_label_rect,
                                                        text="ASSIGNED TICKETS", manager=manager)
    
    return assigned_ticket_label


def assigned_tickets(manager, ticket_list):
    
    assigned_ticket_slist_rect = pygame.Rect(375, 250, 405, 390)
    assigned_ticket_slist = pygame_gui.elements.UISelectionList(item_list=ticket_list, 
                                                                relative_rect=assigned_ticket_slist_rect,
                                                                manager=manager)
    return assigned_ticket_slist


def new_account_name_tentry_func(manager):

    account_name_label_rect = pygame.Rect(20, 100, 100, 30)
    account_name_label = pygame_gui.elements.UILabel(relative_rect=account_name_label_rect,
                                                     text="ACCOUNT NAME", manager=manager)
    
    new_account_name_tentry_rect = pygame.Rect(15, 125, 765, 30)
    new_account_name_tentry = pygame_gui.elements.UITextEntryBox(relative_rect=new_account_name_tentry_rect,
                                                                 manager=manager)
    return account_name_label, new_account_name_tentry

def new_account_organization_func(manager):

    organization_label_rect = pygame.Rect(20, 170, 100, 30)
    organization_label = pygame_gui.elements.UILabel(relative_rect=organization_label_rect,
                                                     text="ORGANIZATION NAME", manager=manager)
    
    organization_tentry_rect = pygame.Rect(15, 195, 765, 30)
    organization_tentry = pygame_gui.elements.UITextEntryBox(relative_rect=organization_tentry_rect, 
                                                             manager=manager)
    
    return organization_label, organization_tentry


def new_account_email_func(manager):

    account_email_rect = pygame.Rect(20, 240, 50, 30)
    account_email = pygame_gui.elements.UILabel(relative_rect=account_email_rect,
                                                text="EMAIL", manager=manager)
    
    account_email_tentry_rect = pygame.Rect(15, 265, 765, 30)
    account_email_tentry = pygame_gui.elements.UITextEntryBox(relative_rect=account_email_tentry_rect,
                                                              manager=manager)
    
    return account_email, account_email_tentry


def new_account_contact_func(manager):

    account_contact_rect = pygame.Rect(20, 310, 65, 30)
    account_contact = pygame_gui.elements.UILabel(relative_rect=account_contact_rect,
                                                  text="CONTACT", manager=manager)
    
    account_contact_tentry_rect = pygame.Rect(15, 335, 765, 30)
    account_contact_tentry = pygame_gui.elements.UITextEntryBox(relative_rect=account_contact_tentry_rect,
                                                                manager=manager)
    
    return account_contact, account_contact_tentry


def new_account_picture_path_func(manager):

    account_picture_path_label_rect = pygame.Rect(15, 385, 100, 30)
    account_picture_path_label = pygame_gui.elements.UILabel(relative_rect=account_picture_path_label_rect,
                                                             text="PICTURE PATH", manager=manager)
    
    account_picture_path_tentry_rect = pygame.Rect(15, 405, 765, 30)
    account_picture_path_tentry = pygame_gui.elements.UITextEntryBox(relative_rect=account_picture_path_tentry_rect,
                                                                     manager=manager)
    
    return account_picture_path_label, account_picture_path_tentry


def add_new_account_button_func(manager):

    add_account_button_rect = pygame.Rect(15, 455, 120, 40)
    add_account_button = pygame_gui.elements.UIButton(relative_rect=add_account_button_rect, 
                                                      text="ADD ACCOUNT", manager=manager)
    return add_account_button


def account_confirm_window_func(manager):
    
    account_confirm_window_rect = pygame.Rect(0, 0, 400, 200)
    account_confirm_window = pygame_gui.elements.UIWindow(rect=account_confirm_window_rect,
                                                 window_display_title="MEEPS SECURITY: New Account",
                                                 manager=manager)
    
    account_confirm_window_label_rect = pygame.Rect(0, -10, 300, 200)
    account_confirm_window_label = pygame_gui.elements.UILabel(relative_rect=account_confirm_window_label_rect, 
                                                            text="ACCOUNT SUCCESSFULLY CREATED", 
                                                            manager=manager,
                                                            container=account_confirm_window,
                                                            anchors={'center':'center'})
    
    account_confirm_close_button_rect = pygame.Rect(10, 10, 200, 40)
    account_confirm_close_button_rect.bottomright = (285, -10)
    account_confirm_close_button = pygame_gui.elements.UIButton(relative_rect=account_confirm_close_button_rect, 
                                                                     text="OK", manager=manager,container=account_confirm_window,
                                                                     anchors={'left':'left', 'bottom':'bottom'})
    
    return account_confirm_window, account_confirm_close_button