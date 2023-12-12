# Codigo da moeda:
# valor = 62

# moedas = [25, 10, 5, 1]  # Valores das moedas disponíveis

# for moeda in moedas:
#     quantidade = valor // moeda
#     valor %= moeda
#     print(f"{moeda} centavos = {quantidade}")

#introdução
print("Olá, somos da empresa responsável por guiar turistas na Terra-Média, recomendamos viagens de acordo com suas preferencias")
print("\n")
print("Colocaremos uma pergunta com 4 opçoes, com sua resposta definiremos o melhor lugar para se visitar")
print("\n")
#primeira pergunta
while True:
  pergunta1 = input("1. Qual das seguintes opções melhor descreve o principal aspecto geográfico natural da Terra-média no seu destino? \n\n 1. Montanhas majestosas e picos nevados \n 2. Vastas planícies verdes e férteis \n 3. Florestas antigas e misteriosas \n 4. Terras áridas e desertas \n\n Digite o numero correspondente a opção mais adequada a seu estilo: ")
  if pergunta1 in ["1","2","3","4"]:
         break
  else:
         print("\ninformação invalida\n")
print("\n")
#segunda pergunta
while True:
   pergunta2 = input("2 .Qual dos seguintes aspectos culturais é mais proeminente da Terra-média no destino? \n\n 1. Cultura hobbit com ênfase na vida tranquila e festiva \n 2. Cultura élfica, com ênfase na sabedoria e harmonia com a natureza \n 3. Cultura guerreira e honrada dos Rohirrim \n 4. Cultura sombria e corrompida dos servos de Sauron \n\n Digite o numero correspondente a opção mais adequada a seu estilo: ")
   if pergunta2 in ["1","2","3","4"]:
    break
   else:
    print("\ninformação invalida\n")
print("\n")    
#terceira pergunta
while True:
  pergunta3 = input("3. Qual das seguintes atividades de aventura é mais proeminente da Terra-média no destino? \n\n 1. Exploração de minas e cavernas em busca de tesouros \n 2. Caminhadas e trilhas épicas através de paisagens deslumbrantes \n 3. Batalhas contra inimigos perigosos e criaturas fantásticas \n 4. Jornadas em busca de artefatos mágicos e poderosos \n\n Digite o numero correspondente a opção mais adequada a seu estilo: ")
  if pergunta3 in ["1","2","3","4"]:
   break
  else:
   print("\ninformação invalida\n")
  
print("\n")    
#quarta pergunta
while True:
 print("4. Qual das seguintes experiências de relaxamento é mais proeminente da Terra-média no destino?")
 print("1. Desfrutar da tranquilidade e paz no campo hobbit ")
 print("2. Banhos termais e curativos nas Montanhas da Perdição")
 print("3. Meditação e contemplação nas clareiras de Lothlórien")
 print("4. Retiros de cura e renovação em Valfenda")
 print("\n")
 pergunta4 = input("Digite o numero correspondente a opção mais adequada a seu estilo: ")
 print("\n")
 if pergunta4 in ["1","2","3","4"]:
   break
 else:
   print("\ninformação invalida\n")
#codigo das perguntas

print("\n")   
if pergunta1 in "1":
  if pergunta2 == "1":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")   
#primeiro looping da opção 1
  
  elif pergunta2 == "2":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")     
#segundo looping da opção 1
  
  elif pergunta2 == "3":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Achamos seu destino! Tome um mapa e siga para Erebor")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")   
#terceiro looping da opção 1
  
  elif pergunta2 == "4":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")     
#quarto looping da opção 1

elif pergunta1 in "2":
  if pergunta2 == "1":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Achamos seu destino! Tome um mapa e siga para Hobbiton")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")   
#primeiro looping da opção 2
  
  elif pergunta2 == "2":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")     
#segundo looping da opção 2
  
  elif pergunta2 == "3":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")   
#terceiro looping da opção 2
  
  elif pergunta2 == "4":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")     
#quarto looping da opção 2

elif pergunta1 in "3":
  if pergunta2 == "1":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")   
#primeiro looping da opção 1
  
  elif pergunta2 == "2":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Achamos seu destino! Tome um mapa e siga para Lothlórien")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")     
#segundo looping da opção 1
  
  elif pergunta2 == "3":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")   
#terceiro looping da opção 1
  
  elif pergunta2 == "4":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")     
#quarto looping da opção 3

elif pergunta1 in "4":
  if pergunta2 == "1":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")   
#primeiro looping da opção 4
  
  elif pergunta2 == "2":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")     
#segundo looping da opção 4
  
  elif pergunta2 == "3":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")   
#terceiro looping da opção 4
  
  elif pergunta2 == "4":
    if pergunta3 == "1":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")  
    elif pergunta3 == "2":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "3":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")    
    elif pergunta3 == "4":
      if pergunta4 == "1":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "2":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "3":
        print("Muito complicado suas escolhas, acho melhor você seguir aquele velho de roupa cinza com um cajado")
      elif pergunta4 == "4":
        print("Achamos seu destino! Tome um mapa e siga para Mordor")     
#quarto looping da opção 4

else:
 print("Informação Invalida")

print("\n")  

print("As referencias foram tiradas de Senhor dos Aneis ")

print("\n")  
while True:
  fim = input("Digite (sair) para sair kkk: ")
  if fim == "sair":
    exit()
  else: 
   print("bota sair po")