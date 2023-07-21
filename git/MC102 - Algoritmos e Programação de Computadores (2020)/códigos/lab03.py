print("Você apresenta pelo menos 4 dos sintomas principais do COVID-19? (Tosse, febre, dor de garganta, congestão nasal, coriza, dor de cabeça, cansaço, dores pelo corpo)\n(1) sim\n(2) não")
a1 = int(input())
if a1 == 1:
  print("Você realizou o teste do COVID-19 desde que esses sintomas surgiram?\n(1) não\n(2) sim, deu positivo\n(3) sim, deu negativo")
  a2 = int(input())
  if a2 == 1:
    print("Baseado em suas respostas, a orientação é que você vá ao hospital para ser testado para o COVID-19")
  if a2 == 2:
    print("Você se encontra em estado grave de saúde?\n(1) sim\n(2) não")
    a3 = int(input())
    if a3 == 1:
      print("Baseado em suas respostas, a orientação é que você vá a um hospital para que possa ser internado")
    if a3 == 2:
      print("Você se enquadra em um grupo de risco? (gestante; portador de doenças crônicas; problemas respiratórios; fumante; pessoa de extremos de idade, seja criança ou idoso)\n(1) sim\n(2) não")
      a4 = int(input())
      if a4 == 1:
        print("Baseado em suas respostas, a orientação é que você vá a um hospital para que possa ser internado")
      if a4 == 2:
        print("Baseado em suas respostas, a orientação é que você entre em isolamento")
      elif a4 != 1 and a4 != 2:
        print("Opção inválida, recomece a avaliação")
    elif a3 != 1 and a3 != 2:
      print("Opção inválida, recomece a avaliação")
  if a2 == 3:
    print("Baseado em suas respostas, a orientação é que você permaneça em distanciamento social")
  elif a2 != 1 and a2 != 2 and a2 != 3:
    print("Opção inválida, recomece a avaliação")
if a1 == 2:
  print("Você entrou em contato recentemente com alguém que foi diagnosticado com o vírus?\n(1) sim\n(2) não")
  b1 = int(input())
  if b1 == 1:
    print("Baseado em suas respostas, a orientação é que você entre em isolamento")
  if b1 == 2:
    print("Baseado em suas respostas, a orientação é que você permaneça em distanciamento social")
  elif b1 != 1 and b1 != 2:
    print("Opção inválida, recomece a avaliação")
elif a1 != 1 and a1 != 2:
  print("Opção inválida, recomece a avaliação")
