
from menu import Menu_administrador
from banco import BARBEIROS, ADMINISTRADORES, CLIENTES, salvar_barbeiro, salvar_cliente, salvar_admin
import os
import time

def validacao_cpf(cpf):
    os.system('cls')
    listar_usuarios()
    cpf = input('\nInforme o cpf do usuario que deseja gerenciar: ').strip()

    if cpf in ADMINISTRADORES:
        print("Não é possivel gerenciar usuário do tipo administrador.")
        time.sleep(3)
        return validacao_cpf(cpf)
    elif cpf in CLIENTES:
        return fluxo_administrador(cpf) 
    elif cpf in BARBEIROS:
        return fluxo_administrador(cpf)
    else:
        print("cpf não encontrado.")
        time.sleep(2)
        return validacao_cpf(cpf)


def fluxo_administrador(cpf):
    opc = 0

    while opc != 4:
        opc = Menu_administrador(cpf)

        if opc == 1:
            fluxo_gerar_relatorios(cpf) 
        elif opc == 2:
            fluxo_gerenciar_usuarios(cpf)
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


def fluxo_gerenciar_usuarios(cpf):
    os.system('cls')
    print("=============================")
    print("      gerenciar usuário      ")
    print("=============================")
    
    if cpf in CLIENTES:
        print("\nDados do usuário Cliente:")
        print(f"Nome: {CLIENTES[cpf]['nome']}")
        print(f"Email: {CLIENTES[cpf]['email']}")
        print(f"Senha: {CLIENTES[cpf]['senha']}")
        print(f"histórico: {CLIENTES[cpf]['historico']}")
    elif cpf in BARBEIROS:
        print("\nDados do usuário Barbeiro:")
        print(f"Nome: {BARBEIROS[cpf]['nome']}")
        print(f"Email: {BARBEIROS[cpf]['email']}")
        print(f"Senha: {BARBEIROS[cpf]['senha']}")
        print(f"histórico {BARBEIROS[cpf]['historico']}")
    elif cpf in ADMINISTRADORES:
        print('Não é possivel gerenciar esse usuário!')
        time.sleep(3)
        return fluxo_administrador(cpf)
    else:
        print("CPF não encontrado")
        return fluxo_administrador(cpf)
    
    print("\n1 - editar usuário")
    print("2 - excluir usuário")
    print("3 - Voltar")

    try:
        opc = int(input("Escolha uma opção: "))

        if opc == 1:
            editar_usuario(cpf)
            listar_usuarios()
            time.sleep(3)
            return fluxo_administrador(cpf)
        elif opc == 2:
            deletar_usuario(cpf)
            listar_usuarios()
            time.sleep(3)
            return fluxo_administrador(cpf)
        elif opc == 3:
            return fluxo_administrador(cpf)
        else:
            print("opção inválida")
            time.sleep(2)
            return fluxo_administrador(cpf)
    except ValueError:
        print("opção inválida")
        return fluxo_administrador(cpf)


def fluxo_gerar_relatorios(cpf):
    os.system('cls')
    print("=============================")
    print("          Relatórios         ")
    print("=============================")
    
    if cpf in CLIENTES:
        print('Não é possivel gerar relatórios de usuário que não oferta serviços.')
        time.sleep(3)
        return fluxo_administrador(cpf)
    elif cpf in BARBEIROS:
        print('====relatório de desempenho do barbeiro====')
        print("\nDados do usuário Barbeiro:")
        print(f"Nome: {BARBEIROS[cpf]['nome']}")
        print(f"Email: {BARBEIROS[cpf]['email']}")
        print(f"Senha: {BARBEIROS[cpf]['senha']}")
        print(f"histórico {BARBEIROS[cpf]['historico']}")
        servico_popular(cpf)
        
        try:
            opc = int(input('\nDigite 1 para voltar ao menu anterior: '))
            if opc == 1:
                return fluxo_administrador(cpf)
            else:
                print("Opção inválida!")
                time.sleep(2)
                return fluxo_administrador(cpf)
        except ValueError:
            print("Opção inválida!")
            time.sleep(2)
            return fluxo_administrador(cpf)
            
    elif cpf in ADMINISTRADORES:
        print('Não é possivel gerar relatórios de um usuário que não oferta serviços.')
        time.sleep(3)
        return fluxo_administrador(cpf)
    else:
        print("CPF não encontrado")
        time.sleep(2)
        return fluxo_administrador(cpf)


