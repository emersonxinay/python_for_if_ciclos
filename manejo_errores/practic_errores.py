

def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run():
    try:
        num = int(input("ingrese un numero: "))
        if num <= 0:
            raise ValueError("")

        print(divisor(num))
        print("Termino mi programa")
    except ValueError:
        print("debes ingresar un numero positivo")


if __name__ == '__main__':
    run()
