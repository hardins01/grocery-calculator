# import the grocery_manager class from the other file
from grocery_manager import Grocery_Manager

# test the Grocery_Manager class
gm = Grocery_Manager("slb")

gm.new_entry(34.11, "bl")
gm.new_entry(21.23, "lbbs")

gm.print_data()