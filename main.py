guanyador = False

# Repetim partides fins que hi ha un guanyador
while guanyador == False:
  # Variables d'entrada: pedra, paper, tisora
  j1 = input("J1: ")
  j2 = input("J2: ")

  # Control d'errors
  while (j1 != "V" and j1 != "[]" and j1 != "O") or (j2 != "V" and j2 != "[]"
                                                     and j2 != "O"):
    print('Combinació incorrecta! Tens un altre intent ...')
    j1 = input("J1: ")
    j2 = input("J2: ")

  # Comprobam si el jugador 1 ha guanyat la partida
  if j1 == "V" and j2 == "[]" or j1 == "O" and j2 == "V" or j1 == "[]" and j2 == "O":
    guanyador = True
    print("Guanya J1")
  # Miran si hi ha empat
  elif j1 == j2:
    print("Empat! Fem una altra partida ...")
  # El darrer cas posbile és que segur ha guanyat el jugador 2
  else:
    print("Guanya J2")
    guanyador = True
