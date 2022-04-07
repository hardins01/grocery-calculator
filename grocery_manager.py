# the Grocery_Manager class, which controls the main functionality of the grocery calculator
class Grocery_Manager:

     # constructor
     def __init__(self, initials_string):

          # a dictionary that stores the initials of the people as well as their individual totals
          self.people_totals = { }
          for initial in initials_string:
               self.people_totals[initial] = 0
          
          # the total price of the grocery run, which should always be the sum of everyone's individual totals
          self.total = 0

          # an array of every entry, which is an array of tuples (each tuple contains the price, a float, followed by the initials of that entry)
          self.entries = []
     
     # function to add the given entry to the given peoples' subtotals
     # assume that initials has been error checked (only valid initials, no spaces)
     # returns the id of the new entry
     def new_entry(self, item_total, initials):
          
          # determine the subtotal to add to each person's total
          item_subtotal = item_total / len(initials)

          # loop through initials, adding to each person's total
          for initial in initials:
               self.people_totals[initial] += item_subtotal
          
          # add this item's total to the Grocery_Manager's total
          self.total += item_total

          # add this entry to the entries array
          self.entries.append((item_total, initials))
          return len(self.entries)-1

     # function to print everyone's subtotals, as well as the total
     def print_data(self):

          # print everyone's subtotals
          print("Results:")
          for person in self.people_totals:
               print(f"{person}:       $ {self.people_totals[person]:.2f}")
          
          # print the overall total
          print(f"Total:   $ {self.total:.2f}")



# 
# beyond the Grocery_Manager class, we also want several other helper functions
# 


# function to remove every special character in the input besides the lowercase letters
def clean_initials(initials):

     # loop through the string, removing everything except lowercase letters
     for char in initials:
          if not char.islower():
               initials = initials.replace(char, "")
     
     # return the result
     return initials 


