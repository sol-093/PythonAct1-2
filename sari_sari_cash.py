def get_cash(amount_due):
    while True:
        try:
            cash = float(input(f"Enter cash given (Total: ₱{amount_due:.2f}): "))
            if cash < amount_due:
                print("Insufficient cash. Please enter enough to cover the total.")
                continue
            return cash
        except ValueError:
            print("Invalid input. Please enter a number.")
