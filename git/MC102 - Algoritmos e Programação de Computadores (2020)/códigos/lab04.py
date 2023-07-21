#lab04 da disciplina MC102 1S2020 - Marcos da Mata Sousa (221519)
#Este programa apresenta o montante acumulado de um investimento em n meses, levando em conta aplicações (depósitos), resgates (saques) e juros.
#Dados de entrada:
v_0 = float(input()) #investimento inicial
t = float(input()) # juros
n = int(input()) # quantidade de meses
i = 0
#Adicionando juros e aplicações/resgates sobre o investimento inicial
total = v_0
while i < n:
  k = float(input()) #k são depósitos/saques
  r = total + (t * total)+ k #r está relacionado com o rendimento após aplicação de juros e depósitos/saques
  if r < 0:
    print("Valor inválido no mês",str(i)+". Tente novamente.")
    r = total +( t* total) + k
  else:
    total = r
    i+=1
#convertendo o valor final em string para manipulação
total = str("{:.2f}".format(total))
#impressão da mensagem final
print("O total após", str(n), "meses é de R$" , total+".")