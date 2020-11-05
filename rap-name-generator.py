# Guided Exploration No. 3
# Stoney Stone

# random library
import random

# empty list
possible_names = []

# create output file to write
outputFile = open('rap-names-output.txt', 'a')

# open as datafile to work on it
with open('rap-names.txt', 'r') as dataFile:
    # loop through file
    for name in dataFile:
        # put names into list
        possible_names.append(name.rstrip())

# get how many times
count = int(input('How many rap names would you like to create? '))
# get parts
parts = int(input('How many parts should the name contain? '))

# use count to loop names
for i in range(count):
    # open new list
    name_parts = []
    # pick parts for names
    for j in range(parts):
        # add parts together at random
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
    # put names into file
    outputFile.write(f"{' '.join(name_parts)}\n")
    # join then parts and print out
    print(f"{' '.join(name_parts)}")

# close the door on the way out
outputFile.close()
