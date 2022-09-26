def func():
    while True: yield 1

x=func()
print(f"next function : {x.__next__()}")
