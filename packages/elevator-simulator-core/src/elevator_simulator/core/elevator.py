import time


class Elevator:
    def __init__(self):
        self.current_location = 0.0
        self.seconds_per_floor = 1.0
        self.max_floor = 3
        self.last_update_time = time.perf_counter()

    def update(self):
        now = time.perf_counter()
        elapsed_seconds = now - self.last_update_time
        self.current_location = min(
            self.current_location + elapsed_seconds * self.seconds_per_floor,
            self.max_floor,
        )
        self.last_update_time = now
