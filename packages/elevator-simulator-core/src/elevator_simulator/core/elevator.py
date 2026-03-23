class Elevator:
    def __init__(self):
        self.current_location = 0.0
        self.seconds_per_floor = 1.0
        self.max_floor = 3
        self.target_floor = None

    def set_target_floor(self, floor: int | None = None):
        if floor is None:
            self.target_floor = None
            return
        if floor > self.max_floor or floor < 0:
            raise ValueError(f"Floor must be between 0 and {self.max_floor}")
        self.target_floor = floor

    def update(self, elapsed_seconds: float):
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
