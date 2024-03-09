import pygame
import pygame_gui
import sqlite3
import init
import sqlite
import elements.threats_loop as threat_loops


def threat_database_management_func(database):

    connect = sqlite3.connect(database, timeout=10)
    cursor = connect.cursor()

    window_surface, clock, background = init.pygame_init()
    manager = init.pygame_gui_init()

    threat_list = sqlite.threats(cursor)

    back_button = threat_loops.back_button_func(manager)
    threat_database_image = threat_loops.threat_database_image_func(manager, "Assets/threat_database.png")

    create_button, delete_button = threat_loops.create_button_button_func(manager)
    threat_entry_title_tbox = threat_loops.threat_entry_slist_misc_func(manager)
    threat_entry_slist = threat_loops.threat_entry_slist_func(manager, threat_list)

    threat_details_label, selected_threat_title_tbox, selected_threat_description_tbox, selected_threat_indicators_tbox, selected_threat_countermeasures_tbox = threat_loops.threat_details_func(manager)

    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                    running = False

            if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == threat_entry_slist:
                    selected_threat = event.text

                    cursor.execute('SELECT description, indicators, countermeasures FROM threats WHERE name=?', [selected_threat])
                    description, indicators, countermeasures = cursor.fetchone()

                    selected_threat_title_tbox.set_text(f"<b>{selected_threat}</b>")
                    selected_threat_description_tbox.set_text(f"DESCRIPTION:\n{description}")
                    selected_threat_indicators_tbox.set_text(f"INDICATORS:\n{indicators}")
                    selected_threat_countermeasures_tbox.set_text(f"COUNTERMEASURES:\n{countermeasures}")

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()