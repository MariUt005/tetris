import pygame
import random

pygame.font.init()


def genItem():
    global items
    item_ids = {
        '0_0': 0, '0_180': 0, '0_90': 1, '0_270': 1,
        '1_0': 2, '1_90': 5, '1_180': 4, '1_270': 3,
        '2_0': 6, '2_90': 9, '2_180': 8, '2_270': 7,
        '3_0': 10, '3_90': 10, '3_180': 10, '3_270': 10,
        '4_0': 11, '4_180': 11, '4_90': 12, '4_270': 12,
        '5_0': 13, '5_90': 16, '5_180': 15, '5_270': 14,
        '6_0': 17, '6_180': 17, '6_90': 18, '6_270': 18
    }
    start_coord = {
        0: [130, -95], 1: [80, -20],
        2: [105, -45], 3: [105, -70], 4: [105, -45], 5: [105, -70],
        6: [105, -45], 7: [105, -70], 8: [105, -45], 9: [105, -70],
        10: [105, -45],
        11: [105, -45], 12: [105, -70], 13: [105, -45], 14: [105, -70],
        15: [105, -45], 16: [105, -70],
        17: [105, -45], 18: [105, -70]
    }

    item_index = random.randint(0, 6)
    item = items[item_index]
    item_rotation = random.choice([0, 90, 180, 270])
    item = pygame.transform.rotate(item, item_rotation)
    item_id = item_ids[str(item_index) + '_' + str(item_rotation)]

    return item, item_id, start_coord[item_id][0], start_coord[item_id][1]


def checkLeftSide():
    global field, x, y, item_id
    if x == 5:
        return False

    if item_id == 0 and not field[x - 25][y] and not field[x - 25][y + 25] and not field[x - 25][y + 50] and not field[x - 25][y + 75] \
            or item_id == 1 and not field[x - 25][y] \
            or item_id in [2, 6, 10] and not field[x - 25][y] and not field[x - 25][y + 25] \
            or item_id in [3, 9, 16] and not field[x - 25][y] and not field[x - 25][y + 25] and not field[x - 25][y + 50] \
            or item_id == 4 and not field[x - 25][y] and not field[x + 25][y + 25] \
            or item_id == 5 and not field[x][y] and not field[x][y + 25] and not field[x - 25][y + 50] \
            or item_id == 7 and not field[x - 25][y] and not field[x][y + 25] and not field[x][y + 50] \
            or item_id == 8 and not field[x + 25][y] and not field[x - 25][y + 25] \
            or item_id == 12 and not field[x - 25][y] and not field[x - 25][y + 25] and not field[x][y + 50] \
            or item_id in [11, 15] and not field[x][y] and not field[x - 25][y + 25] \
            or item_id in [13, 17] and not field[x - 25][y] and not field[x][y + 25] \
            or item_id == 14 and not field[x][y] and not field[x - 25][y + 25] and not field[x][y + 50] \
            or item_id == 18 and not field[x][y] and not field[x - 25][y + 25] and not field[x - 25][y + 50]:
        return True
    return False


def checkRightSide():
    global field, x, y, item_id
    if item_id == 0 and x == 230 \
            or item_id == 1 and x == 155 \
            or item_id in [2, 4, 6, 8, 11, 13, 15, 17] and x == 180 \
            or item_id in [3, 5, 7, 9, 10, 12, 14, 16, 18] and x == 205:
        return False

    if item_id == 0 and not field[x + 25][y] and not field[x + 25][y + 25] and not field[x + 25][y + 50] and not field[x + 25][y + 75] \
            or item_id == 1 and not field[x + 100][y] \
            or item_id == 2 and not field[x + 25][y] and not field[x + 75][y + 25] \
            or item_id == 3 and not field[x + 50][y] and not field[x + 25][y + 25] and not field[x + 25][y + 50] \
            or item_id in [4, 8] and not field[x + 75][y] and not field[x + 75][y + 25] \
            or item_id in [5, 7, 14] and not field[x + 50][y] and not field[x + 50][y + 25] and not field[x + 50][y + 50] \
            or item_id == 6 and not field[x + 75][y] and not field[x + 25][y + 25] \
            or item_id == 9 and not field[x + 25][y] and not field[x + 25][y + 25] and not field[x + 50][y + 50] \
            or item_id == 10 and not field[x + 50][y] and not field[x + 50][y + 25] \
            or item_id in [11, 13] and not field[x + 75][y] and not field[x + 50][y + 25] \
            or item_id == 12 and not field[x + 25][y] and not field[x + 50][y + 25] and not field[x + 50][y + 50] \
            or item_id in [15, 17] and not field[x + 50][y] and not field[x + 75][y + 25] \
            or item_id == 16 and not field[x + 25][y] and not field[x + 50][y + 25] and not field[x + 25][y + 50] \
            or item_id == 18 and not field[x + 50][y] and not field[x + 50][y + 25] and not field[x + 25][y + 50]:
        return True
    return False


