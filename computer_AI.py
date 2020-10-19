###############
# computer AI #
###############


from evaluation import get_loc_and_score
import numpy as np

BLACK = 1
WHITE = 2


class ComputerAI:
    def __init__(self):
        self.myScore = 0
        self.hisScore = 0
        self.myLoc = ""
        self.hisLoc = ""
        self.myTable = np.zeros((15, 15))
        np.set_printoptions(suppress=True)

    def ai_go(self, chessboard):
        board = chessboard
        msg = ""
        if board.max() == 0:
            coordinate = [7, 7]
        else:

            self.myLoc, self.myTable = get_loc_and_score(board, WHITE)
            self.myScore = np.max(self.myTable)
            self.hisScore = 0

            t_board = board

            for loc in self.myLoc:
                t_board[loc[0]][loc[1]] = WHITE

                t_his_loc, t_his_table = get_loc_and_score(t_board, BLACK)
                t_his_score = np.max(t_his_table)

                if t_his_score > self.hisScore:
                    self.hisLoc, self.hisScore = t_his_loc, t_his_score
                elif t_his_score == self.hisScore:
                    # To merge two arrays
                    self.hisLoc = np.concatenate((self.hisLoc, t_his_loc))
                    # To remove duplicate coordinates
                    self.hisLoc = list(set([tuple(t) for t in self.hisLoc]))

                t_board[loc[0]][loc[1]] = 0

            msg = ['AI max score is %s, Opponent max score is %s' %
                   (int(self.myScore), int(self.hisScore))]

            if self.myScore >= self.hisScore or self.myScore >= 50:
                msg.append('Score of Table (BLACK = -1, WHITE = -2):')
                msg.append(self.__format_of_table(self.myTable.T))

                index_r = np.random.choice(len(self.myLoc))
                coordinate = self.myLoc[index_r]
            else:
                msg.append('The opponent is more favorable, ai choose defense.')
                index_r = np.random.choice(len(self.hisLoc))
                coordinate = self.hisLoc[index_r]

        # Get coordinates x, y
        coordinate_x = coordinate[0]
        coordinate_y = coordinate[1]
        return int(coordinate_x), int(coordinate_y), msg

    # formatting score table information
    @staticmethod
    def __format_of_table(table):
        text = ""
        row_len = 0
        format_dict_x = [chr(i) for i in np.arange(65, 80)]
        format_dict_y = np.arange(15, 0, -1)

        for y in range(0, 15):
            for x in range(0, 15):
                if len(str(table[y][x])) == 2:
                    text += " " + str(table[y][x])
                else:
                    text += "  " + str(table[y][x])
            if y == 0:
                row_len = len(text)
            if y < 15:
                text += " | "+str(format_dict_y[y])+"\n"

        while row_len > -2:
            text += "-"
            row_len -= 1
        text += "\n"

        for num in range(15):
            text += "  " + format_dict_x[num]

        return text
