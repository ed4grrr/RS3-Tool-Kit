import math
import tkinter
from tkinter import Button, messagebox

import Experience_Calculator
import UsefulLists
from InvalidExperienceException import InvalidExperienceException
from InvalidLevelException import InvalidLevelException
from InvalidUserEntryException import InvalidUserEntryException
from Output_Entry_Frame import Output_Entry_Frame
from Dropdown_Menu_Frame import Dropdown_Menu_Frame
from User_Entry_Area import User_Entry_Area
import RS_USER_HIGHSCORE_API
from UsefulLists import *

class Experience_Lamp_GUI(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.config(bg="black")
        self.option_add("*Background", "black")
        self.option_add("*Foreground", "white")
        self.calculator = Experience_Calculator.XP_Item_Calculator()
        self.is_elite = False
        self.hiscore_api = RS_USER_HIGHSCORE_API.Player_High_Score_API()




        self.temp_storage_for_Output = "test"

        self.user_entry = User_Entry_Area()
        self.output_entry = Output_Entry_Frame()
        self.user_entry.pack()





        row_button_names = ["Small Prismatic Lamp", "Medium Prismatic Lamp","Large Prismatic Lamp","Huge Prismatic Lamp",
                            "Giant Prismatic Lamp","Small Prismatic Fallen Star","Medium Prismatic Fallen Star","Large Prismatic Fallen Star",
                             "Huge Prismatic Fallen Star","Giant Prismatic Fallen Star"]


        self.button = Button( text="Calculate Items Needed",
            command=self.calculate_items)
        self.get_user_data_button = Button( text="Get User Data",
            command=self.get_hiscore_from_api)

        self.options = Dropdown_Menu_Frame(row_button_names[0],*row_button_names)
        self.options.pack()

        self.skill = Dropdown_Menu_Frame(UsefulLists.SKILL_NAMES[0],*UsefulLists.SKILL_NAMES)
        self.skill.pack()

        self.output_entry.pack(side=tkinter.RIGHT)
        self.button.pack()
        self.get_user_data_button.pack()
        self.current_player_data = ""
        self.current_player_name = ""

        self.mainloop()

    def get_hiscore_from_api(self):
        name_from_user = self.user_entry.user_name_entry.get()
        if name_from_user != "" and self.current_player_name != name_from_user:
            temp_data = self.hiscore_api.get_player(name_from_user)

            print(temp_data)
            if temp_data != f"Unfulfilled Request,\nCode: 404\nReason: Not Found":
                self.current_player_name = name_from_user
                self.current_player_data = temp_data
                tkinter.messagebox.showinfo("Success","Retrieval Successful!")
            else:
                tkinter.messagebox.showinfo("Failure", "Username does not exist!")
        else:
            if name_from_user == "":
                tkinter.messagebox.showinfo("Failure","No Username Supplied")
            else:
                tkinter.messagebox.showinfo("Nothing", "User Data already loaded.")
    def calculate_items(self):
        print_test = 0
        try:
            print(f"reached {print_test}")
            print_test +=1
            user_entry_name = self.user_entry.user_name_entry.get()

            user_entry_xp = ""
            if user_entry_name == "":
                print(f"reached {print_test}")
                print_test += 1
                user_entry_xp = self.user_entry.experience_entry.get()
                try:
                    user_entry_xp = int(user_entry_xp)
                    self.calculator.validate_experience(user_entry_xp)

                except ValueError:
                    user_entry_xp = ""
            else:

                print(f"reached {print_test}")
                print_test += 1

                if self.current_player_name == user_entry_name:
                    print(self.current_player_data[self.skill.item_selected][1])
                    user_entry_xp = self.current_player_data[self.skill.item_selected][2]
                else:
                    print(f"reached {print_test}")
                    print_test += 1

                    self.output_entry.edit_disabled_text_box("Update Player Data before Calculating")
                    return

            print(f"reached {print_test}")
            print_test += 1
            """user_entry_level = self.user_entry.level_entry.get()
            try:
                user_entry_level = int(user_entry_level)
                self.calculator.validate_level(is_elite=self.is_elite,level=user_entry_level)
            except ValueError:
                user_entry_level = """""

            user_entry_target_experience = self.user_entry.target_experience_entry.get()
            try:
                user_entry_target_experience = int(user_entry_target_experience)
                self.calculator.validate_experience(user_entry_target_experience)
            except ValueError:
                user_entry_target_experience = ""

            user_entry_target_level = self.user_entry.target_level_entry.get()
            try:
                user_entry_target_level = int(user_entry_target_level)
                self.calculator.validate_level(is_elite=self.is_elite,level=user_entry_target_level)
                if user_entry_target_experience == "":
                    if not self.is_elite:
                        user_entry_target_experience = REGULAR_SKILL_LEVELS[user_entry_target_level]
                    else:
                        user_entry_target_experience = ELITE_LEVEL_SKILLS[user_entry_target_level]
            except ValueError:
                user_entry_target_level = ""

            print(f"reached {print_test}")
            print_test += 1



            if user_entry_xp == "" and user_entry_name == "" or user_entry_target_level == "" and user_entry_target_experience =="":
                self.output_entry.edit_disabled_text_box("All inputs are empty!\nPlease fill in either your user name or current experience"
                                                         " and either target level or target experience.")
                return




            number_required,xp_gained,missing_experience,overshoot = self.calculator.determine_xp_items_required(user_entry_target_experience,
                                                user_entry_target_level,user_entry_xp,self.skill.item_selected,STRING_DICT_DICT[self.options.return_item_selected()])

            self.temp_storage_for_Output = f"You will require {math.ceil( number_required):,} {self.options.return_item_selected()}(s).\nYou need {missing_experience:,} experience " \
                                           f"and you will gain {math.ceil(xp_gained):,} experience.\nTherefore, you will overshoot you goal by about {math.ceil(overshoot):,} experience.\n"
            self.output_entry.edit_disabled_text_box(self.temp_storage_for_Output)
        except InvalidLevelException as e:
            pass
        except InvalidExperienceException as e:
            pass
        except TypeError as e:
            pass


if __name__ == "__main__":
    test = Experience_Lamp_GUI()
