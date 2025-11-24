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

def menu_info_cliente(chave):
    os.system('cls') 
    print("=============================")
    print("|        Barber´sMap        |")
    print("|    Informações Pessoais   |")
    print("=============================")   
    print(f"Nome: {CLIENTES[chave]["nome"]}")
    if len(chave) == 11:
        print(f"CPF: {chave[:3]}.{chave[3:6]}.{chave[6:9]}-{chave[9:11]}")
    elif len(chave) == 14:
        print(f"CNPJ: {chave[:2]}.{chave[2:5]}.{chave[5:8]}/{chave[8:12]}-{chave[12:14]}")
    print(f"Email: {CLIENTES[chave]["email"]}")
    print(f"Senha: {CLIENTES[chave]["senha"]}")
    print("=============================")
    print("1 - Editar informações")
    print("2 - Sair")
    opc = int(input("Digite uma opção: "))
    while opc>2 or opc<1:
        print("Opção inválida!")
        opc = int(input("Digite uma opção: "))
    if opc == 1:
        from cliente import editar_informacoes
        editar_informacoes(chave)

def Menu_administrador(chave):
    os.system('cls') 
    print("=============================")
    print("         Administrador       ")
    print("=============================")
    print("1 - Gerar relatórios")
<<<<<<< HEAD
    print("2 - gerenciar usuário")
    print("3 - Gerenciar serviços")
    print("4 - sair")
    
    try:
        opc = int(input("Digite uma opção: ").strip())
        return opc
    except ValueError:
        return 999
    
=======
    print("2 - gerenciar usuarios")
    print("3 - Gerar serviços")
    print("4 - voltar")
    opc = int(input("Digite uma opção: "))
    return opc
>>>>>>> 015da2ea0c11f55ace51d7d1bdbc437db33079b9

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


