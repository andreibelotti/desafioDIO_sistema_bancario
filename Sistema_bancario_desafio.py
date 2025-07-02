def depositar(saldo, valor, extrato):
    """
    Realiza um depósito na conta.
    Retorna o novo saldo e o extrato atualizado.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido. Por favor, insira um valor positivo.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque da conta.
    Retorna o novo saldo, o extrato atualizado e o novo número de saques.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(f"Operação falhou! Você não tem saldo suficiente. Seu saldo é R${saldo:.2f}")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite." \
        "limite de saque R$500,00")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido. Por favor, insira um valor positivo.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    """
    Exibe o extrato da conta, incluindo todas as movimentações e o saldo atual.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

def main():
    """
    Função principal que gerencia o fluxo do sistema bancário.
    """
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = input("Informe o valor do depósito: ")
            # Garante que o input seja um número válido
            try:
                valor = float(valor)
                saldo, extrato = depositar(saldo, valor, extrato)
            except ValueError:
                print("Valor inválido! Por favor, digite um número para o depósito.")

        elif opcao == "s":
            valor = input("Informe o valor do saque: ")
            # Garante que o input seja um número válido
            try:
                valor = float(valor)
                saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )
            except ValueError:
                print("Valor inválido! Por favor, digite um número para o saque.")

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Saindo do sistema. Obrigado por usar nosso banco!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Garante que a função main() seja executada quando o script for rodado
if __name__ == "__main__":
    main()