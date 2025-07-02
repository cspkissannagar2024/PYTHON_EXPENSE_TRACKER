# Personal Expense Tracker Project - Clean Version

import pandas as pd
import matplotlib.pyplot as plt

# Function to add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Shopping etc): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    # Save to CSV
    new_data = pd.DataFrame([[date, category, amount, description]],
                            columns=["Date", "Category", "Amount", "Description"])
    new_data.to_csv("expenses.csv", mode='a', header=False, index=False)
    print("✅ Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    try:
        df = pd.read_csv("expenses.csv")
        print("\n--- All Expenses ---")
        print(df)
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

# Function to visualize expenses by category
def visualize_expenses():
    try:
        df = pd.read_csv("expenses.csv")

        if df.empty:
            print("No expenses to visualize.\n")
            return

        # Strip any extra spaces from column headers if they exist
        df.columns = df.columns.str.strip()

        # Check if 'Category' and 'Amount' columns exist
        if 'Category' not in df.columns or 'Amount' not in df.columns:
            print("CSV file missing 'Category' or 'Amount' column.\n")
            print(f"Current columns: {df.columns.tolist()}")
            return

        category_totals = df.groupby("Category")["Amount"].sum()

        # If no expenses to plot, show message
        if category_totals.empty:
            print("No expenses to visualize.\n")
            return

        # Plot pie chart
        category_totals.plot(kind="pie", autopct="%1.1f%%", startangle=90)
        plt.title("Expense Distribution by Category")
        plt.ylabel("")  # remove the y-label
        plt.show()

    except FileNotFoundError:
        print("No expenses recorded yet.\n")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program menu
def main():
    while True:
        print("\n========== Personal Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Visualize Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            visualize_expenses()
        elif choice == '4':
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice, please try again.")

# Program entry point
if __name__ == "__main__":
    main()