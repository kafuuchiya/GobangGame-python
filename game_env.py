####################
# game environment #
####################

import tkinter as tk
import tkinter.messagebox
import numpy as np
from game_logic import game_logic

# default value
UNIT = 30  # pixels of unit
GAME_H = 15  # grid height
GAME_W = 15  # grid width
RADIUS = 12  # Chess radius
# height of checkerboard + fine tuning of border
WINDOWS_H = 484 + 8
# width of checkerboard + width of info window + fine tuning of border
WINDOWS_W = 484 + 484 + 10


class Gobang(tk.Tk):

    def __init__(self):
        super().__init__()
        # To set up and create a window
        self.title('My Gobang Game')
        self.resizable(width=False, height=False)  # To set resizable to false
        self.geometry('{0}x{1}'.format(WINDOWS_W, WINDOWS_H))  # window size

        # To initialize the UI parameter
        self.canvas = ""
        self.text_view = ""
        self.rBtn_computerAi = ""
        self.rBtn_pvp = ""
        self.rBtn_val = tk.StringVar()
        self.btn_restart = ""
        self.btn_start = ""

        # To build the UI
        self.__build_game()
        self.__build_show_info()
        self.__build_button()

        # To initialize the game parameter
        self.point_position = np.zeros((GAME_H, GAME_W))
        self.steps = 1
        self.oval = []
        self.game_over = False
        self.mouse_clickable = False
        self.game_start = False

    # To build the game
    def __build_game(self):
        col_name = [chr(i) for i in np.arange(65, 80)]  # ['A', 'B', 'C', 'D', ..., 'O']
        row_name = np.arange(15, 0, -1)  # [15 14 13 12 ...  1]
        self.canvas = tk.Canvas(self,
                                bg='#D3B998',
                                height=(GAME_H + 1) * UNIT + 8,
                                width=(GAME_W + 1) * UNIT + 8)

        # To draw a checkerboard
        # column
        for c in range(GAME_H):
            x0, y0, x1, y1 = (c + 1) * UNIT, UNIT, (c + 1) * UNIT, GAME_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)

            # Generate vertical index
            tk.Label(self,
                     text=col_name[c],
                     bg='#D3B998',
                     font=('Tempus Sans ITC', 12, 'bold'),
                     width=2
                     ).place(x=(c + 1) * UNIT - 12, y=GAME_H * UNIT + 13)

        # row
        for r in range(GAME_W):
            x0, y0, x1, y1 = UNIT, (r + 1) * UNIT, GAME_W * UNIT, (r + 1) * UNIT
            self.canvas.create_line(x0, y0, x1, y1)

            # Generate horizontal index
            tk.Label(self,
                     text=row_name[r],
                     bg='#D3B998',
                     font=('roman', 12, 'bold'),
                     width=2,
                     justify='center'
                     ).place(x=GAME_H * UNIT + 14, y=(r + 1) * UNIT - 12)

        # show it
        self.canvas.place(x=0, y=0, anchor='nw')

    # To build the info box
    def __build_show_info(self):
        self.text_view = tk.Text(self, height=34, width=65)
        scroll = tk.Scrollbar(self, command=self.text_view.yview)
        self.text_view.configure(yscrollcommand=scroll.set)
        # To set the tag for text style
        self.text_view.tag_configure('text_style',
                                     foreground='#ffffff',
                                     font=('Nimbus Mono L', 12, 'normal'))
        self.text_view['background'] = 'black'
        self.text_view.place(x=496, y=2)
        scroll.place(x=958, y=2, height=430)

        info_title = 'Hello, welcome to play my gobang game!\n'
        self.show_result(info_title)

    def __build_button(self):
        # To set radio button
        self.rBtn_computerAi = tk.Radiobutton(self, text='Computer AI',
                                              variable=self.rBtn_val, value='A',
                                              command=self.__radio_button_listener)
        self.rBtn_computerAi.place(x=500, y=460)

        self.rBtn_pvp = tk.Radiobutton(self, text='Stand-alone Game',
                                       variable=self.rBtn_val, value='B',
                                       command=self.__radio_button_listener)
        self.rBtn_pvp.place(x=610, y=460)

        self.rBtn_computerAi.configure(state='disable')
        self.rBtn_val.set('A')
        self.show_result('Computer AI was selected\n')

        # To set button 'restart' and 'start'
        self.btn_restart = tk.Button(self, text='RESTART', command=self.__restart_game)
        self.btn_restart.place(x=790, y=458, width='80')

        self.btn_start = tk.Button(self, text='START', command=self.__start_game)
        self.btn_start.place(x=880, y=458, width='80')

    # To handle related events of button
    def __radio_button_listener(self):
        if self.steps == 1:
            selected = self.rBtn_val.get()
            if selected == 'A':
                self.rBtn_computerAi.configure(state='disable')
                self.rBtn_pvp.configure(state='normal')
                self.show_result('Computer AI was selected\n')

            elif selected == 'B':
                self.rBtn_computerAi.configure(state='normal')
                self.rBtn_pvp.configure(state='disable')
                self.show_result('People vs People battle was selected\n')

    def __restart_game(self):
        if self.steps == 1:
            msg = 'The game has not started yet.'
            tk.messagebox.showinfo(title='Tips', message=msg)
        else:
            msg = 'Do you want to start the game again?'
            ok = tk.messagebox.askyesno("Restart the game", msg)
            if ok:
                self.__reset_game()

    def __start_game(self):
        self.game_start = True
        self.btn_start.configure(state='disable')
        self.rBtn_computerAi.configure(state='disable')
        self.rBtn_pvp.configure(state='disable')

    # To restart the game
    def __reset_game(self):
        for n in range(len(self.oval)):
            self.canvas.delete(self.oval[n])
        self.point_position = np.zeros((GAME_H, GAME_W))
        self.steps = 1
        self.game_over = False
        self.game_start = False
        self.btn_start.configure(state='normal')
        self.text_view.config(state='normal')
        self.text_view.delete(3.0, tk.END)
        self.text_view.config(state='disable')
        self.__radio_button_listener()

    # To show the info on box
    def show_result(self, text):

        # To enable text view for edit
        self.text_view.config(state='normal')

        # There is a newline symbol by default, so > 1.
        # Also, you can change 'tk.END' to 'end-1c' for missing calculation of symbol
        if len(self.text_view.get(1.0, tk.END)) > 1:
            self.text_view.insert('end', '\n', 'text_style')

        self.text_view.insert('end', text, 'text_style')
        self.text_view.see('end')

        # To disable text view
        self.text_view.config(state='disable')

    def paint_mouse_click(self, event):
        x, y = event.x, event.y
        if self.game_over or (self.game_start is False):
            return

        # To make a effective area for the clicked event
        border_l = UNIT - RADIUS  # left border
        border_r = UNIT * GAME_W + RADIUS  # right border
        border_up = UNIT - RADIUS  # upper border
        border_low = UNIT * GAME_H + RADIUS  # lower border

        # To check if the click coordinates are valid, and if they are correct, format them
        if (border_l < x < border_r) & (border_up < y < border_low):

            if (x % UNIT < RADIUS) & (y % UNIT < RADIUS):
                x = (x // UNIT) * UNIT
                y = (y // UNIT) * UNIT

            elif (x % UNIT > (UNIT - RADIUS)) & (y % UNIT < RADIUS):
                x = (x // UNIT) * UNIT + UNIT
                y = (y // UNIT) * UNIT

            elif (x % UNIT < RADIUS) & (y % UNIT > (UNIT - RADIUS)):
                x = (x // UNIT) * UNIT
                y = (y // UNIT) * UNIT + UNIT

            elif (x % UNIT > (UNIT - RADIUS)) & (y % UNIT > (UNIT - RADIUS)):
                x = (x // UNIT) * UNIT + UNIT
                y = (y // UNIT) * UNIT + UNIT
            else:
                self.show_result('Invalid click\n')
                return
        else:
            return

        # To insert coordinate to 2d array
        coordinate_x, coordinate_y = (x // UNIT - 1), (y // UNIT - 1)
        if self.point_position[coordinate_x][coordinate_y] == 0:
            # To paint a chess
            self.__paint(coordinate_x, coordinate_y)
        else:
            self.show_result('Invalid click\n')

    # formatting coordinate information
    @staticmethod
    def __format_of_coordinate(x, y):
        format_dict_x = [chr(i) for i in np.arange(65, 80)]
        format_dict_y = np.arange(15, 0, -1)
        coordinate = '(%s, %s)' % (format_dict_x[x], format_dict_y[y])
        return str(coordinate)

    # To paint chess for computer AI
    def paint_ai(self, x, y):

        # To check if x and y are integers
        if isinstance(x, int):
            pass
        else:
            self.show_result('"x" axis coordinate error for AI')
            return

        if isinstance(y, int):
            pass
        else:
            self.show_result('"y" axis coordinate error for AI')
            return

        self.__paint(x, y)

    # To paint chess
    def __paint(self, x, y):
        if self.point_position[x][y] == 0:
            if self.steps % 2 == 0:
                color_of_chess = "#FFFFFF"  # white
                # chess = 'White'
                self.point_position[x][y] = 2
            else:
                color_of_chess = "#111111"  # black
                # chess = 'Black'
                self.point_position[x][y] = 1

            self.oval.append(self.canvas.create_oval((x + 1) * UNIT - RADIUS,
                                                     (y + 1) * UNIT - RADIUS,
                                                     (x + 1) * UNIT + RADIUS,
                                                     (y + 1) * UNIT + RADIUS,
                                                     fill=color_of_chess))
            self.steps += 1

            # To insert msg
            role = "Black" if self.point_position[x][y] == 1 else "White"
            self.show_result('Round %s: %s, falling chess %s\n' %
                             (self.steps, role, self.__format_of_coordinate(x, y)))

            self.game_over = game_logic(self.point_position, x, y)
            self.__game_result(self.point_position[x][y])

    # Check the judged result, whether it is a victory
    def __game_result(self, role):
        if self.game_over:
            if role == 1:
                name = 'Black'
            elif role == 2:
                name = 'White'
            else:
                self.show_result('error of getting role')
                return

            self.show_result(name + ' win!\n')
            msg = name + " win! Please click YES to restart this game!"
            ok = tk.messagebox.askyesno("Game over", msg)
            # self.game_over = True
            self.mouse_clickable = False
            if ok:
                self.__reset_game()

        elif self.steps == 225:
            self.show_result('The result of the game is a draw')
            self.game_over = True
            self.mouse_clickable = False
            msg = "The result of the game is a draw!"
            ok = tk.messagebox.askyesno("Game over", msg)
            if ok:
                self.__reset_game()
        else:
            self.mouse_clickable = True

    # mouse click events
    def get_mouse_clickable(self):
        return self.mouse_clickable

    def set_mouse_clickable(self, clickable):
        self.mouse_clickable = clickable

    def get_game_over(self):
        return self.game_over

    def get_chess_loc(self):
        return self.point_position

    def get_rbtn_val(self):
        return self.rBtn_val.get()
