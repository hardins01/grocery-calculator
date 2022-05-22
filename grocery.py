# import the grocery_manager class from the other file
from grocery_manager import Grocery_Manager
from config import INITIALS, CREDENTIALS
import json
import os
from venmo_api import Client


def main():
     # create the grocery_manager
     groc_man = Grocery_Manager(INITIALS)

     # define all valid versions of each command
     add_commands = ["a", "add"]
     delete_commands = ["d", "drop", "delete"]
     receipt_commands = ["r", "receipt", "ls"]
     help_commands = ["h", "help"]
     quit_commands = ["s", "stop", "e", "exit", "q", "quit"]
     confirmation_commands = ["y", "yes", "n", "no"]
     venmo_commands = ["v", "venmo"]


     # print the introduction message
     print("Hello, Welcome to Grocery-Calculator!         By Sebastian Hardin")
     print("Enter 'h' or 'help' for a list of valid commands")


     # the main control loop of the program
     keep_looping = True
     while keep_looping:
          
          # get the user's input
          print("> ", end="")
          user_input = input()

          # split every token (string of consecutive non-whitespaces)
          # user_input[0] is the command the user gave, followed by the parameters
          user_input = user_input.split()
          command = user_input[0]

          if command in add_commands:      # a or add command
               
               # check the number of parameters
               if len(user_input) < 3:
                    print("Error: invalid input for 'add' command (see 'help' for details)")
               else:
                    # get the price, checking for error
                    price = 0.0
                    valid_price = True
                    try:
                         price = float(user_input[1])
                    except ValueError as e:
                         print("Error: invalid input for 'add' command (see 'help' for details)")
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
                              print("Error: invalid initials given")
                         else:
                              # create a new entry in the grocery manager
                              entry_id = groc_man.new_entry(price, initials)

                              # confirm the entry, printing its id for reference
                              print("ID#{}\t$ {} {}".format(entry_id, "{:.2f}".format(price), initials))

          elif command in delete_commands:       # d or delete/drop command

               # check if the next token is "p", "prev", or "previous", in which case drop the most recent entry
               if user_input[1] == "p" or user_input[1] == "prev" or user_input[1] == "previous":
                    
                    # drop the previous entry
                    return_code = groc_man.delete_prev_entry()

                    # check the return code
                    if return_code == 0 or return_code == -1:
                         print("Error: no previous entry to delete")
                    else:
                         print("Success: previous entry has been deleted")
                    
               else:     # the user wants to delete a specific entry

                    # check if the entry id given is valid
                    entry_id = 0
                    valid_id = True
                    try:
                         entry_id = int(user_input[1])
                    except ValueError as e:
                         print("Error: invalid input for 'delete'/'drop' command (see 'help' for details)")
                         valid_id = False
                    
                    # continue on if the given id is an integer
                    if valid_id:
                         return_code = groc_man.delete_entry(entry_id)

                         # check the return code
                         if return_code == 0:
                              print("Error: entry id given is outside the valid range of entry id's")
                         elif return_code == -1:
                              print("Error: entry has already been deleted")
                         else:
                              print("Success: entry ID#{} has been deleted".format(entry_id))


          
          elif command in receipt_commands:           # r or receipt or ls command

               # validate the rest of the input is valid
               if len(user_input) != 1:
                    print("Error: invalid input for 'r'/'ls'/'receipt' command (see 'help' for details)")
               else:
                    # print all active non-deleted entries and current subtotals
                    groc_man.print_status()

          elif command in help_commands:         # h or help command

               # print all valid commands
               print(
                    "\n"\
                    "\t\tAll valid commands for Grocery-Calculator:\n\n\n"\
                    "\ta / add : Add a new item to the grocery run\n\n"\
                    "\t\t> { a | add } PRICE INITIALS\n\n"\
                    "\t\tPRICE = the price of the item, must be convertable to a float\n"\
                    "\t\tINITIALS = the initials of the people paying for this item\n"\
                    "\t\t\tnote: an initial can appear multiple times to achieve the desired ratio of cost per person\n\n"\
                    "\tr / receipt / ls : Print the currently active items, along with everyone's subtotals\n\n"\
                    "\t\t> { r | ls | receipt }\n\n"\
                    "\td / drop / delete : Delete a specific item or the most recently added active item\n\n"\
                    "\t\t> { d | drop | delete } { ENTRY_ID | { p | prev | previous } }\n\n"\
                    "\t\tENTRY_ID = the id of the item to be deleted, must be a valid id that hasn't already been deleted\n\n"\
                    "\tq / quit / s / stop / e / exit : Exit the program, printing everyone's totals that they owe, and optionally initiate Venmo transactions\n\n"\
                    "\t\t> { q | s | e | quit | stop | exit } [{ v | venmo }]\n\n"\
                    "\th / help : Bring up this menu, a list of all available commands to use\n\n"\
                    "\t\t> { h | help }\n\n"
               )

          elif command in quit_commands:          # s or stop or e or exit or q or quit command

               # check if the user wants to end usage with venmo transaction(s)
               if len(user_input) == 1:
                    confirmation = ""
                    groc_man.print_results(False)
                    while confirmation not in confirmation_commands:
                         print("Are you sure you want to stop running Grocery-Calculator, confirming the above totals?")
                         print("(y/n) > ", end="")
                         confirmation = input()
                         if confirmation not in confirmation_commands:
                              print("Invalid input, must be 'y', 'yes', 'n', or 'no'")
                    
                    # exit the main control loop if the user wants to be done (just keep going as normal otherwise)
                    if confirmation == "y" or confirmation == "yes":
                         keep_looping = False

               else:
                    if user_input[1] in venmo_commands:
                         confirmation = ""
                         groc_man.print_results(False)
                         while confirmation not in confirmation_commands:
                              print("Are you sure you want to stop running Grocery-Calculator, confirming the above totals and initiating Venmo requests?")
                              print("(y/n) > ", end="")
                              confirmation = input()
                              if confirmation not in confirmation_commands:
                                   print("Invalid input, must be 'y', 'yes', 'n', or 'no'")

                         # initiate venmo actions if the user said yes
                         if confirmation == "y" or confirmation == "yes":
                              payer = " "
                              while payer not in INITIALS:
                                   print("Who paid at the grocery store? Your response MUST be one of the initials provided in config.py")
                                   print("> ", end="")
                                   payer = input()
                                   if len(payer) != 1 or payer not in INITIALS:
                                        print("Invalid input, must be one of the people provided in config.py")
                              
                              # check if credentials have been generated (access_tokens.json isn't empty)
                              if os.stat("access_tokens.json").st_size == 0:
                                   print("Error: credentials not found, please generate them with    python config.py venmo-init")
                              else:
                                   # prep for venmo logic
                                   print()
                                   payer_index = INITIALS.find(payer)
                                   payer_username = CREDENTIALS[payer_index][0]
                                   tokens = []
                                   with open("access_tokens.json", "r") as token_file:
                                        tokens = json.load(token_file)
                                   payer_access_token = tokens[payer_username]

                                   # if the payer didn't provide credentials, then the others will pay them
                                   if payer_access_token == "":
                                        for ower in INITIALS:
                                             if ower != payer:
                                                  ower_index = INITIALS.find(ower)
                                                  ower_username = CREDENTIALS[ower_index][0]
                                                  ower_access_token = tokens[ower_username]
                                                  owed_amount = groc_man.get_subtotal(ower)
                                                  if owed_amount == 0:
                                                       print("{} owes $0, so no payment was made".format(ower_username))
                                                  elif ower_access_token == "":
                                                       print("No access token provided for {}, cannot complete that transaction".format(ower_username))
                                                  else:
                                                       # complete a payment on behalf of the owner to the payer
                                                       client = Client(ower_access_token)
                                                       users = client.user.search_for_users(query=payer_username)
                                                       for user in users:
                                                            if user.username == payer_username:
                                                                 print("Paying {} ${:.2f} from {}'s account with their default payment method".format(payer_username, owed_amount, ower_username))
                                                                 client.payment.send_money(amount=owed_amount, note="Groceries", target_user_id=user.id)
                                                                 break
                                   else:
                                        # the payer did give credentials, so complete requests on their behalf
                                        for ower in INITIALS:
                                             if ower != payer:
                                                  ower_index = INITIALS.find(ower)
                                                  ower_username = CREDENTIALS[ower_index][0]
                                                  owed_amount = groc_man.get_subtotal(ower)
                                                  if owed_amount == 0:
                                                       print("{} owes $0, so no request was made".format(ower_username))
                                                  else:
                                                       client = Client(payer_access_token)
                                                       users = client.user.search_for_users(query=ower_username)
                                                       for user in users:
                                                            if user.username == ower_username:
                                                                 print("Requesting ${:.2f} from {} on behalf of {}".format(owed_amount, ower_username, payer_username))
                                                                 client.payment.request_money(amount=owed_amount, note="Groceries", target_user_id=user.id)
                                                                 break
                              keep_looping = False

                    else:
                         print("Error: invalid input for 'quit'/'stop'/'exit' command (see 'help' for details)")

          else:

               # tell the user their input was invalid
               print("Error: command '{}' not found (see 'help' for details)".format(command))
          

     # print the results
     print("")
     groc_man.print_results(True)
     print("\nThank you for using Grocery-Calculator!")


if __name__ == "__main__":
     main()
