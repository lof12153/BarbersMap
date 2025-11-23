from banco import BARBEIROS, CLIENTES, salvar_barbeiro, salvar_cliente
import os

def painel_busca(chave):
    os.system("cls")
    print("=============================")
    print("|        Barber´sMap        |")
    print("|   Barbeiros Disponiveis   |")
    print("=============================")
    cont = 1
    filtrar_nota = []
    filtrar_preco = []
    for barbeiro in BARBEIROS:
        media = 0
        preco_medio = 0
        for i in range(len(BARBEIROS[barbeiro]["servicos"])):
            media += sum(BARBEIROS[barbeiro]["servicos"][i]["avaliacao"])/len(BARBEIROS[barbeiro]["servicos"][i]["avaliacao"])
            preco_medio += BARBEIROS[barbeiro]["servicos"][i]["valor"]
        if len(BARBEIROS[barbeiro]["servicos"]) == 0:
            media = 0
            preco_medio = 0
        else:
            media = media/len(BARBEIROS[barbeiro]["servicos"])
            preco_medio = preco_medio/len(BARBEIROS[barbeiro]["servicos"])
        filtrar_nota.append(media)
        filtrar_preco.append(preco_medio)
        print(f"{cont}° Barbeiro")
        print(f"Nome: {BARBEIROS[barbeiro]["nome"]}")
        print(f"Nota Media: {media:.2f}")
        print(f"Preço Médio: R${preco_medio:.2f}\n")
        cont += 1
        if cont >= 10:
            break
    print("=============================")
    print("1 - Pesquisar")
    print("2 - Filtrar Resultados por Nota")
    print("3 - Sair")
    opc = input("Digite uma opção: ")
    filtrar_nota.sort(reverse=True)
    filtrar_preco.sort()
    for i in range(len(filtrar_preco)):
        for barbeiro in BARBEIROS:
            preco_medio = 0
            for c in range(len(BARBEIROS[barbeiro]["servicos"])):
                preco_medio += BARBEIROS[barbeiro]["servicos"][c]["valor"]
            if len(BARBEIROS[barbeiro]["servicos"]) == 0:
                    preco_medio = 0
            else:
                preco_medio = preco_medio/len(BARBEIROS[barbeiro]["servicos"])
            if filtrar_preco[i] == preco_medio:
                filtrar_preco[i] = barbeiro
                break
    for i in range(len(filtrar_nota)):
        for barbeiro in BARBEIROS:
            media = 0
            for c in range(len(BARBEIROS[barbeiro]["servicos"])):
                media += sum(BARBEIROS[barbeiro]["servicos"][c]["avaliacao"])/len(BARBEIROS[barbeiro]["servicos"][c]["avaliacao"])
            if len(BARBEIROS[barbeiro]["servicos"]) == 0:
                media = 0
            else:
                media = media/len(BARBEIROS[barbeiro]["servicos"])
            if filtrar_nota[i] == media:
                filtrar_nota[i] = barbeiro
                break
    while opc != "3":
        if opc == "1":
            nome = input("Digite o nome do barbeiro: ")
            for barbeiro in BARBEIROS:
                if nome == BARBEIROS[barbeiro]["nome"]:
                    if chave == False:
                        from cadastroElogin import fluxo_cadastrar
                        fluxo_cadastrar()
                        break
                    else:
                        busca(barbeiro, chave)
                        break
                else:
                    cont = False
            if cont == False:
                print("Nome não encontrado! Pressione ENTER para continuar.")
                input()
            break
        elif opc == "2":
            conta = 1
            os.system("cls")
            print("=============================")
            print("|        Barber´sMap        |")
            print("|   Barbeiros Disponiveis   |")
            print("=============================")
            for i in range(len(filtrar_nota)):
                media = 0
                preco_medio = 0
                for I in range(len(BARBEIROS[filtrar_nota[i]]["servicos"])):
                    media += sum(BARBEIROS[filtrar_nota[i]]["servicos"][I]["avaliacao"])/len(BARBEIROS[filtrar_nota[i]]["servicos"][I]["avaliacao"])
                    preco_medio += BARBEIROS[filtrar_nota[i]]["servicos"][I]["valor"]
                if len(BARBEIROS[filtrar_nota[i]]["servicos"]) == 0:
                    media = 0
                    preco_medio = 0
                else:
                    media = media/len(BARBEIROS[filtrar_nota[i]]["servicos"])
                    preco_medio = preco_medio/len(BARBEIROS[filtrar_nota[i]]["servicos"])
                print(f"{conta}° Barbeiro")
                print(f"Nome: {BARBEIROS[filtrar_nota[i]]["nome"]}")
                print(f"Nota Media: {media:.2f}")
                print(f"Preço Médio: R${preco_medio:.2f}\n")
                conta += 1
            print("=============================")
            print("1 - Pesquisar")
            print("2 - Filtrar Resultados por Preço")
            print("3 - Sair")
            opc = input("Digite uma opção: ")
            os.system("cls")
            if opc == "2":
                opc = "FILTRAR PREÇO"
        elif opc == "FILTRAR PREÇO":
            conta = 1
            os.system("cls")
            print("=============================")
            print("|        Barber´sMap        |")
            print("|   Barbeiros Disponiveis   |")
            print("=============================")
            for i in range(len(filtrar_preco)):
                media = 0
                preco_medio = 0
                for I in range(len(BARBEIROS[filtrar_preco[i]]["servicos"])):
                    media += sum(BARBEIROS[filtrar_preco[i]]["servicos"][I]["avaliacao"])/len(BARBEIROS[filtrar_preco[i]]["servicos"][I]["avaliacao"])
                    preco_medio += BARBEIROS[filtrar_preco[i]]["servicos"][I]["valor"]
                if len(BARBEIROS[filtrar_preco[i]]["servicos"]) == 0:
                    media = 0
                    preco_medio = 0
                else:
                    media = media/len(BARBEIROS[filtrar_preco[i]]["servicos"])
                    preco_medio = preco_medio/len(BARBEIROS[filtrar_preco[i]]["servicos"])
                print(f"{conta}° Barbeiro")
                print(f"Nome: {BARBEIROS[filtrar_preco[i]]["nome"]}")
                print(f"Nota Media: {media:.2f}")
                print(f"Preço Médio: R${preco_medio:.2f}\n")
                conta += 1
            print("=============================")
            print("1 - Pesquisar")
            print("2 - Filtrar Resultados por Nota")
            print("3 - Sair")
            opc = input("Digite uma opção: ")
        else:
            print("Opção inválida! Digite uma das opções abaixo.")
            print("1 - Pesquisar")
            print("2 - Filtrar Resultados")
            print("3 - Sair")
            opc = input("Digite uma opção: ")

