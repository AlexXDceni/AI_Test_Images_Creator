import datetime
import os

import pygame
import pygame_gui

pygame.init()

SETUP_WIDTH, SETUP_HEIGHT = 400, 300
GRID_SIZE = 20
PADDING = 10
MENU_HEIGHT = 65

setup_surface = pygame.display.set_mode((SETUP_WIDTH, SETUP_HEIGHT))
pygame.display.set_caption("AI Tests Image Creator - Setup")
setup_manager = pygame_gui.UIManager((SETUP_WIDTH, SETUP_HEIGHT))
setup_font = pygame.font.Font(None, 32)
setup_clock = pygame.time.Clock()
setup_running = True

DARK_GRAY = (35, 35, 35)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

title_text = setup_font.render("AI Image Creator", True, BLACK)
title_rect = title_text.get_rect(center=(SETUP_WIDTH // 2, 50))

width_label = pygame.font.Font(None, 24).render("Width:", True, BLACK)
height_label = pygame.font.Font(None, 24).render("Height:", True, BLACK)

width_label_rect = width_label.get_rect(center=(100, 130))
height_label_rect = height_label.get_rect(center=(100, 170))

width_entry = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((SETUP_WIDTH // 2 - 50, 115), (100, 30)),
    manager=setup_manager,
    placeholder_text="28",
)
width_entry.set_text("28")

height_entry = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((SETUP_WIDTH // 2 - 50, 155), (100, 30)),
    manager=setup_manager,
    placeholder_text="28",
)
height_entry.set_text("28")

lock_ratio_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((SETUP_WIDTH // 2 + 60, 115), (50, 30)),
    text="1:1",
    manager=setup_manager,
)
lock_ratio = False
last_focused = "width"

start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((SETUP_WIDTH // 2 - 75, 210), (150, 50)),
    text="Start",
    manager=setup_manager,
)

while setup_running:
    time_delta = setup_clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        setup_manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == lock_ratio_button:
                lock_ratio = not lock_ratio
                if lock_ratio:
                    try:
                        size = int(width_entry.get_text())
                        height_entry.set_text(str(size))
                        last_focused = "width"
                    except ValueError:
                        pass
            elif event.ui_element == start_button:
                try:
                    PIXELS_WIDTH = max(1, int(width_entry.get_text()))
                    PIXELS_HEIGHT = max(1, int(height_entry.get_text()))
                except ValueError:
                    PIXELS_WIDTH = 28
                    PIXELS_HEIGHT = 28
                setup_running = False
                continue

        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            if lock_ratio:
                try:
                    if event.ui_element == width_entry:
                        val = int(width_entry.get_text())
                        height_entry.set_text(str(val))
                    elif event.ui_element == height_entry:
                        val = int(height_entry.get_text())
                        width_entry.set_text(str(val))
                except ValueError:
                    pass

    setup_manager.update(time_delta)

    setup_surface.fill((200, 200, 200))
    setup_surface.blit(title_text, title_rect)
    setup_surface.blit(width_label, width_label_rect)
    setup_surface.blit(height_label, height_label_rect)

    setup_manager.draw_ui(setup_surface)
    pygame.display.update()

pygame.display.set_caption("AI Tests Image Creator")

HEIGHT = max((PIXELS_HEIGHT * GRID_SIZE) + MENU_HEIGHT + PADDING, 400)
WIDTH = HEIGHT * 16 // 9
GRID_START_OX = (WIDTH - (PIXELS_WIDTH * GRID_SIZE)) // 2
GRID_END_OX = GRID_START_OX + (PIXELS_WIDTH * GRID_SIZE)
GRID_START_OY = MENU_HEIGHT + (HEIGHT - MENU_HEIGHT - (PIXELS_HEIGHT * GRID_SIZE)) // 2
GRID_END_OY = GRID_START_OY + (PIXELS_HEIGHT * GRID_SIZE)

window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
manager = pygame_gui.UIManager((WIDTH, HEIGHT))
FONT = pygame.font.Font(None, 24)

GRAY = (170, 170, 170)
LIGHT_GRAY = (245, 245, 245)

pixels = {}
current_color = BLACK
status_message = ""
status_timer = 0.0

save_directory = os.path.join(os.path.dirname(__file__), "saved_drawings")
save_dialog = None
save_text_entry = None
save_confirm_button = None
save_cancel_button = None

top_panel = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect((0, 0), (WIDTH, MENU_HEIGHT)),
    manager=manager,
    starting_height=0,
)

clear_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 10), (100, 40)),
    text="Clear",
    manager=manager,
    container=top_panel,
)

save_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((120, 10), (100, 40)),
    text="Save",
    manager=manager,
    container=top_panel,
)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == clear_button:
                pixels.clear()
            elif event.ui_element == save_confirm_button:
                if save_text_entry and save_dialog:
                    filename = save_text_entry.get_text()
                    if not filename.endswith(".png"):
                        filename += ".png"
                    if not os.path.exists(save_directory):
                        os.makedirs(save_directory)
                    filepath = os.path.join(save_directory, filename)
                    surface = pygame.Surface(
                        (PIXELS_WIDTH * GRID_SIZE, PIXELS_HEIGHT * GRID_SIZE)
                    )
                    surface.fill(WHITE)
                    for pos, color in pixels.items():
                        pygame.draw.rect(
                            surface,
                            color,
                            (
                                pos[0] * GRID_SIZE,
                                pos[1] * GRID_SIZE,
                                GRID_SIZE,
                                GRID_SIZE,
                            ),
                        )
                    pygame.image.save(surface, filepath)
                    status_message = f"Saved: {filename}"
                    status_timer = 2.0
                    save_dialog.kill()
                    save_dialog = None
                    save_text_entry = None
                    save_confirm_button = None
                    save_cancel_button = None
            elif event.ui_element == save_cancel_button:
                if save_dialog:
                    save_dialog.kill()
                    save_dialog = None
                    save_text_entry = None
                    save_confirm_button = None
                    save_cancel_button = None
            elif event.ui_element == save_button:
                dialog_width, dialog_height = 300, 120
                save_dialog = pygame_gui.elements.UIWindow(
                    rect=pygame.Rect(
                        (WIDTH - dialog_width) // 2,
                        (HEIGHT - dialog_height) // 2,
                        dialog_width,
                        dialog_height,
                    ),
                    manager=manager,
                    window_display_title="Save Drawing",
                )
                save_text_entry = pygame_gui.elements.UITextEntryLine(
                    relative_rect=pygame.Rect(10, 10, 280, 30),
                    manager=manager,
                    container=save_dialog,
                    placeholder_text="Enter filename",
                )
                save_text_entry.set_text("drawing")
                save_confirm_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(10, 50, 90, 35),
                    text="Save",
                    manager=manager,
                    container=save_dialog,
                )
                save_cancel_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(200, 50, 90, 35),
                    text="Cancel",
                    manager=manager,
                    container=save_dialog,
                )

    if pygame.mouse.get_pressed()[0]:
        if (
            GRID_START_OX <= mouse_pos[0] <= GRID_END_OX
            and GRID_START_OY <= mouse_pos[1] <= GRID_END_OY
        ):
            grid_x = (mouse_pos[0] - GRID_START_OX) // GRID_SIZE
            grid_y = (mouse_pos[1] - GRID_START_OY) // GRID_SIZE
            if 0 <= grid_x < PIXELS_WIDTH and 0 <= grid_y < PIXELS_HEIGHT:
                pixels[(grid_x, grid_y)] = current_color

    if pygame.mouse.get_pressed()[2]:
        if (
            GRID_START_OX <= mouse_pos[0] <= GRID_END_OX
            and GRID_START_OY <= mouse_pos[1] <= GRID_END_OY
        ):
            grid_x = (mouse_pos[0] - GRID_START_OX) // GRID_SIZE
            grid_y = (mouse_pos[1] - GRID_START_OY) // GRID_SIZE
            if 0 <= grid_x < PIXELS_WIDTH and 0 <= grid_y < PIXELS_HEIGHT:
                pixels[(grid_x, grid_y)] = WHITE

    if status_timer > 0:
        status_timer -= time_delta
        if status_timer <= 0:
            status_message = ""

    manager.update(time_delta)

    window_surface.fill(LIGHT_GRAY)

    pygame.draw.rect(window_surface, DARK_GRAY, (0, 0, WIDTH, MENU_HEIGHT))

    pygame.draw.rect(
        window_surface,
        WHITE,
        (
            GRID_START_OX,
            GRID_START_OY,
            PIXELS_WIDTH * GRID_SIZE,
            PIXELS_HEIGHT * GRID_SIZE,
        ),
    )

    for pos, color in pixels.items():
        pygame.draw.rect(
            window_surface,
            color,
            (
                pos[0] * GRID_SIZE + GRID_START_OX,
                pos[1] * GRID_SIZE + GRID_START_OY,
                GRID_SIZE,
                GRID_SIZE,
            ),
        )

    for x in range(0, PIXELS_WIDTH + 1):
        pygame.draw.line(
            window_surface,
            GRAY,
            (x * GRID_SIZE + GRID_START_OX, GRID_START_OY),
            (x * GRID_SIZE + GRID_START_OX, GRID_END_OY),
            1,
        )

    for y in range(0, PIXELS_HEIGHT + 1):
        pygame.draw.line(
            window_surface,
            GRAY,
            (GRID_START_OX, y * GRID_SIZE + GRID_START_OY),
            (GRID_END_OX, y * GRID_SIZE + GRID_START_OY),
            1,
        )

    pygame.draw.rect(
        window_surface,
        BLACK,
        (
            GRID_START_OX,
            GRID_START_OY,
            PIXELS_WIDTH * GRID_SIZE,
            PIXELS_HEIGHT * GRID_SIZE,
        ),
        2,
    )

    manager.draw_ui(window_surface)

    if status_message:
        text_surface = FONT.render(status_message, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, MENU_HEIGHT - 10))
        bg_rect = text_rect.inflate(20, 10)
        pygame.draw.rect(window_surface, DARK_GRAY, bg_rect, border_radius=5)
        window_surface.blit(text_surface, text_rect)

    pygame.display.update()

pygame.quit()
