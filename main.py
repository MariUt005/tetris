import pygame
import random

pygame.font.init()


def genItem():
    item_index = random.randint(0, 6)
    item = items[item_index]
    item_rotation = random.choice([0, 90, 180, 270])
    item = pygame.transform.rotate(item, item_rotation)
    if item_index == 0 and item_rotation in [0, 180]:
        item_id = 0
        x = 130
        y = -95
    elif item_index == 0 and item_rotation in [90, 270]:
        item_id = 1
        x = 80
        y = -20
    elif item_index in [1, 2, 4, 5, 6] and item_rotation in [0, 180]:
        x = 105
        y = -45
        if item_index == 1:
            item_id = 2 if item_rotation == 0 else 4
        elif item_index == 2:
            item_id = 6 if item_rotation == 0 else 8
        elif item_index == 4:
            item_id = 11
        elif item_index == 5:
            item_id = 13 if item_rotation == 0 else 15
        elif item_index == 6:
            item_id = 17
    elif item_index in [1, 2, 4, 5, 6] and item_rotation in [90, 270]:
        x = 105
        y = -70
        if item_index == 1:
            item_id = 3 if item_rotation == 90 else 5
        elif item_index == 2:
            item_id = 7 if item_rotation == 270 else 9
        elif item_index == 4:
            item_id = 12
        elif item_index == 5:
            item_id = 14 if item_rotation == 270 else 16
        elif item_index == 6:
            item_id = 18
    elif item_index == 3:
        x = 105
        y = -45
        item_id = 10

    return item, item_id, x, y


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
        while x <= 230:
            field[x][y] = field[x][y - 25]
            x += 25
        y -= 25


