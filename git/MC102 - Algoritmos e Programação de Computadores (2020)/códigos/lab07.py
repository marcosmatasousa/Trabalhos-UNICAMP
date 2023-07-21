##########################################################################################
# MC102 W - 2020 1S
# Aluno: MARCOS DA MATA SOUSA
# RA: 221519
# Data: 10/07/2020
# Descrição: Este programa simula o funcionamento da Guerra 4.0, um jogo em que,
# dados dois heróis e seus atributos (como vida, dano, bloqueio e mana) cria uma luta
# mágica envolvendo cartas especiais que só tem fim quando um dos heróis morre.
##########################################################################################


class Heroi:
    def __init__(self, nome, vida, dano, bloq, mana, max_mana, max_vida, atv_dren=0, taxa_dren=0, passe_ins=0,
                 atv_ins=0, dano_ins=0, dura_ins=0, custo_ins=0, passe_star=0, atv_star=0, dura_star=0, custo_star=0):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.bloq = bloq
        self.mana = mana
        self.max_mana = max_mana
        self.max_vida = max_vida
        self.atv_dren = atv_dren
        self.taxa_dren = taxa_dren
        self.atv_ins = atv_ins
        self.dano_ins = dano_ins
        self.dura_ins = dura_ins
        self.atv_star = atv_star
        self.dura_star = dura_star
        self.passe_ins = passe_ins
        self.passe_star = passe_star
        self.custo_ins = custo_ins
        self.custo_star = custo_star

    def atk(self, enemy):  #Método de ataque
        if self.atv_ins == 1 and self.dura_ins > 0:
            if enemy.atv_star == 1:
                print(self.nome, "deu um ataque insano em", enemy.nome)
                print(enemy.nome, "estava invulnerável")
                enemy.dura_star -= 1
                self.dura_ins -= 1
                if enemy.dura_star <= 0:
                    enemy.atv_star = 0
                    enemy.passe_star = 0
                if self.dura_ins <= 0:
                    self.atv_ins = 0
                    self.passe_ins = 0
            else:
                enemy.vida = enemy.vida - (self.dano + self.dano_ins) + \
                             int(((self.dano + self.dano_ins) * enemy.bloq / 100))
                print(self.nome, "deu um ataque insano em", enemy.nome)
                self.dura_ins -= 1
                if self.dura_ins == 0:
                    self.atv_ins = 0
                    self.passe_ins = 0
        else:
            if enemy.atv_star == 1:
                print(self.nome, "atacou", enemy.nome)
                print(enemy.nome, "estava invulnerável")
                enemy.dura_star -= 1
                if enemy.dura_star <= 0:
                    enemy.atv_star = 0
                    enemy.passe_star = 0
            else:
                enemy.vida = enemy.vida - self.dano + int((self.dano * enemy.bloq) / 100)
                print(self.nome, "atacou", enemy.nome)
        enemy.mana -= self.taxa_dren
        if enemy.mana < 0:
            enemy.mana = 0

    def cura(self, acao):  # Método de ativação da carta Cura
        print(self.nome, "encontrou a carta Cura")
        self.mana -= int(acao[2])
        if self.mana < 0:
            print(self.nome, "não possui mana suficiente para a mágica")
            self.mana += int(acao[2])
        else:
            self.vida += int(acao[3])
            if self.vida > self.max_vida:
                self.vida = self.max_vida

    def forca(self, acao):  # Método de ativação da carta Força
        print(self.nome, "encontrou a carta Força")
        self.mana -= int(acao[2])
        if self.mana < 0:
            print(self.nome, "não possui mana suficiente para a mágica")
            self.mana += int(acao[2])
        else:
            self.dano += int(acao[3])

    def protec(self, acao):  # Método de ativação da carta Proteção
        print(self.nome, "encontrou a carta Proteção")
        self.mana -= int(acao[2])
        if self.mana < 0:
            print(self.nome, "não possui mana suficiente para a mágica")
            self.mana += int(acao[2])
        else:
            self.bloq += int(acao[3])
            if self.bloq > 100:
                self.bloq = 100

    def eter(self, acao):  # Método de ativação da carta Éter
        print(self.nome, "encontrou a carta Éter")
        self.mana += int(acao[2])
        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def dren(self, acao):  # Método da carta Drenagem
        print(self.nome, "encontrou a carta Drenagem")
        if self.atv_dren == 1:
            print(self.nome, "já possui a carta Drenagem")
        else:
            self.atv_dren = 1
            self.taxa_dren = int(acao[2])

    def insano(self, acao):  # Método para encontrar a carta Insano
        print(self.nome, "encontrou a carta Insano")
        self.passe_ins += 1
        if self.passe_ins > 1:
            print(self.nome, "já possui a carta Insano")
            self.passe_ins -= 1
        else:
            self.custo_ins = int(acao[2])
            self.dura_ins = int(acao[3])
            self.dano_ins = int(acao[4])

    def atv_insano(self):  # Método de ativação da carta Insano
        if self.passe_ins == 1:
            if self.atv_ins == 1:
                print(self.nome, "já ativou a carta Insano")
            if self.atv_ins == 0:
                self.mana -= self.custo_ins
                if self.mana < 0:
                    self.mana += self.custo_ins
                    print(self.nome, "não possui mana suficiente para a mágica")
                else:
                    print(self.nome, "ativou a carta Insano")
                    self.atv_ins = 1
        else:
            print(self.nome, "não possui a carta Insano")

    def estrela(self, acao):  # Método para encontrar a carta Estrela
        print(self.nome, "encontrou a carta Estrela")
        self.passe_star += 1
        if self.passe_star > 1:
            print(self.nome, "já possui a carta Estrela")
            self.passe_star -= 1
        else:
            self.custo_star = int(acao[2])
            self.dura_star = int(acao[3])

    def atv_estrela(self):  # Método de ativação da carta Estrela
        if self.passe_star == 1:
            if self.atv_star == 1:
                print(self.nome, "já ativou a carta Estrela")
            if self.atv_star == 0:
                self.mana -= self.custo_star
                if self.mana < 0:
                    print(self.nome, "não possui mana suficiente para a mágica")
                    self.mana += self.custo_star
                else:
                    print(self.nome, "ativou a carta Estrela")
                    self.atv_star = 1
        else:
            print(self.nome, "não possui a carta Estrela")


