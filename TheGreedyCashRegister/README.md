# 💰 The Greedy Cash Register

A command-line Python application that simulates a checkout process. It calculates total costs, validates customer payments, and computes the exact change using a greedy algorithm to dispense the fewest number of bills and coins.

## ✨ Technologies

- `Python 3`

## 🚀 Features

- Uses the greedy algorithm to optimize change dispensing
- Processes transactions in cents to eliminate floating-point arithmetic errors
- Built-in payment validation to handle underpayment and exact change
- Continuous session loop to handle multiple customers consecutively
 
## 📍 The Process

I've been on a mission to understand algorithmic thinking, specifically how simple greedy algorithms work in real-world scenarios. A cash register felt like the perfect project. I started by setting up a basic shopping loop, but quickly realized that handling decimals in currency often leads to floating-point math errors. My solution was to convert everything to cents! From there, I used integer division and modulo operations to cascade down the denominations—from $20 bills all the way to pennies. It's a simple terminal app, but I'm really happy with how robust the validation logic and the math turned out! 

## 🚦 Running the Project

1. Clone the repository or download `TheGreedyCashRegister.py`
2. Ensure you have Python 3 installed on your system
3. Open your terminal and navigate to the project directory
4. Run the script: `python TheGreedyCashRegister.py`

## 🎞️ Preview

```
-----The Greedy Cash Register-----
Enter item price (in cents): 1000
End shopping? (Yes/No): No
Enter item price (in cents): 359
End shopping? (Yes/No): Yes

Total due: 1359 cents
Amount Paid (in cents): 1000
Error, payment is too low. Try again.
Amount Paid (in cents): 5000

Total change to return: 3641 cents
--- Dispense ---
Hand back 1 twenty-dollar bill(s).
Hand back 1 ten-dollar bill(s).
Hand back 1 five-dollar bill(s).
Hand back 1 one-dollar bill(s).
Hand back 1 quarter(s).
Hand back 1 dime(s).
Hand back 1 nickel(s).
Hand back 1 penny/pennies.

----------------------------------
End machine session? (Yes/No): No

Starting next customer transaction...

Enter item price (in cents): 250
End shopping? (Yes/No): Yes

Total due: 250 cents
Amount Paid (in cents): 250
Exact change! Thank you for shopping with us.

----------------------------------
End machine session? (Yes/No): Yes
Shutting down the register. Goodbye!
```
