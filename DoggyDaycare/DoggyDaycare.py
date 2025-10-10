
"""I want to create a scheduling app for a doggy daycare
at any given time, there will be a limit of the number of dogs at the daycare

you can schedule a time to bring your dog for x number of hours
you can only schedule a time with 30 min increments

add dog to schedule
check number of dogs at a time of day
suggest open time slots
create a new dog customer
store time in a data set which closes off the allocated time"""


# pandas.date_range

from datetime import time

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

class Schedule:
    def __init__(self):
        self.timeslots = {}
        self.create_timeslots()
        self.limit = 15
        self.dogs = []

    def create_timeslots(self):
        """this will load all timeslots with no dogs"""
        for hour in range(6,18):
            for minute in range(0,2):
                timeslot = time(hour, minute * 30, 0).isoformat("minutes")
                self.timeslots[timeslot] = {}

        # print(self.timeslots)

    def add_dog(self):
        """this will create a new dog object"""
        name = input("\nWhat is the dog's name? ")
        age = input(f"What is {name}'s age? ")
        breed = input(f"What is {name}'s breed? ")

        print("\nAdd a new dog to the roster:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Breed: {breed}")

        confirm = input("\nPlease confirm the information provided: (Y/N) ").capitalize()

        if confirm == "Y":
            self.dogs.append(Dog(name, age, breed))
            self.display_menu()
        else:
            self.add_dog()

    def schedule_timeslot(self):
        """this will schedule a timeslot for a dog at a certain time"""
        for option, dog in enumerate(self.dogs,1):
            print(f"{option}. {dog.name}")

        input("Please select your dog: ")

    def display_menu(self):
        """this will display the menu"""
        print("\nWelcome to DoggyDaycare!")
        print("1. View all timeslots")
        print("2. Add a dog\n")

        match(input("Please select an option: ")):
            case "1":
                self.display_timeslots()
            case "2":
                self.add_dog()

    def display_timeslots(self):
        """this will display the timeslots available"""
        for timeslot, dogs in self.timeslots.items():
            start_time = ""
            count = -1
            if len(dogs) < self.limit:
                if count != len(dogs):
                    print(f"{timeslot}: {self.limit- len(dogs)} spaces available")
                start_time = self.timeslot


schedule = Schedule()
schedule.display_menu()
