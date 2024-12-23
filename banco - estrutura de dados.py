import textwrap

def menu():
  menu = """
  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [nc]\tNova Conta
  [nu]\tNovo Usuário
  [q] Sair

  ==> """
  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
  if valor > 0:
    saldo += valor
    extrato += f"Depósito de R$ {valor:.2f}\n"
    print("Depósito realizado com sucesso!")
  else:
    print("Valor inválido")
  return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= limite_saques

  if excedeu_saldo:
    print("Saldo insuficiente")
  elif excedeu_limite:
    print("Valor de saque excedido")
  elif excedeu_saques:
    print("Limite de saques excedido")
  elif valor > 0:
    saldo -= valor
    extrato += f"Saque de R$ {valor:.2f}\n"
    numero_saques += 1
    print("Saque realizado com sucesso!")
  else:
    print("Operação falhou")
  return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
      print("\n================ EXTRATO ================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo:\t\tR$ {saldo:.2f}")
      print("==========================================")

def criar_usuario(usuarios):
  cpf = input("Digite o CPF: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Usuário já cadastrado")
    return

  nome = input("Digite o nome: ")
  data_nascimento = input("Digite a data de nascimento: ")
  endereco = input("Digite o endereço: ")

  usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
  print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Digite o CPF do usuário: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("conta criada com sucesso!")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

  print("Usuário não encontrado")

def main():
  LIMITE_SAQUES = 3
  AGENCIA = "001"

  saldo = 0 
  limite = 500
  extrato = ""
  numero_saques = 0
  usuarios = []
  contas = []

  while True:
    opcao = menu()

    if opcao == "d":
      valor = float(input("Quanto deseja depositar? "))

      saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "s":
      valor = float(input("Quanto deseja sacar? "))
      
      saldo, extrato = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=LIMITE_SAQUES,
      )
    elif opcao == "e":
      exibir_extrato(saldo, extrato=extrato)
    elif opcao == "nu":
      criar_usuario(usuarios)
    elif opcao == "nc":
      numero_conta = len(contas) + 1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)

      if conta:
        contas.append(conta)
    elif opcao == "q":
      break 
    else:
      print("Opção inválida")

main()