def checkDownSide():
    global field, x, y, item_id
    if item_id == 0 and y + 100 < 505 and not field[x][y + 100] \
            or item_id == 1 and y + 25 < 505 and not field[x][y + 25] and not field[x + 25][y + 25] and not field[x + 50][y + 25] and not field[x + 75][y + 25] \
            or item_id in [2, 8, 15] and y + 50 < 505 and not field[x][y + 50] and not field[x + 25][y + 50] and not field[x + 50][y + 50] \
            or item_id == 3 and y + 75 < 505 and not field[x][y + 75] and not field[x + 25][y + 25] \
            or item_id == 4 and y + 50 < 505 and not field[x][y + 25] and not field[x + 25][y + 25] and not field[x + 50][y + 50] \
            or item_id in [5, 9] and y + 75 < 505 and not field[x][y + 75] and not field[x + 25][y + 75] \
            or item_id == 6 and y + 50 < 505 and not field[x][y + 50] and not field[x + 25][y + 25] and not field[x + 50][y + 25] \
            or item_id == 7 and y + 75 < 505 and not field[x][y + 25] and not field[x + 25][y + 75] \
            or item_id == 10 and y + 50 < 505 and not field[x][y + 50] and not field[x + 25][y + 50] \
            or item_id == 11 and y + 50 < 505 and not field[x][y + 50] and not field[x + 25][y + 50] and not field[x + 50][y + 25] \
            or item_id in [12, 14] and y + 75 < 505 and not field[x][y + 50] and not field[x + 25][y + 75] \
            or item_id == 13 and y + 50 < 505 and not field[x][y + 25] and not field[x + 25][y + 50] and not field[x + 50][y + 25] \
            or item_id in [16, 18] and y + 75 < 505 and not field[x][y + 75] and not field[x + 25][y + 50] \
            or item_id == 17 and y + 50 < 505 and not field[x][y + 25] and not field[x + 25][y + 50] and not field[x + 50][y + 50]:
        return True
    return False


