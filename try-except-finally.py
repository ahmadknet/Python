try:
    numerator = 10
    denominator = 0
    result = numerator / denominator # This will raise a ZeroDivisionError
except Exception as e:
    # Catches the exception and assigns the object to variable 'e'
    print(f"An error occurred: {e}") # e will contain the message 'division by zero'
finally:
    print("This cleanup code always runs.")

# Output:
# An error occurred: division by zero
# This cleanup code always runs.
