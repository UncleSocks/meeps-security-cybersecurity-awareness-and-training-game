import pygame
import pygame_gui


def back_button_func(manager):
    
    back_button_rect = pygame.Rect(5, 5, 30, 30)
    back_button = pygame_gui.elements.UIButton(relative_rect=back_button_rect,
                                                 text="<", manager=manager)
    return back_button


def threat_database_image_func(manager, image_path):

    threat_database_image_rect = pygame.Rect(20, 35, 320, 80)
    threat_database_image_load = pygame.image.load(image_path)
    threat_database_image = pygame_gui.elements.UIImage(relative_rect=threat_database_image_rect,
                                                       image_surface=threat_database_image_load,
                                                       manager=manager)
    return threat_database_image


def create_button_button_func(manager):

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


def threat_entry_slist_misc_func(manager):
    
    threat_entry_title_tbox_rect = pygame.Rect(0, 0, 265, 30)
    threat_entry_title_tbox_rect.bottomleft = (15, -470)
    threat_entry_title_tbox = pygame_gui.elements.UITextBox(relative_rect=threat_entry_title_tbox_rect,
                                                            html_text="THREAT ENTRIES", manager=manager,
                                                            anchors={'left':'left', 'bottom':'bottom'})
    
    return threat_entry_title_tbox


def threat_entry_slist_func(manager, threat_list):
    
    threat_entry_slist_rect = pygame.Rect(0, 0, 350, 460)
    threat_entry_slist_rect.bottomleft = (15, -10)
    threat_entry_slist = pygame_gui.elements.UISelectionList(item_list=threat_list,
                                                             relative_rect=threat_entry_slist_rect,
                                                             manager=manager,
                                                             anchors={'left':'left', 'bottom':'bottom'})
    
    return threat_entry_slist


def threat_details_func(manager):

    threat_details_label_rect = pygame.Rect(360, 15, 150, 30)
    threat_details_label = pygame_gui.elements.UILabel(relative_rect=threat_details_label_rect,
                                                           text="THREAT DETAILS", manager=manager)
    
    selected_threat_title_tbox_rect = pygame.Rect(375, 40, 405, 30)
    selected_threat_title_tbox = pygame_gui.elements.UITextBox(relative_rect=selected_threat_title_tbox_rect,
                                                               html_text="", manager=manager)
    
    selected_threat_description_tbox_rect = pygame.Rect(375, 75, 405, 185)
    selected_threat_description_tbox = pygame_gui.elements.UITextBox(relative_rect=selected_threat_description_tbox_rect,
                                                                     html_text="THREAT DESCRIPTION", manager=manager)
    
    selected_threat_indicators_tbox_rect = pygame.Rect(375, 265, 405, 185)
    selected_threat_indicators_tbox = pygame_gui.elements.UITextBox(relative_rect=selected_threat_indicators_tbox_rect,
                                                                     html_text="THREAT INDICATORS", manager=manager)
    
    selected_threat_countermeasures_tbox_rect = pygame.Rect(375, 455, 405, 185)
    selected_threat_countermeasures_tbox = pygame_gui.elements.UITextBox(relative_rect=selected_threat_countermeasures_tbox_rect,
                                                                     html_text="THREAT COUNTERMEASURES", manager=manager)
    
    return threat_details_label, selected_threat_title_tbox, selected_threat_description_tbox, selected_threat_indicators_tbox, selected_threat_countermeasures_tbox