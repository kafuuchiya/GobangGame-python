from game_evaluation import get_loc_and_score
import numpy as np

BLACK = 1
WHITE = 2


class ComputerAI:
    def __init__(self):
        self.myScore = np.zeros((15, 15))
        self.hisScore = np.zeros((15, 15))
        self.myLoc = ""
        self.hisLoc = ""
        np.set_printoptions(suppress=True)

    def ai_go(self, chessboard):
        board = chessboard.T
        msg = ""
        if board.max() == 0:
            coordinate = [7, 7]
            print()
        else:
            self.myLoc, self.myScore = get_loc_and_score(board, WHITE)
            self.hisLoc, self.hisScore = get_loc_and_score(board, BLACK)

            msg = ['AI max score is %s, Opponent max score is %s' %
                   (int(np.max(self.myScore)), int(np.max(self.hisScore)))]

            if np.max(self.myScore) >= np.max(self.hisScore) or np.max(self.myScore) >= 50:
                msg.append('Score of Table')
                msg.append(self.myScore)
                coordinate = self.myLoc
            else:
                msg.append('The opponent is more favorable, ai choose defense.')
                coordinate = self.hisLoc

        # Get coordinates x, y
        coordinate_y = coordinate[1]
        coordinate_x = coordinate[0]
        return int(coordinate_x), int(coordinate_y), msg
