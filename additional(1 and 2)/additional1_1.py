def mul12(x):
    b = x
    x = x+x+x
    x = x+x
    x = x+x
    print(str(b) + " * 12 = " + str(x))
def mul16(x):
    b = x
    x=x+x
    x=x+x
    x=x+x
    x=x+x
    print(str(b) + " * 16 = " + str(x))
def mul15(x):
    b=x
    x=x+x
    x=x+x
    x=x+x
    x=x-(-x)-b
    print(str(b) + " * 15 = " + str(x))
def mul29(x):
    b = x
    x = x + x
    x = x + x
    x = x + b
    x = x + x+ x
    x = x + x
    x = x - b
    print(str(b) + " * 29 = " + str(x))

x = int(input("x = "))
mul12(x)
mul15(x)
mul16(x)
mul29(x)