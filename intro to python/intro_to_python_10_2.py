
# data types, data structures, loops, conditionals

hobby = "gundam building" # string - text
number_of_pieces = 5_000 # int - whole number
cost = 29.99 # float - floating point decimal number
is_difficult = True

# list - ordered, indexable, mutable, allow duplicates
animals = ["cat", "dog", "elephant","wolf","snake", "giraffe", "mouse"]
# print(animals[-1])
# print(len(animals))
#
# animals.sort()
# print(animals[::-1])

animals[0] = "whale"
animals.append("rabbit")
animals.remove("dog")
# del animals[0]
# print(animals)
#
# print(animals[1:5:3])

#turtle - draw using python

# tuples - ordered, indexable, not mutable, allow duplicates
colors = ("blue", "green", "red", "cyan", "pink","magenta")


# akhaia - if you go over loops, could you touch on loops inside of loops?? like while-for and such

double_array = [[1,2,3],
                [4,5,6,8],
                [7,8,9],
                [1,3,5]]

def print_2d_array(array):
    row = 0
    column = 0

    # time complexity O(n^2)
    while row < len(double_array):
        while column < len(double_array[row]):
            print(double_array[row][column], end=" ")
            column += 1
        print()
        row += 1
        column = 0

print_2d_array(double_array)

# DRY - don't repeat yourself
# each method should have one job



