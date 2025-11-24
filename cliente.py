from menu import menu_cliente, menu_sac, menu_info_cliente
from pesquisa import painel_busca
from banco import CLIENTES, BARBEIROS, salvar_cliente, salvar_barbeiro
import os
import time

def fluxo_cliente(chave):
    opc = 0
    while opc != 6:
        opc = menu_cliente()
        if opc == 1:
            painel_busca(chave)
        elif opc == 2:
            menu_info_cliente(chave)
        elif opc == 3:
            agendamentos_cliente(chave)
        elif opc == 4:
            historico_cliente(chave)
        elif opc == 5:
            menu_sac()
        elif opc == 6:
            print("Até logo! Pressione ENTER para continuar.")
            input()
            os.system("cls")
        else:
            print("Opção inválida!")


def editar_informacoes(chave):
    nome = input("Informe seu novo nome: ").strip()
    while True:
        if not nome == "":
            break
        else:
            nome = input("Digite um nome válido!: ").strip()
    email = input("Informe seu novo Email: ").strip()
    while True:
        if "@gmail.com" in email or "@hotmail.com" in email or "@outlook.com" in email or "@mail.com" in email:
            break
        else:
            email = input("Email inválido! Informe seu novo email: ")
    while True:
        senha = str(input("Informe sua senha : "))
        if senha.islower():
            print("A senha deve ter pelo menos um caractere MAIUSCULO: ")
        elif len(senha) < 7 :
            print("A senha deve ter pelo menos 8 caracteres: ")
        elif senha.isalpha() :
            print("A senha deve ter pelo menos 1 número: ")
        elif senha.isalnum() :
            print("A senha deve ter pelo menos 1 caractere especial (!@#$%¨&*): ")
        else:
            break
    CLIENTES[chave]["nome"] = nome
    CLIENTES[chave]["email"] = email
    CLIENTES[chave]["senha"] = senha
    for chave in BARBEIROS:
        for I in range(len(BARBEIROS[chave]["agendamentos"])):
            if BARBEIROS[chave]["agendamentos"][I]["chave"] == chave:
                BARBEIROS[chave]["agendamentos"][I]["cliente"] = nome
        for i in range(len(BARBEIROS[chave]["historico"])):
            if BARBEIROS[chave]["historico"][i]["chave"] == chave:
                BARBEIROS[chave]["historico"][i]["cliente"] = nome
    print("Informações alteradas com sucesso! Pressione ENTER para continuar.")
    input()
    salvar_cliente()
    os.system('cls') 

