#######################################################################################
## MC102 W - 2020 1S
## Aluno: MARCOS DA MATA SOUSA
## RA: 221519
## Data: 26/07/2020
## Descrição: Este programa simula o funcionamento de um sistema que cadastra países e
## os ordena por nome, população, PIB e IDH.
########################################################################################

class Paises:
    def __init__(self, nome='', populacao=0, pib=0, long=0, educ=0, renda=0, desi=0, idh=0):
        self.nome = nome
        self.populacao = populacao
        self.pib = pib
        self.long = long
        self.educ = educ
        self.renda = renda
        self.desi = desi
        self.idh = idh

    def cadastro(self, pais_info):
        self.nome = pais_info[0]
        self.populacao = int(pais_info[1])
        self.pib = int(pais_info[2])
        self.long = int(pais_info[3])
        self.educ = int(pais_info[4])
        self.renda = int(pais_info[5])
        self.desi = int(pais_info[6])
        self.idh = (self.desi*(self.long + self.educ + self.renda))/3
        self.idh = int(self.idh)


countries = []
ordem_cadastro = []
lista_pib = []
i = 0
while i != "*":
    comando = int(input())
    if comando == 1:  # cadastro
        numero_paises = int(input())
        for j in range(numero_paises):
            p = Paises()
            pais = input().split(" ")
            if int(pais[3]) < 0:
                print("Longevidade fora do intervalo")
                i = '*'
            elif int(pais[4]) < 0 or int(pais[4]) > 10:
                print("Educação fora do intervalo")
                i = "*"
            elif int(pais[6]) < 0 or int(pais[6]) > 10:
                print("Desigualdade fora do intervalo")
                i = "*"
            elif int(pais[3]) >= 0 and 0 <= int(pais[4]) <= 10 and 0 <= int(pais[4]) <= 10:
                p.cadastro(pais)
                countries.append(p)
                ordem_cadastro.append(p)
                lista_pib.append(p)

    elif comando == 2:  # Ordenando por ondem de cadastro
        print("Ordenado por Cadastro")
        for j in range(len(countries)):
            print(ordem_cadastro[j].nome, ordem_cadastro[j].populacao, ordem_cadastro[j].pib, ordem_cadastro[j].idh)

    elif comando == 3:  # Ordenando por nome
        for j in range(1, len(countries)):
            aux = countries[j]
            k = j
            while k > 0 and countries[k - 1].nome > aux.nome:
                countries[k] = countries[k - 1]
                k -= 1
            countries[k] = aux
        print("Ordenado por Nome")
        for j in (range(len(countries))):
            print(countries[j].nome, countries[j].populacao, countries[j].pib, countries[j].idh)

    elif comando == 4:  # Ordenando por tamanho populacional
        for j in range(1, len(countries)):
            aux = countries[j]
            k = j
            while k > 0 and countries[k - 1].populacao >= aux.populacao:
                countries[k] = countries[k - 1]
                k -= 1
            countries[k] = aux
        print("Ordenado por População")
        for j in reversed(range(len(countries))):
            print(countries[j].nome, countries[j].populacao, countries[j].pib, countries[j].idh)

    elif comando == 5:  # Ordenando por PIB
        for j in range(1, len(lista_pib)):
            aux = lista_pib[j]
            k = j
            while k > 0 and lista_pib[k - 1].pib >= aux.pib:
                lista_pib[k] = lista_pib[k - 1]
                k -= 1
            lista_pib[k] = aux
        print("Ordenado por PIB")
        for j in reversed(range(len(lista_pib))):
            print(lista_pib[j].nome, lista_pib[j].populacao, lista_pib[j].pib, lista_pib[j].idh)

    elif comando == 6:  # Ordenando por IDH
        for j in range(1, len(countries)):
            aux = countries[j]
            k = j
            while k > 0 and countries[k - 1].idh > aux.idh:
                countries[k] = countries[k - 1]
                k -= 1
            countries[k] = aux
        print("Ordenado por IDH")
        for j in reversed(range(len(countries))):
            print(countries[j].nome, countries[j].populacao, countries[j].pib, countries[j].idh)

    else:  #Finalizando o programa
        i = "*"