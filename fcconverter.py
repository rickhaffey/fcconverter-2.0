print("welcome to fcconverter 2.0!")


while(True):
    a=input("input fahr value (q to quit): ")

    if a == "q" or a == "Q":
        break

    f = float(a)
    c = (f - 32) * 0.5556
    print("your value is")
    print("...")
    print(c)
