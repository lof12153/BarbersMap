#%%
from banco import BARBEIROS, ADMINISTRADORES, CLIENTES, salvar_barbeiro, salvar_cliente, salvar_admin
import os
import time

def buscar_servico_por_nome(palavra_chave, dados_barbeiros):
    resultados = []
    palavra_chave = palavra_chave.lower().strip()

    if not palavra_chave:
        return resultados

    for chave, info_barbeiro in dados_barbeiros.items():
        
        if "servicos" not in info_barbeiro:
            continue
        
        lista_servicos = info_barbeiro["servicos"]

        if "nome" in info_barbeiro:
            nome_barbeiro = info_barbeiro["nome"]
        else:
            nome_barbeiro = "Barbeiro não encontrado"
            
        for servico in lista_servicos:
            
            if "nome" not in servico:
                continue
            
            nome_servico = servico["nome"]
            nome_servico_padrao = nome_servico.lower().strip()

            if palavra_chave in nome_servico_padrao:
                
                if "valor" in servico:
                    valor_servico = servico["valor"]
                else:
                    valor_servico = "Valor não definido"

                # formataçao
                resultado = f"Serviço: {nome_servico} - R${valor_servico:.2f} - Oferecido por: {nome_barbeiro}"
                resultados.append(resultado)
    return resultados


def fluxo_buscar_servicos():
    while True:
        os.system('cls') 
        print("=============================")
        print("         Barber'sMap         ")
        print("      Busca de serviços      ")
        print("=============================")
        print("(Para voltar ao menu, pressione enter deixando o espaço em branco)\n")
        busca = input("Digite o serviço que deseja buscar: ")
        
        if not busca:
            print("Voltando ao menu...")
            time.sleep(1) 
            break

        result = buscar_servico_por_nome(busca, BARBEIROS)


        if not result:
            print(f"\nNenhum serviço encontrado com esse nome.")
            print("Por favor, tente novamente.")
            time.sleep(3) 
        else:
            print(f"\n---Resultados da Busca para '{busca}'---")
            for r in result:
                print(r)

            print("\nPressione Enter para voltar ao menu...")
            input()
            break
#%%

fluxo_buscar_servicos()