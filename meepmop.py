import pygame
import pygame_gui
import random
import sqlite3


def title_label_func(manager):
    title_rect = pygame.Rect(10, 5, 150, 100)
    title = pygame_gui.elements.UILabel(relative_rect=title_rect, text="MEEPS SECURITY", manager=manager)
    return title


def sla_main_func(manager, countdown_duration):
    sla_main_label_rect = pygame.Rect(210, 95, 100, 60)
    sla_main_label = pygame_gui.elements.UILabel(relative_rect=sla_main_label_rect, 
                                                        text="SLA: ".format(countdown_duration), 
                                                        manager=manager)
    return sla_main_label    


def submit_button_func(manager):
    submit_button_layout_rect = pygame.Rect(0, 0, 300, 40)
    submit_button_layout_rect.bottomleft = (15, -10)
    submit_button = pygame_gui.elements.UIButton(relative_rect=submit_button_layout_rect,
                                                 text="SUBMIT", manager=manager,
                                                 anchors={'left':'left', 'bottom':'bottom'})
    return submit_button


def threat_entry_title_func(manager):
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


def threat_desc_label_func(manager):
    threat_desc_rect = pygame.Rect(0, 0, 460, 350)
    threat_desc_rect.bottomright = (-15, -10)
    threat_desc_label = pygame_gui.elements.UITextBox(relative_rect=threat_desc_rect,
                                                      html_text="Select a threat", manager=manager,
                                                      anchors={'right':'right', 'bottom':'bottom'})
    return threat_desc_label


def scenario_label_func(manager, entry):
    scenario_rect = pygame.Rect(325, 15, 460, 220)
    scenario_label = pygame_gui.elements.UITextBox(relative_rect=scenario_rect, 
                                                   html_text=entry, manager=manager)
    return scenario_label


def profile_label_func(manager, caller_profile):
    profile_rect = pygame.Rect(120, 135, 195, 100)
    profile_label = pygame_gui.elements.UITextBox(relative_rect=profile_rect, 
                                                    html_text=caller_profile, manager=manager)
    return profile_label


def picture_func(manager, picture_path):
    picture_rect = pygame.Rect(18, 135, 98, 98)
    caller_picture = pygame.image.load(picture_path)
    picture = pygame_gui.elements.UIImage(relative_rect=picture_rect, image_surface=caller_picture, manager=manager)
    return picture


def pop_up_window_func(manager, countdown_duration):
    pop_up_window_rect = pygame.Rect(0, 0, 400, 200)
    pop_up_window = pygame_gui.elements.UIWindow(rect=pop_up_window_rect,
                                                 window_display_title="New Caller",
                                                 manager=manager)
    pop_up_window_content_rect = pygame.Rect(15, -60, 300, 200)
    pop_up_window_content = pygame_gui.elements.UILabel(relative_rect=pop_up_window_content_rect, 
                                                        text="INCOMING CALLER...", 
                                                        manager=manager,
                                                        container=pop_up_window)

    pop_up_window_countdown_rect = pygame.Rect(0, 0, 100, 60)
    pop_up_window_countdown_rect.bottomright = (-30, -5)
    pop_up_window_countdown = pygame_gui.elements.UILabel(relative_rect=pop_up_window_countdown_rect, 
                                                        text="SLA: {:.1f}".format(countdown_duration), 
                                                        manager=manager,
                                                        container=pop_up_window,
                                                        anchors={'right':'right', 'bottom':'bottom'})
    
    answer_button_layout_rect = pygame.Rect(0, 0, 200, 40)
    answer_button_layout_rect.bottomleft = (15, -10)
    answer_button = pygame_gui.elements.UIButton(relative_rect=answer_button_layout_rect,
                                                 text="ANSWER", manager=manager,
                                                 container=pop_up_window,
                                                 anchors={'left':'left', 'bottom':'bottom'})
    return pop_up_window, answer_button, pop_up_window_countdown

def all_scenario_ids():
    cursor.execute('SELECT id FROM tickets')
    all_ids = [row[0] for row in  cursor.fetchall()]
    
    return all_ids

connect = sqlite3.connect('data.db', timeout=10)
cursor = connect.cursor()
pygame.init()

pygame.display.set_caption('MEEPS SECURITY: A SOC Training Game')
window_width, window_height = 800, 600
window_surface = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()

