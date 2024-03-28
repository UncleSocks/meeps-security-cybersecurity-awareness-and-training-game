import pygame
import pygame_gui


def back_button_func(manager):
    
    back_button_rect = pygame.Rect(5, 5, 30, 30)
    back_button = pygame_gui.elements.UIButton(relative_rect=back_button_rect,
                                                 text="<", manager=manager)
    return back_button


def create_delete_button_func(manager):

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


def account_entry_slist_misc_func(manager):

    account_entry_title_tbox_rect = pygame.Rect(0, 0, 265, 30)
    account_entry_title_tbox_rect.bottomleft = (15, -470)
    account_entry_title_tbox = pygame_gui.elements.UITextBox(relative_rect=account_entry_title_tbox_rect, 
                                                             html_text="ACCOUNT LIST", manager=manager,
                                                             anchors={'left':'left', 'bottom':'bottom'})
    return account_entry_title_tbox


def account_entry_slist_func(manager, account_list):

    account_entry_slist_rect = pygame.Rect(0, 0, 350, 460)
    account_entry_slist_rect.bottomleft = (15, -10)
    account_entry_slist = pygame_gui.elements.UISelectionList(item_list=account_list,
                                                              relative_rect=account_entry_slist_rect,
                                                              manager=manager,
                                                              anchors={'left':'left', 'bottom':'bottom'})

    return account_entry_slist
