def verificarFinalizacao():
    verificacao = input("Você deseja calcular novamente?(s/n)")
    if verificacao == "s":
        calcular()
    elif verificacao == "n":
        print("Fechando a Calculadora.")
    else:
        verificarFinalizacao()
def calcular():
    numero1 = int (input("Digite um numero: "))
    numero2 = int (input("Digite outro número: "))

    tipoOperacao = input("Qual o tipo de operação?(+, -, *, /)")
    if tipoOperacao == "+":
        print("O resultado de {} + {} é igual a {}".format(numero1, numero2, numero1 + numero2))
    elif tipoOperacao == "-":
        print("O resultado de {} - {} é igual a {}".format(numero1, numero2, numero1 - numero2))
    elif tipoOperacao == "*":
        print("O resultado de {} * {} é igual a {}".format(numero1, numero2, numero1 * numero2))
    elif tipoOperacao == "/":
        print("O resultado de {} / {} é igual a {}".format(numero1, numero2, numero1 / numero2))
    verificarFinalizacao()

calcular()