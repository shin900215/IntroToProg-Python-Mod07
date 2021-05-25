# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Description of Pickling and
#              Structured Error Handling. Textbook example used in order to
#              describe two terms referenced above.
# ChangeLog (Who,When,What):
# CShin,5.24.2021, added and executed code to complete assignment 7
# ------------------------------------------------------------------------ #

# Part 1-1: Pickling Description------------------------------------------ #
# Import pickle
import pickle
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
# "wb" - pickled objects must be stored in a binary file and cannot be
# stored in text file. "wb" writes to a binary file. Below opens the
# "Pickles1.dat" file.
f = open("pickles1.dat", "wb")
# storing the variety and the shape of the pickle using pickle.dump() function
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
# close the file
f.close()

# Part 1-2: Reading data from a file and unpickling it.------------------- #
print("\nUnpickling lists.")
# opens the data file from Part 1-1.
f = open("pickles1.dat", "rb")# "rb" used to read from a binary file.
variety = pickle.load(f)# Loads each variety, shape, and brand of pickle.
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)# Print to see if the process worked
print(shape)
print(brand)
print("\n\n")# two line spacing for the next step: shelving

import shelve #import shelve
#open shelve data file and shelving data
s = shelve.open("pickles2.dat")
s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]
print("print shelved data to see if they are properly shelved")
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])

print("\n\n")

# Part 2: Structured Error Handling.
try:
    UserChoice = input("what do you want to see? (variety, shape, or brand) : ")
    print(s[UserChoice])
except:
    print("Wrong Input! Good Bye!") #Customized notification if value is not correct.

input("Press enter to exit")