def updateField(value):
    global item_id, field, x, y
    if item_id == 0:
        field[x][y] = field[x][y + 25] = field[x][y + 50] = field[x][y + 75] = value
    elif item_id == 1:
        field[x][y] = field[x + 25][y] = field[x + 50][y] = field[x + 75][y] = value
    elif item_id == 2:
        field[x][y] = field[x][y + 25] = field[x + 25][y + 25] = field[x + 50][y + 25] = value
    elif item_id == 3:
        field[x][y] = field[x + 25][y] = field[x][y + 25] = field[x][y + 50] = value
    elif item_id == 4:
        field[x][y] = field[x + 25][y] = field[x + 50][y] = field[x + 50][y + 25] = value
    elif item_id == 5:
        field[x + 25][y] = field[x + 25][y + 25] = field[x + 25][y + 50] = field[x][y + 50] = value
    elif item_id == 6:
        field[x][y] = field[x + 25][y] = field[x + 50][y] = field[x][y + 25] = value
    elif item_id == 7:
        field[x][y] = field[x + 25][y] = field[x + 25][y + 25] = field[x + 25][y + 50] = value
    elif item_id == 8:
        field[x + 50][y] = field[x][y + 25] = field[x + 25][y + 25] = field[x + 50][y + 25] = value
    elif item_id == 9:
        field[x][y] = field[x][y + 25] = field[x][y + 50] = field[x + 25][y + 50] = value
    elif item_id == 10:
        field[x][y] = field[x + 25][y] = field[x][y + 25] = field[x + 25][y + 25] = value
    elif item_id == 11:
        field[x + 25][y] = field[x + 50][y] = field[x][y + 25] = field[x + 25][y + 25] = value
    elif item_id == 12:
        field[x][y] = field[x][y + 25] = field[x + 25][y + 25] = field[x + 25][y + 50] = value
    elif item_id == 13:
        field[x][y] = field[x + 25][y] = field[x + 50][y] = field[x + 25][y + 25] = value
    elif item_id == 14:
        field[x + 25][y] = field[x][y + 25] = field[x + 25][y + 25] = field[x + 25][y + 50] = value
    elif item_id == 15:
        field[x + 25][y] = field[x][y + 25] = field[x + 25][y + 25] = field[x + 50][y + 25] = value
    elif item_id == 16:
        field[x][y] = field[x][y + 25] = field[x][y + 50] = field[x + 25][y + 25] = value
    elif item_id == 17:
        field[x][y] = field[x + 25][y] = field[x + 25][y + 25] = field[x + 50][y + 25] = value
    elif item_id == 18:
        field[x + 25][y] = field[x + 25][y + 25] = field[x][y + 25] = field[x][y + 50] = value


def isLoss():
    i = 5
    while i < 255:
        if field[i][-20]:
            return True
        i += 25
    return False


def checkRows():
    global field, score
    y = 5
    while y <= 480:
        x = 5
        count = 0
        while x <= 230:
            count += field[x][y]
            x += 25
        if count == 10:
            deleteRow(y)
            score += 10
        y += 25


def deleteRow(y):
    global field
    while y > 0:
        x = 5
        while x < 255:
            field[x][y] = field[x][y - 25]
            x += 25
        y -= 25


def addNewRow():
    global field
    y = -20
    while y < 505 - 25:
        x = 5
        while x < 255:
            field[x][y] = field[x][y+25]
            x += 25
        y += 25

    x = 5
    y = 480
    while x < 255:
        field[x][y] = random.choice([0, 1])
        x += 25


def rotation():
    global item, item_id, x, y

    def isRotationPossible(item_id, x, y):
        global field
        cells_to_check = [
            [field[x - 25][y + 50], field[x + 25][y + 50], field[x + 50][y + 50]],
            [field[x + 25][y - 50], field[x + 25][y - 25], field[x + 50][y + 25]],
            [field[x + 50][y], field[x + 50][y - 25]],
            [field[x + 25][y + 50], field[x + 50][y + 50]],
            [field[x][y + 25], field[x][y + 50]],
            [field[x][y], field[x - 25][y]],
            [field[x][y + 50], field[x + 25][y + 50]],
            [field[x - 25][y], field[x - 25][y + 25]],
            [field[x + 25][y], field[x + 50][y]],
            [field[x + 50][y + 25], field[x + 50][y + 50]],
            [None],
            [field[x][y], field[x + 25][y + 50]],
            [field[x + 25][y], field[x + 50][y]],
            [field[x + 25][y - 25]],
            [field[x + 50][y + 25]],
            [field[x + 25][y + 50]],
            [field[x - 25][y + 25]],
            [field[x + 50][y], field[x + 25][y + 50]],
            [field[x - 25][y], field[x][y]]
        ]
        for cell in cells_to_check[item_id]:
            if cell:
                return False
        return True

    copy_x, copy_y = x, y

    new_item_id = [1, 0, 5, 2, 3, 4, 9, 6, 7, 8, 10, 12, 11, 16, 13, 14, 15, 18, 17]
    coord_diff = [
        [-25, 50], [25, -50],
        [25, -25], [0, 25], [0, 0], [-25, 0],
        [0, 0], [-25, 0], [25, -25], [0, 25],
        [0, 0],
        [0, 0], [0, 0],
        [25, -25], [0, 25], [0, 0], [-25, 0],
        [25, 0], [-25, 0]
    ]
    min_possible_x = [30, 5, 5, 5, 5, 30, 5, 30, 5, 5, 5, 5, 5, 5, 5, 30, 30, 5, 30]
    max_possible_x = [180, 155, 180, 180, 180, 205, 180, 205, 180, 180, 205, 180, 180, 180, 180, 180, 205, 180, 205]
    max_possible_y = [405, 455, 455, 430, 430, 430, 430, 430, 455, 430, 455, 430, 430, 455, 430, 430, 430, 430, 430]

    if copy_y > max_possible_y[item_id]:
        return None
    elif copy_x < min_possible_x[item_id]:
        copy_x += 25
    elif copy_x - 25 == max_possible_x[item_id]:
        copy_x -= 25
    elif copy_x - 50 == max_possible_x[item_id]:
        copy_x -= 50

    if isRotationPossible(item_id, copy_x, copy_y):
        copy_x += coord_diff[item_id][0]
        copy_y += coord_diff[item_id][1]
        x, y = copy_x, copy_y
        item_id = new_item_id[item_id]
        item = pygame.transform.rotate(item, 90)