#  Criando heróis
heroes = []
for i in range(0, 2):
    nome = input()
    vida = int(input())
    dano = int(input())
    bloq = int(input())
    mana = int(input())
    h = Heroi(nome, vida, dano, bloq, mana, mana, vida)
    heroes.append(h)
print("O reino Snowland indicou o herói", heroes[0].nome)
print("O reino Sunny Kingdom indicou o herói", heroes[1].nome)

r = 1  # rodada
while heroes[0].vida > 0 and heroes[1].vida > 0:
    j = 0  # controle de impressão
    for i in range(len(heroes)):
        vez = input().split(" ")
        player = int(vez[1])
        if player == 1:
            enemy = heroes[1]
        if player == 2:
            enemy = heroes[0]
        print("Rodada", str(r) + ": vez de", heroes[player - 1].nome)
        passa = 0  # enquanto for 0 não passa a vez
        while passa == 0:
            acao = input().split(" ")
            if acao[0] == "I":
                heroes[player - 1].atv_insano()
            if acao[0] == "S":
                heroes[player - 1].atv_estrela()
            if acao[0] == "M":
                if acao[1] == "C":
                    heroes[player - 1].cura(acao)
                if acao[1] == "F":
                    heroes[player - 1].forca(acao)
                if acao[1] == "P":
                    heroes[player - 1].protec(acao)
                if acao[1] == "E":
                    heroes[player - 1].eter(acao)
                if acao[1] == "D":
                    heroes[player - 1].dren(acao)
                if acao[1] == "I":
                    heroes[player - 1].insano(acao)
                if acao[1] == "S":
                    heroes[player - 1].estrela(acao)
                if acao[1] == "X":
                    print(heroes[player - 1].nome, "não encontrou nenhuma carta")
            if acao[0] == "A":
                passa = 1  # passa a vez
                heroes[player - 1].atk(enemy)
                j += 1  #

        #  se algum dos heróis morre
        if heroes[0].vida <= 0 or heroes[1].vida <= 0:
            break

    #  Correção da negatividade do atributo vida
    if heroes[0].vida < 0:
        heroes[0].vida = 0
    if heroes[1].vida < 0:
        heroes[1].vida = 0

    if j == 2:  # informações impressas ao fim da rodada apenas se ambos fizeram suas jogadas
        print(heroes[0].nome, "possui", heroes[0].vida, "de vida,", heroes[0].mana, "pontos mágicos,", heroes[0].dano,
              "de dano e", str(heroes[0].bloq) + "% de bloqueio")
        print(heroes[1].nome, "possui", heroes[1].vida, "de vida,", heroes[1].mana, "pontos mágicos,", heroes[1].dano,
              "de dano e", str(heroes[1].bloq) + "% de bloqueio")
    r += 1

if heroes[0].vida > 0 and heroes[1].vida <= 0:
    print("O herói", heroes[0].nome, "do reino Snowland venceu o duelo")

if heroes[1].vida > 0 and heroes[0].vida <= 0:
    print("O herói", heroes[1].nome, "do reino Sunny Kingdom venceu o duelo")

print(heroes[0].nome, "possui", heroes[0].vida, "de vida,", heroes[0].mana, "pontos mágicos,", heroes[0].dano,
      "de dano e", str(heroes[0].bloq) + "% de bloqueio")
print(heroes[1].nome, "possui", heroes[1].vida, "de vida,", heroes[1].mana, "pontos mágicos,", heroes[1].dano,
      "de dano e", str(heroes[1].bloq) + "% de bloqueio")