def rotation():
    global item, item_id, field, x, y
    previous_position = item_id
    if item_id == 0:
        item_id = 1
        if x + 100 <= 255 and not field[x + 25][y] and not field[x + 50][y] and not field[x + 75][y]:
            pass
        elif x + 100 == 255 + 25 and not field[x - 25][y] and not field[x + 25][y] and not field[x + 50][y]:
            x -= 25
        elif x + 100 == 255 + 50 and not field[x - 50][y] and not field[x - 25][y] and not field[x + 25][y]:
            x -= 50
        elif x + 100 == 255 + 75 and not field[x - 75][y] and not field[x - 50][y] and not field[x - 25][y]:
            x -= 75
        else:
            item_id = 0
    elif item_id == 1:
        if y + 100 < 505 and not field[x][y + 25] and not field[x][y + 50] and not field[x][y + 75]:
            item_id = 0
    elif item_id == 2:
        if y + 50 < 505 and not field[x + 25][y] and not field[x][y + 50]:
            item_id = 3
    elif item_id == 3:
        if x + 50 < 255 and not field[x + 50][y] and not field[x + 50][y + 25]:
            item_id = 4
        elif not field[x - 25][y] and not field[x + 25][y + 25]:
            item_id = 4
            x -= 25
    elif item_id == 4:
        if y + 50 < 505 and not field[x + 25][y + 25] and not field[x + 25][y + 50] and not field[x][y + 50]:
            item_id = 5
    elif item_id == 5:
        if x + 50 < 255 and not field[x][y] and not field[x][y + 25] and not field[x + 50][y + 25]:
            item_id = 2
        elif not field[x - 25][y] and not field[x - 25][y + 25] and not field[x][y + 25]:
            item_id = 2
            x -= 25
    elif item_id == 6:
        if y + 50 < 505 and not field[x + 25][y + 25] and not field[x + 25][y + 50]:
            item_id = 7
    elif item_id == 7:
        if x + 50 < 255 and not field[x][y + 25] and not field[x + 50][y] and not field[x + 50][y + 25]:
            item_id = 8
        elif not field[x - 25][y + 25] and not field[x][y + 25]:
            item_id = 8
            x -= 25
    elif item_id == 8:
        if y + 50 < 505 and not field[x][y] and not field[x][y + 50] and not field[x + 25][y + 50]:
            item_id = 9
    elif item_id == 9:
        if x + 50 < 255 and not field[x + 25][y] and not field[x + 50][y]:
            item_id = 6
        elif not field[x - 25][y] and not field[x - 25][y + 25] and not field[x + 25][y]:
            item_id = 6
            x -= 25
    elif item_id == 11:
        if y + 50 < 505 and not field[x][y] and not field[x + 25][y + 50]:
            item_id = 12
    elif item_id == 12:
        if x + 50 < 250 and not field[x + 25][y] and not field[x + 50][y]:
            item_id = 11
        elif not field[x - 25][y + 25] and not field[x + 25][y]:
            item_id = 11
            x -= 25
    elif item_id == 13:
        if y + 50 < 505 and not field[x][y + 25] and not field[x + 25][y + 50]:
            item_id = 14
    elif item_id == 14:
        if x + 50 < 255 and not field[x + 50][y + 25]:
            item_id = 15
        elif not field[x - 25][y + 25] and not field[x][y]:
            item_id = 15
            x -= 25
    elif item_id == 15:
        if y + 50 < 505 and not field[x][y] and not field[x][y + 50]:
            item_id = 16
    elif item_id == 16:
        if x + 50 < 255 and not field[x + 25][y] and not field[x + 50][y]:
            item_id = 13
        elif not field[x - 25][y] and not field[x + 25][y]:
            item_id = 13
            x -= 25
    elif item_id == 17:
        if y + 50 < 505 and not field[x][y + 25] and not field[x][y + 50]:
            item_id = 18
    elif item_id == 18:
        if x + 50 < 255 and not field[x][y] and not field[x + 50][y + 25]:
            item_id = 17
        elif not field[x - 25][y] and not field[x][y]:
            item_id = 17
            x -= 25
    if previous_position == item_id:
        item = pygame.transform.rotate(item, 90)


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
        lover_font.render('->a or left', True, (255, 255, 255)),
        lover_font.render(' to move left', True, (180, 180, 180)),
        lover_font.render('->d or right', True, (255, 255, 255)),
        lover_font.render(' to move right', True, (180, 180, 180)),
        lover_font.render('->s or down', True, (255, 255, 255)),
        lover_font.render(' to move down', True, (180, 180, 180)),
        lover_font.render('->SPACE', True, (255, 255, 255)),
        lover_font.render(' to rotate', True, (180, 180, 180))
    ]
    win.blit(manual[0], (260, 200))
    win.blit(manual[1], (260, 215))
    win.blit(manual[2], (260, 240))
    win.blit(manual[3], (260, 255))
    win.blit(manual[4], (260, 280))
    win.blit(manual[5], (260, 295))
    win.blit(manual[6], (260, 320))
    win.blit(manual[7], (260, 335))
    win.blit(manual[8], (260, 360))
    win.blit(manual[9], (260, 375))
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
i = 5
while i <= 230:
    j = -95
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
item_exist = True

next_item, next_item_id, next_item_x, next_item_y = genItem()
is_items_merged = False
is_visible = False

count_to_lowering = 0

score = 0
is_game_over = False
is_win = False

is_game_stop = True
is_running = True
while is_running:
    pygame.time.delay(90)

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
        if item_exist:
            updateField(0)

            if is_items_merged and is_visible:
                next_item, next_item_id, next_item_x, next_item_y = genItem()
                is_items_merged = False

            if count_to_lowering >= 10:
                if checkDownSide():
                    y += 25
                    is_visible = True
                else:
                    item_exist = False
                count_to_lowering = 0
            else:
                count_to_lowering += level % 10 + 1

            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and checkLeftSide():
                x -= 25
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and checkRightSide():
                x += 25
            if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and checkDownSide():
                y += 25
                is_visible = True
            if keys[pygame.K_SPACE]:
                rotation()
        else:
            i = 5
            while i < 255:
                if field[i][-20]:
                    is_game_over = True
                i += 25
            item, item_id, x, y = next_item, next_item_id, next_item_x, next_item_y
            is_items_merged = True
            is_visible = False
            item_exist = True
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
