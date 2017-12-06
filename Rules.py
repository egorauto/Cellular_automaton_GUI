import numpy as np

def neighbour_state(self):

    '''B2/S23'''

    # self.neighbours stores the number of neighbours for each cell in self.cell_state_space
    self.neighbours = np.zeros((self.row_cells, self.column_cells))

    for i in range(0, self.row_cells):
        for j in range(0, self.column_cells):

            if (i == 0) and (j == 0):
                # Upper left corner
                self.neighbours[i][j] = self.cell_state_space[i][j + 1] + self.cell_state_space[i + 1][j + 1] + \
                                        self.cell_state_space[i + 1][j]

            elif (i == self.row_cells - 1) and (j == self.column_cells - 1):
                # Lower right corner
                self.neighbours[i][j] = self.cell_state_space[i][j - 1] + self.cell_state_space[i - 1][j - 1] + \
                                        self.cell_state_space[i - 1][j]

            elif (i == self.row_cells - 1) and (j == 0):
                # Upper right corner
                self.neighbours[i][j] = self.cell_state_space[i][j + 1] + self.cell_state_space[i - 1][j + 1] + \
                                        self.cell_state_space[i - 1][j]

            elif (i == 0) and (j == self.column_cells) - 1:
                # Lower left corner
                self.neighbours[i][j] = self.cell_state_space[i][j - 1] + self.cell_state_space[i + 1][j - 1] + \
                                        self.cell_state_space[i + 1][j]

            elif (i == 0) and (j > 0) and (j < self.column_cells - 1):
                # Upper boundary
                self.neighbours[i][j] = self.cell_state_space[i][j + 1] + self.cell_state_space[i + 1][j + 1] + \
                                        self.cell_state_space[i + 1][j] + self.cell_state_space[i + 1][j - 1] + \
                                        self.cell_state_space[i][j - 1]

            elif (i > 0) and (i < self.row_cells - 1) and (j == 0):
                # Left boundary
                self.neighbours[i][j] = self.cell_state_space[i][j + 1] + self.cell_state_space[i + 1][j + 1] + \
                                        self.cell_state_space[i + 1][j] + self.cell_state_space[i + 1][j - 1] + \
                                        self.cell_state_space[i][j - 1]

            elif (i == self.row_cells - 1) and (j > 0) and (j < self.column_cells - 1):
                # Bottom Boundary
                self.neighbours[i][j] = self.cell_state_space[i][j + 1] + self.cell_state_space[i - 1][j + 1] + \
                                        self.cell_state_space[i - 1][j] + self.cell_state_space[i - 1][j - 1] + \
                                        self.cell_state_space[i][j - 1]

            elif (i > 0) and (i < self.row_cells - 1) and (j == self.column_cells - 1):
                # Right Boundary
                self.neighbours[i][j] = self.cell_state_space[i][j - 1] + self.cell_state_space[i + 1][j - 1] + \
                                        self.cell_state_space[i + 1][j] + self.cell_state_space[i - 1][j - 1] + \
                                        self.cell_state_space[i - 1][j]

            else:
                # Not touching the boundaries
                self.neighbours[i][j] = self.cell_state_space[i][j - 1] + self.cell_state_space[i + 1][j - 1] + \
                                        self.cell_state_space[i + 1][j] + self.cell_state_space[i - 1][j - 1] + \
                                        self.cell_state_space[i - 1][j] + self.cell_state_space[i - 1][j + 1] + \
                                        self.cell_state_space[i][j + 1] + self.cell_state_space[i + 1][j + 1]

    return self.neighbours

def conway(self):

    '''B2/S23'''

    for i in range(0, self.row_cells):
        for j in range(0, self.column_cells):
            if self.cell_state_space[i][j] == 1:
                if self.neighbours[i][j] < 2:
                    self.cell_state_space[i][j] = 0
                elif self.neighbours[i][j] > 3:
                    self.cell_state_space[i][j] = 0
                else:
                    pass

            else:
                if self.neighbours[i][j] == 3:
                    self.cell_state_space[i][j] = 1
                else:
                    pass

    return self.cell_state_space

def day_and_night(self):

    '''B3678/S34678'''

    for i in range(0, self.row_cells):
        for j in range(0, self.column_cells):
            if self.cell_state_space[i][j] == 1:
                if self.neighbours[i][j] == 3 or self.neighbours[i][j] == 4:
                    pass
                elif self.neighbours[i][j] >= 6:
                    pass
                else:
                    self.cell_state_space[i][j] = 0
            else:
                if self.neighbours[i][j] == 3 or self.neighbours[i][j] >= 6:
                    self.cell_state_space[i][j] = 1
                else:
                    pass

    return self.cell_state_space

def morley(self):

    '''B368/S245'''

    for i in range(0, self.row_cells):
        for j in range(0, self.column_cells):
            if self.cell_state_space[i][j] == 1:
                if self.neighbours[i][j] == 2 or self.neighbours[i][j] == 4 or self.neighbours[i][j] == 5:
                    pass
                else:
                    self.cell_state_space[i][j] = 0
            else:
                if self.neighbours[i][j] == 3 or self.neighbours[i][j] == 6 or self.neighbours[i][j] == 8:
                    self.cell_state_space[i][j] = 1
                else:
                    pass

    return self.cell_state_space

def rule_30(self):

    ''''''

    for i in range(0, self.column_cells):

            if self.cell_state_space[i][self.counter] == 0:
                if self.cell_state_space[i-1][self.counter] == 0 and self.cell_state_space[self.counter][i+1] == 0:
                    pass
                elif self.cell_state_space[i-1][self.counter] == 0 and self.cell_state_space[self.counter][i+1] == 1:
                    self.cell_state_space[i][self.counter + 1] = 1
                elif self.cell_state_space[i-1][self.counter] == 0 and self.cell_state_space[self.counter][i+1] == 0:
                    self.cell_state_space[i][self.counter + 1] = 1
                else:
                    self.cell_state_space[i][self.counter+1] = 0
            else:
                if self.cell_state_space[i-1][self.counter] == 1 and self.cell_state_space[self.counter][i+1] == 1:
                    self.cell_state_space[i][self.counter+1] = 0
                elif self.cell_state_space[i-1][self.counter] == 1 and self.cell_state_space[self.counter][i+1] == 0:
                    self.cell_state_space[i][self.counter+1] = 0
                elif self.cell_state_space[i-1][self.counter] == 0 and self.cell_state_space[self.counter][i+1] == 1:
                    self.cell_state_space[i][self.counter + 1] = 1
                else:
                    self.cell_state_space[i][self.counter + 1] = 1

    return self.cell_state_space
