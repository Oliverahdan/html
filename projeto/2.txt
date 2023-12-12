atomico = int(input("Digite o numero atomico:"))

if atomico >= 1 and atomico <=2:
  print("O periodo é 1")

elif atomico >= 3 and atomico <= 10:
  print("O periodo é 2")
elif atomico >= 11 and atomico <= 18:
  print("O periodo é 3")
elif atomico >= 19 and atomico <= 36:
  print("O periodo é 4")
elif atomico >= 37 and atomico <= 54:
  print("O periodo é 5")
elif atomico >= 55 and atomico <= 86: 
  print("O periodo é 6")
elif atomico >= 87 and atomico <= 118:
  print("O periodo é 7")

print("\n")

if atomico in [1,3,11,19,37,55,87]:
    print("O grupo é 1")
elif atomico in [4,12,20,38,56,88]:
  print("O grupo é 2")
elif atomico in [21,39]:
  print("O grupo é 3")
elif atomico in range(57,72):
  print("O grupo é 3")
elif atomico in range(89,103):
  print("O grupo é 3")
elif atomico in [22,40,72,104]:
  print("O grupo é 4")
elif atomico in [23,41,73,105]:
  print("O grupo é 5")
elif atomico in [24,42,74,106]:
  print("O grupo é 6")
elif atomico in [25,43,75,107]:
  print("O grupo é 7")
elif atomico in [26,44,76,108]:
  print("O grupo é 8")
elif atomico in [27,45,77,109]:
  print("O grupo é 9")
elif atomico in [28,46,78,110]:
  print("O grupo é 10")
elif atomico in [29,47,79,111]:
  print("O grupo é 11")
elif atomico in [30,48,80,112]:
  print("O grupo é 12")
elif atomico in [5,13,31,49,81,113]:
  print("O grupo é 13")
elif atomico in [6,14,32,50,82,114]:
  print("O grupo é 14")
elif atomico in [7,15,33,51,83,115]:
  print("O grupo é 15")
elif atomico in [8,16,34,52,84,116]:
  print("O grupo é 16")
elif atomico in [9,17,35,53,85,117]:
  print("O grupo é 17")
elif atomico in [2,10,18,36,54,86,118]:
  print("O grupo é 18")

print("\n")

sair = input("Digite (sair) para sair: ")