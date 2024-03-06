import random
import pygame
import pygame_gui
from colors import color
import elements


def pygame_init():

    pygame.init()
    pygame.display.set_caption('MEEPS SECURITY: Cyberecurity Awareness and Training Game')

    window_width, window_height = 800, 600
    window_surface = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    background = pygame.Surface((window_width, window_height))
    background.fill(pygame.Color(color('black')))

    return window_surface, clock, background


def pygame_gui_init():
    
    window_width, window_height = 800, 600
    manager = pygame_gui.UIManager((window_width, window_height), 'theme.json')

    return manager


def meeps_background_init(manager, threat_list):
    
    title_label = elements.title_label_func(manager)
    main_sla_timer_label = elements.main_sla_timer_label_func(manager)
    caller_profile_tbox = elements.caller_profile_tbox_func(manager, "NO CURRENT CALLER")
    submit_button = elements.submit_button_func(manager)
    threat_entry_title_tbox = elements.threat_entry_title_tbox_func(manager)
    threat_entry_slist = elements.threat_entry_slist_func(manager, threat_list)
    threat_description_label = elements.threat_description_label_func(manager)
    ticket_entry_label = elements.ticket_entry_label_func(manager, "AWAITING TICKETS")

    return title_label, main_sla_timer_label, caller_profile_tbox, submit_button, threat_entry_title_tbox, threat_entry_slist, threat_description_label, ticket_entry_label


def meeps_timers_init():

    ticket_timer = 0
    randomized_ticket_entry = random.uniform(2, 12)
    popup_window_close_timer = 0
    popup_window_sla_countdown = 15
    
    main_sla_timer = 0
    main_sla_countdown = 120

    return ticket_timer, randomized_ticket_entry, popup_window_close_timer, popup_window_sla_countdown, main_sla_timer, main_sla_countdown


def meeps_loop_init():

    running = True
    ticket_presence = False
    caller_popup_window = None
    popup_button_accepted = False
    total_score = 0

    return running, ticket_presence, caller_popup_window, popup_button_accepted, total_score