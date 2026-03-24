from math import fabs

from elevator_simulator.core.constants import EPSILON


class Elevator:
    def __init__(self):
        self.current_location = 0.0
        self.seconds_per_floor = 1.5
        self.seconds_to_open = 0.3
        self.seconds_to_close = 0.5
        self.max_floor = 3
        self.door_position = 1.0  # 1 means fully open; 0 means fully closed
        self.target_floor = None

    @property
    def need_to_move(self) -> bool:
        return (
            self.target_floor is not None
            and fabs(self.target_floor - self.current_location) > EPSILON
        )

    @property
    def door_is_open(self) -> bool:
        return fabs(self.door_position - 1) < EPSILON

    @property
    def door_is_closed(self) -> bool:
        return fabs(self.door_position) < EPSILON

    def set_target_floor(self, floor: int | None = None):
        if floor is None:
            self.target_floor = None
            return
        if floor > self.max_floor or floor < 0:
            raise ValueError(f"Floor must be between 0 and {self.max_floor}")
        self.target_floor = floor

    def update(self, elapsed_seconds: float):
        if self.need_to_move:
            if not self.door_is_closed:
                self.close_door(elapsed_seconds)
            else:
                self._update_location(elapsed_seconds)
        else:
            if not self.door_is_open:
                self.open_door(elapsed_seconds)

    def close_door(self, elapsed_seconds: float):
        new_door_position = self.door_position - (
            elapsed_seconds / self.seconds_to_close
        )
        self.door_position = max(new_door_position, 0.0)

    def open_door(self, elapsed_seconds: float):
        new_door_position = self.door_position + (
            elapsed_seconds / self.seconds_to_open
        )
        self.door_position = min(new_door_position, 1.0)

    def _update_location(self, elapsed_seconds: float):
        direction = self._get_direction()
        if direction != 0:
            next_location = (
                self.current_location
                + direction * elapsed_seconds * self.seconds_per_floor
            )
            self._set_current_location(next_location)

    def _get_direction(self) -> int:
        if self.target_floor is None:
            return 0
        return 1 if self.current_location < self.target_floor else -1

    def _set_current_location(self, next_location: float):
        if self.current_location < self.target_floor <= next_location:
            self.current_location = self.target_floor
            self.set_target_floor(None)
            return
        if self.current_location > self.target_floor >= next_location:
            self.current_location = self.target_floor
            self.set_target_floor(None)
            return
        self.current_location = next_location
