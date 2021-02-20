import random

memoria = [' '] * 100
opcao = 0
saida = 0
tamanho = 0
letra = ''
#gera aleatóriamente uma lista
for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '

for i in range(0,20):
    print(memoria[i], end="|")
print()
for i in range(20,40):
    print(memoria[i], end="|")
print()
for i in range(40,60):
    print(memoria[i], end="|")
print()
for i in range(60,80):
    print(memoria[i], end="|")
print()
for i in range(80,100):
    print(memoria[i], end="|")
print()


while(opcao != 4):
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    if opcao < 1 or opcao > 4: #se opção diferente de 1, 2 e 3 quebra o programa
        print("Esta opção não existe, por favor selecione uma opção válida") #mensagem de opçãp invalida
        print("")
        continue #reinicia o programa
    if opcao == 4:
        print("Processo finalizado!")
        break #quebra o programa
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

#Está opção insere a letra a ser utilizada no primeiro espaço possivel
    if opcao == 1:
        contslot = 0
        qnt = 0
        inicio = 0
        Achei = False
        for i in range(100):
            if tamanho <= contslot:
                Achei = True
                while(qnt < tamanho): #grava o valor na lista
                    memoria[inicio] = letra #grava informação no campo 'inicio'
                    inicio += 1
                    qnt += 1 #contador para saber até onde vai ser colocada a infrmação
                break #quebra o programa
            if memoria[i] != ' ': # se espaço for diferente de vazio, zera contador
                contslot = 0 #zera contador
            if memoria[i] == ' ': #se espaço for vazio, contador + 1
                contslot += 1 #contador + 1
                if contslot == 1: #se o contador for igual a 1, aquele é o primeiro campo vazio encontrado nesse processo
                    inicio = i #variavel inicio recebe a posicao inicial
        if not Achei: #se não existe espaço disponivel apresenta mensagem
            print("Não há armazenamento disponível!")

#Está opção insere a letra a ser utilizada no menor espaço possivel
    if opcao == 2:
        contslot = 0
        omenor = 999999999999
        qnt = 0
        print("A Melhor escolha")
        for i in range(100):
            if memoria[i] != ' ': # se espaço for diferente de vazio, zera contador
                contslot = 0 #zera contador
            if memoria[i] == ' ': #se espaço for vazio, contador + 1
                contslot += 1 #contador + 1
                if contslot == 1: #se o contador for igual a 1, aquele é o primeiro campo vazio encontrado nesse processo
                    inicio = i #variavel inicio recebe a posicao inicial
                if tamanho == contslot:
                    if contslot < omenor:
                        omenor = contslot
                        posicaoi = inicio
        while(qnt < tamanho):
            if tamanho < omenor: #se não existe espaço disponivel apresenta mensagem
                print("Não há armazenamento disponível!")
                break #quebra o programa
            else: #grava o valor na lista
                memoria[posicaoi] = letra
                posicaoi += 1
                qnt += 1

#Está opção insere a letra a ser utilizada no maior espaço possivel
    if opcao == 3:
        contslot = 0
        omaior = 0
        qnt = 0
        posicaoi = 0
        print("A pior escolha")
        for i in range(100):
            if memoria[i] != ' ': # se espaço for diferente de vazio, zera contador
                contslot = 0 #zera contador
            if memoria[i] == ' ': #se espaço for vazio, contador + 1
                contslot += 1 #contador + 1
                if contslot == 1: #se o contador for igual a 1, aquele é o primeiro campo vazio encontrado nesse processo
                    inicio = i #variavel inicio recebe a posicao inicial
                if tamanho <= contslot:
                    if contslot > omaior:
                        omaior = contslot
                        posicaoi = inicio
        while(qnt < tamanho):
            if tamanho > omaior: #se não existe espaço disponivel apresenta mensagem
                print("Não há armazenamento disponível!")
                break #quebra o programa
            else: #grava o valor na lista
                memoria[posicaoi] = letra
                posicaoi += 1
                qnt += 1


    for i in range(0,20):
        print(memoria[i], end="|")
    print()
    for i in range(20,40):
        print(memoria[i], end="|")
    print()
    for i in range(40,60):
        print(memoria[i], end="|")
    print()
    for i in range(60,80):
        print(memoria[i], end="|")
    print()
    for i in range(80,100):
        print(memoria[i], end="|")
    print()
