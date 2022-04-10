# grocery-calculator

A python program to calculate the bill that everyone owes after a grocery run. When only one person pays at the grocery store, there needs to be a way to calculate the money each person needs to pay, since not every item is equally shared. This program provides a convenient command-line-style interface to replicate your grocery store receipt, correctly divvying up items by price. Each item is added one at a time, along with the initials of the people that are partaking in that item. See below for more details.

## Installation

Prerequisites: `git` and `python` are installed.

`$ git clone https://github.com/hardins01/grocery-calculator.git`

## Usage

Before use, open the file `grocery.py` and change the global variable called `INITIALS` at the top. It must contain the initial of every person involved, once and only once. No duplicate initials are allowed. An initial can be any printable non-whitespace character. However, it's recommended to not use numerical characters to avoid confusion. Lowercase and uppercase letters are treated as different as well, so that increases the number of usable initials. For example, if the people in the grocery run are Sebastian, Logan, Ben, and Will, then `INITIALS` could be `"slbw"`, `"lswb"`, or any other permutation.

To run the program, navigate into the `grocery-calculator` directory and enter:

`$ python grocery.py`

The grocery-calculator works like a command-line-interface, with the following valid commands:

```text
> { a | add } PRICE INITIALS
     this command adds an item to the grocery run, allocating its total price to the people specified in INITIALS
     PRICE = the price of the item, which must be convertable to a float
          examples: 4.99, 8, 23.1, 2.09
     INITIALS = a series of initials that must be a subset of those provided at the top of grocery.py
          note: an initial can appear multiple times to achieve the correct ratio of cost for the designated item
          examples: slbw, sl, bss, blwssb
examples:      > a 9.34 ls      > add 8 lsbw      > a 23.11 lsbs

> { r | receipt | ls }
     this command lists the current subtotals and every item that hasn't been deleted
examples:      > r      > receipt      > ls

> { d | drop | delete } { ENTRY_ID | { p | prev | previous } }
     this command deletes the item with the given id or the previous item
     ENTRY_ID = the id of the item to be deleted (the id is provided when the item is added or in the r/receipt/ls command)
          examples: 0, 8, 3
examples:      > d 4      > drop prev      > delete p      > drop 6

> { q | s | e | quit | stop | exit }
     this command ends the program, along with printing everyone's totals of what they owe
examples:      > q      > s      > e      > quit      > stop      > exit

> { h | help }
     this command prints a list of all allowable commands
```

The general usage scenario is as follows: add items from the grocery store receipt with `a`, periodically check progress with `r` and use `d` to fix any mistakes, then end the program with `q` to see the final results of what everyone owes.