def fallDown():
    global item_id, field, x, y
    while True:
        if checkDownSide():
            y += 25
        else:
            break


def draw():
    global win, field, item, x, y, square, score, is_game_over, is_game_stop, is_win, next_item, level
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 360, 510))
    pygame.draw.rect(win, (50, 50, 50), (5, 5, 250, 500))
    pygame.draw.rect(win, (0, 0, 0), (5, 0, 250, 5))
    i = 5
    while i <= 230:
        j = 5
        while j <= 480:
            if field[i][j]:
                win.blit(square, (i, j))
            j += 25
        i += 25
    font = pygame.font.Font('font/362_LCDNOVA.ttf', 30)
    lover_font = pygame.font.Font('font/362_LCDNOVA.ttf', 15)
    result = font.render(str(score), True, (255, 255, 255))
    pygame.draw.rect(win, (50, 50, 50), (260, 5, 100, 30))
    win.blit(result, (262, 9))
    pygame.draw.rect(win, (50, 50, 50), (260, 40, 100, 30))
    lvl = font.render('lvl: ' + str(level), True, (255, 255, 255))
    win.blit(lvl, (262, 43))
    pygame.draw.rect(win, (50, 50, 50), (260, 75, 100, 100))
    win.blit(next_item, (260, 75))
    manual = [
        lover_font.render('->ESC', True, (255, 255, 255)),
        lover_font.render(' to pause', True, (180, 180, 180)),
        lover_font.render('->a, left', True, (255, 255, 255)),
        lover_font.render(' to move left', True, (180, 180, 180)),
        lover_font.render('->d, right', True, (255, 255, 255)),
        lover_font.render(' to move right', True, (180, 180, 180)),
        lover_font.render('->s, down', True, (255, 255, 255)),
        lover_font.render(' to move down', True, (180, 180, 180)),
        lover_font.render('->w, UP, SPACE', True, (255, 255, 255)),
        lover_font.render(' to rotate', True, (180, 180, 180)),
        lover_font.render('->ENTER', True, (255, 255, 255)),
        lover_font.render(' to fall down', True, (180, 180, 180)),
    ]
    i, j = 200, 0
    while i <= 400:
        win.blit(manual[j], (260, i))
        win.blit(manual[j + 1], (260, i + 15))
        i += 40
        j += 2

    if is_game_over:
        if score == 0:
            x = 120
        elif score < 100:
            x = 115
        elif score < 1000:
            x = 110
        elif score < 10000:
            x = 98
        else:
            x = 87
        game_over = font.render('Game over!', True, (255, 0, 0))
        your_score = font.render('Your score:', True, (180, 180, 180))
        result = font.render(str(score), True, (255, 255, 255))
        pygame.draw.rect(win, (25, 25, 25), (30, 180, 200, 150))
        win.blit(game_over, (60, 200))
        win.blit(your_score, (53, 243))
        win.blit(result, (x, 286))
    elif is_win:
        congrats = [
            font.render('Winning!', True, (0, 255, 0)),
            font.render('Now you are', True, (180, 180, 180)),
            font.render('The Lord of Tetris', True, (255, 255, 255))
        ]
        pygame.draw.rect(win, (25, 25, 25), (30, 180, 300, 150))
        win.blit(congrats[0], (120, 200))
        win.blit(congrats[1], (95, 243))
        win.blit(congrats[2], (55, 286))
    elif is_game_stop:
        pause = font.render('pause', True, (255, 255, 255))
        press_r_to_start = font.render('-> press r to start', True, (180, 180, 180))
        pygame.draw.rect(win, (25, 25, 25), (30, 180, 300, 107))
        win.blit(pause, (140, 200))
        win.blit(press_r_to_start, (50, 243))
    pygame.display.update()


