import tkinter
from tkinter import Frame,Label,Entry,Text,Button,LEFT,RIGHT


class User_Entry_Area(Frame):
    def __init__(self):
        super().__init__()


        self.user_name_frame = Frame(self)
        self.user_name_label = Label(master=self.user_name_frame, text="Username:")
        self.user_name_label.pack()
        self.user_name_entry = Entry(master=self.user_name_frame)
        self.user_name_entry.pack()

        self.experience_frame = Frame(self)
        self.experience_label = Label(master=self.experience_frame, text="Experience:")
        self.experience_label.pack()
        self.experience_entry = Entry(master=self.experience_frame)
        self.experience_entry.pack()

        self.level_frame = Frame(self)
        self.level_label = Label(master=self.level_frame, text="Level:")
        self.level_label.pack()
        self.level_entry = Entry(master=self.level_frame)
        self.level_entry.pack()

        self.target_experience_frame = Frame(self)
        self.target_experience_label = Label(master=self.target_experience_frame, text="Target Experience:")
        self.target_experience_label.pack()
        self.target_experience_entry = Entry(master=self.target_experience_frame)
        self.target_experience_entry.pack()




        self.target_level_frame = Frame(self)
        self.target_level_label = Label(master=self.target_level_frame, text="Target Level:")
        self.target_level_label.pack()
        self.target_level_entry = Entry(master=self.target_level_frame)
        self.target_level_entry.pack()

        self.user_name_frame.pack(side=LEFT)
        self.level_frame.pack(side=LEFT)
        self.experience_frame.pack(side=LEFT)
        self.target_level_frame.pack(side=LEFT)
        self.target_experience_frame.pack(side=LEFT)



    def return_username(self):
        returnable = self.user_name_entry.get()
        if returnable == "":
            return 0
        else:
            return returnable
    def return_level(self):
        returnable = self.level_entry.get()
        if returnable == "":
            return 0
        else:
            return returnable
    def return_experience(self):
        returnable = self.experience_entry.get()
        if returnable == "":
            return 0
        else:
            return returnable
    def reutrn_target_level(self):
        returnable = self.target_level_entry.get()
        if returnable == "":
            return 0
        else:
            return returnable
    def return_target_experience(self):
        returnable = self.target_experience_entry.get()
        if returnable == "":
            return 0
        else:
            return returnable
