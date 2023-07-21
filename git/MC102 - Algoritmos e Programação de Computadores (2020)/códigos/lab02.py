nome = input()
hora = int(input())
valor = float(input())

if hora <8 or hora > 14:
  print("Número de horas diárias não admitido")

elif hora >=9 and hora <=12:
  valor = 22*(8*valor+(1.25*(hora-8)*valor))
  valor = "{:.2f}".format(valor)
  print("O salário do(a) funcionário(a)",nome,"será de R$"+str(valor),"para esse mês")

elif hora >=13 and hora <=14:
  valor = 22*(8*valor+(1.5*(hora-8)*valor))
  valor = "{:.2f}".format(valor)
  print("O salário do(a) funcionário(a)",nome,"será de R$"+str(valor),"para esse mês")

else:
  if hora == 8:
    valor = valor*8*22
    valor = "{:.2f}".format(valor)
    print("O salário do(a) funcionário(a)",nome,"será de R$"+str(valor),"para esse mês")