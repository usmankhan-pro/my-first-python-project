# ------------------------------------------------------------------
# PYTHON CONCEPT: LOOPS (while & for)
# Loops allow us to repeat a block of code multiple times.
# - 'while' loops repeat while a condition is True (unknown number of times).
# - 'for' loops repeat over a specific range or collection (set number of times).
# ------------------------------------------------------------------

print("=== 3. LOOPS DEMONSTRATION ===")

# --- Part 1: The 'while' Loop ---
# We keep asking the user to guess the secret number until they get it correct.
secret_number = 7
user_guess = 0
attempts = 0

print("\n--- While Loop: Guessing Game ---")
print("Guess the secret number between 1 and 10.")

while user_guess != secret_number:
    user_guess = int(input("Enter your guess: "))
    attempts = attempts + 1  # Track how many loops have run
    
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")

print(f"Correct! You solved it in {attempts} attempts.")


# --- Part 2: The 'for' Loop ---
# We use a for loop with range() to run a block of code exactly 5 times.
print("\n--- For Loop: Multiples Table ---")
number = int(input("Enter a number to see its first 5 multiples: "))

for multiplier in range(1, 6):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
