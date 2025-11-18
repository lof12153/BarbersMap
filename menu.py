from banco import ADMINISTRADORES, CLIENTES, BARBEIROS
import os


def menu():
    os.system('cls') 
    print("=============================")
    print("|        Barber´sMap        |")
    print("|   Serviços de barbeiros   |")
    print("=============================")
    print("1 - Buscar serviços disponiveis")
    print("2 - Login")
    print("3 - Cadastrar-se")
    print("4 - Atendimento ao consumidor")
    print("5 - Sair")
    opc = int(input("Digite uma opção: "))
    return opc

def menu_barbeiro():
    os.system('cls') 
    print("=============================")
    print("|        Barber´sMap        |")
    print("|   Interface do Barbeiro   |")
    print("=============================")
    print("1 - Informações profissionais")
    print("2 - Serviços")
    print("3 - Agendamentos")
    print("4 - Histórico")
    print("5 - Receita")
    print("6 - Suporte")
    print("7 - Sair")
    opc = int(input("Digite uma opção: "))
    return opc

def menu_cliente():
    os.system('cls') 
    print("=============================")
    print("|        Barber´sMap        |")
    print("|   Serviços de barbeiros   |")
    print("=============================")
    print("1 - Buscar serviços disponiveis")
    print("2 - Informações pessoais")
    print("3 - Agendamentos")
    print("4 - Histórico")
    print("5 - Atendimento ao consumidor")
    print("6 - Sair")
    opc = int(input("Digite uma opção: "))
    return opc

def menu_info_cliente(cpf):
    os.system('cls') 
    print("=============================")
    print("|        Barber´sMap        |")
    print("|    Informações Pessoais   |")
    print("=============================")   
    print(f"Nome: {CLIENTES[cpf]["nome"]}")
    print(f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}")
    print(f"Email: {CLIENTES[cpf]["email"]}")
    print(f"Senha: {CLIENTES[cpf]["senha"]}")
    print("=============================")
    print("1 - Editar informações")
    print("2 - Sair")
    opc = int(input("Digite uma opção: "))
    while opc>2 or opc<1:
        print("Opção inválida!")
        opc = int(input("Digite uma opção: "))
    if opc == 1:
        from cliente import editar_informacoes
        editar_informacoes(cpf)

def Menu_administrador():
    os.system('cls') 
    print("=============================")
    print("         Administrador       ")
    print("=============================")
    print("1 - Gerar relatórios")
    print("2 - gerenciar usuarios")
    print("3 - Gerar serviços")
    print("4 - voltar")
    opc = int(input("Digite uma opção: "))
    return opc

def menu_sac():
    os.system('cls') 
    print("=============================")
    print("|        Barber´sMap        |")
    print("|   Canais de Atendimento   |")
    print("=============================")
    print("Email: barbersmap@gmail.com")
    print("Telefone e Whatsapp: (73) 98248-9941")
    print("Redes Sociais: @BarbersMap")
    print("1 - Sair")
    opc = int(input("Digite uma opção: "))
    while not opc == 1:
        print("Opção invalida!")
        opc = int(input("Digite uma opção: "))
    return opc


