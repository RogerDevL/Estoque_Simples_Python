from colorama import Fore, init
init(autoreset=True)


produtos = [] 

def menu():
  print(f"{Fore.GREEN}\nControle de Estoque Simples")
  print(f"{Fore.GREEN}1. Adicionar produto")
  print(f"{Fore.GREEN}2. Remover produto")
  print(f"{Fore.GREEN}3. Atualizar produto")
  print(f"{Fore.GREEN}4. Visualizar estoque")
  print(f"{Fore.GREEN}0. Sair")

  while True:
    opcao = input("Digite sua opção: ")
    if opcao in ("0", "1", "2", "3", "4"):
      return opcao
    else:
      print(f"{Fore.RED}Opção inválida. Tente novamente.")

def adicionar_produto():
  nome = input("Nome do produto: ")
  quantidade = int(input("Quantidade: "))
  preco = float(input("Digite o preço do produto: "))

  produtos.append((nome, quantidade, preco))
  print(f"{Fore.BLUE}O produto {nome} foi adicionado com sucesso!")

def remover_produto():
    if not produtos:
        print(f"{Fore.RED}O estoque está vazio.")
        return

    print("Produtos:")
    for i, produto in enumerate(produtos):
        print(f"{Fore.BLUE}{i + 1}. {produto[0]} - unidades: {produto[1]} - preço: {produto[2]}")

    while True:
        try:
            indice = int(input("Digite o número do produto a remover: ")) - 1
            if 0 <= indice < len(produtos):
                break 
            else:
                print(f"{Fore.RED}inválido. O valor deve estar entre 1 e {len(produtos)}.")
        except ValueError:
            print(f"{Fore.RED}Digite um número inteiro válido.")

    produto_removido, quantidade_removida, preco_removido = produtos.pop(indice)

    print(f"{Fore.BLUE}Produto removido com sucesso!")







def visualizar_estoque():
 
  if not produtos:
    print(f"{Fore.RED}O estoque está vazio.")
    return

  for produto in produtos:
   print(f"{Fore.LIGHTYELLOW_EX}- produto: {produto[0]} - unidades: {produto[1]} -  preço: {produto[2]}")

def atualizar_produto():
    if not produtos:
        print(f"{Fore.RED}O estoque está vazio.")
        return

    print("Produtos:")
    for i, produto in enumerate(produtos):
        print(f"{i + 1}. {produto[0]} ({produto[1]} unidades - R${produto[2]:.2f})")

    while True:
        try:
            indice = int(input("Digite o número do produto a atualizar: ")) - 1
            if 0 <= indice < len(produtos):
                break  # Índice válido, sai do loop
            else:
                print(f"{Fore.RED}Índice inválido. Tente novamente.")
        except ValueError:
            print("Digite um número inteiro.")

    nome_atualizado = input("Digite o novo nome do produto: ")
    quantidade_atualizada = int(input("Digite a nova quantidade: "))
    preco_atualizado = float(input("Digite o novo preço do produto: "))

    produtos[indice] = (nome_atualizado, quantidade_atualizada, preco_atualizado)
    print(f"{Fore.BLUE}O produto {nome_atualizado} foi atualizado com sucesso!")



while True:
  opcao = menu()

  if opcao == "0":
    break
  elif opcao == "1":
    adicionar_produto()
  elif opcao == "2":
    remover_produto()
  elif opcao == "3":
    atualizar_produto()
  elif opcao == "4":
    visualizar_estoque()
