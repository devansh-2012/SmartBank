import matplotlib.pyplot as plt
from datetime import datetime
import random
from collections import defaultdict

class FinancialAssistant:
    def __init__(self):
        # Stores (Type, Amount, Time, Location)
        self.history = []
        self.total_deposits = 0.0
        self.total_withdrawals = 0.0

        # Simulated AI-based locations
        self.locations = [
            "ATM - Bhopal",
            "Online Banking",
            "Bank Branch",
            "Mobile App",
            "UPI Payment"
        ]

    def generate_location(self):
        return random.choice(self.locations)

    def log_transaction(self, category, amount):
        if amount <= 0:
            return
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        location = self.generate_location()

        self.history.append((category, amount, timestamp, location))

        if category == "Deposit":
            self.total_deposits += amount
        elif category == "Withdrawal":
            self.total_withdrawals += amount

    def display_summary(self):
        print("\n--- AI Financial Summary ---")
        print(f"Total Deposited:   ${self.total_deposits:.2f}")
        print(f"Total Withdrawn:   ${self.total_withdrawals:.2f}")
        print(f"Net Cash Flow:     ${(self.total_deposits - self.total_withdrawals):.2f}")
        print(f"Transaction Count: {len(self.history)}")

        print("\n--- Detailed Transaction History ---")
        for i, txn in enumerate(self.history, start=1):
            print(f"\n{i}. {txn[0]} of ${txn[1]:.2f}")
            print(f"   Time: {txn[2]}")
            print(f"   Location: {txn[3]}")

    def plot_history(self):
        if not self.history:
            print("No history to plot yet.")
            return

        labels = [f"{i+1}.{t[0]}" for i, t in enumerate(self.history)]
        amounts = [t[1] for t in self.history]
        colors = ['green' if t[0] == "Deposit" else 'red' for t in self.history]

        plt.figure(figsize=(8, 5))
        plt.bar(labels, amounts, color=colors)
        plt.xlabel('Transaction History')
        plt.ylabel('Amount ($)')
        plt.title('Deposit vs Withdrawal History')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def generate_monthly_report(self):
        if not self.history:
            print("No transactions available for monthly report.")
            return

        monthly_data = defaultdict(lambda: {"deposit": 0, "withdrawal": 0})

        for txn in self.history:
            category, amount, timestamp, _ = txn
            month = timestamp[:7]

            if category == "Deposit":
                monthly_data[month]["deposit"] += amount
            elif category == "Withdrawal":
                monthly_data[month]["withdrawal"] += amount

        print("\n--- AI Monthly Financial Report ---")

        for month, data in sorted(monthly_data.items()):
            net = data["deposit"] - data["withdrawal"]
            print(f"\nMonth: {month}")
            print(f"  Total Deposits:    ${data['deposit']:.2f}")
            print(f"  Total Withdrawals: ${data['withdrawal']:.2f}")
            print(f"  Net Savings:       ${net:.2f}")

    def plot_monthly_report(self):
        if not self.history:
            print("No data to plot.")
            return

        monthly_data = defaultdict(lambda: {"deposit": 0, "withdrawal": 0})

        for txn in self.history:
            category, amount, timestamp, _ = txn
            month = timestamp[:7]

            if category == "Deposit":
                monthly_data[month]["deposit"] += amount
            else:
                monthly_data[month]["withdrawal"] += amount

        months = sorted(monthly_data.keys())
        deposits = [monthly_data[m]["deposit"] for m in months]
        withdrawals = [monthly_data[m]["withdrawal"] for m in months]

        x = range(len(months))

        plt.figure(figsize=(8, 5))
        plt.plot(x, deposits, marker='o', label="Deposits")
        plt.plot(x, withdrawals, marker='o', label="Withdrawals")
        plt.xticks(x, months)
        plt.xlabel("Month")
        plt.ylabel("Amount ($)")
        plt.title("Monthly Financial Trends")
        plt.legend()
        plt.tight_layout()
        plt.show()


def show_balance(balance):
    print(f"\nYour Current Balance is: ${balance:.2f}")


def deposit():
    try:
        amount = float(input("Enter amount to be deposited: "))
        if amount > 0:
            return amount
        else:
            print("That's not a valid amount.")
            return 0
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0


def withdraw(balance):
    try:
        amount = float(input("Enter amount to be withdrawn: "))
        if amount > balance:
            print("Insufficient funds.")
            return 0
        elif amount <= 0:
            print("Your amount is not valid.")
            return 0
        else:
            return amount
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0


def main():
    balance = 0.0
    choice = 0
    ai_assistant = FinancialAssistant()

    while choice != 6:
        print("\n**********************")
        print("   BANKING MENU")
        print("**********************")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View AI Analytics & Chart")
        print("5. View Monthly Report")
        print("6. Exit")

        user_input = input("Selection: ")

        if not user_input.isdigit():
            print("Invalid choice. Please enter a number (1-6).")
            continue

        choice = int(user_input)

        if choice == 1:
            show_balance(balance)

        elif choice == 2:
            amount = deposit()
            balance += amount
            ai_assistant.log_transaction("Deposit", amount)
            show_balance(balance)

        elif choice == 3:
            amount = withdraw(balance)
            balance -= amount
            ai_assistant.log_transaction("Withdrawal", amount)
            show_balance(balance)

        elif choice == 4:
            ai_assistant.display_summary()
            ai_assistant.plot_history()

        elif choice == 5:
            ai_assistant.generate_monthly_report()
            ai_assistant.plot_monthly_report()

        elif choice == 6:
            print("Thanks for visiting!")

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
