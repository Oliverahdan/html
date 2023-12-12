menu = 0
while True:
    menu = input("Olá, seja bem-vindo(a) à Pizzaria Freddy Fazbear's Pizzaria.\n\nConfira nosso cardápio:\n\n1. Frango com Catupiry do Freddy (R$39,90)\n2. Calabresa da Foxy (R$39,90)\n3. Marguerita da Chica (R$49,90)\n4. Pepperoni da Bonnie (R$49,90)\n5. Vegetariana do Golden Freddy (R$29,90)\n\nDigite o número correspondente à pizza escolhida: ")

    if menu in ["1", "2", "3", "4", "5"]:
        break
    else: 
      print("\n Informação invalida!\n")
      
print("\n")
while True:
    quantidade = input("Quantas pizzas deseja? (fazemos até 10 pizzas por pessoa) ")
    if quantidade in ["1", "2", "3", "4", "5","6","7","8","9","10"]:
        break
    else: 
      print("\n Informação invalida!\n")
print("\n")      

while True:
    entrega = input("Deseja que entregue ao seu endereço? (s/n), se (sim=s) será cobrado R$ 2,99 : ")
    if entrega.lower() == "s" or entrega.lower() == "n":
          break
    else:
      print("\n Informação invalida! \n")


print("\n")
# Pizzas
menu = int(menu)
if menu == 1:
    pizza = "Frango com Catupiry do Freddy"
    preço = 39.90
    
elif menu == 2:
    pizza = "Calabresa da Foxy"
    preço = 39.90
     
elif menu == 3:
    pizza = "Marguerita da Chica"
    preço = 49.90
      
elif menu == 4:
    pizza = "Pepperoni da Bonnie"
    preço = 49.90
  
elif menu == 5:
    pizza = "Vegetariana do Golden Freddy"
    preço = 29.90

# Verifica se a opção de menu é válida
if menu >= 1 and menu <= 5:
    print("Pizza selecionada:", pizza)
    
    if entrega.lower() == "s":
      preço_entrega = 2.99
      print("Entrega a domicilio")
    elif entrega.lower() == "n":
      preço_entrega = 0
      print("Pedido para retirada no local.")

    quantidade = int(quantidade)
    preço_total = round(preço * quantidade + preço_entrega,2)
    if quantidade >= 1:
        print("Preço total: R$", preço_total)
    data = "20/05/1983"
    print("Data de hoje:", data)
  
print("\n")

print("Nossa pizzaria agradece a sua escolha!")
print("\n")
print("Para pedir pizzas diferentes entre novamente!")
print("\n")
while True:
    afton = input("Antes de ir, deseja comparecer à festa de aniversário do filho mais novo do nosso chefe? (s/n): ")
  
    if afton.lower() == "s":
        print("Ok, esperamos você em nossa pizzaria!")
        break
    elif afton.lower() == "n":
        print("Ok")
        break
    else:
        print("\nInformação inválida!\n")
print("\n")
while True:
    saida = input("Todas as referências foram ao jogo Five Nights at Freddy's. Para sair, digite (sair) :")
    if saida.lower() == "sair":
        break
    else:
        print("Adeus")