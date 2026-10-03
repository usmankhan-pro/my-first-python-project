# ------------------------------------------------------------------
# PYTHON CONCEPT: VARIABLES & USER INPUT
# Variables are used to store data, and user input allows interaction.
# ------------------------------------------------------------------

print("=== 1. TRIP BUDGET CALCULATOR ===")

# 1. Storing Text (Strings)
# We use input() to get text from the keyboard and save it in a variable.
destination = input("Enter travel destination: ")

# 2. Storing Numbers & Type Casting (Integers and Floats)
# input() always gets data as text. We convert it to numbers using int() or float().
days = int(input("Enter number of days (whole number): "))
daily_budget = float(input("Enter estimated budget per day ($): "))

# 3. Performing Calculations
# We use basic math operators (+, -, *, /) on our variables.
total_cost = days * daily_budget

# 4. Printing Output
# We use f-strings (formatted strings) to print variables inside text.
print("\n--- BUDGET SUMMARY ---")
print(f"Trip to: {destination}")
print(f"Duration: {days} days")
print(f"Daily Cost: ${daily_budget}")
print(f"Total Estimated Cost: ${total_cost}")
