import pygame
import math

pygame.init()
background = pygame.image.load("board.png")
screen = pygame.display.set_mode((1200, 850))
icon = pygame.image.load("board.png")
pygame.display.set_caption("The Game")

# bulshit and stupid things:
XImg = []
num_of_X = 10
for a in range(num_of_X):
    XImg.append(pygame.image.load('x.png'))
OImg = []
num_of_O = 10
for a in range(num_of_O):
    OImg.append(pygame.image.load('o.png'))


def X(xy, i):
    x = xy[0]
    y = xy[1]
    screen.blit(XImg[i], (x, y))


def O(xy, i):
    x = xy[0]
    y = xy[1]
    screen.blit(OImg[i], (x, y))


def check(num, place, status):
    if (place[num] != "X" or place[num] != "O") and num != 1 and status == "ok":
        return True
    else:
        return False


def distance(x, y, x1y1):
    x1, y1 = x1y1
    return math.sqrt(math.pow(x - x1, 2) + math.pow(y - y1, 2))


def where(x, y, boardList):
    for j in range(1, len(boardList)):
        if distance(x, y, boardList[j]) < 150:
            return j
    return False


font = pygame.font.Font("freesansbold.ttf", 90)
textX = 250
textY = 300


def game_over(status, textX, textY):
    over_text = font.render(status, True, (255, 100, 70))
    again_text = font.render("please restart the game", True, (255, 100, 70))
    screen.blit(over_text, (textX, textY))
    screen.blit(again_text, (textX - 150, textY + 100))


turns = [10]
num_of_turns = 0
status = "ok"
# the real code:
boardList = [[0, 0], [100, 25], [425, 25], [750, 25], [100, 300], [450, 300], [750, 300], [100, 590], [425, 590],
             [750, 590]]
place = ["0", "X", "2", "3", "4", "5", "6", "7", "8", "9"]

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            where1 = where(x, y, boardList)
            if where1:
                if check(where1, place, status):
                    place[where1] = "O"
                    num_of_turns += 1
                    turns.append(where1)
    # the if conditions:
    if num_of_turns > 0:
        # 2,4,6,8:
        if turns[1] % 2 == 0:
            place[5] = "X"
            if num_of_turns > 1:
                if turns[2] != 9:
                    place[9] = "X"
                    status = "computer wins!"
                elif turns[1] == 6 or turns[1] == 4:
                    place[3] = "X"
                    if num_of_turns > 2:
                        if turns[3] != 2:
                            place[2] = "X"
                            status = "computer wins!"
                        else:
                            place[7] = "X"
                            status = "computer wins!"
                elif turns[1] == 2 or turns[1] == 8:
                    place[7] = "X"
                    if num_of_turns > 2:
                        if turns[3] != 3:
                            place[3] = "X"
                            status = "computer wins!"
                        else:
                            place[4] = "X"
                            status = "computer wins!"
        # 5,7,3:
        elif turns[1] == 3 or turns[1] == 5 or turns[1] == 7:
            place[9] = "X"
            if num_of_turns > 1:

                if turns[2] != 5 and turns[1] != 5:
                    place[5] = "X"
                    status = "computer wins!"
                elif turns[2] == 3:
                    place[7] = "X"
                    if num_of_turns > 2:
                        if turns[3] != 2:
                            place[2] = "X"
                            status = "computer wins!"
                        else:
                            place[6] = "X"
                            status = "computer wins!"
                elif turns[2] == 7:
                    place[3] = "X"
                    if num_of_turns > 2:
                        if turns[3] != 4:
                            place[4] = "X"
                            status = "computer wins!"
                        else:
                            place[8] = "X"
                            status = "computer wins!"
                elif turns[2] == 8:
                    place[2] = "X"
                    if num_of_turns > 2:
                        if turns[3] != 3:
                            place[3] = "X"
                            status = "computer wins!"
                        else:
                            place[7] = "X"
                            if num_of_turns > 3:
                                if turns[4] != 4:
                                    place[4] = "X"
                                    status = "computer wins!"
                                else:
                                    place[6] = "X"
                                    status = "well done it's a tie!"

                elif turns[2] == 4:
                    place[6] = "X"
                    if num_of_turns > 2:
                        if turns[3] != 3:
                            place[3] = "X"
                        else:
                            place[7] = "X"
                            if num_of_turns > 3:
                                if turns[4] != 8:
                                    place[8] = "X"
                                    status = "computer wins!"
                                else:
                                    place[2] = "X"
                                    status = "well done it's a tie!"
                elif turns[2] == 6:
                    place[4] = "X"
                    if num_of_turns > 2:
                        if turns[3] != 7:
                            place[7] = "X"
                            status = "computer wins!"
                        else:
                            place[3] = "X"
                            if num_of_turns > 3:
                                if turns[4] != 2:
                                    place[2] = "X"
                                    status = "computer wins!"
                                else:
                                    place[8] = "X"
                                    status = "well done it's a tie!"
                elif turns[2] == 5 and turns[1] != 3:
                    place[3] = "X"
                    if num_of_turns > 2:
                        if turns[3] != 2:
                            place[2] = "X"
                            status = "computer wins!"
                        else:
                            place[6] = "X"
                elif turns[2] == 5 and turns[1] != 7:
                    place[7] = "X"
                    if num_of_turns > 2:
                        if turns[3] != 4:
                            place[4] = "X"
                            status = "computer wins!"
                        else:
                            place[8] = "X"
                            status = "computer wins!"
                elif turns[2] == 2:
                    place[8] = "X"
                    if num_of_turns > 2:
                        if turns[3] != 7:
                            place[7] = "X"
                            status = "computer wins!"
                        else:
                            place[3] = "X"
                            if num_of_turns > 3:
                                if turns[4] != 6:
                                    place[6] = "X"
                                    status = "computer wins"
                                else:
                                    place[4] = "X"
                                    status = "well done it's a tie!"
        else:  # 9
            place[3] = "X"
            if num_of_turns > 1:
                if turns[2] != 2:
                    place[2] = "X"
                    status = "computer wins!"
                else:
                    place[7] = "X"
                    if num_of_turns > 2:
                        if turns[3] != 4:
                            place[4] = "X"
                            status = "computer wins!"
                        else:
                            place[5] = "X"
                            status = "computer wins!"

    for i in range(len(place)):
        if place[i] == "X":
            X(boardList[i], 1)
        elif place[i] == "O":
            O(boardList[i], 1)
    if status != "ok":
        game_over(status, textX, textY)

    pygame.display.update()
