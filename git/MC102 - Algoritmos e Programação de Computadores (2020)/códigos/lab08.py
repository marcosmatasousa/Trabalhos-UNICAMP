##########################################################################################
# MC102 W - 2020 1S
# Aluno: MARCOS DA MATA SOUSA
# RA: 221519
# Data: 01/07/2020
# Descrição: Este programa simula o funcionamento de um sistema de auxílio emergencial
# através da utilização de classes (governo e beneficiários).
##########################################################################################

class Beneficiario:
    def __init__(self, nome="", cpf="", status=0, rendap=0, rendat=0, idade=0, emprego="", t_auxilio=0, completo = 0, saldo = 0, negado=0):
        self.nome = nome
        self.cpf = cpf
        self.status = 0
        self.rendap = rendap
        self.rendat = rendat
        self.idade = idade
        self.emprego = emprego
        self.t_auxilio = t_auxilio
        self.completo = completo
        self.saldo = saldo
        self.negado = negado

    def opcao_beneficiario(self, option):
        # nome
        if option[0] == "1":
            nome = []
            for i in range(1, len(option)):
                nome.append(option[i])
            self.nome = ' '.join(nome)
            self.nome = self.nome.upper()
            print("Nome inserido")
            self.completo += 1

        # cpf
        if option[0] == "2":
            cpf = option[1]
            cpf = cpf.replace(".", '')
            cpf = cpf.replace("-", '')
            j = cpf[0:3]
            k = cpf[3:6]
            l = cpf[6:9]
            m = cpf[9:11]
            cpf_final = j + "." + k + "." + l + "-" + m
            self.cpf = cpf_final
            print("CPF inserido")
            self.completo += 1

        # renda percapita
        if option[0] == "3":
            percapita = option[1]
            self.rendap = float(percapita)
            print("Renda per capita inserida")
            self.completo += 1

        # renda total
        if option[0] == "4":
            rendatotal = option[1]
            self.rendat = float(rendatotal)
            print("Renda total inserida")
            self.completo += 1

        # idade
        if option[0] == "5":
            age = option[1]
            self.idade = int(age)
            print("Idade inserida")
            self.completo += 1

        # emprego
        if option[0] == "6":
            job = option[1]
            self.emprego = job
            print("Emprego inserido")
            self.completo += 1

        if self.completo == 6:
            self.status = 1
            self.completo = 0

        # transferindo para conta
        if option[0] == "8":
            print("Valor de R$", '{:.2f}'.format(self.saldo), "transferido para a conta corrente", option[1])

    def solicitar(self):
        print("Auxílio solicitado, aguarde avaliação")
        self.status = 2
        g.pendentes.append(b)

    def imprime_nome(self):
        print("Nome completo:", self.nome)

    def imprime_status(self):
        if self.status == 0:
            print("Status: Perfil incompleto")
        if self.status == 1:
            print("Status: Perfil completo")
        if self.status == 2:
            print("Status: Pendente")
        if self.status == 3:
            print("Status: Negado")
        if self.status == 4:
            print("Status: Com auxílio")
        if self.status == 5:
            print("Status: Auxílio finalizado")

    def imprime_cpf(self):
        print("CPF:", self.cpf)

    def imprime_tudo(self):
        print("Nome completo:", self.nome)
        if self.status == 0:
            print("Status: Perfil incompleto")
        if self.status == 1:
            print("Status: Perfil completo")
        if self.status == 2:
            print("Status: Pendente")
        if self.status == 3:
            print("Status: Negado")
        if self.status == 4:
            print("Status: Com auxílio")
        if self.status == 5:
            print("Status: Auxílio finalizado")
        print("CPF:", self.cpf)
        print("Renda per capita:", "R$", '{:.2f}'.format(self.rendap))
        print("Renda total:", "R$", '{:.2f}'.format(self.rendat))
        print("Idade:", self.idade)
        print("Emprego:", self.emprego)
        print("Tempo de recebimento:", self.t_auxilio, "meses")

