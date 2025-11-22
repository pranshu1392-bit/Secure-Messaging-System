x=4
print(f"The global x is {x}")
def hello():
    x=5
    print(f"The local x is {x}")
hello()
print(f"The global x is {x}")