import random


class AI:
    def __init__(self, size=6):
        self.size = size
        self.tried = set()
        self.last_hit = None

    def choose(self):
        options = [(r, c) for r in range(self.size) for c in range(self.size)
                   if (r, c) not in self.tried]
        if not options:
            return None

        if self.last_hit is not None:
            row, col = self.last_hit
            nearby = [(row - 1, col), (row + 1, col),
                      (row, col - 1), (row, col + 1)]
            nearby = [pos for pos in nearby
                      if 0 <= pos[0] < self.size and 0 <= pos[1] < self.size
                      and pos not in self.tried]
            if nearby:
                options = nearby

        pos = random.choice(options)
        return pos

    def record_result(self, pos, result):
        if result not in ("HIT", "MISS", "SUNK"):
            return
        self.tried.add(pos)
        if result == "HIT":
            self.last_hit = pos
        elif result == "SUNK":
            self.last_hit = None
