
resposta="sim"
while(resposta=="sim"):

    print("--Calculadora--")
    numero1=int(input ("Digite seu primeiro numero:"))
    numero2=int(input("Digite seu segundo numero:"))
    operacao=input("Digite sua operação: +/-*:")


    if operacao == "+" :
        print("Sua soma é: ",numero1 + numero2)

    elif operacao == "-":
         print("sua subtração é:",numero1 - numero2)

    elif operacao == "*":
        print("sua mutiplicação é:",numero1 * numero2)
    
    elif operacao == "/":
        print("sua divisão é:",numero1 / numero2)

    resposta= (input("Deseja fazer mais calculo?\n"))

 