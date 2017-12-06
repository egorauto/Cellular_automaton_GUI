import numpy as np
import random as rnd


def initiate_cell_space(self):

    '''Initiates the cell state space according to the chosen mode'''

    self.column_cells = self.canvas_height / self.cell_size
    self.row_cells = self.canvas_width / self.cell_size
    self.cell_state_space = np.zeros((self.row_cells, self.column_cells))

    if self.rule.get() == 'Pure Glider':

        self.cell_state_space[self.row_cells / 2][self.column_cells / 2] = 1
        self.cell_state_space[self.row_cells / 2][(self.column_cells / 2) + 1] = 1
        self.cell_state_space[self.row_cells / 2][(self.column_cells / 2) - 1] = 1
        self.cell_state_space[(self.row_cells / 2) + 1][(self.column_cells / 2)] = 1

        self.cell_state_space[(self.row_cells / 2) - 5][(self.column_cells / 2) + 2] = 1
        self.cell_state_space[(self.row_cells / 2) - 5][(self.column_cells / 2) + 3] = 1
        self.cell_state_space[(self.row_cells / 2) - 5][(self.column_cells / 2) + 4] = 1
        self.cell_state_space[(self.row_cells / 2) - 6][(self.column_cells / 2) + 2] = 1
        self.cell_state_space[(self.row_cells / 2) - 7][(self.column_cells / 2) + 2] = 1

        self.cell_state_space[(self.row_cells / 2) + 5][(self.column_cells / 2) - 2] = 1
        self.cell_state_space[(self.row_cells / 2) + 5][(self.column_cells / 2) - 3] = 1
        self.cell_state_space[(self.row_cells / 2) + 5][(self.column_cells / 2) - 4] = 1
        self.cell_state_space[(self.row_cells / 2) + 6][(self.column_cells / 2) - 2] = 1
        self.cell_state_space[(self.row_cells / 2) + 7][(self.column_cells / 2) - 2] = 1

    elif self.rule.get() == 'Diamond':

        self.cell_state_space[self.row_cells / 2][self.column_cells / 2] = 1
        self.cell_state_space[(self.row_cells / 2) + 2][self.column_cells / 2] = 1
        self.cell_state_space[(self.row_cells / 2) - 2][self.column_cells / 2] = 1
        self.cell_state_space[(self.row_cells / 2) + 4][self.column_cells / 2] = 1
        self.cell_state_space[(self.row_cells / 2) - 4][self.column_cells / 2] = 1

        for i in range(1, 6):
            self.cell_state_space[self.row_cells / 2][(self.column_cells / 2) - i] = 1
        for i in range(1, 7):
            self.cell_state_space[self.row_cells / 2][(self.column_cells / 2) + i] = 1

        for i in range(1, 4):
            self.cell_state_space[(self.row_cells / 2) + 2][(self.column_cells / 2) - i] = 1
            self.cell_state_space[(self.row_cells / 2) - 2][(self.column_cells / 2) - i] = 1
        for i in range(1, 5):
            self.cell_state_space[(self.row_cells / 2) + 2][(self.column_cells / 2) + i] = 1
            self.cell_state_space[(self.row_cells / 2) - 2][(self.column_cells / 2) + i] = 1

        for i in range(1, 2):
            self.cell_state_space[(self.row_cells / 2) + 4][(self.column_cells / 2) - i] = 1
            self.cell_state_space[(self.row_cells / 2) - 4][(self.column_cells / 2) - i] = 1
        for i in range(1, 3):
            self.cell_state_space[(self.row_cells / 2) + 4][(self.column_cells / 2) + i] = 1
            self.cell_state_space[(self.row_cells / 2) - 4][(self.column_cells / 2) + i] = 1

    elif self.rule.get() == 'Gosper\'s gun':

        self.cell_state_space[(self.row_cells / 2) - 18][(10)] = 1
        self.cell_state_space[(self.row_cells / 2) - 17][(10)] = 1
        self.cell_state_space[(self.row_cells / 2) - 18][(10) + 1] = 1
        self.cell_state_space[(self.row_cells / 2) - 17][(10) + 1] = 1

        self.cell_state_space[(self.row_cells / 2) + 17][(10) - 1] = 1
        self.cell_state_space[(self.row_cells / 2) + 16][(10) - 1] = 1
        self.cell_state_space[(self.row_cells / 2) + 17][(10) - 2] = 1
        self.cell_state_space[(self.row_cells / 2) + 16][(10) - 2] = 1

        self.cell_state_space[(self.row_cells / 2) - 8][(10)] = 1
        self.cell_state_space[(self.row_cells / 2) - 8][(10) + 1] = 1
        self.cell_state_space[(self.row_cells / 2) - 8][(10) + 2] = 1
        self.cell_state_space[(self.row_cells / 2) - 7][(10) - 1] = 1
        self.cell_state_space[(self.row_cells / 2) - 7][(10) + 3] = 1
        self.cell_state_space[(self.row_cells / 2) - 6][(10) - 2] = 1
        self.cell_state_space[(self.row_cells / 2) - 5][(10) - 2] = 1
        self.cell_state_space[(self.row_cells / 2) - 6][(10) + 4] = 1
        self.cell_state_space[(self.row_cells / 2) - 5][(10) + 4] = 1
        self.cell_state_space[(self.row_cells / 2) - 4][(10) + 1] = 1
        self.cell_state_space[(self.row_cells / 2) - 3][(10) - 1] = 1
        self.cell_state_space[(self.row_cells / 2) - 3][(10) + 3] = 1
        self.cell_state_space[(self.row_cells / 2) - 2][(10)] = 1
        self.cell_state_space[(self.row_cells / 2) - 2][(10) + 1] = 1
        self.cell_state_space[(self.row_cells / 2) - 2][(10) + 2] = 1
        self.cell_state_space[(self.row_cells / 2) - 1][(10) + 1] = 1

        self.cell_state_space[(self.row_cells / 2) + 2][(10)] = 1
        self.cell_state_space[(self.row_cells / 2) + 3][(10)] = 1
        self.cell_state_space[(self.row_cells / 2) + 2][(10) - 1] = 1
        self.cell_state_space[(self.row_cells / 2) + 3][(10) - 1] = 1
        self.cell_state_space[(self.row_cells / 2) + 2][(10) - 2] = 1
        self.cell_state_space[(self.row_cells / 2) + 3][(10) - 2] = 1
        self.cell_state_space[(self.row_cells / 2) + 4][(10) - 3] = 1
        self.cell_state_space[(self.row_cells / 2) + 4][(10) + 1] = 1
        self.cell_state_space[(self.row_cells / 2) + 6][(10) + 1] = 1
        self.cell_state_space[(self.row_cells / 2) + 6][(10) + 2] = 1
        self.cell_state_space[(self.row_cells / 2) + 6][(10) - 4] = 1
        self.cell_state_space[(self.row_cells / 2) + 6][(10) - 3] = 1

    elif self.rule.get() == 'Rule 30':

        self.cell_state_space[rnd.randint(0, self.column_cells)] = 1

    else:

        for i in range(0, self.row_cells):
            for j in range(0, self.column_cells):
                if rnd.random() < 0.4:
                    self.cell_state_space[i][j] = 1
                else:
                    self.cell_state_space[i][j] = 0

    return self.cell_state_space


def draw_square_cells(self):

    '''Draws the cells in their new states updated by the chosen rule'''

    self.canvas.delete('all')

    for x in range(self.cell_size, self.canvas_width, self.cell_size):
        self.canvas.create_line(x, 0, x, self.canvas_height, fill="grey")
    for y in range(self.cell_size, self.canvas_height, self.cell_size):
        self.canvas.create_line(0, y, self.canvas_width, y, fill="grey")

    for i in range(0, self.row_cells):
        for j in range(0, self.column_cells):
            if self.cell_state_space[i][j] == 1:
                self.canvas.create_rectangle(i * self.cell_size, j * self.cell_size,
                                             (i * self.cell_size) + self.cell_size,
                                             (j * self.cell_size) + self.cell_size, fill='black')
            else:
                pass

    self.canvas.update()