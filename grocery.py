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
     user_input = input()

     # split every token (string of consecutive non-whitespaces)
     # user_input[0] is the command the user gave, followed by the parameters
     user_input = user_input.split()
     command = user_input[0]

     if command == "a" or command == "add":      # a or add command
          
          # get the price, checking for error
          price = 0.0
          valid_price = True
          try:
               price = float(user_input[1])
          except ValueError as e:
               print("Error: Invalid input for \'add\' command (see \'help\' for details)")
               valid_price = False
          
          if valid_price:
               # get the initials, which can be many tokens long
               initials = ""
               for i in range(2, len(user_input)):
                    initials += user_input[i]
               initials = clean_initials(initials)

               # create a new entry in the grocery manager
               entry_id = groc_man.new_entry(price, initials)

               # confirm the entry, printing its id for reference
               print("ID#{}\t{} {}".format(entry_id, price, initials))

     elif command == "d" or command == "delete" or command == "drop":       # d or delete/drop command

          # delete entry here
          pass
     
     elif command == "r" or command == "receipt":           # r or receipt command

          # print all active non-deleted entries and current subtotals
          pass

     elif command == "h" or command == "help":         # h or help command

          # print all valid commands
          pass 

     elif command == "s" or command == "stop" or command == "e" or command == "exit":          # s or stop or e or exit command

          # exit from the while loop
          pass 

     

# print the results
groc_man.print_data()