# import the grocery_manager class from the other file
from grocery_manager import Grocery_Manager

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
          
          # check the number of parameters
          if len(user_input) < 3:
               print("Error: Invalid input for 'add' command (see 'help' for details)")
          else:
               # get the price, checking for error
               price = 0.0
               valid_price = True
               try:
                    price = float(user_input[1])
               except ValueError as e:
                    print("Error: Invalid input for 'add' command (see 'help' for details)")
                    valid_price = False
               
               if valid_price:
                    # get the initials, which can be many tokens long
                    initials = ""
                    for i in range(2, len(user_input)):
                         initials += user_input[i]
                    initials = "".join(initials.split())

                    # verify the initials before attempting the entry
                    valid_initials = groc_man.verify_initials(initials)
                    if valid_initials == 0:
                         print("Error: Invalid initials given")
                    else:
                         # create a new entry in the grocery manager
                         entry_id = groc_man.new_entry(price, initials)

                         # confirm the entry, printing its id for reference
                         print("ID#{}\t{} {}".format(entry_id, price, initials))

     elif command == "d" or command == "delete" or command == "drop":       # d or delete/drop command

          # check if the next token is "p", "prev", or "previous", in which case drop the most recent entry
          if user_input[1] == "p" or user_input[1] == "prev" or user_input[1] == "previous":
               
               # drop the previous entry
               return_code = groc_man.delete_prev_entry()

               # check the return code
               if return_code == 0 or return_code == -1:
                    print("Error: No previous entry to delete")
               else:
                    print("Success: Previous entry has been deleted")
               
          else:     # the user wants to delete a specific entry

               # check if the entry id given is valid
               entry_id = 0
               valid_id = True
               try:
                    entry_id = int(user_input[1])
               except ValueError as e:
                    print("Error: Invalid input for 'delete'/'drop' command (see 'help' for details)")
                    valid_id = False
               
               # continue on if the given id is an integer
               if valid_id:
                    return_code = groc_man.delete_entry(entry_id)

                    # check the return code
                    if return_code == 0:
                         print("Error: Entry id given is outside the valid range of entry id's")
                    elif return_code == -1:
                         print("Error: Entry has already been deleted")
                    else:
                         print("Success: Entry ID#{} has been deleted".format(entry_id))


     
     elif command == "r" or command == "receipt":           # r or receipt command

          # print all active non-deleted entries and current subtotals
          pass

     elif command == "h" or command == "help":         # h or help command

          # print all valid commands
          pass 

     elif command == "s" or command == "stop" or command == "e" or command == "exit":          # s or stop or e or exit command

          # exit from the while loop
          break

     

# print the results
groc_man.print_data()