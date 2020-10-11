##############
# game logic #
##############

# judgment of result by vertical, horizontal, left and right tilt
def game_logic(p_loc, x, y):

    # chess number. '1' for black chess, '2' for white chess
    chess_num = int(p_loc[x][y])
    game_over = False

    # 1 ↑↓
    if game_over:
        return True
    else:
        count = 1
        for i in range(1, 5):
            if (y - i >= 0) and (p_loc[x][y - i] == chess_num):
                count += 1
            else:
                break

        for i in range(1, 5):
            if (y + i <= 14) and (p_loc[x][y + i] == chess_num):
                count += 1
            else:
                break

        game_over = check_result(count)

    # 2 ←→
    if game_over:
        return True
    else:
        count = 1
        for i in range(1, 5):
            if (x - i >= 0) and (p_loc[x - i][y] == chess_num):
                count += 1
            else:
                break

        for i in range(1, 5):
            if (x + i <= 14) and (p_loc[x + i][y] == chess_num):
                count += 1
            else:
                break

        game_over = check_result(count)

    # 3 ↖↘
    if game_over:
        return True
    else:
        count = 1
        for i in range(1, 5):
            if (x - i >= 0) and (y - i >= 0) and (p_loc[x - i][y - i] == chess_num):
                count += 1
            else:
                break

        for i in range(1, 5):
            if (x + i <= 14) and (y + i <= 14) and (p_loc[x + i][y + i] == chess_num):
                count += 1
            else:
                break

        game_over = check_result(count)

    # 4 ↗↙
    if game_over:
        return True
    else:
        count = 1
        for i in range(1, 5):
            if (x + i <= 14) and (y - i >= 0) and (p_loc[x + i][y - i] == chess_num):
                count += 1
            else:
                break

        for i in range(1, 5):
            if (x - i >= 0) and (y + i <= 14) and (p_loc[x - i][y + i] == chess_num):
                count += 1
            else:
                break

        game_over = check_result(count)

    return game_over


def check_result(count):
    if (count == 5) or (count > 5):
        return True
    else:
        return False