def busca(barbeiro, chave):
    os.system('cls') 
    media = 0
    for i in range(len(BARBEIROS[barbeiro]["servicos"])):
        media += sum(BARBEIROS[barbeiro]["servicos"][i]["avaliacao"])/len(BARBEIROS[barbeiro]["servicos"][i]["avaliacao"])
    if len(BARBEIROS[barbeiro]["servicos"]) == 0:
        media = 0
    else:
        media = media/len(BARBEIROS[barbeiro]["servicos"])
    print("=============================")
    print("|        Barber´sMap        |")
    print("| Informações Profissionais |")
    print("=============================")
    print(f"Nome: {BARBEIROS[barbeiro]["nome"]}")
    print(f"Email: {BARBEIROS[barbeiro]["email"]}")
    print(f"Endereço: {BARBEIROS[barbeiro]["endereco"]}")
    print(f"Sobre: {BARBEIROS[barbeiro]["sobre"]}")
    print(f"Avaliação média: {media:.2f}")
    print("\n1 - Serviços")
    print("2 - Voltar")
    opc = input("Digite uma opção: ")
    while opc != "2":
        if opc == "1":
            print("=============================")
            print("|        Barber´sMap        |")
            print("|    Serviços Disponiveis   |")
            print("=============================")
            for i in range(len(BARBEIROS[barbeiro]["servicos"])):
                print(f"{i+1}° Serviço")
                print(f"Nome: {BARBEIROS[barbeiro]["servicos"][i]["nome"]}")
                print(f"Valor: R${BARBEIROS[barbeiro]["servicos"][i]["valor"]}")
                print(f"Tempo médio: {BARBEIROS[barbeiro]["servicos"][i]["tempo"]} minutos\n")
            print("=============================")
            print("1 - Escolher Serviço")
            print("2 - Voltar")
            esc = input("Digite uma opção: ")
            while esc != "2":
                if esc == "1":
                    escolha = input("Digite o nome do serviço: ").lower().strip()
                    cont = False
                    for i in range(len(BARBEIROS[barbeiro]["servicos"])):
                        if escolha == BARBEIROS[barbeiro]["servicos"][i]["nome"].lower().strip():
                            cont = True
                            data = input("Informe a data (dd\mm): ")
                            BARBEIROS[barbeiro]["agendamentos"].append({
                                "cliente": CLIENTES[chave]["nome"],
                                "chave": chave,
                                "servico": escolha,
                                "valor": BARBEIROS[barbeiro]["servicos"][i]["valor"],
                                "data": data
                            })
                            CLIENTES[chave]["agendamentos"].append({
                                "barbeiro": BARBEIROS[barbeiro]["nome"],
                                "chave": barbeiro,
                                "valor": BARBEIROS[barbeiro]["servicos"][i]["valor"],
                                "data": data,
                                "servico": escolha
                            })
                            salvar_barbeiro()
                            salvar_cliente()
                            break
                    if cont == False:
                        print("Serviço não encontrado!")
                    else:
                        break
                else:
                    print("Opção inválida!")
                    esc = input("Digite uma opção: ")
            break
        else:
            print("Opção inválida!")
            opc = input("Digite uma opção: ")