background = pygame.Surface((window_width, window_height))
background.fill(pygame.Color(0,0,0))

manager = pygame_gui.UIManager((window_width,window_height), 'theme.json')

cursor.execute('SELECT name FROM threats')
threat_list_results = cursor.fetchall()
threat_list = [threat_list_result[0] for threat_list_result in threat_list_results]

submit_button = submit_button_func(manager)
threat_entry_title = threat_entry_title_func(manager)
threat_entry_selection_list = threat_entry_selection_list_func(manager, threat_list)
threat_desc_label = threat_desc_label_func(manager)
scenario_label = scenario_label_func(manager, "Awaiting tickets")
title = title_label_func(manager)
profile_label = profile_label_func(manager,"No current caller")

remaining_ids = all_scenario_ids()
scenario_timer = 0
time_to_show_scenario = random.uniform(2, 12)
has_scenario = False
#current_scenario = scenarios[0]
total_score = 0


running = True

pop_up_window = None
popup_button_clicked = False
pop_up_close_timer = 0
sla_timer = 0
sla_countdown_duration = 10
countdown_duration = 15

while running:
    time_delta = clock.tick(60) / 1000.0
    scenario_timer += time_delta

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
            if event.ui_element == threat_entry_selection_list:
                selected_threat = event.text
                print(selected_threat)
                cursor.execute('SELECT description, impact, mitigation FROM threats WHERE name=?', [selected_threat])
                selected_threat_desc, impact, mitigation = cursor.fetchone()
                threat_desc_label.set_text(f'<b>{selected_threat.upper()}</b>\n<b>Description</b>:\n{selected_threat_desc}\n<b>Impact:\n</b>{impact}\n<b>Mitigation:</b>\n{mitigation}')

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == submit_button and has_scenario == True:
                scenario_label.kill()
                picture.kill()
                profile_label.kill()
                has_scenario = False
                scenario_timer = 0

                if selected_threat == answer:
                    print("Correct!")
                    total_score += 1
                else:
                    print("Wrong")
                has_scenario = False

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    

    if scenario_timer >= time_to_show_scenario and not has_scenario and pop_up_window is None:
        pop_up_window, accept_button, pop_up_window_countdown = pop_up_window_func(manager, countdown_duration)
        pop_up_close_timer = 0

    if not remaining_ids and not has_scenario:
        print("Game Over")
        running = False
    else:
        if pop_up_window:
            pop_up_window.show()  
            manager.draw_ui(window_surface)
            countdown_time_left = countdown_duration - pop_up_close_timer
            pop_up_window_countdown.set_text("SLA: {:.1f}".format(max(0, countdown_time_left)))
            pop_up_close_timer += time_delta

            if countdown_time_left <= 0:
                pop_up_window.hide()
                pop_up_window = None
                selected_id = random.choice(remaining_ids)
                remaining_ids.remove(selected_id)
                scenario_timer = 0

            for event in pygame.event.get():
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == accept_button:

                        sla_timer = 0
                        
                        selected_id = random.choice(remaining_ids)
                        cursor.execute('SELECT entry, answer, caller, picture_path FROM tickets WHERE id=?', [selected_id])
                        current_scenario, answer, caller, path = cursor.fetchone()
                        selected_threat = None

                        scenario_label = scenario_label_func(manager, current_scenario)
                        picture = picture_func(manager, path)
                        profile_label = profile_label_func(manager, caller)
                        has_scenario = True
                        remaining_ids.remove(selected_id)

                        pop_up_window.hide()
                        pop_up_window = None

                manager.process_events(event)

        else:
            manager.draw_ui(window_surface)

        if has_scenario and pop_up_window is None:
            sla_main_label = sla_main_func(manager, sla_countdown_duration)
            sla_countdown_time_left = sla_countdown_duration - sla_timer
            sla_main_label.set_text("SLA: {:.1f}".format(max(0, sla_countdown_duration)))
            sla_timer += time_delta

            if sla_countdown_time_left <= 0:
                    scenario_label.kill()
                    picture.kill()
                    profile_label.kill()
                    has_scenario = False
                    scenario_timer = 0

    manager.draw_ui(window_surface)
    pygame.display.update()

connect.close()
print(total_score)