def listar_usuarios():
   print("\n=== Lista de Usuários ===")

   print("\nAdministradores:")
   for cpf, admin_data in ADMINISTRADORES.items():
     print(f"cpf: {cpf} | nome: {admin_data['nome']} | email: {admin_data['email']} | senha: {admin_data['senha']}")
     
   print("\nBarbeiros:")
   for cpf, barbeiros_data in BARBEIROS.items():
     print(f"cpf: {cpf} | nome: {barbeiros_data['nome']} | email: {barbeiros_data['email']} | senha: {barbeiros_data['senha']}")

   print("\nclientes:")
   for cpf, clientes_data in CLIENTES.items():
     print(f"cpf: {cpf} | nome: {clientes_data['nome']} | email: {clientes_data['email']} | senha: {clientes_data['senha']}")

def deletar_usuario(cpf):
   if cpf in CLIENTES:
     confirmacao = input(f"Tem certeza que deseja deletar o cliente com CPF {cpf}? (s/n): ").strip().lower()
     if confirmacao == 's':
         del CLIENTES[cpf]
         print(f"\n Cliente com CPF {cpf} excluído com sucesso.")
         #salvar_cliente()
     else:
         print("\n Exclusão cancelada.")
   elif cpf in BARBEIROS:
     confirmacao = input(f"Tem certeza que deseja deletar o barbeiro com CPF {cpf}? (s/n): ").strip().lower()
     if confirmacao == 's':
         del BARBEIROS[cpf]
         print(f"\n Barbeiro com CPF {cpf} excluído com sucesso.")
         #salvar_barbeiro()
     else:
         print("\n Exclusão cancelada.")
   elif cpf in ADMINISTRADORES:
     if len(ADMINISTRADORES) == 1:
         print("\n Não é possível deletar o único administrador do sistema.")
         return

def editar_usuario(cpf):
    if cpf in CLIENTES:
        dado = input('Qual informação deseja alterar(nome, email ou senha): ').lower().strip()
        
        if dado == 'nome':
            novo_dado = input('informe o novo nome:')
            CLIENTES[cpf]['nome'] = novo_dado
            #salvar_cliente()
            print('nome atualizado com sucesso!')
        elif dado == 'email':
            novo_dado = input('informe o novo email:')
            CLIENTES[cpf]['email'] = novo_dado
            #salvar_cliente()
            print('email atualizado com sucesso!')
        elif dado == 'senha':
            novo_dado = input('informe a nova senha:')
            CLIENTES[cpf]['senha'] = novo_dado
            #salvar_cliente()
            print('senha atualizada com sucesso!')
        else:
            print("Opção de dado inválida!")
            time.sleep(1)
    elif cpf in BARBEIROS:
        dado = input('Qual informação deseja alterar(nome, email ou senha): ').lower().strip()
        
        if dado == 'nome':
            novo_dado = input('informe o novo nome:')
            BARBEIROS[cpf]['nome'] = novo_dado
            #salvar_barbeiro()
            print('nome atualizado com sucesso!')
        elif dado == 'email':
            novo_dado = input('informe o novo email:')
            BARBEIROS[cpf]['email'] = novo_dado
            #salvar_barbeiro()
            print('email atualizado com sucesso!')
        elif dado == 'senha':
            novo_dado = input('informe a nova senha:')
            BARBEIROS[cpf]['senha'] = novo_dado
            #salvar_barbeiro()
            print('senha atualizada com sucesso!')
        else:
            print("Opção de dado inválida!")
            time.sleep(1)


def servico_popular(cpf):
    barbeiro = BARBEIROS[cpf]
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

def faturamento_total(cpf):
    if cpf in BARBEIROS and 'valor' in BARBEIROS[cpf]:
        faturamento = sum(BARBEIROS[cpf]['valor'])
        return faturamento
    else:
        return 0