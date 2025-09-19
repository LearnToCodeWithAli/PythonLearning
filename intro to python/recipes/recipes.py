# What are the requirements?
# 1. CLI app (command line interface)
# 2. want to select recipes from a list
#     and read the ingredients
#     (key - ingredient, value - measurement)
# 3. want to be able to add groceries to a
#    shopping list based on a recipe
# 4. store each recipe in a json file
# 5. use io to read files

# posole, # alfredo.json, pumpkin pie


# try to define ur functions like def(name: str) -> list[str]
# and then when you create docstrings for functions it helps ur code clarity
# im talking about type hints and docstrings (structured comments for functions)
# just fyi pathlib module is a bit more modern way of doing path related things not that os
# if you want to call it statically, you need to put @staticmethod above the function def line
# just want to clarify you have to choose between init, or use @staticmethod

# What are your coding strategies I like DRY

import os
import json

# todo add option to show shopping list and display shopping list
class RecipeBook:

    def __init__(self):
        self.all_entries = None
        self.folder_path = "./recipes_json"
        self.selected_recipe = None
        self.shopping_list = set()

    def go_to_main_menu(self):
        # Replace with the actual path
        self.all_entries = os.listdir(self.folder_path)

        files = []
        for entry in self.all_entries:
            full_path = os.path.join(self.folder_path, entry)
            if os.path.isfile(full_path):
                files.append(entry)

        recipe_names = []

        print("All Recipes")
        for index, file_name in enumerate(files):
            name = file_name.split(".")[0].replace("_", " ")
            capitalized_name = name.title()
            recipe_names.append(capitalized_name)
            print(f"{index + 1} - {capitalized_name}")

    def add_to_shopping_list(self):
        for ingredient, measurement in self.selected_recipe.items():
            self.shopping_list.add(ingredient)

    def select_recipe(self, recipe_index):
        file_name = self.all_entries[recipe_index]
        file_path = os.path.join(self.folder_path, file_name)

        try:
            with open(file_path, 'r') as file:
                self.selected_recipe = json.load(file)
        except FileNotFoundError:
            print("We could not find your file")

        print(f"\nYou selected: {file_name.split(".")[0].title()}")

        for ingredient, measurement in self.selected_recipe.items():
            print(f"{measurement} {ingredient}")

        print("\nB - Back to Main Menu")
        print("A - Add recipe to grocery list")

    # select a recipe
    # display the recipe
    # have an option to add the recipe to
    # the shopping list
    # have an option to go back to the main menu
    # todo add option to display shopping list, and display shopping list


user_input = ""

while user_input != 0:
    recipe_book = RecipeBook()
    recipe_book.go_to_main_menu()
    user_input = int(input("\nPlease select an option: ")) - 1
    recipe_book.select_recipe(user_input)
    user_input = input("\nWhat would you like to do? ")

    match user_input:
        case "A":
            recipe_book.add_to_shopping_list()
        case "B":
            recipe_book.add_to_shopping_list()






































