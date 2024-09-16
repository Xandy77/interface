from modulo import *

# Programa principal
if __name__ == "__main__":
    cc = ContaCorrente('Fulano', '123.456.789-12', '1001-1', '10010-1', 0)

    # Entrada de dados
    cc.nome = input('Informe o nome do titular: ')
    cc.cpf = input('Informe o CPF do titular: ')

    # Exibe informações da conta
    print(f'\nNome: {cc.nome}.')
    print(f'CPF: {cc.cpf}.')
    print(f'Agência: {cc.agencia}.')
    print(f'Conta: {cc.conta}.')
    print(f'Saldo: R${cc.consultar_saldo():.2f}')
    

    # Menu de operações
    while True:
        print("\nEscolha uma operação:")
        print("1. Saque")
        print("2. Depósito")
        print("3. Sair")
        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            valor = float(input("Digite o valor do saque: "))
            if cc.fazer_saque(valor):
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
            print(f"Saldo atual: R${cc.consultar_saldo():.2f}")

        elif escolha == '2':
            valor = float(input("Digite o valor do depósito: "))
            cc.fazer_deposito(valor)
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            print(f"Saldo atual: R${cc.consultar_saldo():.2f}")

        elif escolha == '3':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

'''
Complete o programa: o usuário vai informar o nome e o CPF, e o programa informa qual a agência, conta e saldo. E aí o usuário vai poder escolher se deseja fazer saque, depósito ou sair do programa.
'''
