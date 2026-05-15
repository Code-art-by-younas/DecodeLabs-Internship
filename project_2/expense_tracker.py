# Expense Tracker Project
# Week 2 - Decode Lab Python Project

print("=== Expense Tracker ===")
print("Enter your expenses one by one.")
print("Type 'quit' to finish.\n")

# Accumulator (running total)
total = 0

while True:
    user_input = input("Enter expense amount: ")

    # Kill Switch
    if user_input.lower() == "quit":
        break

    # Defensive Coding
    try:
        expense = int(user_input)
        total += expense
        print(f"Current Total: ${total:.2f}")
    except ValueError:
        print("Invalid Data! Please enter a valid number.")

# Final Output
print("\n=== Summary ===")
print(f"FINAL TOTAL: ${total:.2f}")
print("Thank you for using Expense Tracker!")