
# Função criada melhorar a estetica invertendo coluna e linha formando os degraus a partir da ordem 1
def imprimir(matriz):
    matrizTemp = []
    cabecalho = ["x"]

    # inicia-se uma lista de listas vazia
    for linha in range(len(matriz[0])):
        temp = []
        matrizTemp.append(temp)
   
   #Inverte a matriz
    for coluna in range(len(matriz)):
        if (coluna > 0):
            cabecalho.append(coluna-1)
        for linha in range(len(matriz[coluna])):
            if (coluna > 1):
                matrizTemp[linha+(coluna-1)].append(matriz[coluna][linha])
            else:
                matrizTemp[linha].append(matriz[coluna][linha])

    #imprime
    print(cabecalho)
    for linha in range(len(matrizTemp)):
        print(matrizTemp[linha])

#Calculo
def interNewton(matriz, x, cErro):
    temp = []
    coluna = len(matriz)-1

    #Calculo para a diferença dividida da coluna
    for i in range(len(matriz[coluna])-1):
        temp.append((matriz[coluna][i+1]-matriz[coluna][i]) /
                    (matriz[0][i+coluna]-matriz[0][i])) # (Y(n+1) - Y(n))/(X(n+1) - X(n))

    matriz.append(temp)

    #Calcula até chegar na ultima coluna que tem apenas 1 elemento
    if len(temp) > 1:
        interNewton(matriz, x, cErro)
    else:
        imprimir(matriz)

        #Se escolheu com o calculo de erro pede-se as informações necessarias
        if cErro == 1:
            print("Escolha as opções para calcular o erro:")
            linhaescolha = int(input("Informe a linha inicial:"))-1
            ordemescolha = int(input("Informe a ordem limite:"))+1
        else:
            linhaescolha = 0
            ordemescolha = len(matriz)

        resultado = matriz[1][linhaescolha]
        coluna = 2
        ordemAtual = 0

        # Calcula o resultado para a interpolação
        while coluna < len(matriz):
            #Para o calculo do erro para ao chegar na ordem escolhida.
            if coluna > (ordemescolha):
                break
            temp = 1
            i = 0
            while i < ordemAtual+1:
                temp *= (x-matriz[0][i+linhaescolha])
                i += 1
            temp *= matriz[coluna][linhaescolha]
            resultado += temp
            ordemAtual += 1
            coluna += 1
        print("result =", resultado)

        if cErro == 1:
            erro = 1

            # Calculando o erro.
            for i in range(ordemescolha):
                erro *= x - matriz[0][linhaescolha+i]
            erro *= max(matriz[ordemescolha+1])
            print("erro =", erro)


def menu():
    matriz = []
    temp = []
    tam = int(input("Informe a quantidade de pontos:"))
    i = 0
    while (i < tam):
        temp.append(float(input("X:")))
        i += 1
    matriz.append(temp)
    temp = []
    i = 0
    while (i < tam):
        temp.append(float(input("Y:")))
        i += 1
    matriz.append(temp)
    x = float(input("Informar o valor de x:"))

    erro = int(input("Calcular o erro? 1 - sim, 2 - não: "))
    interNewton(matriz, x, erro)


menu()
