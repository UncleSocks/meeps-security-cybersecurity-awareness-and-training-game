import pygame
import pygame_gui
import random
import sqlite3
from colors import color


def submit_button_func(manager):
    submit_button_layout_rect = pygame.Rect(0, 0, 300, 40)
    submit_button_layout_rect.bottomleft = (15, -10)
    submit_button = pygame_gui.elements.UIButton(relative_rect=submit_button_layout_rect,
                                                 text="SUBMIT", manager=manager,
                                                 anchors={'left':'left', 'bottom':'bottom'})
    return submit_button


def thrat_entry_title_func(manager):
    threat_entry_title_rect = pygame.Rect(15, 240, 300, 30)
    threat_entry_title_label = pygame_gui.elements.UITextBox(relative_rect=threat_entry_title_rect,
                                                             html_text="Threat Entries", manager=manager)
    return threat_entry_title_label


def threat_entry_selection_list_func(manager, threat_list):
    threat_entry_selection_rect = pygame.Rect(0, 0, 300, 280)
    threat_entry_selection_rect.bottomleft = (15, -50)
    threat_entry_selection_list = pygame_gui.elements.UISelectionList(item_list=threat_list, 
                                                                      relative_rect=threat_entry_selection_rect,
                                                                      manager=manager,
                                                                      anchors={'left':'left', 'bottom':'bottom'})
    return threat_entry_selection_list


con = sqlite3.connect('data.db', timeout=10)
cur = con.cursor
pygame.init()

pygame.display.set_caption('Meeps Ransomware: A SOC Training Game')
window_width, window_height = 800, 600
window_surface = pygame.display.set_mode((window_width, window_height))

background = pygame.Surface((window_width, window_height))
background.fill(pygame(color('black')))

manager = pygame_gui.UIManager((window_width, window_height), 'theme.json')