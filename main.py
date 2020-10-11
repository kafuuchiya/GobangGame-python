from game_env import Gobang
from computer_AI import ComputerAI
import numpy as np


def update_board(event):

    env.paint_mouse_click(event)
    if (env.get_game_over() is False) and (np.sum(env.get_chess_loc()) > 0):

        if env.get_mouse_clickable():
            radio_selected = env.get_rbtn_val()
            if radio_selected == 'A':
                computer_ai()

            elif radio_selected == 'B':
                stand_alone_game()

            env.set_mouse_clickable(False)


def computer_ai():

    if not env.get_game_over():
        x, y, msg = cai.ai_go(env.get_chess_loc())
        for msg_t in msg:
            env.show_result(msg_t)
        env.paint_ai(x, y)


def stand_alone_game():
    # None
    return


if __name__ == '__main__':
    env = Gobang()
    # <Button-1> Left click event for the mouse
    env.canvas.bind("<Button-1>", update_board)
    cai = ComputerAI()
    env.mainloop()
