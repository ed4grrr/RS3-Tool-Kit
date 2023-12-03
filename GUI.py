import tkinter
from tkinter import Button

import Experience_Calculator
from Output_Entry_Frame import Output_Entry_Frame
from Radio_Option_Frame import Radio_Option_Frame
from User_Entry_Area import User_Entry_Area


class Experience_Lamp_GUI(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.calculator = Experience_Calculator.XP_Item_Calculator()

        self.label = tkinter.Label(text="Edgar Was Here",
                                   foreground="white",  # Set the text color to white
                                   background="black")

        self.temp_storage_for_Output = "test"

        self.user_entry = User_Entry_Area()
        self.output_entry = Output_Entry_Frame()
        self.user_entry.pack()

        radio_options = Radio_Option_Frame()

        row1_button_names = ["Small Prismatic Lamp", "Medium Prismatic Lamp","Large Prismatic Lamp","Huge Prismatic Lamp",
                            "Giant Prismatic Lamp"]
        row2_button_names = ["Small Prismatic Fallen Star","Medium Prismatic Fallen Star","Large Prismatic Fallen Star",
                             "Huge Prismatic Fallen Star","Giant Prismatic Fallen Star"]
        for i in range(2):
            radio_options.add_a_row()

        for name in row1_button_names:
            radio_options.add_a_dial(0,name)

        for name in row2_button_names:
            radio_options.add_a_dial(1,name)

        radio_options.pack_radios()

        radio_options.pack()

        self.button = Button(
            command=lambda
                text=self.temp_storage_for_Output:
            self.output_entry.edit_disabled_text_box((text)))

        self.label.pack()
        self.output_entry.pack(side=tkinter.RIGHT)
        self.button.pack()

        self.mainloop()


if __name__ == "__main__":
    test = Experience_Lamp_GUI()
