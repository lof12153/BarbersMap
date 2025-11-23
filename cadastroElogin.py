from banco import CLIENTES, BARBEIROS, ADMINISTRADORES, salvar_barbeiro, salvar_cliente
from cliente import fluxo_cliente
from barbeiro import fluxo_barbeiro
from administador import validacao_chave
import os

def cadastrar_usuario(nome, email, chave, senha, tipo_usuario):
    if chave in CLIENTES or chave in BARBEIROS: 
        print("Usuário já cadastrado! Pressione ENTER para continuar.")
        input()
        return False
    if tipo_usuario == "cliente":
        CLIENTES[chave] = {"nome": nome.strip(), "senha": senha, "email": email, "tipo_usuario": tipo_usuario, "agendamentos": [], "historico": [], }
        print("Cadastro realizado com sucesso! Pressione ENTER para continuar.")
        salvar_cliente()
        input()
        return fluxo_cliente(chave)
    elif tipo_usuario == "barbeiro": 
        BARBEIROS[chave] = {"nome": nome.strip(), "senha": senha, "email": email, "tipo_usuario": tipo_usuario, "endereco": input("Informe o endereço do seu local de trabalho: ") , "sobre": input("Escreva um breve resumo sobre você: "), "servicos": [], "agendamentos": [], "historico": []}
        print("Cadastro realizado com sucesso! Pressione ENTER para continuar.")
        salvar_barbeiro()
        input()
        return fluxo_barbeiro(chave)

def login(chave, email, senha):   
    if chave in CLIENTES:
        usuario = CLIENTES[chave]
    elif chave in BARBEIROS:
        usuario = BARBEIROS[chave]
    elif chave in ADMINISTRADORES:
        usuario = ADMINISTRADORES[chave]
    else:
        print("Falha no login! Seu email, senha e CPF ou CNPJ podem estar incorretos, verifique suas informações e tente novamente! Pressione ENTER para continuar.")
        input()
        return False
    
    if usuario and usuario["senha"] == senha and usuario["email"] == email:
        print("Login realizado com sucesso! Pressione ENTER para continuar.")
        input()
        if usuario["tipo_usuario"] == "cliente":
            return fluxo_cliente(chave)
        elif usuario["tipo_usuario"] == "barbeiro":
            return fluxo_barbeiro(chave)
        elif usuario["tipo_usuario"] == "administrador":
            return validacao_chave(chave)
    else: 
        print("Falha no login! Seu email, senha ou chave podem estar incorretos, verifique suas informações e tente novamente! Pressione ENTER para continuar.")
        input()
        return False

def fluxo_cadastrar():
    os.system('cls') 
    print("=============================")
    print("       Crie sua conta!       ")
    print("=============================")
    nome = input("Nome: ").strip()
    while True:
        if not nome == "":
            break
        else:
            nome = input("Digite um nome válido!: ")
    email = input("Email: ").strip()
    while True:
        if "@gmail.com" in email or "@hotmail.com" in email or "@outlook.com" in email or "@mail.com" in email:
            break
        else:
            email = input("Email inválido! Informe email: ")
    while True:
        chave = input("CPF ou CNPJ: ").strip()
        if len(chave) != 14 and len(chave) != 11:
            print("Tamanho inválido! Digite apenas os números.")
        else:
            break
    print("AVISO \nSua senha deve ter pelo menos 8 digitos, uma letra MAIÚSCULA, um número e um caractere especial (!@#$%¨&*).")
    while True:
        senha = str(input("Digite sua senha : "))
        if senha.islower():
            print("A senha deve ter pelo menos um caractere MAIUSCULO: ")
        elif len(senha) < 7 :
            print("A senha deve ter pelo menos 8 caracteres: ")
        elif senha.isalpha() :
            print("A senha deve ter pelo menos um numero: ")
        elif senha.isalnum() :
            print("A senha deve ter pelo menos um Caractere especial: ")
        else:
            break
    tipo_usuario = input("Deseja ofertar serviços na plataforma? [S/N] ").strip().lower()
    if tipo_usuario == "s":
        tipo_usuario = "barbeiro"
    else:
        tipo_usuario = "cliente"
    cadastrar_usuario(nome, email, chave, senha, tipo_usuario)
    
def fluxo_login():
    os.system('cls') 
    print("=============================")
    print("            Login            ")
    print("=============================")
    chave = input("CPF ou CNPJ: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    login(chave, email, senha)