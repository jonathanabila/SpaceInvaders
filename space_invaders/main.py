from typing import List


class Position:
    x: int
    y: int


class CollisionObserver:
    observers: list

    def register(self, observer):
        ...

    def notify(self, player):
        for observer in self.observers:
            observer.check_colision(player)


class Score:
    _score: int


class Bullet:
    position: Position


class CollisionChecker:
    def check_collision(self, player):
        ...


class Invader:
    position: Position


class Invaders(CollisionChecker):
    _invaders: List[Invader]


class Asteroid:
    position: Position


class Asteroids(CollisionChecker):
    _asteroids: List[Asteroid]


class SpaceShip:
    position: Position
    bullets: List[Bullet]

    def move_right(self):
        ...

    def move_left(self):
        ...

    def shoot(self):
        ...


class Game:
    width: int
    height: int
    position: Position
    score: Score
    invaders: Invaders
    asteroids: Asteroids
    space_ship: SpaceShip
    observer: CollisionObserver

    def __init__(self) -> None:
        self.invaders = Invaders()
        self.asteroids = Asteroids()

        self.space_ship = SpaceShip()
        self.score = Score()

        self.observer = CollisionObserver()
        self._register_observers()

    def _register_observers(self) -> None:
        self.observer.register(self.asteroids)
        self.observer.register(self.invaders)
        self.observer.register(self.score)

    def run(self) -> None:
        while True:
            command = self.get_command()  # type: ignore
            if command == "LEFT":
                self.space_ship.move_left()
            elif command == "RIGHT":
                self.space_ship.move_right()
            elif command == "SHOOT":
                self.space_ship.shoot()
            else:
                break


if __name__ == "__main__":
    game = Game()
    game.run()
