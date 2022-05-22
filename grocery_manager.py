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

          # an array containing the ids of the entries that have been deleted
          self.deleted_entries = []
     
     # function to verify if the given initials are valid for this grocery manager
     # assume that all whitespace has been removed from initials
     # return 0 for invalid initials, return 1 for valid initials
     def verify_initials(self, initials):

          # loop through initials to find one that doesn't exist as a key in self.people_totals
          for initial in initials:
               if initial not in self.people_totals.keys():
                    return 0
          
          return 1
     
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

     # function to print the final results, which are the subtotals and total
     def print_results(self):

          # print everyone's subtotals
          print("Results:")
          for person in self.people_totals:
               print(f"{person}:       $ {abs(self.people_totals[person]):.2f}")
          
          # print the overall total
          print(f"Total:   $ {self.total:.2f}")
     
     # function to print the current status, which is every active entry AND the subtotals and total
     def print_status(self):

          # print all active entries
          num_printed = 0
          print("")
          for i in range(0, len(self.entries)):
               if i not in self.deleted_entries:
                    string_to_print = "ID#{}  $ {} {}".format(i, "{:.2f}".format(self.entries[i][0]), self.entries[i][1])
                    correct_spacing = ""
                    for j in range(len(string_to_print), 32):
                         correct_spacing += " "
                    print(string_to_print, end=correct_spacing)
                    num_printed += 1
               
                    if num_printed % 4 == 0:
                         print("")
          
          # print everyones subtotal along with the total
          print("")
          if num_printed % 4 != 0:
               print("")
          for person in self.people_totals:
               print(f"{person}:       $ {abs(self.people_totals[person]):.2f}")
          print(f"Total:   $ {self.total:.2f}\n")

     # function to delete an entry, given its id
     # returns 1 if successful, 0 if the id wasn't found, -1 if the entry has already been deleted
     def delete_entry(self, entry_id):

          # check if the given id is too large/too small
          if entry_id < 0 or entry_id >= len(self.entries):
               return 0
          
          # check if the entry has already been deleted
          if entry_id in self.deleted_entries:
               return -1
          
          # delete the entry
          self.deleted_entries.append(entry_id)
          item_subtotal = self.entries[entry_id][0] / len(self.entries[entry_id][1])
          for initial in self.entries[entry_id][1]:
               self.people_totals[initial] -= item_subtotal
          self.total -= self.entries[entry_id][0]
          return 1
     
     # function to drop the previous entry, the most recent one that's been added
     # return 1 if successful, 0 or -1 if not
     def delete_prev_entry(self):

          # find the entry closest to the end of the array that hasn't been deleted already
          return_code = 0
          delete_id = len(self.entries) - 1
          while(return_code != 1 and delete_id >= 0):
               return_code = self.delete_entry(delete_id)
               delete_id -= 1
          
          return return_code

     # function to get the subtotal for the given person, their stake in the total amount
     # person must be one of the initials
     def get_subtotal(self, person):
          return self.people_totals[person]

