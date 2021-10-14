from Ship import Rock, Satelite
import Image_Loader as IL

# class Rock(Enemy):
#     def __init__(self, x, y, vx, vy, icon, rot)
# class Satelite(Enemy):
#     def __init__(self, x, y, vx, vy, icon, rot)

lev_list = [
    [
        Rock(700, 100, 10, 100, IL.ROCK, 0)
    ],
    [
        Rock(700, 100, 10, 100, IL.ROCK, 0),
        Rock(700, 600, -50, 10, IL.ROCK, 0),
        Rock(100, 600, 10, -100, IL.ROCK, 0)
    ],
    [
        Satelite(400, 200, 100, 0, IL.SAT, 0)
    ]
]
