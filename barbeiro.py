from menu import menu_barbeiro, menu_sac
from banco import BARBEIROS, CLIENTES, salvar_barbeiro, salvar_cliente
import os
import time

def fluxo_barbeiro(chave):
    opc = 0
    while opc != 7:
        opc = menu_barbeiro()
        if opc == 1:
            info_profissional(chave)
        elif opc == 2:
            gerenciar_servicos(chave)
        elif opc == 3:
            listar_agendamentos(chave)
        elif opc == 4:
            visualizar_historico(chave)
        elif opc == 5:
            central_receita(chave)
        elif opc == 6:
            menu_sac()
        elif opc == 7:
            print("Até logo! Pressione ENTER para continuar.")
            input()
            os.system("cls")
        else:
            print("Opção inválida!")

def info_profissional(chave):
    os.system('cls') 
    medias = 0
    for i in range(len(BARBEIROS[chave]["servicos"])):
        medias += sum(BARBEIROS[chave]["servicos"][i]["avaliacao"])/len(BARBEIROS[chave]["servicos"][i]["avaliacao"])
    if len(BARBEIROS[chave]["servicos"]) == 0:
        media = 0
    else:
        media = medias/len(BARBEIROS[chave]["servicos"])
    print("=============================")
    print("|        Barber´sMap        |")
    print("| Informações Profissionais |")
    print("=============================")
    print(f"Nome: {BARBEIROS[chave]["nome"]}")
    print(f"Email: {BARBEIROS[chave]["email"]}")
    print(f"Endereço: {BARBEIROS[chave]["endereco"]}")
    print(f"Sobre: {BARBEIROS[chave]["sobre"]}")
    print(f"Avaliação média: {media:.2f}")
    print("\n1 - Editar informações")
    print("2 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 2 :
        if opc == 1:
            nome = input("Informe seu novo nome: ")
            email = input("Informe seu novo email: ")
            endereco = input("Informe seu novo endereço: ")
            sobre = input("Informe seu novo texto pessoal: ")
            BARBEIROS[chave]["nome"] = nome
            BARBEIROS[chave]["email"] = email
            BARBEIROS[chave]["endereco"] = endereco
            BARBEIROS[chave]["sobre"] = sobre
            salvar_barbeiro()
            break
        else:
            print("OPÇÂO INVALIDA!")
            opc = int(input("Digite uma opção: "))

def gerenciar_servicos(chave):
    os.system("cls")
    print("=============================")
    print("|        Barber´sMap        |")
    print("|     Painel de Serviços    |")
    print("=============================")
    servicos = BARBEIROS[chave]["servicos"]
    if len(servicos)==0 :
        print("\nNenhum serviço cadastrado.")
    else:
        for i, s in enumerate(servicos, start=1):
            if len(s["avaliacao"]) == 0:
                media = 0
            else: 
                media = sum(s["avaliacao"])/len(s["avaliacao"])
            print(f"{i}. {s['nome']} - R${s['valor']:.2f} | Tempo: {s['tempo']} min | Avaliação média: {media:.2f}")
    print("\n1 - Adiconar serviço")
    print("2 - Editar serviço")
    print("3 - Apagar serviço")
    print("4 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 4: 
        if opc == 1:
            nome = input("Nome do serviço: ")
            valor = float(input("Valor (R$): "))
            tempo = int(input("Tempo estimado (min): "))
            novo_servico = {"nome": nome, "valor": valor, "tempo": tempo, "avaliacao": []}
            BARBEIROS[chave]["servicos"].append(novo_servico)
            salvar_barbeiro()
            print(f"Serviço '{nome}' adicionado com sucesso! Pressione ENTER para continuar.")
            input()
            break
        elif opc == 2:
            nome_servico = input("Digite o nome do serviço que deseja editar: ").lower()
            for i in range(len(BARBEIROS[chave]["servicos"])):
                if nome_servico == BARBEIROS[chave]["servicos"][i]["nome"].lower():
                    nome = input("Informe o novo nome do serviço: ")
                    valor = float(input("Informe o novo valor do serviço: R$"))
                    tempo = int(input("Informe o novo prazo de tempo serviço: "))
                    BARBEIROS[chave]["servicos"][i]["nome"] = nome
                    BARBEIROS[chave]["servicos"][i]["valor"] = valor
                    BARBEIROS[chave]["servicos"][i]["tempo"] = tempo
                    cont = True
                    print("Serviço alterado! Pressione ENTER para continuar.")
                    input()
                    salvar_barbeiro()
                    break
            if cont != True:
                print("Serviço não encontrado no banco de dados!. Tente novamente. Pressione ENTER para continuar.")
                input()
            break
        elif opc == 3:
            nome = input("Digite o nome do serviço que deseja parar de ofertar: ").lower()
            for i in range(len(BARBEIROS[chave]["servicos"])):
                if nome == BARBEIROS[chave]["servicos"][i]["nome"].lower():
                    del BARBEIROS[chave]["servicos"][i]
                    salvar_barbeiro()
                    print("Serviço deletado! Pressione ENTER para continuar.")
                    input()
                    cont = True
                    break
            if cont != True:
                print("Serviço não encontrado no banco de dados! Tente novamente. Pressione ENTER para continuar.")
                input()
            break
        else:
            print("OPÇÂO INVÁLIDA!")
            opc = int(input("Digite uma opção: "))

def listar_agendamentos(chave):
    os.system("cls")
    print("=============================")
    print("|        Barber´sMap        |")
    print("|        Agendamentos       |")
    print("=============================")
    agendamentos = BARBEIROS[chave]["agendamentos"]
    if len(agendamentos)==0:
        print("\nNenhum agendamento ativo.")
    else:
        for a in agendamentos:
            print(f"Cliente: {a['cliente']} | chave: {a['chave']} | Serviço: {a['servico']} | Data: {a['data']}")
    print("\n1 - Cancelar agendamento")
    print("2 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 2:
        if opc == 1:
            nome = input("Informe o nome do cliente que deseja cancelar o agendamento: ").lower()
            for i in range(len(BARBEIROS[chave]["agendamentos"])):
                if nome == BARBEIROS[chave]["agendamentos"][i]["cliente"].lower():
                    for I in range(len(CLIENTES[BARBEIROS[chave]["agendamentos"][i]["chave"]]["agendamentos"])):
                        if chave == CLIENTES[BARBEIROS[chave]["agendamentos"][i]["chave"]]["agendamentos"][i]["chave"]:
                            del CLIENTES[BARBEIROS[chave]["agendamentos"][i]["chave"]]["agendamentos"][i]
                            del BARBEIROS[chave]["agendamentos"][i]
                            print("Agendamento cancelado! Pressione ENTER para continuar.")
                            salvar_barbeiro()
                            salvar_cliente()
                            input()
                            break
                    break
            break
        else:
            print("OPÇÂO INVÁLIDA!")
            opc = int(input("Digite uma opção: "))

def visualizar_historico(chave):
    os.system("cls")
    print("=============================")
    print("|        Barber´sMap        |")
    print("|         Histórico         |")
    print("=============================")
    historico = BARBEIROS[chave]["historico"]
    if len(historico)==0:
        print("\nNenhum serviço realizado ainda.")
    else:
        for h in historico:
            cont = 1
            print(f"{cont}° - Cliente: {h['cliente']} | Serviço: {h['servico']} | Valor: R${h['valor']:.2f} | Data: {h['data']}")
            cont += 1
    print("\n1 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 1:
        print("OPÇÂO INVÁLIDA!")
        opc = int(input("Digite uma opção: "))

def central_receita(chave):
    os.system("cls")
    print("=============================")
    print("|        Barber´sMap        |")
    print("|     Central de Receita    |")
    print("=============================")
    print(f"Total de agendamentos concluidos: {len(BARBEIROS[chave]["historico"])}")
    print(f"Total de agendamentos pendentes: {len(BARBEIROS[chave]["agendamentos"])}")
    soma = 0
    for i in range(len(BARBEIROS[chave]["historico"])):
        if len(BARBEIROS[chave]["historico"]) == 0:
            break
        soma += BARBEIROS[chave]["historico"][i]["valor"]
    print(f"Receita total: R${soma}")
    media = 0
    if len(BARBEIROS[chave]["historico"]) != 0:
        media = soma/len(BARBEIROS[chave]["historico"])
    print(f"Valor médio por serviço: R${media}")
    print("\n1 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 1:
        print("OPÇÂO INVÁLIDA!")
        opc = int(input("Digite uma opção: "))    