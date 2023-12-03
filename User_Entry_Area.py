import tkinter
from tkinter import Frame,Label,Entry,Text,Button,LEFT,RIGHT


class User_Entry_Area(Frame):
    def __init__(self):
        super().__init__()
        self.user_name_label = Label(master=self, text="Username:")
        self.user_name_label.pack()
        self.user_name_entry = Entry(master=self)
        self.user_name_entry.pack()

        self.experience_label = Label(master=self, text="Experience:")
        self.experience_label.pack()
        self.experience_entry = Entry(master=self)
        self.experience_entry.pack()


        self.level_label = Label(master=self, text="Level:")
        self.level_label.pack()
        self.level_entry = Entry(master=self)
        self.level_entry.pack()
