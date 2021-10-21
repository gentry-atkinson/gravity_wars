from Ship import Rock, Satelite, HeavySat, EnemyShip

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
        Satelite(400, 200, 180, 0, 0)
    ],
    4
    [
        Rock(500, 100, 50, 100, 0),
        Rock(500, 600, -50, 50,  0),
        Rock(100, 600, 10, -100, 0),
        Satelite(400, 200, 150, 0,  0)
    ],
    5
    [
        Rock(500, 100, 100, 100,  0),
        Rock(500, 600, -50, 10,  0),
        Satelite(500, 200, 150, 0,  0),
        Satelite(500, 500, -50, 100,  0),
        Satelite(300, 400, 50, -100, 0)
    ],
    6
    [
        HeavySat(400, 200, 180, 0, 0)
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
        Satelite(300, 500, 40, -100, 0)
    ],
    #9
    [
        HeavySat(400, 200, 200, 0, 0),
        Satelite(500, 500, -50, 100,  0),
        Satelite(300, 500, 40, -150, 0),
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
    13
    [
        HeavySat(600, 400, 0, 200, 0),
        EnemyShip(400, 200, 200, 0, 270),
        HeavySat(400, 600, -200, 0, 0)
    ],
    #14
    [
        Rock(400, 150, 0, 100,  0),
        Rock(400, 180, 0, 100,  0),
        Rock(420, 170, 0, 100,  0),
        Rock(700, 400, 100, 0,  0),
        Rock(670, 400, 100, 0,  0),
        Rock(680, 415, 100, 0,  0),
        Rock(400, 700, 0, -100,  0),
        Rock(400, 730, 0, -100,  0),
        Rock(420, 720, 0, -100,  0),
        Rock(100, 400, -100, 0,  0),
        Rock(70, 400, -100, 0,  0),
        Rock(80, 415, -100, 0,  0),
    ],
    #15
    [
        EnemyShip(100, 100, 100, 0, 180),
        EnemyShip(700, 100, 0, 100, 270),
        EnemyShip(700, 700, -100, 0, 90),
        EnemyShip(100, 700, 0, -100, 90),
        Rock(500, 100, 50, 100, 0),
        Rock(500, 600, -50, 50,  0),
        Rock(100, 600, 10, -100, 0)
    ],
    #16
    [
        EnemyShip(100, 100, 100, 0, 180),
        EnemyShip(700, 100, 0, 100, 270),
        HeavySat(500, 400, 0, 300, 0),
        HeavySat(500, 300, 0, -300, 0),
        Satelite(400, 600, -180, 0, 0),
        Satelite(400, 580, -190, 0, 0),
        Satelite(400, 560, -200, 0, 0),
    ],
    #17
    [
        EnemyShip(100, 700, 00, 100, 0),
        EnemyShip(700, 700, 0, 100, 0),
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
        Rock(400, 525, -200, 0, 0)
    ],
    #18
    [
        EnemyShip(100, 700, 00, 100, 0),
        EnemyShip(700, 700, 0, 100, 0),
        Satelite(700, 100, 10, 100,  0),
        Satelite(700, 600, -50, 10,  0),
        Satelite(100, 600, 10, -100,  0),
        Satelite(700, 200, 10, 100,  0),
        Rock(700, 500, -50, 10,  0),
        Rock(100, 500, 10, -100,  0),
        Rock(600, 100, 10, 100,  0),
        Rock(600, 600, -50, 10,  0),
        Rock(150, 600, 10, -100,  0),
        Rock(400, 550, -200, 0, 0),
        Rock(400, 525, -200, 0, 0)
    ],
    #19
    [
        HeavySat(500, 400, 0, 300, 0),
        HeavySat(500, 300, 0, -300, 0),
        HeavySat(300, 400, 0, 300, 0),
        HeavySat(300, 300, 300, 0, 0),
        HeavySat(400, 500, -300, 0, 0),
        HeavySat(400, 550, 0, -300, 0),
        HeavySat(400, 300, 300, 0, 0),
        HeavySat(400, 350, -300, -0, 0)
    ],
    #20
    [
        HeavySat(500, 400, 0, 300, 0),
        Rock(500, 300, 0, -300, 0),
        HeavySat(300, 400, 0, 300, 0),
        Rock(300, 300, 300, 0, 0),
        HeavySat(400, 500, -300, 0, 0),
        Rock(400, 550, 0, -300, 0),
        HeavySat(400, 300, 300, 0, 0),
        Rock(400, 350, -300, -0, 0),
        EnemyShip(100, 700, 00, 100, 0),
        EnemyShip(700, 700, 0, 100, 0),
        EnemyShip(100, 100, 100, 0, 180),
        EnemyShip(700, 100, 0, 100, 270),
    ]
]
