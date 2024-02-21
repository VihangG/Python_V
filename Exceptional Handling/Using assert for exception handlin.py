try:
    x = -1
    assert x >=0, "Only positive values are allowed"
    print(x)
except AssertionError as e:
    print("An Error occurred", str (e))