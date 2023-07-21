######################################################################
## MC102 W - 2020 1S
## Aluno: MARCOS DA MATA SOUSA
## RA: 221519
## Data: 14/06/2020
## Descrição: Este programa é a implementação do Respondenator 3000,
## sistema que compara n possíveis respostas e encontra a resposta mais adequada.
######################################################################

from PontStop import *

dic = {}
chave = input()
sinom = 0  # sinonimo
while sinom != "}":
    sinom = input()
    if sinom == "}":
        break
    else:
        key = sinom.split(":")
        value = (key[1].split(","))
        dic[key[0]] = value

quest = input()  # entrada pergunta
quest_original = quest
quest = quest.lower()  # 1) padronizando
quest = quest.replace(".", "")
quest = quest.replace(",", "")
quest = quest.replace("?", "")
quest = quest.replace("!", "")
quest = quest.replace("(", "")
quest = quest.replace(")", "")
quest = quest.replace(":", "")
quest = quest.replace(";", "")
quest = quest.split(" ")  # 2) tokenização

i = 0
while i < (len(quest)):  # 3) limpeza
    if quest[i] in stop_words:
        quest[i] = ""
    i += 1

for i, j in dic.items():  # 4) reescrita
    for k in range(len(quest)):
        if quest[k] in j:
            quest[k] = i

quest = set(quest)  # 5) representação
quest = sorted(quest)
del(quest[0])
print("Descritor pergunta:", ",".join(quest))

dic_respostas_originais = {}
dic_respostas = {}
n = int(input())
i = 0
for i in range(n):
    j = 0
    answer = input()
    dic_respostas_originais[i + 1] = answer
    answer = answer.lower()  # 1) padronização
    answer = answer.replace(".", "")
    answer = answer.replace(",", "")
    answer = answer.replace("?", "")
    answer = answer.replace("!", "")
    answer = answer.replace("(", "")
    answer = answer.replace(")", "")
    answer = answer.replace(":", "")
    answer = answer.replace(";", "")
    answer = answer.split(" ")  # 2) tokenização

    while j < (len(answer)):  # 3) limpeza
        if answer[j] in stop_words:
            answer[j] = ""
        j += 1

    for o, p in dic.items():  # 4) reescrita
        for q in range(len(answer)):
            if answer[q] in p:
                answer[q] = o
    dic_respostas[i + 1] = answer

    answer = set(answer)  # 5) representação
    answer = sorted(answer)
    if answer[0] == "":
        del(answer[0])

    print("Descritor resposta", str(i+1) + ":", ",".join(answer))

i = 0
j = 0
k = 0
for i, j in dic_respostas.items():  # Resposta adequada
    if set(j).issuperset(set(quest)):
        print("")
        print("A resposta para a pergunta", '"' + quest_original + '"', "é", '"' + dic_respostas_originais[i] + '"')
    else:
        k += 1

if k == i:  # 42
    print("")
    print("A resposta para a pergunta", '"' + quest_original + '"', "é", '"' + "42" + '"')

