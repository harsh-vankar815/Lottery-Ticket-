# Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.
from random import choices


def winning_lottery(lottery_list):
    """Simulates the winning lottery number"""
    raw_ticket = choices(lottery_list, k=4)
    few_raw_ticket = str(raw_ticket).replace(',', '')
    winning_ticket = few_raw_ticket.replace('\'', '')
    # print(winning_ticket)
    # print(f"Any ticket matching {winning_ticket} these 4 numbers or letters wins a prize.")
    return winning_ticket


def purchasing_ticket(my_ticket):
    """Simulates the my lotter number"""
    raw_ticket = choices(my_ticket, k=4)
    few_raw_ticket = str(raw_ticket).replace(',', '')
    customer_ticket = few_raw_ticket.replace('\'', '')
    return customer_ticket


def checking_lottery_winning_attempts(my_ticket, winning_ticket):
    """Simulates the ticket how many attempts user take to win it"""
    attempts = 0
    while my_ticket:

        # Winning Ticket
        raw_ticket = choices(lottery, k=4)
        few_raw_ticket = str(raw_ticket).replace(',', '')
        winning_ticket = few_raw_ticket.replace('\'', '')

        if my_ticket == winning_ticket:
            print(f"YOU GOT A LOTTERY!, but you take {attempts} attempts for winning a lottery.")
            break

        attempts += 1

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e']

# Generating the Winning Lottery:
win_lottery = winning_lottery(lottery)
print(f"Winning Lottery Ticket: {win_lottery}")

# Getting My Lottery:
my_lottery = purchasing_ticket(lottery)
print(f"My Lottery Ticket: {my_lottery}")

# Checking Possible Attempts I've take to win a Lottery:
checking_lottery_winning_attempts(my_lottery, win_lottery)


# I CAN EASILY RAP THIS CODE INTO THE SEPERATE MODULE BUT IT'S VERY EXTREMELY GOOD CODE SO I WILL UPLOAD THIS IN THE LINKDIN AND MY GITHUB ACCOUNT. 