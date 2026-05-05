import random

x = random.randint(1,5)

match x:
    case 1:
        print(f"El valor es igual a {x}")
    case _ if x > 1:
        print(f"El valor {x} es mayor a 1")
    case _:
        print(f"El valor es diferente a {x}")


    