# Wallet Tracker

A simple wallet tracker project written in Python using a class-based approach.

This project is mainly created to practice Python OOP concepts like classes, objects, methods, attributes, and basic encapsulation. It allows a user to create a wallet account, add money, withdraw money, check the PIN, and view the current balance.

## Features

- Create a wallet account with an account number and PIN
- Check whether the PIN has a combination of uppercase, lowercase, numbers, and special characters
- Add money to the wallet
- Withdraw money from the wallet
- Check the PIN before adding or withdrawing money
- Display the current wallet balance

## Technologies Used

- Python
- Object-Oriented Programming (OOP)

## How It Works

The main part of the project is the `wallet` class. It stores the wallet balance, account number, and PIN.

The project uses different methods for different operations:

- `addingaccount()` - creates the account and checks the PIN strength
- `addamount()` - adds money after checking the PIN
- `withdrawamount()` - withdraws money after checking the PIN
- `checkpin()` - checks whether the entered PIN matches the saved PIN
- `displaybalance()` - displays the current balance

## Example

The current program creates a wallet with an account number and PIN, adds ₹1000, displays the balance, withdraws ₹500, and displays the updated balance.

The expected balance after these operations is:

```text
500
```

## How to Run

1. Make sure Python is installed on your system.
2. Download or clone this repository.
3. Open the project folder in a terminal or VS Code.
4. Run the Python file:

```bash
python wallet_project.py
```

5. Enter the PIN whenever the program asks for verification.

## What I Learned

While building this project, I practiced:

- Creating classes and objects
- Using `__init__()` to initialize object data
- Creating and calling methods
- Using `self` to access object attributes
- Using conditions and loops
- Checking strings with methods such as `islower()`, `isupper()`, and `isdigit()`
- Using a simple PIN verification system

## Future Improvements

There are a few things that can be improved in the next version:

- Add proper error handling for invalid inputs
- Prevent withdrawing more money than the available balance
- Make the PIN validation return a clear success or failure result
- Add options through a menu instead of fixed operations
- Store account details more safely
- Add transaction history
- Allow multiple wallet accounts

## Note

This is a learning project and is not intended to be used as a real payment or banking application. The PIN and account details are handled only for practicing Python programming and OOP concepts.

## Author

Saimadhan Dharmaji

BTech Computer Science Student
