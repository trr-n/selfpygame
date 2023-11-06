class Animation:
    def __init__(self, total_count: int, seconds: float) -> None:
        self.total_count = total_count
        self.seconds = seconds

    def now_count(self) -> int:
        return self.seconds % self.total_count
