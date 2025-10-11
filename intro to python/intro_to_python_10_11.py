
cat = "Rocket" # string - text
number_of_pancakes = 10 # int
temperature = 109.5 # floating point number
is_cold =True


# if is_cold:
#     print("The water is cold")

count = 5

# while count > 0:
#     print(f"Take a deep breath {count}")
#     count -= 1

# for each in range(count):
#     print(each)



# list - ordered, indexable, mutable, allow duplicates
# fruits = ["mango", "strawberry", "peach", "blackberries"]
# fruits.append("pears")
# fruits.remove("peach")
# print(fruits)
#
# fruits.insert(1, "pineapple")
# print(fruits)

fruit = "pineapple"

# for letter in fruit:
#     print(letter)

# fruit[start(inclusive):end(exclusive:increment]

print(fruit[:4])
print(fruit[0:4] + " " + fruit[4:])


import logging

# Configure basic logging (e.g., to a file)
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Get a logger instance
logger = logging.getLogger(__name__)

logger.debug("This is a debug message.")
logger.info("Application started successfully.")
logger.warning("Configuration file not found, using default settings.")
logger.error("Failed to connect to the database.")
logger.critical("System shutdown imminent due to critical error.")






