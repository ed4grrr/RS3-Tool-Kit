import tkinter
from tkinter import Frame,Label,Entry,Text,Button,LEFT,RIGHT,Radiobutton



class Dropdown_Menu_Frame(Frame):

    def __init__(self,starting_string,*row_button_names ):
        super().__init__()
        self.item_selected = tkinter.StringVar()
        self.options_box = tkinter.OptionMenu(self, self.item_selected, *row_button_names)
        self.item_selected.set(starting_string)
        self.options_box.pack()

    def return_item_selected(self):
        return self.item_selected.get()