def agendamentos_cliente(chave):
    os.system('cls') 
    print("=============================")
    print("|        Barber´sMap        |")
    print("|        Agendamentos       |")
    print("=============================")
    for i in range(len(CLIENTES[chave]["agendamentos"])):
        print(f"{i+1}° Agendamento:")
        print(f"Serviço: {CLIENTES[chave]["agendamentos"][i]["servico"]}")
        print(f"Barbeiro: {CLIENTES[chave]["agendamentos"][i]["barbeiro"]}")
        print(f"Valor: R${CLIENTES[chave]["agendamentos"][i]["valor"]}  -  Data: {CLIENTES[chave]["agendamentos"][i]["data"]}\n")
    if len(CLIENTES[chave]["agendamentos"]) == 0:
        print("Nenhum agendamento marcado!")
        print("\n1 - Voltar")
        opc = int(input("Digite uma opção: "))
        while opc != 1:
            print("Opção inválida!")
            opc = int(input("Digite uma opção: "))
            os.system('cls') 
    else:
        print("1 - Cancelar agendamento")
        print("2 - Concluir agendamento")
        print("3 - Voltar")
        opc = int(input("Digite uma opção: "))
        while opc>3 or opc<1:
            print("Opção inválida!")
            opc = int(input("Digite uma opção: "))
        if opc == 1:
            servico = input("Informe o nome do serviço que deseja cancelar o agendamento: ")
            for i in range(len(CLIENTES[chave]["agendamentos"])):
                if servico.lower().strip() == CLIENTES[chave]["agendamentos"][i]["servico"].lower().strip():
                    for I in range(len(BARBEIROS[CLIENTES[chave]["agendamentos"][i]["chave"]]["agendamentos"])):
                        if chave == BARBEIROS[CLIENTES[chave]["agendamentos"][i]["chave"]]["agendamentos"][I]["chave"]:
                            del BARBEIROS[CLIENTES[chave]["agendamentos"][i]["chave"]]["agendamentos"][I]
                            del CLIENTES[chave]["agendamentos"][i]
                            print("Agendamento cancelado! Pressione ENTER para continuar.")
                            salvar_cliente()
                            salvar_barbeiro()
                            input()
                            os.system('cls') 
                            break
                else:
                    print("Serviço não encontrado!")
                    os.system('cls') 
        elif opc == 2:
            servico = input("Informe o nome do serviço que deseja confirmar a realização: ")
            for i in range(len(CLIENTES[chave]["agendamentos"])):
                if servico.lower().strip() == CLIENTES[chave]["agendamentos"][i]["servico"].lower().strip():
                    for I in range(len(BARBEIROS[CLIENTES[chave]["agendamentos"][i]["chave"]]["agendamentos"])):
                        if chave == BARBEIROS[CLIENTES[chave]["agendamentos"][i]["chave"]]["agendamentos"][I]["chave"] and servico.lower().strip() == BARBEIROS[CLIENTES[chave]["agendamentos"][i]["chave"]]["agendamentos"][I]["servico"]:
                            CLIENTES[chave]["historico"].append(CLIENTES[chave]["agendamentos"][i])
                            BARBEIROS[CLIENTES[chave]["agendamentos"][i]["chave"]]["historico"].append(BARBEIROS[CLIENTES[chave]["agendamentos"][i]["chave"]]["agendamentos"][I])
                            del BARBEIROS[CLIENTES[chave]["agendamentos"][i]["chave"]]["agendamentos"][I]
                            del CLIENTES[chave]["agendamentos"][i]
                            nota = float(input("De uma nota para o serviço [0 a 5]: "))
                            while nota>5 or nota<0:
                                print("A nota tem que ser entre 0 e 5!")
                                nota = float(input("De uma nota para o serviço [0 a 5]: "))
                            for P in range(len(BARBEIROS[CLIENTES[chave]["historico"][i]["chave"]]["servicos"])):
                                if BARBEIROS[CLIENTES[chave]["historico"][i]["chave"]]["servicos"][i]["nome"] == CLIENTES[chave]["historico"][len(CLIENTES[chave]["historico"])-1]["servico"]:
                                    BARBEIROS[CLIENTES[chave]["historico"][i]["chave"]]["servicos"][i]["avaliacao"].append(nota)
                            print("Agendamento concluido! Muito obrigado! Pressione ENTER para continuar!")
                            salvar_cliente()
                            salvar_barbeiro()
                            input()
                            os.system('cls') 
                            break
                    else:
                        print("Serviço não encontrado!")
                        os.system('cls') 

def historico_cliente(chave):
    os.system('cls') 
    print("=============================")
    print("|        Barber´sMap        |")
    print("|         Histórico         |")
    print("=============================")
    for i in range(len(CLIENTES[chave]["historico"])):
        print(f"Serviço concluido N{i+1}°:")
        print(f"Serviço: {CLIENTES[chave]["historico"][i]["servico"]}")
        print(f"Barbeiro: {CLIENTES[chave]["historico"][i]["barbeiro"]}")
        print(f"Valor: R${CLIENTES[chave]["historico"][i]["valor"]}  -  Data: {CLIENTES[chave]["historico"][i]["data"]}\n")
    if len(CLIENTES[chave]["historico"]) == 0:
        print("Histórico vazio!")
    print("\n1 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 1:
        print("Opção inválida!")
        opc = int(input("Digite uma opção: "))
    os.system('cls') 
