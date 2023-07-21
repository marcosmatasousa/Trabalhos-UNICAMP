##lab06 da disciplina MC102 1S2020 - Marcos da Mata Sousa (221519)
#Este programa simula o funcionamento de uma fábrica de cajuína.

# Definindo a função de classificação dos cajus.
# Para todas as funções: r = lista das remessas de cajú /i = indice das listas/f = lista referente à "fábrica"
def classi(r, i, f):
    r[i] = int((2 / 3) * r[i])
    f[0] = r[i]
    del (r[i])
    r.insert(0, 0)

# Definindo a função de prenssagem dos cajus.
def prensa(r, i, f):  # lista, indice, fabrica
    if f[0] >= 10:
        f[1] = 2 * f[0]
        f[0] = 0
    else:
        f[1] = 5 * f[0]
        f[0] = 0

# Definindo a função de filtragem dos cajus.
def filt(r, i, f):  # lista, indice, fabrica
    if f[1] > 45:
        f[2] = int((1 / 10) * f[1])
        f[1] = 0
    else:
        f[2] = int((8 / 9) * f[1])
        f[1] = 0

#Definindo a função de tratamento dos cajus.
def trat(r, i, f):
    f[3] = f[2] * 2
    f[2] = 0

# Definindo a função fábrica, que engloba todas as outras funções juntas.
def fabrica(n):
    r = []
    final = []
    fab = [0, 0, 0, 0]
    for i in range(n):  # Loop de entrada das remessas
        remessa = int(input())
        if remessa >= 2:
            r.append(remessa)
        else:
            print("É necessário pelo menos dois cajus para produção de cajuína!")
            exit()
    print("T=0 |", r, "->", fab, "->", final)

    for x in range(n + 4): #Loop de funcionamento da fábrica.
        if fab[3] != 0:
            final.append(fab[3])
            fab.pop()
            fab.append(0)
        if x >= 3:
            trat(r, x, fab)
        if x >= 2:
            filt(r, x, fab)
        if x >= 1:
            prensa(r, x, fab)
        if x < n:
            classi(r, x, fab)
        print("T=" + str(x + 1), "|", r, "->", fab, "->", final)

# Dando a entrada da quantidade de remessas e chamando a função fábrica.
n = int(input())
fabrica(n)