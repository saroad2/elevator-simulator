import pygame

from elevator_simulator.gui.constants import (
    ELEVATOR_WIDTH,
    ELEVATOR_HEIGHT,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    LEVEL_HEIGHT,
)


def draw_elevator(elevator, screen):
    rect = pygame.Rect(0, 0, ELEVATOR_WIDTH, ELEVATOR_HEIGHT)
    rect.midbottom = (
        SCREEN_WIDTH // 2,
        SCREEN_HEIGHT - int(LEVEL_HEIGHT * elevator.current_location),
    )
    pygame.draw.rect(screen, "red", rect)
