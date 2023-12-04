
# Your data
from InvalidLevelException import InvalidLevelException
from InvalidExperienceException import InvalidExperienceException
from UsefulLists import MEDIUM_PRISMATIC_LAMP_XP, REGULAR_SKILL_LEVELS, ELITE_LEVEL_SKILLS, \
    MEDIUM_PRISMATIC_FALLEN_STAR_XP


class XP_Item_Calculator:

    def __init__(self):
        pass


    def find_level_given_experience(self,skill_dict, xp):     # more accurate than using just level
        """
        find a level based on giving a specific xp amount.

        :param skill_dict: an orderedDict that contains the level(int):minimum(int) experience for that level.
        :param xp: an int that is the current xp in the skill in question
        :return: an int that represents the level based on the amount of xp
        """
        previous_level = 0
        for level in skill_dict.keys():
            if skill_dict[level] < xp:
                previous_level +=1
                continue
            elif skill_dict[level] == xp:
                return level
            else:
                return previous_level

    def find_minimum_xp_given_level(self,skill_dict, level): # less accurate than using xp
        """
        Find the minimum xp required for a level, given the level.

        :param skill_dict: an orderedDict that contains the level(int):minimum(int) experience for that level.
        :param level: an int that represents the current level of the skill in question
        :return: an int that represents the minimum amount of xp per the given level
        """

        return skill_dict[level]


    def validate_level(self,level, is_elite):
        """
        takes a given level and validates that the number is a valid level for that skill or returns the string "Max" if
        maxed.

        :param level:  int that is the current level to be validated
        :param is_elite: boolean that describes whether this is an elite skill or not
        :return: the level given in the params if correct. raises exception otherwise
        :raises: ValueError: not a number or Max, InvalidLevelException: number is not a valid level
        """
        if type(level) is int:
            if not is_elite:
                return self.check_to_see_if_levels_are_in_a_valid_range(level, 127, 0)
            else:
                return self.check_to_see_if_levels_are_in_a_valid_range(level, 151, 0)
        else:
            if type(level) is str and level.to_lower() == "max":
                return "Max"
            else:
                correct_level_range = "1-126" if not is_elite else "1-150"
                raise ValueError(f"{level} is not within the acceptable range of {correct_level_range} or the value 'Max'")


    def check_to_see_if_levels_are_in_a_valid_range(self,level, max, min):
        """
        this is used to shorten code. this is the main comparison logic for assuring the level is within a valid range.

        :param level: int the level in a skill
        :param max: int the max level for that skill
        :param min: int the min level for that skill
        :return:the supplied level if it is valid, otherwise raises an exception
        :raises:InvalidLevelException: the level is outside the acceptable range of levels for that skill
        """
        if min < level < max:
            return level
        else:
            raise InvalidLevelException(f'{level} is not within the acceptable range of {min} and {max}')

    def validate_experience(self,xp):
        """
        Makes sure that a given xp value is within the acceptable range of 0-200,000,000 experience

        :param xp:
        :return:
        """
        if type(xp) is int:
            if -1 < xp < 200000000:
                return xp
            else:
                raise InvalidExperienceException(f"{xp} is not within the valid range of 0-200,000,000")
        else:
            raise ValueError(f"{xp} is not a valid integer")

    def determine_level_xp(self,skills_dict, experience, level):
        """
        a CYA function to assure the calculator has both level and experience to work from.
        especially useful when the user provides only half or no data. USE ONLY AFTER
        VALIDATING WITH CORRESPONDING VALIDATE FUNCTION

        :param skills_dict: an orderedDict that contains the level(int):minimum(int) experience for that level.
        :param experience: an int that describes the experience amount in the skill in question
        :param level: an int that describes the level in the skill in question
        :return: two ints, current_level and current_experience based on the given info from the user
        """
        current_level =1
        current_experience = 0
        if level == "":
            # experience used, more accurate
            current_level = self.find_level_given_experience(skills_dict, experience)
            current_experience = experience
        elif experience =="":
            # level used, less accurate
            current_experience = self.find_minimum_xp_given_level(skills_dict, level)
            current_level = level
        return current_level,current_experience

    def determine_xp_items_required(self,tar_xp,target_level,level,experience,skill,item_xp_levels):
        """
        used to determine the amount of experience items needed to reach a certain experience amount

        :param tar_xp: int representing the target xp
        :param tar_level: int representing the target level
        :param level: int representing the current level
        :param experience: int representing the current experience
        :param skill: str used to determine if an elite skill is chosen
        :param item_xp_levels: orderedDict that contains level:"experience granted that level" pairs
        :return: str describing the amount needed
        """

        if skill != "Invention":
            current_skill_levels = REGULAR_SKILL_LEVELS
        else:
            current_skill_levels = ELITE_LEVEL_SKILLS

        current_level,current_experience=self.determine_level_xp(current_skill_levels,experience,level)

        missing_experience = tar_xp - current_experience

        number_required,xp_gained=self.count_xp_items(current_level,current_experience,tar_xp,current_skill_levels,item_xp_levels)


        return number_required,xp_gained,missing_experience,xp_gained-missing_experience


    def count_xp_items(self,current_level, current_experience, target_xp, skill_dict, item_xp_dict):
        """
            used to determine the specific amount of experience items (like xp lamps, stars, etc) required to go from the
            current experience to a target level of experience

        :param current_level: int representing the current level of the skill
        :param current_experience: int representing the current xp in a skill
        :param target_xp: int the target amount of xp the user want's to reach
        :param skill_dict: an orderedDict that has "Level:minimum experience for that level" pairs
        :param item_xp_dict: an orderedDict that has "level:experience granted" pairs for the requested item
        :return: int that represent number of xp items required, float that represent xp
        """
        xp = current_experience
        xp_gained = 0
        curr_level = current_level
        number_of_xp_items = 0
        while xp < target_xp:
            while xp < skill_dict[curr_level + 1]:

                xp +=item_xp_dict[curr_level]
                xp_gained +=item_xp_dict[curr_level]

                number_of_xp_items +=1
            curr_level = self.find_level_given_experience(skill_dict, xp)

        return number_of_xp_items,xp_gained



if __name__ == "__main__":
    # print(len(data["experience"]))
    # print(len(data["level"]))

    """number_required, xp_gained, missing_experience, xp_gained_missing_experience = determine_xp_items_required(
        self.find_minimum_xp_given_level(REGULAR_SKILL_LEVELS, 92), "", 5910258, "aGILITY", MEDIUM_PRISMATIC_LAMP_XP)

    print(
        f"you need {number_required} items and will gain {xp_gained:,}. you needed this {missing_experience}\nYou will"
        f" overshoot by {xp_gained_missing_experience}")
"""

