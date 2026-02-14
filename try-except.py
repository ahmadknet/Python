try:
    num = int(input("Enter number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Division by zero")

except ValueError:
    print("Invalid input")

else:
    print(f"Result: {result}")

try:
    # Code that might raise an exception
    numerator = 10
    denominator = int(input("Enter a number: "))
    result = numerator / denominator
except ValueError:
    # Handles cases where input is not a valid integer
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    # Handles cases where the number is zero
    print("Error: Denominator cannot be 0.")
else:
    # Executes if no exceptions occur in the try block
    print(f"Result is {result}")
finally:
    # Always runs, useful for cleanup
    print("Execution complete.")
