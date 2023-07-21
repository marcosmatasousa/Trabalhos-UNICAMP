#lab05 da disciplina MC102 1S2020 - Marcos da Mata Sousa (221519)
#Este programa simula o funcionamento Cyclic Redundancy Check (CRC)

#Entradas
m = list(input()) #mensagem
p = list(input()) #polinomio
m1 = len(m)
l = []
grau = len(p) - 1

#Alinhamento entre bits da mensagem e bits do polinomio
if len(m) < len(p):
  while len(m) < len (p):
    m.append('0')

#Alihamento entre bits do polinomio e bits da mensagem
if len(p) < len(m):
  while len(p) < len (m):
    p.append('0')

#aplicando operações XOR
for j in range(m1):
    if p[j] == '1' and m[j] == '1':
        for i in range(len(p)):
            if p[i] == m[i]:
                l.append('0')
            else:
                l.append('1')
        m = l
        l = []
        p.insert(0, '0')
        m.append('0')
    elif p[j] == '1' and m[j] == '0':
        p.insert(0,'0')
        m.append('0')

#Eliminando todos os elementos desnecessários
k = 0
while k < m1:
    del(m[0])
    k+=1

while len(m) > grau:
    m.pop()

#CRC
z = []
for x in range(len(m)):
    if m[x] == '1':
        z.append(1)
    else:
        z.append(0)

#Impressão final
print(''.join(m))


