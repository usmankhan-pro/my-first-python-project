# ------------------------------------------------------------------
# PYTHON CONCEPT: CONDITIONALS (if, elif, else)
# Conditionals allow the program to make decisions and execute different code paths.
# ------------------------------------------------------------------

print("=== 2. MOVIE TICKET CALCULATOR ===")

# 1. Gather variables for decision making
age = int(input("Enter your age: "))
has_student_card = input("Are you a student? (yes/no): ").strip().lower()

# 2. Checking conditions
# We use comparison operators (<, >=, ==) and logical operators (or).
if age < 5:
    # Free for kids under 5
    ticket_price = 0
    discount_reason = "Toddler Free Ticket"
elif age < 18:
    # Discounted rate for kids/teens
    ticket_price = 8
    discount_reason = "Youth Discount"
elif age >= 65:
    # Discounted rate for seniors
    ticket_price = 7
    discount_reason = "Senior Citizen Discount"
else:
    # Standard rate for adults (check if they have a student card)
    if has_student_card == "yes" or has_student_card == "y":
        ticket_price = 9
        discount_reason = "Student Discount"
    else:
        ticket_price = 14
        discount_reason = "No Discount (Standard Ticket)"

# 3. Print the outcome based on our conditional checks
print("\n--- Ticket Invoice ---")
print(f"Ticket Price: ${ticket_price}")
print(f"Category: {discount_reason}")
