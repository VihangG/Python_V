try:
    result = 10 /2
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("This block of code will always execute")