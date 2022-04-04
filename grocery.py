# function to take apart the inputted string, in the form of   [price] [initials]
def add_prices_to_people(input_string, seb_running_total, logan_running_total, ben_running_total, will_running_total):
     # split input_string, goes into an array
     price_and_initials = input_string.split()
     
     # get the price from price_and_initials
     price = float(price_and_initials[0])

     # get the initials from the rest
     initals = price_and_initials[1]

     # divide price by number of people, add them to each person
     price_per_person = price / len(initals)
     if "s" in initals:
          seb_running_total += price_per_person
     if "l" in initals:
          logan_running_total += price_per_person
     if "b" in initals:
          ben_running_total += price_per_person
     if "w" in initals:
          will_running_total += price_per_person
     
     #return everyone's new running totals
     return seb_running_total, logan_running_total, ben_running_total, will_running_total


# initialize all running totals to 0
seb_total, logan_total, ben_total, will_total = 0, 0, 0, 0


# tell the user to start inputting items
print("start inputting items, one at a time, in the following format:\n")
print("                   [price] [initials]\n\nwhere price is a float and initials contains \"s\", \"l\", \"b\", or \"w\" only once")
print("to stop entering values and get the total, simply type \"stop\"\n")


# while loop, getting all the items from the user
while 1:
     # get the line of input
     print(": ", end="")
     input_string = input()

     # check if it's the "stop" command
     if input_string == "stop":
          break
     
     # tally the totals for everyone
     seb_total, logan_total, ben_total, will_total = add_prices_to_people(input_string, seb_total, logan_total, ben_total, will_total)


# print the final values
print("\n\nhere's everyone's total values:")
print(f"seb total:\t$ {seb_total:.2f}")
print(f"logan total:\t$ {logan_total:.2f}")
print(f"ben total:\t$ {ben_total:.2f}")
print(f"will total:\t$ {will_total:.2f}", "\n\n")