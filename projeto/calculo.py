calculo = input("O que você deseja calcular? escreva assim: (velocidade/tempo/distancia): ")
if calculo == "velocidade":
  distancia_velo = int(input("Digite a distancia:"))
  tempo_velo = int(input("Digite o tempo:"))
  calculo_velocidade = distancia_velo / tempo_velo
  print("A velocidade é: ", calculo_velocidade)
elif calculo == "tempo":
  distancia_tem = int(input("Digite a distancia:"))
  velocidade_tem = int(input("Digite a velocidade:"))
  calculo_tem = distancia_tem / velocidade_tem
  print("O tempo é: ", calculo_tem)
elif calculo == "distancia":
  tempo_dis = int(input("Digite o tempo:"))
  velocidade_dis = int(input("Digite a velocidade:"))
  calculo_dis = tempo_dis * velocidade_dis
  print("A distancia é: ", calculo_dis)
sair = input("Digite (sair) para sair: ")