import mysql.connector

import conexaoBD

db_connection = conexaoBD.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def cadastrarMotorista(cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento):
    try:
        sql = "insert into motorista(cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento) values ('{}','{}','{}','{}','{}','{}','{}')".format(cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento)
        con.execute(sql) # prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, "Inserido!!")
    except Exception as erro:
        print(erro)
def consultar():#Consultar os dados do banco de dados
    try:
        sql =  'select from motorista where CPF'
        con.execute(sql)
        for (cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento) in con:
            print("CPF:  " + cpf + "\n" + "Nome:  " + nome + "\n" + "Telefone:  " + telefone + "\n"+ "Endereço:  " + endereco + "\n"+ "Modelo do Veiculo:  " + modelo + "\n" + "Placa do Veiculo:  " + placa + "\n"+ "Data De Nascimento:  "+ dataDeNascimento)
            print("\n")
    except Exception as erro:
        print(erro)

def atualizarNome(codigo, nome ): #Atualizar os dados no banco de dados
    try:
        sql = "update cliente set nome = '{}' where codigo = '{}'".format(nome,codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Nome Atualizado")
    except Exception as erro:
        print(erro)

def atualizarTelefone(codigo, telefone):  # Atualizar os dados no banco de dados
    try:
        sql = "update cliente set telefone = '{}' where codigo = '{}'".format(telefone, codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Telefone Atualizado")
    except Exception as erro:
        print(erro)

def atualizarEndereco(codigo, endereco):  # Atualizar os dados no banco de dados
    try:
        sql = "update cliente set endereco = '{}' where codigo = '{}'".format(endereco, codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Endereco Atualizado")
    except Exception as erro:
        print(erro)

def atualizarDataAtual(codigo, dataAtual):  # Atualizar os dados no banco de dados
    try:
        sql = "update cliente set endereco = '{}' where codigo = '{}'".format(dataAtual, codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Data Atualizada")
    except Exception as erro:
        print(erro)

def excluir(codigo):
    try:
        sql = "delete from cliente where codigo = '{}'".format(codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Deletado!")
    except Exception as erro:
        print(erro)


