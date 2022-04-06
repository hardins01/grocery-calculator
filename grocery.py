# import the grocery_manager class from the other file
from grocery_manager import Grocery_Manager

# the initials that represent each person in the grocery calculator
INITIALS = "slb"

# create the grocery_manager
groc_man = Grocery_Manager(INITIALS)

# the main control loop of the program
while 1:
     
     # get the user's input
     print(": ", end="")
     command = input()

     # check if the command is the stop command
     if command == "stop":
          break

     # separate command into the necessary components (price and initials)
     split_command = command.split()

     # create a new entry in the grocery manager
     groc_man.new_entry(float(split_command[0]), split_command[1])

# print the results
groc_man.print_data()