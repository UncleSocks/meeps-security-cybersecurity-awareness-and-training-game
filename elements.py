import pygame
import pygame_gui


def back_button_func(manager):
    
    back_button_rect = pygame.Rect(5, 5, 30, 30)
    back_button = pygame_gui.elements.UIButton(relative_rect=back_button_rect,
                                                 text="<", manager=manager)
    return back_button


def title_image_func(manager, image_path):

    title_image_rect = pygame.Rect(30, 35, 280, 110)
    title_image_load = pygame.image.load(image_path)
    title_image = pygame_gui.elements.UIImage(relative_rect=title_image_rect,
                                                       image_surface=title_image_load,
                                                       manager=manager)
    return title_image


def main_sla_timer_label_func(manager):
    
    main_sla_timer_label_rect = pygame.Rect(210, 140, 100, 60)
    main_sla_timer_label = pygame_gui.elements.UILabel(relative_rect=main_sla_timer_label_rect,
                                                       text="SLA: ", manager=manager)
    return main_sla_timer_label


def caller_profile_tbox_func(manager):

    caller_profile_tbox_rect = pygame.Rect(120, 180, 195, 100)
    caller_profile_tbox = pygame_gui.elements.UITextBox(relative_rect=caller_profile_tbox_rect,
                                                        html_text="NO CALLER",
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


def ticket_title_tbox_func(manager):

    ticket_title_tbox_rect = pygame.Rect(325, 5, 460, 40)
    ticket_title_tbox = pygame_gui.elements.UITextBox(relative_rect=ticket_title_tbox_rect, 
                                                       html_text="", manager=manager)
    return ticket_title_tbox


def ticket_entry_tbox_func(manager):

    ticket_entry_tbox_rect = pygame.Rect(325, 45, 460, 235)
    ticket_entry_tbox = pygame_gui.elements.UITextBox(relative_rect=ticket_entry_tbox_rect, 
                                                       html_text="AWAITING TICKET...", manager=manager)
    return ticket_entry_tbox


def caller_popup_window_func(manager):
    
    caller_popup_window_rect = pygame.Rect(0, 0, 400, 200)
    caller_popup_window = pygame_gui.elements.UIWindow(rect=caller_popup_window_rect,
                                                 window_display_title="MEEPS SECURITY: New Caller",
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


def shift_report_tbox_func(manager, score, ticket_count, missed_calls, missed_tickets, assessment_result):
    
    shift_report_tbox_rect = pygame.Rect(0, 0, 300, 230)
    shift_report_tbox = pygame_gui.elements.UITextBox(relative_rect=shift_report_tbox_rect,
                                                           html_text=f"Employee No: #1361\nTitle: L1 SOC Analyst\nTotal Tickets: {ticket_count}\nAccurate Ticket Resolution: {score}\nMissed Calls: {missed_calls}\nMissed Tickets: {missed_tickets}\n\n<b>ASSESSMENT RESULT:<b> {assessment_result}", 
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


def main_title_image_func(manager, image_path):

    main_title_image_rect = pygame.Rect(165, 80, 500, 190)
    main_title_image_load = pygame.image.load(image_path)
    main_title_image = pygame_gui.elements.UIImage(relative_rect=main_title_image_rect,
                                                       image_surface=main_title_image_load,
                                                       manager=manager)
    return main_title_image


def main_title_slogan_label_func(manager):

    main_title_slogal_label_rect = pygame.Rect(150, 180, 500, 190)
    main_title_slogal_label = pygame_gui.elements.UILabel(relative_rect=main_title_slogal_label_rect, 
                                                          text="Guarding the Cyberspace", 
                                                          manager=manager)
    return main_title_slogal_label


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


def version_label_func(manager, version):

    version_label_rect = pygame.Rect(0, 0, 200, 150)
    version_label_rect.bottomleft = (-35, 60)
    version_label = pygame_gui.elements.UILabel(relative_rect=version_label_rect,
                                                text=version, manager=manager,
                                                anchors={'left':'left', 'bottom':'bottom'})
    return version_label


def github_label_func(manager):

    github_label_rect = pygame.Rect(0, 0, 200, 200)
    github_label_rect.bottomright = (0, 85)
    github_label = pygame_gui.elements.UILabel(relative_rect=github_label_rect,
                                               text="GitHub @unclesocks", 
                                               manager=manager,
                                               anchors={'right':'right', 'bottom':'bottom'})
    return github_label