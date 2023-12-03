import tkinter
from tkinter import Frame,Label,Entry,Text,Button,LEFT,RIGHT,Radiobutton



class Radio_Option_Frame(Frame):

    def __init__(self):
        super().__init__()
        self.list_of_list_of_options =[]

    def add_a_row(self):
        self.list_of_list_of_options.append([])

    def add_a_dial(self,row,name):
        radio = Radiobutton(self, text=name)
        self.list_of_list_of_options[row].append(radio)

    def pack_radios(self):
        for list_of_radio_buttons in self.list_of_list_of_options:
            for radio_button in list_of_radio_buttons:
                radio_button.pack(side=LEFT)
