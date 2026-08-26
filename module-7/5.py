lista = [5, 10, 3, 2]
def func(arg):
    dual_list = []
    for i in arg:
        if i % 2 == 0:
            dual_list.append(i)
    return dual_list

while True:
    meow = func(lista)
    print("Parilliset ja parittomat:")
    for i in lista:
        print(i)
    print("\nParilliset:")
    for i in meow:
        print(i)
    break
