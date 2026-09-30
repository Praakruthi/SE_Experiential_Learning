class Ship:
    def __init__(self, cells):
        self.cells = set(cells)
        self.hits = set()

    @property
    def sunk(self):
        return self.cells <= self.hits


class Board:
    SIZE = 6

    def __init__(self):
        self.ships = []
        self.shots = set()

    def place_ship(self, cells):
        self.ships.append(Ship(cells))

    def fire(self, pos):
        if pos in self.shots:
            return "REPEAT"
        self.shots.add(pos)
        for ship in self.ships:
            if pos in ship.cells:
                ship.hits.add(pos)
                return "SUNK" if ship.sunk else "HIT"
        return "MISS"

    def all_sunk(self):
        return bool(self.ships) and all(ship.sunk for ship in self.ships)
