import pygame
import pygame_gui


def back_button_func(manager):
    
    back_button_rect = pygame.Rect(5, 5, 30, 30)
    back_button = pygame_gui.elements.UIButton(relative_rect=back_button_rect,
                                                 text="<", manager=manager)
    return back_button


def title_label_func(manager):

    title_label_rect = pygame.Rect(10, 5, 150, 100)
    title_label = pygame_gui.elements.UILabel(relative_rect=title_label_rect,
                                              text="MEEPS SECURITY",
                                              manager=manager)
    return title_label


def main_sla_timer_label_func(manager):
    
    main_sla_timer_label_rect = pygame.Rect(210, 140, 100, 60)
    main_sla_timer_label = pygame_gui.elements.UILabel(relative_rect=main_sla_timer_label_rect,
                                                       text="SLA: ", manager=manager)
    return main_sla_timer_label


def caller_profile_tbox_func(manager, caller_profile):

    caller_profile_tbox_rect = pygame.Rect(120, 180, 195, 100)
    caller_profile_tbox = pygame_gui.elements.UITextBox(relative_rect=caller_profile_tbox_rect,
                                                        html_text=caller_profile,
                                                        manager=manager)
    return caller_profile_tbox


def caller_profile_image_func(manager, image_path):

    caller_profile_image_rect = pygame.Rect(18, 180, 98, 98)
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

    threat_entry_title_tbox_rect = pygame.Rect(15, -360, 300, 30)
    threat_entry_title_tbox = pygame_gui.elements.UITextBox(relative_rect=threat_entry_title_tbox_rect,
                                                            html_text="THREAT ENTRIES", manager=manager,
                                                            anchors = {'bottom':'bottom'})
    return threat_entry_title_tbox


def threat_entry_slist_func(manager, threat_list):

    threat_entry_slist_rect = pygame.Rect(0, 0, 300, 280)
    threat_entry_slist_rect.bottomleft = (15, -50)
    threat_entry_slist = pygame_gui.elements.UISelectionList(item_list=threat_list,
                                                             relative_rect=threat_entry_slist_rect,
                                                             manager=manager,
                                                             anchors={'left':'left', 'bottom':'bottom'})
    return threat_entry_slist


def threat_description_tbox_func(manager):

    threat_description_tbox_rect = pygame.Rect(0, 0, 460, 350)
    threat_description_tbox_rect.bottomright = (-15, -10)
    threat_description_tbox = pygame_gui.elements.UITextBox(relative_rect=threat_description_tbox_rect,
                                                           html_text="SELECT A THREAT", manager=manager,
                                                           anchors={'right':'right', 'bottom':'bottom'})
    return threat_description_tbox


def ticket_title_tbox_func(manager, current_title):

    ticket_title_tbox_rect = pygame.Rect(325, 20, 460, 40)
    ticket_title_tbox = pygame_gui.elements.UITextBox(relative_rect=ticket_title_tbox_rect, 
                                                       html_text=current_title, manager=manager)
    return ticket_title_tbox


def ticket_entry_tbox_func(manager, current_ticket):

    ticket_entry_tbox_rect = pygame.Rect(325, 60, 460, 220)
    ticket_entry_tbox = pygame_gui.elements.UITextBox(relative_rect=ticket_entry_tbox_rect, 
                                                       html_text=current_ticket, manager=manager)
    return ticket_entry_tbox


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


def shift_report_tbox_func(manager, score, ticket_count, missed_calls, missed_tickets):
    
    shift_report_tbox_rect = pygame.Rect(0, 0, 300, 170)
    shift_report_tbox = pygame_gui.elements.UITextBox(relative_rect=shift_report_tbox_rect,
                                                           html_text=f"<b>Employee No:</b> #1361\n<b>Title:</b> L1 SOC Analyst\n<b>Total Tickets:</b> {ticket_count}\n<b>Correct Assessment:</b> {score}\n<b>Missed Calls:</b> {missed_calls}\n<b>Missed Tickets:</b> {missed_tickets}", 
                                                           manager=manager,
                                                           anchors={'center':'center'})
    return shift_report_tbox


def end_shift_button_func(manager):

    end_shift_button_rect = pygame.Rect(0, -210, 300, 40)
    end_shift_button = pygame_gui.elements.UIButton(relative_rect=end_shift_button_rect,
                                                 text="END SHIFT", manager=manager,
                                                 anchors={'centerx':'centerx', 'bottom':'bottom'})
    return end_shift_button


def end_shift_title_label_func(manager):

    end_shift_title_label_rect = pygame.Rect(0, 170, 100, 60)
    end_shift_title_label = pygame_gui.elements.UILabel(relative_rect=end_shift_title_label_rect,
                                                       text="SHIFT REPORT", manager=manager,
                                                       anchors={'centerx':'centerx'})
    return end_shift_title_label


def start_button_func(manager):

    start_button_rect = pygame.Rect(0, 30, 300, 40)
    start_button = pygame_gui.elements.UIButton(relative_rect=start_button_rect,
                                                 text="START SHIFT", manager=manager,
                                                 anchors={'center':'center'})
    return start_button


def ticket_creation_button_func(manager):

    ticket_creation_button_rect = pygame.Rect(0, -255, 300, 40)
    ticket_creation_button = pygame_gui.elements.UIButton(relative_rect=ticket_creation_button_rect,
                                                 text="CREATE TICKET", manager=manager,
                                                 anchors={'centerx':'centerx', 'bottom':'bottom'})
    return ticket_creation_button


def quit_button_func(manager):

    quit_button_rect = pygame.Rect(0, -195, 300, 40)
    quit_button = pygame_gui.elements.UIButton(relative_rect=quit_button_rect,
                                                 text="LOG OFF", manager=manager,
                                                 anchors={'centerx':'centerx', 'bottom':'bottom'})
    return quit_button