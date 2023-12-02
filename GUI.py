import tkinter
import Experience_Calculator

class Experience_Lamp_GUI(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.label = tkinter.Label(text="Edgar Was Here",    foreground="white",  # Set the text color to white
    background="black")
        self.Output = tkinter.Text(height=5,
                      width=25,
                      bg="light cyan",
                      state="disabled")

        self.user_name_label = tkinter.Label(text="Username")
        self.user_name_label.pack(side = tkinter.LEFT)
        self.user_name_entry = tkinter.Entry()
        self.user_name_entry.pack(side = tkinter.RIGHT)

        self.button = tkinter.Button(Command=self.edit_disabled_text_box(self.Output,"hello"))
        self.Output.insert("insert","edgar")
        self.label.pack()
        self.Output.pack()
        self.button.pack()

        self.mainloop()
    def edit_disabled_text_box(self,textbox,text):
        textbox.config(state="normal")
        textbox.insert('1.0',text)
        textbox.config(state="disabled")

if __name__ == "__main__":
    test = Experience_Lamp_GUI()
