try:
    raise ValueError("This is a custom error message")
except ValueError as e:
    print("An error occureed",str(e))