import pygame
import pygame_gui


def back_button_func(manager):
    
    back_button_rect = pygame.Rect(5, 5, 30, 30)
    back_button = pygame_gui.elements.UIButton(relative_rect=back_button_rect,
                                                 text="<", manager=manager)
    return back_button


def ticket_manager_image_func(manager, image_path):

    ticket_manager_image_rect = pygame.Rect(20, 35, 320, 75)
    ticket_manager_image_load = pygame.image.load(image_path)
    ticket_manager_image = pygame_gui.elements.UIImage(relative_rect=ticket_manager_image_rect,
                                                       image_surface=ticket_manager_image_load,
                                                       manager=manager)
    return ticket_manager_image


def create_ticket_button_func(manager):

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


def ticket_entry_slist_misc_func(manager):
    
    ticket_entry_title_tbox_rect = pygame.Rect(0, 0, 265, 30)
    ticket_entry_title_tbox_rect.bottomleft = (15, -470)
    ticket_entry_title_tbox = pygame_gui.elements.UITextBox(relative_rect=ticket_entry_title_tbox_rect,
                                                            html_text="TICKET LIST", manager=manager,
                                                            anchors={'left':'left', 'bottom':'bottom'})
    
    return ticket_entry_title_tbox


def ticket_entry_slist_func(manager, ticket_list):
    
    ticket_entry_slist_rect = pygame.Rect(0, 0, 350, 460)
    ticket_entry_slist_rect.bottomleft = (15, -10)
    ticket_entry_slist = pygame_gui.elements.UISelectionList(item_list=ticket_list,
                                                             relative_rect=ticket_entry_slist_rect,
                                                             manager=manager,
                                                             anchors={'left':'left', 'bottom':'bottom'})
    
    return ticket_entry_slist


def ticket_information_label_func(manager):

    ticket_information_label_rect = pygame.Rect(360, 10, 150, 30)
    ticket_information_label = pygame_gui.elements.UILabel(relative_rect=ticket_information_label_rect,
                                                           text="TICKET DETAILS", manager=manager)
    return ticket_information_label


def selected_ticket_tbox_func(manager):
    
    selected_ticket_title_tbox_rect = pygame.Rect(375, 35, 405, 30)
    selected_ticket_title_tbox = pygame_gui.elements.UITextBox(relative_rect=selected_ticket_title_tbox_rect,
                                                               html_text="", manager=manager)
    
    selected_ticket_description_tbox_rect = pygame.Rect(375, 70, 405, 570)
    selected_ticket_description_tbox = pygame_gui.elements.UITextBox(relative_rect=selected_ticket_description_tbox_rect,
                                                               html_text="SELECT A TICKET", manager=manager)
    
    return selected_ticket_title_tbox, selected_ticket_description_tbox


def new_ticket_image_func(manager, image_path):

    new_ticket_image_rect = pygame.Rect(50, 10, 200, 20)
    new_ticket_image_load = pygame.image.load(image_path)
    new_ticket_image = pygame_gui.elements.UIImage(relative_rect=new_ticket_image_rect,
                                                       image_surface=new_ticket_image_load,
                                                       manager=manager)
    
    return new_ticket_image

def bar_image_func(manager, image_path):

    bar_image_rect = pygame.Rect(255, 15, 520, 10)
    bar_image_load = pygame.image.load(image_path)
    bar_image = pygame_gui.elements.UIImage(relative_rect=bar_image_rect,
                                                       image_surface=bar_image_load,
                                                       manager=manager)
    
    return bar_image


def title_text_entry_func(manager):
    
    title_text_entry_rect = pygame.Rect(15, 85, 765, 30)
    title_text_entry = pygame_gui.elements.UITextEntryBox(relative_rect=title_text_entry_rect,
                                                          placeholder_text="Enter Ticket Title",
                                                          initial_text="Enter Ticket Title",
                                                          manager=manager)
    return title_text_entry


def ticket_text_entry_func(manager):

    ticket_text_entry_rect = pygame.Rect(15, 120, 765, 240)
    ticket_text_entry = pygame_gui.elements.UITextEntryBox(relative_rect=ticket_text_entry_rect,
                                                           placeholder_text="Enter Ticket Description",
                                                           initial_text="Enter Ticket Description",
                                                           manager=manager)
    return ticket_text_entry


def threat_entry_slist_func(manager, threat_list):

    create_button_rect = pygame.Rect(0, 0, 300, 40)
    create_button_rect.bottomleft = (15, -10)
    create_button = pygame_gui.elements.UIButton(relative_rect=create_button_rect,
                                                 text="CREATE TICKET", manager=manager,
                                                 anchors={'left':'left', 'bottom':'bottom'})

    threat_entry_title_tbox_rect = pygame.Rect(0, 0, 300, 30)
    threat_entry_title_tbox_rect.bottomleft = (15, -250)
    threat_entry_title_tbox = pygame_gui.elements.UITextBox(relative_rect=threat_entry_title_tbox_rect,
                                                            html_text="TICKET RESOLUTION", manager=manager,
                                                            anchors={'left':'left', 'bottom':'bottom'})

    threat_entry_slist_rect = pygame.Rect(0, 0, 300, 200)
    threat_entry_slist_rect.bottomleft = (15, -50)
    threat_entry_slist = pygame_gui.elements.UISelectionList(item_list=threat_list,
                                                             relative_rect=threat_entry_slist_rect,
                                                             manager=manager,
                                                             anchors={'left':'left', 'bottom':'bottom'})
    
    return create_button, threat_entry_title_tbox, threat_entry_slist


def threat_description_tbox_func(manager):

    threat_description_tbox_rect = pygame.Rect(325, 370, 455, 270)
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