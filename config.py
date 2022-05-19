# this config file will support the creation of venmo access tokens
from venmo_api import Client
import sys
import json


# the initials that represent each person in the grocery calculator
# edit this string to contain the valid initials for each person involved
# a valid initial is anything except whitespace, but it's suggested to not use numbers to avoid confusion
# capital and lowercase letters are allowed and will be distinguished between, and any other printable special character is allowed as well
# this string cannot contain anything except the unique initials
INITIALS = "slb"

# the list of venmo credentials
# each entry in the list contains two strings: the email, followed by the password
# the list must have the same number of entries as INITIALS
# each entry corresponds to the initial at the same index   i.e. the first set of credentials belongs to the first letter of INITIALS, etc
# a credential can be left blank, but it must be present in the list
CREDENTIALS = [
     ("xxxxxxxx@xxxxxx.com", "xxxxxxxxx"),
     ("", ""),
     ("", "")
]

# perform different actions based on command line argument
try:
     command = sys.argv[1]
except IndexError:
     print("no command given")
     quit()

if len(sys.argv) > 2 or (command != "venmo-init" and command != "venmo-logout"):
     print("invalid command given")
     quit()

if command == "venmo-init":
     print("command given: venmo-init")
     access_tokens = {}
     for index, cred in enumerate(CREDENTIALS):
          if cred[0] != "" and cred[1] != "":
               access_tokens.update({INITIALS[index]: Client.get_access_token(username=cred[0], password=cred[1])})
     with open("access_tokens.json", "w") as file:
          json.dump(access_tokens, file)
     

if command == "venmo-logout":
     print("command given: venmo-logout")
     access_tokens = {}
     with open("access_tokens.json", "r") as file:
          access_tokens = json.load(file)
     for token in access_tokens.values():
          client = Client(access_token=token)
          client.log_out(token)
     open('access_tokens.json', 'w').close()

