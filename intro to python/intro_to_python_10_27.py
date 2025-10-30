# string, int, float, boolean

title = "Surf's Up" # text, whitespace, special characters
whole_number = 10_000_000 # int
protein = 13.2 # float, floating point number
is_tired = True

if not is_tired:
    print("Go to sleep")

# list, set, typle

# list - ordered, indexable, mutable, allow duplicates
flowers = ["rose", "dahlia", "sunflower"]

# print(flowers[2]) #ordered, indexable
flowers.append("rose")
flowers.append("cosmos")
# print(flowers)

# list[start:end:increment]
concatenate_example = "hi" + "my" + "name" + "is" + "henry"
# print(concatenate_example)

# tuple - ordered, indexable, not mutable, allow duplicates
scents = ("fabuloso", "jasmine", "lavender", "woody")

# print(scents[1])

# set - not ordered, not indexable, mutable,
cartoons = {"mickey", "buttercup", "johnny bravo"}

# print(cartoons)
#
# if "mickey" in cartoons:
#     print("where's minnie")


signs = {"leo": "soda",
         "capricorn": "water",
         "scorpio":"coffee",
         "virgo":"wine",
         "sagitarius": "pumpkin spice latte"}

# for sign, drink in signs.items():
#     print(f"{sign} likes to drink {drink}")















