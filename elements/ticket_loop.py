import pygame
import pygame_gui


def back_button_func(manager):
    
    back_button_rect = pygame.Rect(5, 5, 30, 30)
    back_button = pygame_gui.elements.UIButton(relative_rect=back_button_rect,
                                                 text="<", manager=manager)
    return back_button


def title_text_entry_func(manager):

    title_label_rect = pygame.Rect(60, 25, 60, 30)
    title_label = pygame_gui.elements.UILabel(relative_rect=title_label_rect,
                                              text="TITLE", manager=manager)
    
    title_text_entry_rect = pygame.Rect(65, 50, 700, 30)
    title_text_entry = pygame_gui.elements.UITextEntryBox(relative_rect=title_text_entry_rect,
                                                          manager=manager)
    return title_label, title_text_entry


def ticket_text_entry_func(manager):

    ticket_label_rect = pygame.Rect(55, 85, 120, 30)
    ticket_label = pygame_gui.elements.UILabel(relative_rect=ticket_label_rect,
                                               text="DESCRIPTION", manager=manager)

    ticket_text_entry_rect = pygame.Rect(65, 110, 700, 200)
    ticket_text_entry = pygame_gui.elements.UITextEntryBox(relative_rect=ticket_text_entry_rect,
                                                           manager=manager)
    return ticket_label, ticket_text_entry


def threat_entry_slist_func(manager, threat_list):

    create_button_rect = pygame.Rect(0, 0, 300, 40)
    create_button_rect.bottomleft = (65, -10)
    create_button = pygame_gui.elements.UIButton(relative_rect=create_button_rect,
                                                 text="CREATE TICKET", manager=manager,
                                                 anchors={'left':'left', 'bottom':'bottom'})

    threat_entry_title_tbox_rect = pygame.Rect(65, -330, 300, 30)
    threat_entry_title_tbox = pygame_gui.elements.UITextBox(relative_rect=threat_entry_title_tbox_rect,
                                                            html_text="THREAT ENTRIES", manager=manager,
                                                            anchors = {'bottom':'bottom'})

    threat_entry_slist_rect = pygame.Rect(0, 0, 300, 250)
    threat_entry_slist_rect.bottomleft = (65, -50)
    threat_entry_slist = pygame_gui.elements.UISelectionList(item_list=threat_list,
                                                             relative_rect=threat_entry_slist_rect,
                                                             manager=manager,
                                                             anchors={'left':'left', 'bottom':'bottom'})
    
    return create_button, threat_entry_title_tbox, threat_entry_slist


def threat_description_tbox_func(manager):

    threat_description_tbox_rect = pygame.Rect(375, 320, 390, 320)
    threat_description_tbox = pygame_gui.elements.UITextBox(relative_rect=threat_description_tbox_rect,
                                                           html_text="SELECT A THREAT", manager=manager)
    return threat_description_tbox