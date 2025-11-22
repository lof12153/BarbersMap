
from menu import Menu_administrador
from banco import BARBEIROS, ADMINISTRADORES, CLIENTES, salvar_barbeiro, salvar_cliente, salvar_admin
import os
import time

def validacao_chave(chave):
    os.system('cls')
    listar_usuarios()
    chave = input('\nInforme o chave do usuario que deseja gerenciar: ').strip()

    if chave in ADMINISTRADORES:
        print("Não é possivel gerenciar usuário do tipo administrador.")
        time.sleep(3)
        return validacao_chave(chave)
    elif chave in CLIENTES:
        return fluxo_administrador(chave) 
    elif chave in BARBEIROS:
        return fluxo_administrador(chave)
    else:
        print("chave não encontrado.")
        time.sleep(2)
        return validacao_chave(chave)


def fluxo_administrador(chave):
    opc = 0

    while opc != 4:
        opc = Menu_administrador(chave)

        if opc == 1:
            fluxo_gerar_relatorios(chave) 
        elif opc == 2:
            fluxo_gerenciar_usuarios(chave)
        elif opc == 3:
            print("Trabalho em andamento")
            time.sleep(2)
        elif opc == 4:
            print("Até logo!")
            time.sleep(2)
            os.system("cls")
        else:
            print("opção inválida!")
            time.sleep(2)


def fluxo_gerenciar_usuarios(chave):
    os.system('cls')
    print("=============================")
    print("      gerenciar usuário      ")
    print("=============================")
    
    if chave in CLIENTES:
        print("\nDados do usuário Cliente:")
        print(f"Nome: {CLIENTES[chave]['nome']}")
        print(f"Email: {CLIENTES[chave]['email']}")
        print(f"Senha: {CLIENTES[chave]['senha']}")
        print(f"histórico: {CLIENTES[chave]['historico']}")
    elif chave in BARBEIROS:
        print("\nDados do usuário Barbeiro:")
        print(f"Nome: {BARBEIROS[chave]['nome']}")
        print(f"Email: {BARBEIROS[chave]['email']}")
        print(f"Senha: {BARBEIROS[chave]['senha']}")
        print(f"histórico {BARBEIROS[chave]['historico']}")
    elif chave in ADMINISTRADORES:
        print('Não é possivel gerenciar esse usuário!')
        time.sleep(3)
        return fluxo_administrador(chave)
    else:
        print("chave não encontrado")
        return fluxo_administrador(chave)
    
    print("\n1 - editar usuário")
    print("2 - excluir usuário")
    print("3 - Voltar")

    try:
        opc = int(input("Escolha uma opção: "))

        if opc == 1:
            editar_usuario(chave)
            listar_usuarios()
            time.sleep(3)
            return fluxo_administrador(chave)
        elif opc == 2:
            deletar_usuario(chave)
            listar_usuarios()
            time.sleep(3)
            return fluxo_administrador(chave)
        elif opc == 3:
            return fluxo_administrador(chave)
        else:
            print("opção inválida")
            time.sleep(2)
            return fluxo_administrador(chave)
    except ValueError:
        print("opção inválida")
        return fluxo_administrador(chave)


def fluxo_gerar_relatorios(chave):
    os.system('cls')
    print("=============================")
    print("          Relatórios         ")
    print("=============================")
    
    if chave in CLIENTES:
        print('Não é possivel gerar relatórios de usuário que não oferta serviços.')
        time.sleep(3)
        return fluxo_administrador(chave)
    elif chave in BARBEIROS:
        print('====relatório de desempenho do barbeiro====')
        print("\nDados do usuário Barbeiro:")
        print(f"Nome: {BARBEIROS[chave]['nome']}")
        print(f"Email: {BARBEIROS[chave]['email']}")
        print(f"Senha: {BARBEIROS[chave]['senha']}")
        print(f"histórico {BARBEIROS[chave]['historico']}")
        servico_popular(chave)
        
        try:
            opc = int(input('\nDigite 1 para voltar ao menu anterior: '))
            if opc == 1:
                return fluxo_administrador(chave)
            else:
                print("Opção inválida!")
                time.sleep(2)
                return fluxo_administrador(chave)
        except ValueError:
            print("Opção inválida!")
            time.sleep(2)
            return fluxo_administrador(chave)
            
    elif chave in ADMINISTRADORES:
        print('Não é possivel gerar relatórios de um usuário que não oferta serviços.')
        time.sleep(3)
        return fluxo_administrador(chave)
    else:
        print("CPF ou CNPJ não encontrado")
        time.sleep(2)
        return fluxo_administrador(chave)


