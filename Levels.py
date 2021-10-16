from Ship import Rock, Satelite
import Image_Loader as IL

# class Rock(Enemy):
#     def __init__(self, x, y, vx, vy, icon, rot)
# class Satelite(Enemy):
#     def __init__(self, x, y, vx, vy, icon, rot)

lev_list = [
    [
        Rock(500, 300, 10, 100, IL.ROCK, 0)
    ],
    [
        Rock(700, 100, 10, 100, IL.ROCK, 0),
        Rock(700, 600, -50, 10, IL.ROCK, 0),
        Rock(100, 600, 10, -100, IL.ROCK, 0)
    ],
    [
        Satelite(400, 200, 200, 0, IL.SAT, 0)
    ],
    [
        Rock(500, 100, 50, 100, IL.ROCK, 0),
        Rock(500, 600, -50, 50, IL.ROCK, 0),
        Rock(100, 600, 10, -100, IL.ROCK, 0),
        Satelite(400, 200, 150, 0, IL.SAT, 0)
    ],
    [
        Rock(500, 100, 10, 100, IL.ROCK, 0),
        Rock(500, 600, -50, 10, IL.ROCK, 0),
        Satelite(400, 200, 150, 0, IL.SAT, 0),
        Satelite(500, 500, -50, 100, IL.SAT, 0),
        Satelite(300, 200, 50, -100, IL.SAT, 0)
    ]
]
