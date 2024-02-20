try:
    result = 10 / 0
except(ZeroDivisionError, TypeError) as e:
    print("Error occurred:", str(e))


