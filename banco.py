menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == "d":
    deposito = input("Quanto deseja depositar? ")
    saldo += float(deposito)
  elif opcao == "s":
    saque = float(input("Quanto deseja sacar? "))
    
    if numero_saques > LIMITE_SAQUES:
      print("Limite de saques atingido")
    elif saque > limite: 
      print("Limite de saque excedido")
    elif saque > saldo:
      print("Saldo insuficiente")
    else:
      numero_saques += 1
      extrato += f"Saque: R$ {saque: .2f}\n"
      saldo -= saque
  elif opcao == "e":
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
  elif opcao == "q":
    break 
  else:
    print("Opção inválida")