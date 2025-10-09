# 1. CLI App (command line interface)
# 2. Select recipes from a list
#    read the ingredients
#    (key - ingredient, value - measurement)
# 3. want to be able to add groceries to a shopping list
#    based on the recipe
# 4. store each recipe in a json file
# 5. use io to read files

import os
import json
from pprint import pp

class RecipeApp:
    def __init__(self):
        self.all_file_names = []
        self.file_path = "./recipes_json"
        self.recipes = dict()
        self.shopping_list = dict()
        self.recipe_names = []
        self.load_recipes()

    def load_recipes(self):
        all_file_names = os.listdir(self.file_path)

        # go through all files in the folder
        for recipe in all_file_names:
            full_path = os.path.join(self.file_path,recipe)

            recipe_name = recipe.replace("_", " ")
            recipe_name = recipe_name.split(".")[0].title()
            #if this is a file, then add it to a list
            if os.path.isfile(full_path):
                #self.files.append(recipe)
                try:
                    with open(full_path, 'r') as file:
                        self.recipes[recipe_name] = json.load(file)
                except FileNotFoundError:
                    print("we could not find the file")

            self.recipe_names = list(self.recipes.keys())
        #pp(self.recipes)

    def display_menu(self):
        print("Recipes in Book")
        for index, recipe in enumerate(self.recipe_names, 1):
            print(f"{index} {recipe}")
        print()

    def display_recipe(self, recipe_name:str):
        print(f"\nIngredients for {recipe_name} \n")
        for ingredient, measurement in self.recipes[recipe_name].items():
            print(f"{measurement} {ingredient}")

        print("\nB - Back to Main Menu")
        print("A - Add to Shopping List")

        user_input = input("What would you like to do next? ")

        match(user_input.capitalize()):
            case "A":
                self.add_to_shopping_list()
            case "B":
                #todo
                pass

    def add_to_shopping_list(self):
        print("Now we have to add something to the list")

        print("Added to shopping list. Heading back to the main menu")


app = RecipeApp()

user_input = ""

while user_input != "0":
    app.display_menu()
    user_input= input("Please select an option: ")
    app.display_recipe(app.recipe_names[0])