class Governo:
    def __init__(self, beneficiandos = [], pendentes = [], recursos = 0):
        self.beneficiandos = beneficiandos
        self.recursos = recursos
        self.pendentes = pendentes

    def avaliar(self):
        for i in range(len(self.pendentes)):
            avaliando = self.pendentes[i]
            r1 = 1
            r2 = 1
            r3 = 1
            r4 = 1
            r5 = 1
            r6 = 1
            if avaliando.idade < 18:
                r1 = 0
            if (avaliando.emprego != "desempregado" and avaliando.emprego != "desempregada" and avaliando.emprego != "autonomo"
                        and avaliando.emprego != "autonoma" and avaliando.emprego != "microempreendedor" and avaliando.emprego != "microempreendedora"):
                r2 = 0
            if avaliando.status == 4 or avaliando.status == 5:
                r3 = 0
            if avaliando.negado == 1:
                r4 = 0
            if avaliando.rendap > 522.50 and avaliando.rendat > 3135:
                r5 = 0
            if avaliando.nome == '' or avaliando.cpf == '' or (avaliando.rendap == 0 and avaliando.rendat == 0) or avaliando.idade == 0 \
            or avaliando.emprego == '':
                r6 = 0
            if r1 == 1 and r2 == 1 and r3 == 1 and r4 == 1 and r5 == 1 and r6 == 1:
                avaliando.status = 4
                self.beneficiandos.append(avaliando)
            else:
                avaliando.status = 3
                avaliando.negado = 1
        print("Beneficiários avaliados")
        print("Lista de beneficiários atualizada")
        self.pendentes.clear()


    def add_recursos(self, valor):
        self.recursos += (valor)
        print("Recursos adicionados")

    def imprime_recursos(self):
        print("Recursos disponíveis: R$", '{:.2f}'.format((self.recursos)))

    def imprime_beneficiandos(self):
        print("Beneficiários atuais:")
        for i in range(len(self.beneficiandos)):
            print(self.beneficiandos[i].cpf + ":", self.beneficiandos[i].nome)

    def enviar_beneficio(self):
        insuf = 0
        for i in range(len(self.beneficiandos)):
            self.beneficiandos[i].saldo += 600
            self.recursos -= 600
            if self.recursos < 0:
                self.beneficiandos[i].saldo -= 600
                self.recursos += 600
                insuf += 1
            else:
                self.beneficiandos[i].t_auxilio += 1
                if self.beneficiandos[i].t_auxilio == 3:
                    self.beneficiandos[i].status = 5
                    del(self.beneficiandos[i])
        if insuf != 0:
            print("Recursos insuficientes")
        else:
            print("Auxílio mensal enviado")

g = Governo()
lista_consulta = []
avalia_cpf = []

orgao = '   '
while orgao != "X":
    orgao = input()

    #  realizando operações de beneficiário
    if orgao == "beneficiario":
        b = Beneficiario()
        opcao = '   '
        while opcao[0] != "F":
            opcao = input().split(" ")
            if opcao[0] == "7":
                if b.status < 1:
                    print("Complete seu perfil e tente novamente")
                else:
                    b.solicitar()
            if opcao[0] == "9":
                b.imprime_nome()
            if opcao[0] == "10":
                b.imprime_status()
            if opcao[0] == "11":
                b.imprime_cpf()
            if opcao[0] == "12":
                b.imprime_tudo()
            if opcao[0] == "F":
                lista_consulta.append(b)
                break
            else:
                if opcao[0] != "13" and opcao[0] != "10" and opcao[0] != "11" and opcao[0] != "12":
                    b.opcao_beneficiario(opcao)
                else:
                    pass

    #  realizando operações do governo
    if orgao == "governo":
        opcao1 = '   '
        while opcao1[0] != "F":
            opcao1 = input().split(" ")
            if opcao1[0] == "1":
                g.avaliar()
            if opcao1[0] == "3":
                g.imprime_recursos()
            if opcao1[0] == "4":
                g.imprime_beneficiandos()
            if opcao1[0] == "5":
                g.enviar_beneficio()
            if opcao1[0] == "F":
                break
            else:
                if opcao1[0] != "1" and opcao1[0] != "3" and opcao1[0] != "4" and opcao1[0] != "5":
                    valor = float(opcao1[1])
                    g.add_recursos(valor)
                else:
                    pass

    if orgao == "X":
        break

    #  consultar status de beneficiarios cadastrados
    if orgao != "beneficiario" and orgao != "governo":
        orgao.split(" ")
        i = 0
        for i in range(13, len(orgao)):
            avalia_cpf.append(orgao[i])
        if avalia_cpf[3] != ".":
            avalia_cpf.insert(3 , ".")
        if avalia_cpf[7] != ".":
            avalia_cpf.insert(7, ".")
        if avalia_cpf[11] != "-":
            avalia_cpf.insert(11, "-")
        avalia_cpf = ''.join(avalia_cpf)
        for x in range(len(lista_consulta)):
            if avalia_cpf == lista_consulta[x].cpf:
                opcao2 = '   '
                while opcao2[0] != "F":
                    opcao2 = input().split(" ")
                    if opcao2[0] == "7":
                        if lista_consulta[x].status < 1:
                            print("Complete seu perfil e tente novamente")
                        elif lista_consulta[x].status < 2:
                                lista_consulta[x].solicitar()
                    if opcao2[0] == "9":
                        lista_consulta[x].imprime_nome()
                    if opcao2[0] == "10":
                        lista_consulta[x].imprime_status()
                    if opcao2[0] == "11":
                        lista_consulta[x].imprime_cpf()
                    if opcao2[0] == "12":
                        lista_consulta[x].imprime_tudo()
                    if opcao2[0] == "F":
                        pass
                    else:
                        if opcao2[0] != "13" and opcao2[0] != "10" and opcao2[0] != "11" and opcao2[0] != "12":
                            lista_consulta[x].opcao_beneficiario(opcao2)
                        else:
                            pass
        avalia_cpf = []