# import the grocery_manager class from the other file
from grocery_manager import Grocery_Manager, clean_initials

# the initials that represent each person in the grocery calculator
INITIALS = "slb"

# create the grocery_manager
groc_man = Grocery_Manager(INITIALS)

# the main control loop of the program
while 1:
     
     # get the user's input
     print("> ", end="")
     command = input()

     # check if the command is the stop command
     if command == "stop":
          break

     # remove all extra whitespaces from command, leaving everything to be separated by a single space
     command = " ".join(command.split())

     # search for the first space in the command and split it between the price and the initials
     space_idx = command.find(" ")
     price = float (command[:space_idx])
     initials = clean_initials(command[space_idx:])

     # create a new entry in the grocery manager
     entry_id = groc_man.new_entry(price, initials)

     # confirm the entry, printing its id for reference
     print("ID#{}\t{} {}".format(entry_id, price, initials))

# print the results
groc_man.print_data()