from Ship import Rock, Satelite, HeavySat, EnemyShip
import Image_Loader as IL

# class Rock(Enemy):
#     def __init__(self, x, y, vx, vy, icon, rot)
# class Satelite(Enemy):
#     def __init__(self, x, y, vx, vy, icon, rot)

lev_list = [
    #1
    [
        Rock(500, 300, 10, 100,  0)
    ],
    #2
    [
        Rock(700, 100, 10, 100,  0),
        Rock(700, 600, -50, 10,  0),
        Rock(100, 600, 10, -100,  0)
    ],
    #3
    [
        Satelite(400, 200, 200, 0, 0)
    ],
    #4
    [
        Rock(500, 100, 50, 100, 0),
        Rock(500, 600, -50, 50,  0),
        Rock(100, 600, 10, -100, 0),
        Satelite(400, 200, 150, 0,  0)
    ],
    #5
    [
        Rock(500, 100, 10, 100,  0),
        Rock(500, 600, -50, 10,  0),
        Satelite(400, 200, 150, 0,  0),
        Satelite(500, 500, -50, 100,  0),
        Satelite(300, 200, 50, -100, 0)
    ],
    #6
    [
        HeavySat(400, 200, 200, 0, 0)
    ],
    #7
    [
        HeavySat(400, 200, 200, 0, 0),
        Rock(700, 100, 10, 100,  0),
        Rock(700, 600, -50, 10,  0),
        Rock(100, 600, 10, -100,  0)
    ],
    #8
    [
        HeavySat(400, 200, 200, 0, 0),
        Satelite(500, 500, -50, 100,  0),
        Satelite(300, 200, 50, -100, 0)
    ],
    #9
    [
        HeavySat(400, 200, 200, 0, 0),
        Satelite(500, 500, -50, 100,  0),
        Satelite(300, 200, 50, -100, 0),
        Rock(500, 100, 50, 100, 0),
        Rock(500, 600, -50, 50,  0),
        Rock(100, 600, 10, -100, 0),
    ],
    #10
    [
        Rock(700, 100, 10, 100,  0),
        Rock(700, 600, -50, 10,  0),
        Rock(100, 600, 10, -100,  0),
        Rock(700, 200, 10, 100,  0),
        Rock(700, 500, -50, 10,  0),
        Rock(100, 500, 10, -100,  0),
        Rock(600, 100, 10, 100,  0),
        Rock(600, 600, -50, 10,  0),
        Rock(150, 600, 10, -100,  0),
        Rock(400, 550, -200, 0, 0),
        Rock(400, 525, -200, 0, 0),
    ],
    #11
    [
        EnemyShip(550, 400, 0, 200, 180)
    ],
    #12
    [
        EnemyShip(600, 400, 0, 200, 180),
        EnemyShip(400, 200, 200, 0, 270),
        EnemyShip(400, 600, -200, 0, 90)
    ],
    #13
    [
        HeavySat(600, 400, 0, 200, 0),
        EnemyShip(400, 200, 200, 0, 270),
        HeavySat(400, 600, -200, 0, 0)
    ]
]
