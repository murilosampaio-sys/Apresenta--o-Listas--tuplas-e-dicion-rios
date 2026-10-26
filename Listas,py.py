cores = ['vermelho', 'verde', 'azul', 'amarelo', 'branco', 'preto']

escolha = input("Você deseja adicionar uma nova cor? ").upper()

while escolha == 'SIM':

  cor = input("Escreva a cor que você deseja adicionar: ")
  cores.append(cor)
  print("Lista atual:", cores)

  trocar_cor = input("Você deseja substituir uma cor por outra? ").upper()
  if trocar_cor == 'SIM':
    index = int(input("Digite o índice da cor que deseja substituir: "))
    nova_cor = input("Digite a nova cor: ")
    cores[index] = nova_cor
    print("Lista atual:", cores)

  escolha2 = input("Você deseja excluir uma cor? ").upper()
  if escolha2 == 'SIM':
    index = int(input("Digite o índice da cor que deseja excluir: "))
    cores.pop(index) 
    print("Lista atual:", cores)

  escolha = input("Você deseja adicionar outra cor? ").upper()

print("\nLista final de cores:", cores)