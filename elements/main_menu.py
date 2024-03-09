import pygame
import pygame_gui




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
                                                 text="MANAGE TICKETS", manager=manager,
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