def divide (a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Division by Zero")
        return None

print(divide(10,0))