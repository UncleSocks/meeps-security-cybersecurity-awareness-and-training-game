import sqlite3
import pygame
import pygame_gui
from colors import color
import elements.main_loop_elements as main_loop_elements


def pygame_init():

    pygame.init()
    pygame.display.set_caption('MEEPS SECURITY Responder.exe')

    icon_path = "assets/images/general/icon.png"
    icon_load = pygame.image.load(icon_path)
    pygame.display.set_icon(icon_load)

    window_width, window_height = 800, 650
    window_surface = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    background = pygame.Surface((window_width, window_height))
    background.fill(pygame.Color(color('black')))

    return window_surface, clock, background


def pygame_gui_init():
    
    window_width, window_height = 800, 650
    manager = pygame_gui.UIManager((window_width, window_height), 'theme.json')

    return manager


def database_init(database):

    connect = sqlite3.connect(database, timeout=10)
    cursor = connect.cursor()

    return connect, cursor