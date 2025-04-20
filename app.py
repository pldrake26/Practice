title = 'monthly budget'
income = 2500
total = 0

print(title.upper())
while True:
    try:
        bill = input('Enter your monthly expense (or 0 to finish): ')
        bill = float(bill)
        if bill < 0:
            print("Expense cannot be negative. Please enter a valid amount.")
            continue
        elif bill == 0:
            break
        else:
            if total + bill > income:
                print("Warning: This expense exceeds your budget!")
            else:
                total += bill
                print(f'Expense added: ${bill:.2f}')
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

print(f'Total monthly expenses: ${total:.2f}')
print(f'Your monthly budget is: ${income - total:.2f}')

