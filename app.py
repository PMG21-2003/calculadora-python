def calculadora():
    while True:
        print("\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair")
        op = input("Escolha: ")

        if op == "5":
            break

        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))

        if op == "1":
            print("Resultado:", n1 + n2)
        elif op == "2":
            print("Resultado:", n1 - n2)
        elif op == "3":
            print("Resultado:", n1 * n2)
        elif op == "4":
            print("Resultado:", n1 / n2)

calculadora()