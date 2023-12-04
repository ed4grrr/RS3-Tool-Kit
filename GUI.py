import tkinter
from tkinter import Button

import Experience_Calculator
from Output_Entry_Frame import Output_Entry_Frame
from Dropdown_Menu_Frame import Dropdown_Menu_Frame
from User_Entry_Area import User_Entry_Area


class Experience_Lamp_GUI(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.config(bg="black")
        self.option_add("*Background", "black")
        self.option_add("*Foreground", "white")
        self.calculator = Experience_Calculator.XP_Item_Calculator()



        self.temp_storage_for_Output = "test"

        self.user_entry = User_Entry_Area()
        self.output_entry = Output_Entry_Frame()
        self.user_entry.pack()





        row_button_names = ["Small Prismatic Lamp", "Medium Prismatic Lamp","Large Prismatic Lamp","Huge Prismatic Lamp",
                            "Giant Prismatic Lamp","Small Prismatic Fallen Star","Medium Prismatic Fallen Star","Large Prismatic Fallen Star",
                             "Huge Prismatic Fallen Star","Giant Prismatic Fallen Star"]


        self.button = Button(
            command=lambda
                text=self.temp_storage_for_Output:
            self.output_entry.edit_disabled_text_box((text)))

        self.options = Dropdown_Menu_Frame(*row_button_names,row_button_names[0])
        self.options.pack()

        self.output_entry.pack(side=tkinter.RIGHT)
        self.button.pack()

        self.mainloop()

    def calculate_items(self):

        self.temp_storage_for_Output = self.calculator.determine_xp_items_required(self.user_entry.


if __name__ == "__main__":
    test = Experience_Lamp_GUI()
