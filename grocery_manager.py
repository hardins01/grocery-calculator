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
     
     # function to add the given entry to the given peoples' subtotals
     # assume that initials has been error checked (only valid initials)
     def new_entry(self, item_total, initials):
          
          # determine the subtotal to add to each person's total
          item_subtotal = item_total / len(initials)

          # loop through initials, adding to each person's total
          for initial in initials:
               self.people_totals[initial] += item_subtotal
          
          # add this item's total to the Grocery_Manager's total
          self.total += item_total

     # function to print everyone's subtotals, as well as the total
     def print_data(self):

          # print everyone's subtotals
          print("Results:")
          for person in self.people_totals:
               print(f"{person}:       $ {self.people_totals[person]:.2f}")
          
          # print the overall total
          print("Total:   $", self.total)