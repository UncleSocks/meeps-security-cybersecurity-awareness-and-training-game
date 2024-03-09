import pygame
import pygame_gui


def back_button_func(manager):
    
    back_button_rect = pygame.Rect(5, 5, 30, 30)
    back_button = pygame_gui.elements.UIButton(relative_rect=back_button_rect,
                                                 text="<", manager=manager)
    return back_button


def create_ticket_button_func(manager):

    create_button_rect = pygame.Rect(600, 5, 180, 40)
    create_button = pygame_gui.elements.UIButton(relative_rect=create_button_rect,
                                                 text="CREATE TICKET", manager=manager)
    
    return create_button


def ticket_entry_slist_misc_func(manager):

    delete_button_rect = pygame.Rect(0, 0, 300, 40)
    delete_button_rect.bottomleft = (65, -10)
    delete_button = pygame_gui.elements.UIButton(relative_rect=delete_button_rect,
                                                 text="DELETE TICKET", manager=manager,
                                                 anchors={'left':'left', 'bottom':'bottom'})
    
    ticket_entry_title_tbox_rect = pygame.Rect(65, -645, 300, 30)
    ticket_entry_title_tbox = pygame_gui.elements.UITextBox(relative_rect=ticket_entry_title_tbox_rect,
                                                            html_text="TICKET MANAGER", manager=manager,
                                                            anchors = {'bottom':'bottom'})
    
    return delete_button, ticket_entry_title_tbox


def ticket_entry_slist_func(manager, ticket_list):
    
    ticket_entry_slist_rect = pygame.Rect(0, 0, 300, 565)
    ticket_entry_slist_rect.bottomleft = (65, -50)
    ticket_entry_slist = pygame_gui.elements.UISelectionList(item_list=ticket_list,
                                                             relative_rect=ticket_entry_slist_rect,
                                                             manager=manager,
                                                             anchors={'left':'left', 'bottom':'bottom'})
    
    return ticket_entry_slist


def selected_ticket_tbox_func(manager):

    selected_ticket_title_tbox_rect = pygame.Rect(375, 65, 405, 30)
    selected_ticket_title_tbox = pygame_gui.elements.UITextBox(relative_rect=selected_ticket_title_tbox_rect,
                                                               html_text="", manager=manager)
    
    selected_ticket_description_tbox_rect = pygame.Rect(375, 100, 405, 400)
    selected_ticket_description_tbox = pygame_gui.elements.UITextBox(relative_rect=selected_ticket_description_tbox_rect,
                                                               html_text="SELECT A TICKET", manager=manager)
    
    return selected_ticket_title_tbox, selected_ticket_description_tbox


def title_text_entry_func(manager):

    title_label_rect = pygame.Rect(60, 0, 60, 30)
    title_label = pygame_gui.elements.UILabel(relative_rect=title_label_rect,
                                              text="TITLE", manager=manager)
    
    title_text_entry_rect = pygame.Rect(65, 25, 700, 30)
    title_text_entry = pygame_gui.elements.UITextEntryBox(relative_rect=title_text_entry_rect,
                                                          manager=manager)
    return title_label, title_text_entry


def ticket_text_entry_func(manager):

    ticket_label_rect = pygame.Rect(55, 65, 120, 30)
    ticket_label = pygame_gui.elements.UILabel(relative_rect=ticket_label_rect,
                                               text="DESCRIPTION", manager=manager)

    ticket_text_entry_rect = pygame.Rect(65, 90, 700, 200)
    ticket_text_entry = pygame_gui.elements.UITextEntryBox(relative_rect=ticket_text_entry_rect,
                                                           manager=manager)
    return ticket_label, ticket_text_entry


def threat_entry_slist_func(manager, threat_list):

    create_button_rect = pygame.Rect(0, 0, 300, 40)
    create_button_rect.bottomleft = (65, -10)
    create_button = pygame_gui.elements.UIButton(relative_rect=create_button_rect,
                                                 text="CREATE TICKET", manager=manager,
                                                 anchors={'left':'left', 'bottom':'bottom'})

    threat_entry_title_tbox_rect = pygame.Rect(65, -350, 300, 30)
    threat_entry_title_tbox = pygame_gui.elements.UITextBox(relative_rect=threat_entry_title_tbox_rect,
                                                            html_text="TICKET RESOLUTION", manager=manager,
                                                            anchors = {'bottom':'bottom'})

    threat_entry_slist_rect = pygame.Rect(0, 0, 300, 270)
    threat_entry_slist_rect.bottomleft = (65, -50)
    threat_entry_slist = pygame_gui.elements.UISelectionList(item_list=threat_list,
                                                             relative_rect=threat_entry_slist_rect,
                                                             manager=manager,
                                                             anchors={'left':'left', 'bottom':'bottom'})
    
    return create_button, threat_entry_title_tbox, threat_entry_slist


def threat_description_tbox_func(manager):

    threat_description_tbox_rect = pygame.Rect(375, 300, 390, 340)
    threat_description_tbox = pygame_gui.elements.UITextBox(relative_rect=threat_description_tbox_rect,
                                                           html_text="SELECT A THREAT", manager=manager)
    return threat_description_tbox


def ticket_confirm_window_func(manager):
    
    ticket_confirm_window_rect = pygame.Rect(0, 0, 400, 200)
    ticket_confirm_window = pygame_gui.elements.UIWindow(rect=ticket_confirm_window_rect,
                                                 window_display_title="MEEPS SECURITY: New Ticket",
                                                 manager=manager)
    
    ticket_confirm_window_label_rect = pygame.Rect(0, -10, 300, 200)
    ticket_confirm_window_label = pygame_gui.elements.UILabel(relative_rect=ticket_confirm_window_label_rect, 
                                                            text="TTCKET SUCCESSFULLY CREATED", 
                                                            manager=manager,
                                                            container=ticket_confirm_window,
                                                            anchors={'center':'center'})
    
    ticket_confirm_close_button_rect = pygame.Rect(10, 10, 200, 40)
    ticket_confirm_close_button_rect.bottomright = (285, -10)
    ticket_confirm_close_button = pygame_gui.elements.UIButton(relative_rect=ticket_confirm_close_button_rect, 
                                                                     text="OK", manager=manager,container=ticket_confirm_window,
                                                                     anchors={'left':'left', 'bottom':'bottom'})
    
    return ticket_confirm_window, ticket_confirm_close_button