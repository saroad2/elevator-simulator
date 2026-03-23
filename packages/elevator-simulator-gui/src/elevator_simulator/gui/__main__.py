import pygame

from elevator_simulator.core.elevator import Elevator
from elevator_simulator.gui.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from elevator_simulator.gui.draw_methods import ElevatorSimulatorDrawer

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

drawer = ElevatorSimulatorDrawer()

clock = pygame.time.Clock()

elevator = Elevator()


def main():
    while True:
        elapsed_seconds = 0.001 * clock.get_time()  # Milliseconds to seconds
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

        elevator.update(elapsed_seconds)

        screen.fill("white")
        drawer.draw_levels(max_level=elevator.max_floor, screen=screen)
        drawer.draw_elevator(elevator=elevator, screen=screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
