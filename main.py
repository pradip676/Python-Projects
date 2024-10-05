import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns,lines,bet,values):
    winnings =0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1)
    return winnings, winning_lines        

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)  # Add each symbol count times to the list

    columns = []  # Initialize empty columns list
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Copy all symbols for this column
        for _ in range(rows):
            value = random.choice(current_symbols)  # Randomly choose a symbol
            current_symbols.remove(value)  # Remove the chosen symbol from available
            column.append(value)  # Add the symbol to the column
        columns.append(column)  # Add the column to columns

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Print symbol followed by separator
            else:
                print(column[row])  # No separator after the last column

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a valid number of lines between 1 and {MAX_LINES}.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You have insufficient balance to bet! Your current balance is ${balance}.")
        else:
            print(f"You are betting ${bet} on {lines} lines.")
            print(f"Your total bet is: ${total_bet}.")
            balance -= total_bet  # Deduct the total bet from the balance
            slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
            print_slot_machine(slots)
            winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
            print(f"You won ${winnings}.")
            if winning_lines:
                print(f"You won on lines:", *winning_lines)
            else:
                print("No winning lines.")
            return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit). ").lower()
        if answer =="q":
            break
        balance +=spin(balance)
    print(f"You left with ${balance}")




main()
