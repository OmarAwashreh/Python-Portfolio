print("-----The Greedy Cash Register-----")

is_running = True

while is_running:
    # 1. Resetting the cart for the new customer
    shopping = True
    total = 0  

    # 2. The Shopping Loop
    while shopping:
        # We ask for input in cents (e.g., $5.00 is 500) to avoid decimal math errors
        item_price = int(input("Enter item price (in cents): "))
        total = total + item_price

        end = input("End shopping? (Yes/No): ")
        if end == "Yes":
            shopping = False

    print(f"\nTotal due: {total} cents")

    # 3. The Payment Validation Loop
    payment_accepted = False
    while not payment_accepted:
        payment = int(input("Amount Paid (in cents): "))

        if payment < total or payment < 0:
            print("Error, payment is too low. Try again.")
        elif payment == total:
            print("Exact change! Thank you for shopping with us.")
            payment_accepted = True
            change = 0 # No change needed
        else:
            change = payment - total
            print(f"\nTotal change to return: {change} cents")
            payment_accepted = True

    # 4. The Change Cascade 
    if change > 0:
        print("--- Dispense ---")
        
        # $20 Bills (2000 cents)
        bills_20 = change // 2000
        change = change % 2000
        if bills_20 > 0:
            print(f"Hand back {bills_20} twenty-dollar bill(s).")

        # $10 Bills (1000 cents)
        bills_10 = change // 1000
        change = change % 1000
        if bills_10 > 0:
            print(f"Hand back {bills_10} ten-dollar bill(s).")

        # $5 Bills (500 cents)
        bills_5 = change // 500
        change = change % 500
        if bills_5 > 0:
            print(f"Hand back {bills_5} five-dollar bill(s).")

        # $1 Bills (100 cents)
        bills_1 = change // 100
        change = change % 100
        if bills_1 > 0:
            print(f"Hand back {bills_1} one-dollar bill(s).")

        # Quarters (25 cents)
        quarters = change // 25
        change = change % 25
        if quarters > 0:
            print(f"Hand back {quarters} quarter(s).")

        # Dimes (10 cents)
        dimes = change // 10
        change = change % 10
        if dimes > 0:
            print(f"Hand back {dimes} dime(s).")

        # Nickels (5 cents)
        nickels = change // 5
        change = change % 5
        if nickels > 0:
            print(f"Hand back {nickels} nickel(s).")

        # Pennies (1 cent - whatever is left!)
        if change > 0:
            print(f"Hand back {change} penny/pennies.")

    # 5. Session Control
    print("\n----------------------------------")
    end_session = input("End machine session? (Yes/No): ")
    if end_session == "Yes":
        is_running = False
        print("Shutting down the register. Goodbye!")
    else:
        print("\nStarting next customer transaction...\n")