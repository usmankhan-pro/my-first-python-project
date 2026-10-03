# ------------------------------------------------------------------
# PYTHON CONCEPT: FUNCTIONS
# Functions are reusable blocks of code that perform a specific task.
# - They can take inputs called parameters.
# - They can send back results using the 'return' keyword.
# ------------------------------------------------------------------

print("=== 4. TEMPERATURE CONVERTER ===")

# 1. Defining a function to convert Celsius to Fahrenheit
# 'celsius' is the input parameter.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit  # Sends the result back to where the function was called

# 2. Defining a function to convert Fahrenheit to Celsius
# 'fahrenheit' is the input parameter.
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius  # Sends the result back to where the function was called


# 3. Main Script: Calling the functions
print("Choose conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter choice (1 or 2): ").strip()

if choice == "1":
    temp_c = float(input("Enter temperature in Celsius: "))
    
    # We CALL the function by name and pass temp_c as the argument.
    # The output returned by the function is stored in the 'result' variable.
    result = celsius_to_fahrenheit(temp_c)
    
    print(f"{temp_c}°C is equal to {result:.2f}°F")
    
elif choice == "2":
    temp_f = float(input("Enter temperature in Fahrenheit: "))
    
    # We CALL the function by name and pass temp_f as the argument.
    result = fahrenheit_to_celsius(temp_f)
    
    print(f"{temp_f}°F is equal to {result:.2f}°C")
    
else:
    print("Invalid choice! Please select 1 or 2.")
