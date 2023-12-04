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

        self.target_experience_label = Label(master=self, text="Target Experience:")
        self.target_experience_label.pack()
        self.target_experience_entry = Entry(master=self)
        self.target_experience_entry.pack()




        self.level_label = Label(master=self, text="Level:")
        self.level_label.pack()
        self.level_entry = Entry(master=self)
        self.level_entry.pack()

        self.target_level_label = Label(master=self, text="Target Level:")
        self.target_level_label.pack()
        self.target_level_entry = Entry(master=self)
        self.target_level_entry.pack()

    def return_username(self):
        return self.user_name_entry.get()
    def return_level(self):
        return self.level_entry.get()
    def return_experience(self):
        return self.experience_entry.get()

    def reutrn_target_return_level(self):
        return self.target_level_entry.get()
    def return_target_return_experience(self):
        return self.target_experience_entry.get()
