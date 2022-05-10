import operacoes, this
this.opcao = -1

def menu():
    print("Escolha uma das opções abaixo: \n\n" +
          "1. Cadastrar Motorista \n" +
          "2. Consultar Tudo \n" +
          "0. Sair")
    this.opcao = int(input())
def operacao():
    while (this.opcao != 0):
        menu()
        if this.opcao == 1:
            print("Informe seu CPF: ")
            cpf = input()
            print("Informe seu Nome: ")
            nome = input()
            print("Informe seu Telefone: ")
            telefone = input()
            print("Informe o seu Endereço: ")
            endereco = input()
            print("Informe o Modelo do Veiculo")
            modelo = input()
            print("Informe A Placa do Veiculo")
            placa = input()
            print("Informe Sua Data de nascimento: ")
            dataDeNascimento = input()

            #Ultilizar o método cadastrar
            operacoes.cadastrarMotorista(cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento)
        elif this.opcao == 2:
            print("Informe o CPF que deseja Consultar:")
            cpf = int(input())
            operacoes.consultar()

        elif this.opcao == 3:
            print("Informe seu CPF: ")
            CPF = input()
            print("Informe o novo Nome: ")
            nome = input()
            operacoes.atualizarNome(CPF, nome)
        elif this.opcao == 4:
            print("Informe seu CPF: ")
            CPF = input()
            print("Informe o novo Telefone: ")
            telefone = input()
            operacoes.atualizarTelefone(CPF, telefone)
        elif this.opcao == 5:
            print("Informe seu CPF: ")
            CPF = input()
            print("Informe o novo Endereço: ")
            endereco = input()
            operacoes.atualizarEndereco(CPF, endereco)
        elif this.opcao == 6:
            print("Informe seu CPF: ")
            CPF = input()
            print("Informe a nova Data: ")
            data = input()
            operacoes.atualizarDataAtual(CPF, modelo)
        elif this.opcao == 7:
            print("Informe seu CPF: ")
            CPF = input()
            print("Informe a nova Data: ")
            data = input()
            operacoes.atualizarDataAtual(CPF, Placa)
        elif this.opcao == 8:
            print("Informe seu CPF: ")
            CPF = input()
            print("Informe a nova Data: ")
            data = input()
            operacoes.atualizarDataAtual(CPF, Data)
        elif this.opcao == 9:
            print("Informe seu CPF: ")
            CPF = input()
            operacoes.excluir(CPF)
        elif this.opcao == 0:
            print("Obrigado!")