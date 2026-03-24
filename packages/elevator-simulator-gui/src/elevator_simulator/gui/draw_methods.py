import pygame

from elevator_simulator.gui.constants import (
    ELEVATOR_WIDTH,
    ELEVATOR_HEIGHT,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    LEVEL_HEIGHT,
    LINE_WIDTH,
    ELEVATOR_DOOR_PADDING,
)


class ElevatorSimulatorDrawer:
    def __init__(self):
        self.floor_font = pygame.font.SysFont("Arial", 30)
        self.half_elevator_width = ELEVATOR_WIDTH // 2

    def draw_levels(self, max_level: int, screen):
        for i in range(0, max_level + 1):
            pygame.draw.line(
                screen,
                "black",
                (0, SCREEN_HEIGHT - (i + 1) * LEVEL_HEIGHT),
                (SCREEN_WIDTH, SCREEN_HEIGHT - (i + 1) * LEVEL_HEIGHT),
                LINE_WIDTH,
            )
            text_surface = self.floor_font.render(f"Level {i}", True, "black")
            screen.blit(text_surface, (0, SCREEN_HEIGHT - (i + 1) * LEVEL_HEIGHT))

    def draw_elevator(self, elevator, screen):
        full_door_rect = pygame.Rect(0, 0, ELEVATOR_WIDTH, ELEVATOR_HEIGHT)
        full_door_rect.midbottom = (
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - int(LEVEL_HEIGHT * elevator.current_location),
        )
        self.draw_rect(rect=full_door_rect, fill_color="red", screen=screen)

        door_width = self.half_elevator_width - int(
            elevator.door_position * (self.half_elevator_width - ELEVATOR_DOOR_PADDING)
        )

        left_door_rect = pygame.Rect(0, 0, door_width, ELEVATOR_HEIGHT)
        left_door_rect.bottomleft = full_door_rect.bottomleft
        self.draw_rect(rect=left_door_rect, fill_color="gray", screen=screen)

        right_door_rect = pygame.Rect(0, 0, door_width, ELEVATOR_HEIGHT)
        right_door_rect.bottomright = full_door_rect.bottomright
        self.draw_rect(rect=right_door_rect, fill_color="gray", screen=screen)

    @classmethod
    def draw_rect(cls, *, rect, fill_color, screen):
        pygame.draw.rect(screen, fill_color, rect)
        pygame.draw.rect(screen, "black", rect, LINE_WIDTH)
