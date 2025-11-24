from menu import Menu_administrador
from banco import BARBEIROS, ADMINISTRADORES, CLIENTES, salvar_barbeiro, salvar_cliente, salvar_admin
import os
import time

<<<<<<< HEAD
def validacao_chave(chave):
    os.system('cls')
    listar_usuarios()
    chave = input('\nInforme a chave do usuario que deseja gerenciar: ').strip()

    if chave in ADMINISTRADORES:
        print("Não é possivel gerenciar usuário do tipo administrador.")
        time.sleep(3)
        return validacao_chave(chave)   
    elif chave in CLIENTES:
        return fluxo_administrador(chave) 
    elif chave in BARBEIROS:
        return fluxo_administrador(chave)
    else:
        print("chave não encontrada.")
        time.sleep(2)
        return validacao_chave(chave)


def fluxo_administrador(chave):
=======
def validacao_cpf(cpf):
    os.system('cls')
    listar_usuarios()
    opc = 0
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
>>>>>>> 015da2ea0c11f55ace51d7d1bdbc437db33079b9
    opc = 0

    while opc != 4:
        opc = Menu_administrador(chave)

        if opc == 1:
            fluxo_gerar_relatorios(chave) 
        elif opc == 2:
            fluxo_gerenciar_usuarios(chave)
        elif opc == 3:
            fluxo_gerenciar_servicos(chave)
            time.sleep(2)
        elif opc == 4:
            print("Até logo!")
            time.sleep(2)
<<<<<<< HEAD
            os.system("cls")
            return
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
=======
        else:
            print("opção inválida!")
            time.sleep(2)
            return fluxo_administrador(cpf)

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
>>>>>>> 015da2ea0c11f55ace51d7d1bdbc437db33079b9

    try:
        opc = int(input("Escolha uma opção: "))

        if opc == 1:
            editar_usuario(chave)
            time.sleep(3)
            return fluxo_administrador(chave)
        elif opc == 2:
            
            deletar_usuario(chave)
            time.sleep(3)
            return validacao_chave(chave)
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
    if chave in CLIENTES:
        os.system('cls')
        print('Não é possivel gerar relatórios de usuário que não oferta serviços.')
        time.sleep(3)
        return fluxo_administrador(chave)
    elif chave in BARBEIROS:
        os.system('cls')
        print('====relatório de desempenho do barbeiro====')
        print("\nDados do usuário Barbeiro:")
        print(f"Nome: {BARBEIROS[chave]['nome']}")
        print(f"cpf: {BARBEIROS[chave]['email']}")
        print("-------------------------------------")
        servico_popular(chave)
        faturamento_total(chave)
        media_avaliacao_barbeiro(chave)
        print("-------------------------------------")  
        
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

def fluxo_gerenciar_servicos(chave):
    os.system('cls')
    print("=============================")
    print("      gerenciar serviços     ")
    print("=============================")
    listar_servicos(chave)
    
    print("\n1 - editar serviço")
    print("2 - excluir serviço")
    print("3 - Voltar")

    try:
        opc = int(input("Escolha uma opção: "))

        if opc == 1:
            editar_servico(chave)
            return
        elif opc == 2:
            deletar_servico(chave)
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
            return editar_usuario(chave)


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

<<<<<<< HEAD
def faturamento_total(chave):
    barbeiro = BARBEIROS[chave]
    historico = barbeiro.get("historico", [])
    faturamento_total = 0
    
    for item in historico:
        if 'valor' in item:
            try:
                valor = float(item['valor'])
                faturamento_total += valor
            except (ValueError, TypeError):
                pass
    
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    return faturamento_total

def media_avaliacao_barbeiro(chave):
    servicos = BARBEIROS[chave]["servicos"]
    total_notas = []
    
    for servico in servicos:
        total_notas.extend(servico["avaliacao"])

    if not total_notas:
        print("Esse barbeiro ainda não possui avaliações.")
        return

    media = sum(total_notas) / len(total_notas)
    print(f"Média geral de avaliação do barbeiro: {media:.2f}")

def listar_servicos(chave):
    print('==========serviços cadastrados==========')
    if chave not in BARBEIROS:
        print("Barbeiro não encontrado.")
        return

    servicos = BARBEIROS[chave]["servicos"]

    if not servicos:
        print("Nenhum serviço cadastrado.")
        return

    for i, servico in enumerate(servicos, start=1):
        print(f"{i}. {servico['nome']} - R${servico['valor']} - {servico['tempo']} min")

def editar_servico(chave):
    os.system('cls')
    listar_servicos(chave)
    servicos = BARBEIROS[chave]['servicos']

    nome_servico = input("\nDigite o nome do serviço que deseja editar: ").lower().strip()

    for servico in servicos:
            if servico['nome'].lower() == nome_servico:
                dado = input("O que deseja alterar (nome, valor ou tempo): ").lower().strip()

                if dado == 'nome':
                    novo_dado = input("Informe o novo nome: ").strip()
                    servico['nome'] = novo_dado
                    print("Nome atualizado com sucesso!")
                    #salvar_barbeiro()
                    return

                elif dado == 'valor':
                    novo_dado = float(input("Informe o novo valor: "))
                    servico['valor'] = novo_dado
                    print("Valor atualizado com sucesso!")
                    #salvar_barbeiro()
                    return

                elif dado == 'tempo':
                    os.system('cls')
                    novo_dado = int(input("Informe o novo tempo (minutos): "))
                    servico['tempo'] = novo_dado
                    print("Tempo atualizado com sucesso!")
                    #salvar_barbeiro()   
                    return
                
                else:
                    print("Opção inválida.")
                    time.sleep(2)
                    return editar_servico(chave)
    print("Serviço não encontrado.")
    os.system('cls')
    time.sleep(2)
    return editar_servico(chave)

def deletar_servico(chave):
    listar_servicos(chave)
    servicos = BARBEIROS[chave]["servicos"]

    if not servicos:
        print("Nenhum serviço cadastrado.")
        time.sleep(2)
        return

    nome_servico = input("\nDigite o nome do serviço que deseja deletar: ").lower().strip()
=======

>>>>>>> 015da2ea0c11f55ace51d7d1bdbc437db33079b9

    for servico in servicos:
        if servico["nome"].lower() == nome_servico:
            confirmacao = input(f"Tem certeza que deseja deletar o serviço '{servico['nome']}'? (s/n): ").strip().lower()

            if confirmacao == 's':
                servicos.remove(servico)
                #salvar_barbeiro()
                print(f"O serviço '{nome_servico}' foi excluído com sucesso.")
            else:
                print("\nExclusão cancelada.")
                time.sleep(2)
                return
    os.system('cls')
    print("Serviço não encontrado.")
    time.sleep(2)
    return deletar_servico(chave)
    
    