win = pygame.display.set_mode((365, 510))
pygame.display.set_caption("Tetris by MariUt005")

field = {}
i = -20
while i <= 255:
    j = -120
    field[i] = {}
    while j <= 480:
        field[i][j] = 0
        j += 25
    i += 25

items = [
    pygame.image.load('img/i.png'),
    pygame.image.load('img/j.png'),
    pygame.image.load('img/l.png'),
    pygame.image.load('img/o.png'),
    pygame.image.load('img/s.png'),
    pygame.image.load('img/t.png'),
    pygame.image.load('img/z.png')
]
square = pygame.image.load('img/square.png')

item, item_id, x, y = genItem()
is_item_exist = True

next_item, next_item_id, next_item_x, next_item_y = genItem()
is_items_merged = False
is_visible = False

count_to_lowering = 0
count_to_adding_new_row = 0

previous_move = None
count_previous_move = 0

score = 0
is_game_over = False
is_win = False

is_game_stop = True
is_running = True
while is_running:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    level = score//100 if score < 1000 else 10

    if is_win:
        is_game_stop = True
    if is_game_over:
        is_game_stop = True
    if score == 99990:
        is_win = True

    keys = pygame.key.get_pressed()
    if not is_game_stop:
        if is_item_exist:
            updateField(0)

            if is_items_merged and is_visible:
                next_item, next_item_id, next_item_x, next_item_y = genItem()
                is_items_merged = False

            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and checkLeftSide() and previous_move != 'left':
                x -= 25
                previous_move = 'left'
                count_previous_move = 0
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and checkRightSide() and previous_move != 'right':
                x += 25
                previous_move = 'right'
                count_previous_move = 0
            if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and checkDownSide() and previous_move != 'down':
                y += 25
                is_visible = True
                previous_move = 'down'
                count_previous_move = 0
            if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and previous_move != 'rotation':
                rotation()
                previous_move = 'rotation'
                count_previous_move = 0
            if keys[pygame.K_RETURN] and previous_move != 'fall down':
                fallDown()
                is_item_exist = False
                previous_move = 'fall down'
                count_previous_move = 0

            if count_previous_move == 1:
                previous_move = None
                count_previous_move = 0
            else:
                count_previous_move += 1

            if count_to_lowering >= 10:
                if checkDownSide():
                    y += 25
                    is_visible = True
                else:
                    is_item_exist = False
                count_to_lowering = 0
            else:
                count_to_lowering += level % 10 + 1

            if count_to_adding_new_row >= 5000:
                for i in range(0, level // 2):
                    addNewRow()
                count_to_adding_new_row = 0
            else:
                count_to_adding_new_row += level
        else:
            is_game_over = True if isLoss() else False
            item, item_id, x, y = next_item, next_item_id, next_item_x, next_item_y
            is_items_merged = True
            is_visible = False
            is_item_exist = True
            count_to_lowering = 10

        checkRows()
        updateField(1)

        if keys[pygame.K_ESCAPE]:
            is_game_stop = True
    else:
        if keys[pygame.K_r] and not is_game_over and not is_win:
            is_game_stop = False

    draw()

pygame.quit()
