import pygame

from elevator_simulator.gui.constants import (
    ELEVATOR_WIDTH,
    ELEVATOR_HEIGHT,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    LEVEL_HEIGHT,
)


class ElevatorSimulatorDrawer:
    def __init__(self):
        self.floor_font = pygame.font.SysFont("Arial", 30)

    def draw_levels(self, max_level: int, screen):
        for i in range(0, max_level + 1):
            pygame.draw.line(
                screen,
                "black",
                (0, SCREEN_HEIGHT - (i + 1) * LEVEL_HEIGHT),
                (SCREEN_WIDTH, SCREEN_HEIGHT - (i + 1) * LEVEL_HEIGHT),
            )
            text_surface = self.floor_font.render(f"Level {i}", True, "black")
            screen.blit(text_surface, (0, SCREEN_HEIGHT - (i + 1) * LEVEL_HEIGHT))

    def draw_elevator(self, elevator, screen):
        rect = pygame.Rect(0, 0, ELEVATOR_WIDTH, ELEVATOR_HEIGHT)
        rect.midbottom = (
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - int(LEVEL_HEIGHT * elevator.current_location),
        )
        pygame.draw.rect(screen, "red", rect)
