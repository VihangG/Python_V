try:
    result = 10 / 0
except Exception as e:
    print("An error occurred:", str(e))

try:
    print("undefined variable")
except Exception as e:
    print("An error occurred", str(e))