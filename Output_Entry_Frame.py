import tkinter
from tkinter import Frame,Label,Entry,Text,Button,LEFT,RIGHT,END

class Output_Entry_Frame(Frame):
    def __init__(self):
        super().__init__()

        self.Output = tkinter.Text(height=20,
                      width=50,
                      bg="black",
                      fg='white',
                      state="disabled")
        self.Output.pack()

    def edit_disabled_text_box(self,text):
        self.Output.config(state="normal")
        self.Output.delete(1.0,END)
        self.Output.insert(1.0,text)
        self.Output.config(state="disabled")