def listar_usuarios():
   print("\n=== Lista de Usuários ===")

   print("\nAdministradores:")
   for chave, admin_data in ADMINISTRADORES.items():
     print(f"chave: {chave} | nome: {admin_data['nome']} | email: {admin_data['email']} | senha: {admin_data['senha']}")
     
   print("\nBarbeiros:")
   for chave, barbeiros_data in BARBEIROS.items():
     print(f"chave: {chave} | nome: {barbeiros_data['nome']} | email: {barbeiros_data['email']} | senha: {barbeiros_data['senha']}")

   print("\nclientes:")
   for chave, clientes_data in CLIENTES.items():
     print(f"chave: {chave} | nome: {clientes_data['nome']} | email: {clientes_data['email']} | senha: {clientes_data['senha']}")

def deletar_usuario(chave):
   if chave in CLIENTES:
     confirmacao = input(f"Tem certeza que deseja deletar o cliente com chave {chave}? (s/n): ").strip().lower()
     if confirmacao == 's':
         del CLIENTES[chave]
         print(f"\n Cliente com chave {chave} excluído com sucesso.")
         #salvar_cliente()
     else:
         print("\n Exclusão cancelada.")
   elif chave in BARBEIROS:
     confirmacao = input(f"Tem certeza que deseja deletar o barbeiro com chave {chave}? (s/n): ").strip().lower()
     if confirmacao == 's':
         del BARBEIROS[chave]
         print(f"\n Barbeiro com chave {chave} excluído com sucesso.")
         #salvar_barbeiro()
     else:
         print("\n Exclusão cancelada.")
   elif chave in ADMINISTRADORES:
     if len(ADMINISTRADORES) == 1:
         print("\n Não é possível deletar o único administrador do sistema.")
         return

def editar_usuario(chave):
    if chave in CLIENTES:
        dado = input('Qual informação deseja alterar(nome, email ou senha): ').lower().strip()
        
        if dado == 'nome':
            novo_dado = input('informe o novo nome:')
            CLIENTES[chave]['nome'] = novo_dado
            #salvar_cliente()
            print('nome atualizado com sucesso!')
        elif dado == 'email':
            novo_dado = input('informe o novo email:')
            CLIENTES[chave]['email'] = novo_dado
            #salvar_cliente()
            print('email atualizado com sucesso!')
        elif dado == 'senha':
            novo_dado = input('informe a nova senha:')
            CLIENTES[chave]['senha'] = novo_dado
            #salvar_cliente()
            print('senha atualizada com sucesso!')
        else:
            print("Opção de dado inválida!")
            time.sleep(1)
    elif chave in BARBEIROS:
        dado = input('Qual informação deseja alterar(nome, email ou senha): ').lower().strip()
        
        if dado == 'nome':
            novo_dado = input('informe o novo nome:')
            BARBEIROS[chave]['nome'] = novo_dado
            #salvar_barbeiro()
            print('nome atualizado com sucesso!')
        elif dado == 'email':
            novo_dado = input('informe o novo email:')
            BARBEIROS[chave]['email'] = novo_dado
            #salvar_barbeiro()
            print('email atualizado com sucesso!')
        elif dado == 'senha':
            novo_dado = input('informe a nova senha:')
            BARBEIROS[chave]['senha'] = novo_dado
            #salvar_barbeiro()
            print('senha atualizada com sucesso!')
        else:
            print("Opção de dado inválida!")
            time.sleep(1)


def servico_popular(chave):
    barbeiro = BARBEIROS[chave]
    historico = barbeiro.get("historico", [])

    if not historico:
        print("Nenhum serviço realizado.")
        return

    contagem_servicos = {}
    for atendimento in historico:
        servico = atendimento.get("servico", "Serviço Desconhecido")
        contagem_servicos[servico] = contagem_servicos.get(servico, 0) + 1

    servico_popular = max(contagem_servicos, key=contagem_servicos.get)
    quantidade = contagem_servicos[servico_popular]

    print(f"O serviço mais popular de {barbeiro['nome']} é '{servico_popular}' ({quantidade} atendimentos).")
    return servico_popular

def faturamento_total(chave):
    if chave in BARBEIROS and 'valor' in BARBEIROS[chave]:
        faturamento = sum(BARBEIROS[chave]['valor'])
        return faturamento
    else:
        return 0