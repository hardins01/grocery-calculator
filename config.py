# this config file will support the creation of venmo access tokens
from venmo_api import Client
import sys
import json
import os




# the initials that represent each person in the grocery calculator
# edit this string to contain the valid initials for each person involved
# a valid initial is anything except whitespace, but it's suggested to not use numbers to avoid confusion
# capital and lowercase letters are allowed and will be distinguished between, and any other printable special character is allowed as well
# this string cannot contain anything except the unique initials
INITIALS = "xyz"

# the list of venmo credentials
# each entry in the list contains three strings: username (without the @), email, and password
# if full venmo capabilities are wanted, then everyone must provide their usernames and at least one person must provide their email and password
# the list must have the same number of entries as INITIALS
# each entry corresponds to the initial at the same index   i.e. the first set of credentials belongs to the first letter of INITIALS, etc
# a credential can be left blank, but it must be present in the list
CREDENTIALS = [
     ("xxxxx", "xxxxxxx@xxxxxx.com", "xxxxxxxx"),
     ("xxxx", "", ""),
     ("xxxxxxxxxxxxxx", "", "")
]




def main():
     # quit if no command line argument was given
     try:
          command = sys.argv[1]
     except IndexError:
          print("Error: no command-line argument was given\nUsage:    python config.py venmo-init    or    python config.py venmo-logout")
          return


     # quit if an invalid command line argument was given
     if len(sys.argv) > 2 or (command != "venmo-init" and command != "venmo-logout"):
          print("Error: invalid command-line argument given\nUsage:    python config.py venmo-init    or    python config.py venmo-logout")
          return


     # if the user wants to initialize credentials
     if command == "venmo-init":
          # first check that the file isn't empty
          if os.stat("access_tokens.json").st_size != 0:
               print("Error: access tokens already initialized, clear them first with    python config.py venmo-logout")
               return

          print("\n============ begin 'venmo-api' messages ============\n")
          
          # proceed to create the access tokens for whoever provided credentials
          access_tokens = {}
          for cred in CREDENTIALS:
               if cred[1] != "" and cred[2] != "":
                    print("Generating access token for {}".format(cred[0]))
                    access_tokens.update({cred[0]: Client.get_access_token(username=cred[1], password=cred[2])})
               else:
                    access_tokens.update({cred[0]: ""})
          
          print("\n============= end 'venmo-api' messages =============\n")

          with open("access_tokens.json", "w") as file:
               json.dump(access_tokens, file)
          
          return
          

     # if the user wants to log out and clear their credentials
     if command == "venmo-logout":
          # first check that the file has contents to clear
          if os.stat("access_tokens.json").st_size == 0:
               print("Error: no access tokens to log out with, generate them with    python config.py venmo-init")
               return

          print("\n============ begin 'venmo-api' messages ============\n")
          
          # proceed to log out of the access tokens
          access_tokens = {}
          with open("access_tokens.json", "r") as file:
               access_tokens = json.load(file)
          for token in access_tokens.values():
               if token != "":
                    client = Client(access_token=token)
                    client.log_out(token)
          
          print("\n============= end 'venmo-api' messages =============\n")

          # clear the contents of the file
          open('access_tokens.json', 'w').close()

          return

if __name__ == "__main__":
     main()
