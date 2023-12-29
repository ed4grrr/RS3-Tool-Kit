from tkinter import Menu,Frame, messagebox


class File_bar(Frame):

    def __init__(self, Master, **kw):
        super().__init__(**kw)
        menu_bar = Menu(master=Master, tearoff=0)
        file_menu = Menu(menu_bar,tearoff=0)
        file_menu.add_command(label = "Open", command=self.pass_me)
        file_menu.add_command(label = "Save", command=None)
        menu_bar.add_cascade(menu=file_menu,label="File")
        help_menu = Menu(menu_bar,tearoff=0)
        help_menu.add_command(label = "User Guide", command=self.display_help)
        menu_bar.add_cascade(menu=help_menu,label="Help")
        Master.config(menu=menu_bar)



    def pass_me(self):
        pass

    def display_help(self):
        # todo create a user guide
        messagebox.showinfo("Help","FILL OUT HELP")