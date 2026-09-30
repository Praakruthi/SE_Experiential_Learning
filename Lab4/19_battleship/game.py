from board import Board
from ai import AI


class Battleship:
    def __init__(self):
        self.player = Board()
        self.enemy = Board()
        self.ai = AI()
        self._setup()

    def _setup(self):
        self.player.place_ship({(0, 0), (0, 1), (0, 2)})
        self.player.place_ship({(3, 0), (4, 0)})
        self.enemy.place_ship({(1, 1), (1, 2), (1, 3)})
        self.enemy.place_ship({(4, 4), (4, 5)})

    def show(self):
        print("\nYour shots are coordinates like 2,3.")
        remaining = sum(len(ship.cells - ship.hits) for ship in self.enemy.ships)
        print("Ship cells remaining:", remaining)

    @staticmethod
    def _show_shot_result(shooter, result):
        if result in ("HIT", "MISS", "SUNK"):
            print(f"{shooter}: {result}!")

    def run(self):
        print("Battleship")
        while True:
            self.show()
            raw = input("> ").strip().lower()
            if raw == "q":
                return
            try:
                r, c = map(int, raw.split(","))
                pos = (r - 1, c - 1)
            except ValueError:
                print("Use row,col.")
                continue
            if not (0 <= pos[0] < Board.SIZE and 0 <= pos[1] < Board.SIZE):
                print("Outside board.")
                continue
            result = self.enemy.fire(pos)
            if result == "REPEAT":
                print("Already fired there.")
                continue
            self._show_shot_result("You", result)
            if self.enemy.all_sunk():
                print("You sank the fleet.")
                return

            ai_pos = self.ai.choose()
            if ai_pos is None:
                print("AI has no valid shots remaining.")
                continue
            print("AI fired at", f"{ai_pos[0] + 1},{ai_pos[1] + 1}")
            ai_result = self.player.fire(ai_pos)
            self.ai.record_result(ai_pos, ai_result)
            self._show_shot_result("AI", ai_result)
