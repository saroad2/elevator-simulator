import pygame

from elevator_simulator.core.elevator import Elevator
from elevator_simulator.gui.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from elevator_simulator.gui.draw_methods import draw_elevator

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

elevator = Elevator()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                key = event.key
                if pygame.K_0 <= key <= pygame.K_9:
                    target_floor = key - pygame.K_0
                    try:
                        elevator.set_target_floor(target_floor)
                    except ValueError:
                        pass

        elevator.update()

        screen.fill("white")
        draw_elevator(elevator=elevator, screen=screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
