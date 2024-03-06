import pygame
import pygame_gui


def title_label_func(manager):

    title_label_rect = pygame.Rect(10, 5, 150, 100)
    title_label = pygame_gui.elements.UILabel(relative_rect=title_label_rect,
                                              text="MEEPS SECURITY",
                                              manager=manager)
    return title_label


def main_sla_timer_label_func(manager):
    
    main_sla_timer_label_rect = pygame.Rect(210, 95, 100, 60)
    main_sla_timer_label = pygame_gui.elements.UILabel(relative_rect=main_sla_timer_label_rect,
                                                       text="SLA: ", manager=manager)
    return main_sla_timer_label


def caller_profile_tbox_func(manager, caller_profile):

    caller_profile_tbox_rect = pygame.Rect(120, 135, 195, 100)
    caller_profile_tbox = pygame_gui.elements.UITextBox(relative_rect=caller_profile_tbox_rect,
                                                        html_text=caller_profile,
                                                        manager=manager)
    return caller_profile_tbox


def caller_profile_image_func(manager, image_path):

    caller_profile_image_rect = pygame.Rect(18, 135, 98, 98)
    caller_profile_image_load = pygame.image.load(image_path)
    caller_profile_image = pygame_gui.elements.UIImage(relative_rect=caller_profile_image_rect,
                                                       image_surface=caller_profile_image_load,
                                                       manager=manager)
    return caller_profile_image


def submit_button_func(manager):

    submit_button_rect = pygame.Rect(0, 0, 300, 40)
    submit_button_rect.bottomleft = (15, -10)
    submit_button = pygame_gui.elements.UIButton(relative_rect=submit_button_rect,
                                                 text="SUBMIT", manager=manager,
                                                 anchors={'left':'left', 'bottom':'bottom'})
    return submit_button


def threat_entry_title_tbox_func(manager):

    threat_entry_title_tbox_rect = pygame.Rect(15, 240, 300, 30)
    threat_entry_title_tbox = pygame_gui.elements.UITextBox(relative_rect=threat_entry_title_tbox_rect,
                                                            html_text="THREAT ENTRIES", manager=manager)
    return threat_entry_title_tbox


def threat_entry_slist_func(manager, threat_list):

    threat_entry_slist_rect = pygame.Rect(0, 0, 300, 280)
    threat_entry_slist_rect.bottomleft = (15, -50)
    threat_entry_slist = pygame_gui.elements.UISelectionList(item_list=threat_list,
                                                             relative_rect=threat_entry_slist_rect,
                                                             manager=manager,
                                                             anchors={'left':'left', 'bottom':'bottom'})
    return threat_entry_slist


def threat_description_label_func(manager):

    threat_description_label_rect = pygame.Rect(0, 0, 460, 350)
    threat_description_label_rect.bottomright = (-15, -10)
    threat_description_label = pygame_gui.elements.UITextBox(relative_rect=threat_description_label_rect,
                                                           html_text="SELECT A THREAT", manager=manager,
                                                           anchors={'right':'right', 'bottom':'bottom'})
    return threat_description_label


def ticket_entry_label_func(manager, current_ticket):

    ticket_entry_label_rect = pygame.Rect(325, 15, 460, 220)
    ticket_entry_label = pygame_gui.elements.UITextBox(relative_rect=ticket_entry_label_rect, 
                                                       html_text=current_ticket, manager=manager)
    return ticket_entry_label


def caller_popup_window_func(manager):
    
    caller_popup_window_rect = pygame.Rect(0, 0, 400, 200)
    caller_popup_window = pygame_gui.elements.UIWindow(rect=caller_popup_window_rect,
                                                 window_display_title="MEEPS Security: New Caller",
                                                 manager=manager)
    
    caller_popup_window_label_rect = pygame.Rect(15, -60, 300, 200)
    caller_popup_window_label = pygame_gui.elements.UILabel(relative_rect=caller_popup_window_label_rect, 
                                                            text="INCOMING CALLER...", 
                                                            manager=manager,
                                                            container=caller_popup_window)

    caller_popup_window_sla_timer_label_rect = pygame.Rect(0, 0, 100, 60)
    caller_popup_window_sla_timer_label_rect.bottomright = (-30, -5)
    caller_popup_window_sla_timer_label = pygame_gui.elements.UILabel(relative_rect=caller_popup_window_sla_timer_label_rect, 
                                                                      text="SLA: ", manager=manager,container=caller_popup_window,
                                                                      anchors={'right':'right', 'bottom':'bottom'})
    
    caller_popup_window_answer_button_rect = pygame.Rect(0, 0, 200, 40)
    caller_popup_window_answer_button_rect.bottomleft = (15, -10)
    caller_popup_window_answer_button = pygame_gui.elements.UIButton(relative_rect=caller_popup_window_answer_button_rect, 
                                                                     text="ANSWER", manager=manager,container=caller_popup_window,
                                                                     anchors={'left':'left', 'bottom':'bottom'})
    
    return caller_popup_window, caller_popup_window_answer_button, caller_popup_window_sla_timer_label


def start_button_func(manager):

    start_button_rect = pygame.Rect(0, 0, 300, 40)
    start_button_rect.bottomleft = (15, -10)
    start_button = pygame_gui.elements.UIButton(relative_rect=start_button_rect,
                                                 text="START SHIFT", manager=manager,
                                                 anchors={'center':'center'})
    return start_button