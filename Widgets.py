from Tkinter import *
from ttk import *

def create_widgets(self):

    self.width = 12

    self.label1 = Label(self.frame, text='Enter the width:')
    self.label1.grid(row=0, column=1, sticky='WE')

    self.entry_width = IntVar()
    self.entry1 = Entry(self.frame, textvariable=self.entry_width, width=self.width)
    self.entry1.grid(row=1, column=1, sticky='WE')
    self.entry1.insert(0, '100')

    self.label2 = Label(self.frame, text='Enter the height:')
    self.label2.grid(row=0, column=2, sticky='WE')

    self.entry_height = IntVar()
    self.entry2 = Entry(self.frame, textvariable=self.entry_height, width=self.width)
    self.entry2.grid(row=1, column=2, sticky='WE')
    self.entry2.insert(0, '80')

    self.label3 = Label(self.frame, text='Enter the cell size:')
    self.label3.grid(row=0, column=3, sticky='WE')

    self.entry_cell_size = IntVar()
    self.entry3 = Entry(self.frame, textvariable=self.entry_cell_size, width=self.width)
    self.entry3.grid(row=1, column=3, sticky='WE')
    self.entry3.insert(0, '2')

    self.button1 = Button(self.frame, text='Start the Game!', command=self.startClicked, width=self.width)
    self.button1.grid(row=3, column=2, columnspan=1)

    self.button_quit = Button(self.frame, text='Quit', command=self._quit, width=self.width)
    self.button_quit.grid(row=3, column=3, columnspan=1)

    self.label4 = Label(self.frame, text='Choose the mode:')
    self.label4.grid(row=2, column=1, sticky='WE')

    self.rule = StringVar()
    self.rule_values = {'Conway': 'conway', 'Day + Night': 'day_and_night', 'Morley': 'morley', 'Pure Glider': 'conway',
                        'Diamond': 'conway', 'Gosper\'s gun': 'conway', 'Rule 30': 'rule_30'}

    self.ruleList = Combobox(self.frame, textvariable=self.rule, width=self.width, values=self.rule_values.keys(),
                             justify='center', state='readonly')
    self.ruleList.grid(row=3, column=1)
    self.ruleList.current(0)

    for child in self.frame.winfo_children():
        child.grid_configure(padx=4, pady=4)



