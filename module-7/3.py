gallona = float(input("Syötä gallonat: "))

def converter(gallona):
    litrat = gallona * 3.785
    return litrat

while True:
    if gallona > 0:
        meow = converter(gallona)
        print("{} galloonaa = {} litraa\n".format(gallona, meow))
        gallona = float(input("Syötä gallonat: "))
    else:
        break
