import time
from Rules import *
from Initiation import *
from Widgets import *

class GameOfLife():

    def __init__(self):

        self.root = Tk()
        self.root.title('Game of Life')
        self.root.resizable(1000, 1000)

        self.frame = LabelFrame(self.root, text='')
        self.frame.grid(row=0, column=0, sticky='WE', columnspan=1)

        create_widgets(self)

    def startClicked(self):

        self.cell_size = int(self.entry_cell_size.get())
        self.canvas_height = int(self.entry_height.get())
        self.canvas_width = int(self.entry_width.get())
        self.rule_chosen = self.rule_values[self.rule.get()]

        self.window = Toplevel(self.root)
        self.window.title('Here\'s the game!')

        self.canvas = Canvas(self.window, height=self.canvas_height, width=self.canvas_width, border=0)
        self.canvas.grid(row=1, column=0, sticky='WE', columnspan=5)

        def stop():

            self.window.destroy()

        stopButton = Button(self.window, text='Stop the Game', command=stop, width=self.width)
        stopButton.grid(row=0, column=2, sticky='WE')

        for child in self.window.winfo_children():
            child.grid_configure(padx=4, pady=4)

        initiate_cell_space(self)
        draw_square_cells(self)

        if self.rule.get() is not 'Rule 30':
            while True:
                neighbour_state(self)
                globals()[self.rule_chosen](self)
                draw_square_cells(self)
                time.sleep(0.1)
        else:
            self.counter = 0
            while True:
                globals()[self.rule_chosen](self)
                self.counter += 1
                draw_square_cells(self)
                time.sleep(0.4)

    def run(self):

        self.root.mainloop()

    def _quit(self):

        self.root.quit()
        self.root.destroy()
        exit()

if __name__ == '__main__':
    app = GameOfLife()
    app.run()
