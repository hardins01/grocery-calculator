# Grocery-Galculator

This is a python program to calculate the bill that everyone owes after a grocery run. When only one person pays at the grocery store, there needs to be a way to calculate the money each person needs to pay, since not every item is equally shared. This program provides a convenient command-line-style interface to replicate your grocery store receipt, correctly divvying up items by price. Each item is added one at a time, along with the initials of the people that are partaking in that item. After adding each item, you can optionally initiate automatic Venmo requests/payments using [`venmo-api`](https://github.com/mmohades/Venmo), a Venmo API wrapper by [@mmohades](https://github.com/mmohades). See below for more details.

## Installation

Prerequisites: `git`, `pip`, and `python` (version 3.6 or greater) are installed.

First, install `venmo-api` via pip:

```shell
pip install venmo-api --upgrade
```

Next, clone this repo and navigate into it:

```shell
git clone https://github.com/hardins01/grocery-calculator.git
cd grocery-calculator
```

## Usage

Before first use, open `config.py` and notice the two global variables near the top, `INITIALS` and `CREDENTIALS`. `INITIALS` must contain the initial of every person involved, once and only once. No duplicate initials are allowed. An initial can be any printable non-whitespace character. However, it's recommended to not use numerical characters to avoid confusion. Lowercase and uppercase letters are treated as different as well, so that increases the number of usable initials. For example, if the people in the grocery run are Robert, Chris, and Chris, then `INITIALS` could be `"rcC"`, `"Crc"`, or any other permutation. The initials don't even have to be the first letter of each person's name, just a character that makes sense and is distinguishable from everyone else.

After that, if you'd like to use the automatic Venmo functionality, enter your credentials into `CREDENTIALS`. Each entry in that list corresponds to that initials in `INITIALS`. The first set of credentials belong to the first initial, the second to the second, etc. For each set of credentials, the first string is that person's Venmo username, without the @. The second string is the email associated with their account. The third is their password. As a bare minimum, in order for any Venmo transactions to take place. Everyone must put their username, and one person needs to put in their username, email, and password. That way, if the person with all their credentials pays at the grocery store, requests can be sent on their behalf to all other people. If the credentials are set up such that someone who owes money is the only one with full credentials filled in, payments will be made on their behalf as well. However, Grocery-Calculator will always prefer to make requests instead of payments wherever possible as an extra step of human verification. As is explained below, there are also extra steps in the process to confirm that Venmo transactions are desired. In the end, it may look like so:

```python
INITIALS = "rcC"

CREDENTIALS = [
     ("RDowneyJ", "rdj@avengers.com", "iamironman3000"),
     ("Chris-Evans", "chris.evans@avengers.com", "icandothisallday"),
     ("ChrisHemsworth", "chrishemsworth@avengers.com", "strongestavenger1")
]
```

Once everyone's credentials are entered, one final step is required: the generation of the access token(s). These access tokens are used to gain access to the Venmo API. They're generated by running `config.py` like so:

```shell
python config.py venmo-init
```

For everyone who entered their full set of credentials, access tokens will be generated, initiating Venmo's 2FA process. The access tokens are saved in `access_tokens.json` for future use, so this step only needs to happen once. Remember that anyone with your access token has full access to your account, so don't give them away or commit them to a repository. Another downside is that they last forever until they're intentionally deactivated. This can be done by running `config.py` like so:

```shell
python config.py venmo-logout
```

This will log out all the access tokens from `access_tokens.py`, then clear out its contents for new ones to be generated later.

Whether Venmo operations are desired or not, Grocery-Calculator's core functionality is still available. To run the program, run `python grocery.py` like so:

```shell
python grocery.py
```

The grocery-calculator works like a command-line-interface, with the following valid commands:

```text
> { a | add } PRICE INITIALS
     this command adds an item to the grocery run, allocating its total price to the people specified in INITIALS
     PRICE = the price of the item, which must be convertable to a float
          examples: 4.99, 8, 23.1, 2.09
     INITIALS = a series of initials that must be a subset of those provided at the top of grocery.py
          note: an initial can appear multiple times to achieve the correct ratio of cost per person
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


> { q | s | e | quit | stop | exit } [{ v | venmo }]
     this command ends the program, along with printing everyone's totals of what they owe
     optionally, before ending the program, Venmo transaction(s) can be initiated
          checking takes place to see if credentials have been provided, and one extra prompt happens to ensure that the user wants to deal with Venmo
examples:      > q v     > s      > e venmo     > stop v     > exit


> { h | help }
     this command prints a list similar to this one of all allowable commands
examples:      > h      > help
```

The general usage scenario is as follows: open `config.py` to modify `INITIALS` and `CREDENTIALS`, generate access tokens with `python config.py venmo-init`, run the program with `python grocery.py`, add items from the grocery store receipt with `a`, periodically check progress with `r` and use `d` to fix any mistakes, then end the program with `q v` to see the final results of what everyone owes and create Venmo requests/payments.
