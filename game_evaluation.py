import numpy as np

BLANK_GRID = 0
BLACK = 1
WHITE = 2

FIVE = 50  # five
FOUR = 25  # four
S_FOUR = 15  # sleep four
THREE = 10  # three
S_THREE = 3  # sleep three
TWO = 5  # two
S_TWO = 2  # sleep two
S_ONE = 1  # sleep one


# Check position in four directions of a point
# judgment of result by vertical, horizontal, left and right tilt
def checkpoints(x, y, checkerboard, role):
    if role == 2:
        oneself = WHITE
        opponent = BLACK
    elif role == 1:
        oneself = BLACK
        opponent = WHITE
    else:
        return

    cb = checkerboard
    count = 1
    head = []
    tail = []

    # 1 ↑↓
    for i in range(1, 5):
        if y - i >= 0:
            if (len(head) == 0) and (cb[x][y - i] == oneself):
                count += 1
            elif (cb[x][y - i] == BLANK_GRID) or (cb[x][y - i] == oneself):
                head.append(cb[x][y - i])
            elif cb[x][y - i] == opponent:
                head.append(cb[x][y - i])
                break
        else:
            break
    for i in range(1, 5):
        if y + i < 15:
            if (len(tail) == 0) and (cb[x][y + i] == oneself):
                count += 1
            elif (cb[x][y + i] == BLANK_GRID) or (cb[x][y + i] == oneself):
                tail.append(cb[x][y + i])
            elif cb[x][y + i] == opponent:
                tail.append(cb[x][y + i])
                break
        else:
            break
    total_point = evaluation(head, count, tail, opponent)

    count = 1
    head = []
    tail = []
    # 2 ←→
    for i in range(1, 5):
        if x - i >= 0:
            if (len(head) == 0) and (cb[x - i][y] == oneself):
                count += 1
            elif (cb[x - i][y] == BLANK_GRID) or (cb[x - i][y] == oneself):
                head.append(cb[x - i][y])
            elif cb[x - i][y] == opponent:
                head.append(cb[x - i][y])
                break
        else:
            break
    for i in range(1, 5):
        if x + i < 15:
            if (len(tail) == 0) and (cb[x + i][y] == oneself):
                count += 1
            elif (cb[x + i][y] == BLANK_GRID) or (cb[x + i][y] == oneself):
                tail.append(cb[x + i][y])
            elif cb[x + i][y] == opponent:
                tail.append(cb[x + i][y])
                break
        else:
            break
    total_point += evaluation(head, count, tail, opponent)

    count = 1
    head = []
    tail = []
    # 3 ↖↘
    for i in range(1, 5):
        if (x - i >= 0) and (y - i >= 0):
            if (len(head) == 0) and (cb[x - i][y - i] == oneself):
                count += 1
            elif (cb[x - i][y - i] == BLANK_GRID) or (cb[x - i][y - i] == oneself):
                head.append(cb[x - i][y - i])
            elif cb[x - i][y - i] == 1:
                head.append(cb[x - i][y - i])
                break
        else:
            break
    for i in range(1, 5):
        if (x + i < 15) and (y + i < 15):
            if (len(tail) == 0) and (cb[x + i][y + i] == oneself):
                count += 1
            elif (cb[x + i][y + i] == BLANK_GRID) or (cb[x + i][y + i] == oneself):
                tail.append(cb[x + i][y + i])
            elif cb[x + i][y + i] == opponent:
                tail.append(cb[x + i][y + i])
                break
        else:
            break
    total_point += evaluation(head, count, tail, opponent)

    count = 1
    head = []
    tail = []
    # 4 ↙↗
    for i in range(1, 5):
        if (x - i >= 0) and (y + i < 15):
            if (len(head) == 0) and (cb[x - i][y + i] == oneself):
                count += 1
            elif (cb[x - i][y + i] == BLANK_GRID) or (cb[x - i][y + i] == oneself):
                head.append(cb[x - i][y + i])
            elif cb[x - i][y + i] == opponent:
                head.append(cb[x - i][y + i])
                break
        else:
            break
    for i in range(1, 5):
        if (x + i < 15) and (y - i >= 0):
            if (len(tail) == 0) and (cb[x + i][y - i] == oneself):
                count += 1
            elif (cb[x + i][y - i] == BLANK_GRID) or (cb[x + i][y - i] == oneself):
                tail.append(cb[x + i][y - i])
            elif cb[x + i][y - i] == opponent:
                tail.append(cb[x + i][y - i])
                break
        else:
            break
    total_point += evaluation(head, count, tail, opponent)

    return total_point


# Score the checkpoints
def evaluation(head, count, tail, opponent):
    score = 0
    if count >= 5:
        # win
        score = FIVE
    elif count == 4:
        if (len(head) == 0) or (len(tail) == 0) or (head[0] == opponent) or (tail[0] == opponent):
            # This count line has an opponent at the head or tail
            # It may also be that the head or tail is beyond the boundary
            score = S_FOUR
        elif (head[0] == BLANK_GRID) and (tail[0] == BLANK_GRID):
            # Empty at the head and tail for this count line
            score = FOUR

    elif count == 3:
        if (len(head) == 0) or (len(tail) == 0) or (head[0] == opponent) or (tail[0] == opponent):
            score = S_THREE
        elif (head[0] == BLANK_GRID) and (tail[0] == BLANK_GRID):
            score = THREE
    elif count == 2:
        if (len(head) == 0) or (len(tail) == 0) or (head[0] == opponent) or (tail[0] == opponent):
            score = S_TWO
        elif (head[0] == BLANK_GRID) and (tail[0] == BLANK_GRID):
            score = TWO
    elif count == 1:
        if (len(head) > 0) and (head[0] == opponent):
            score = S_ONE
        elif (len(tail) > 0) and (tail[0] == opponent):
            score = S_ONE

    return score


# function of 'get_fav_loc' is to get favorable coordinates
# function of 'get_max_score' is to get the score of the max score
# function of 'get_loc_and_score' is to get the coordinate of the max score and the table of the score
def get_fav_loc(checkerboard, role):
    score = np.zeros((15, 15))    # white, AI
    for x in range(0, 15):
        for y in range(0, 15):
            if checkerboard[x][y] == 0:
                score[x][y] = checkpoints(x, y, checkerboard, role)
    coordinate = np.argwhere(score > 0)
    return coordinate


def get_max_score(checkerboard, role):
    score = np.zeros((15, 15))
    for x in range(0, 15):
        for y in range(0, 15):
            if checkerboard[x][y] == 0:
                score[x][y] = checkpoints(x, y, checkerboard, role)

    max_score = score.max()
    return int(max_score)


def get_loc_and_score(checkerboard, role):
    score = np.zeros((15, 15))
    for x in range(0, 15):
        for y in range(0, 15):
            if checkerboard[x][y] == 0:
                score[x][y] = checkpoints(x, y, checkerboard, role)

    coordinate = np.argwhere(score == np.max(score))
    # If there are multiple optional coordinates, randomly select a coordinate
    index = np.random.choice(len(coordinate))
    y = coordinate[index][0]
    x = coordinate[index][1]
    point = [x, y]
    return point, score
