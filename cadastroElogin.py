from banco import CLIENTES, BARBEIROS, ADMINISTRADORES, salvar_barbeiro, salvar_cliente
from cliente import fluxo_cliente
from barbeiro import fluxo_barbeiro
from administador import validacao_cpf
import os
import time

def cadastrar_usuario(nome, email, cpf, senha, tipo_usuario):
    email = email.lower()
    if cpf in CLIENTES or cpf in BARBEIROS: 
        print("Usuário já cadastrado!")
        time.sleep(2.5)
        return False
    if len(senha) < 8:
        print("Senha muito curta! Use pelo menos 8 caracteres!")
        time.sleep(2.5)
        return False
    if not len(cpf) == 11:
        print("Número de cpf inválido!")
        time.sleep(2.5)
        return False
    if tipo_usuario == "cliente":
        CLIENTES[cpf] = {"nome": nome.strip(), "senha": senha, "email": email, "tipo_usuario": tipo_usuario, "agendamentos": [], "historico": [], }
        print("Cadastro realizado com sucesso!")
        salvar_cliente()
        time.sleep(2.5)
        return fluxo_cliente(cpf)
    elif tipo_usuario == "barbeiro": 
        BARBEIROS[cpf] = {"nome": nome.strip(), "senha": senha, "email": email, "tipo_usuario": tipo_usuario, "endereco": input("Informe o endereço do seu local de trabalho: ") , "sobre": input("Escreva um breve resumo sobre você: "), "servicos": [], "agendamentos": [], "historico": []}
        print("Cadastro realizado com sucesso!")
        salvar_barbeiro()
        time.sleep(2.5)
        return fluxo_barbeiro(cpf)

def login(cpf, email, senha):
    email = email.lower()    
    if cpf in CLIENTES:
        usuario = CLIENTES[cpf]
    elif cpf in BARBEIROS:
        usuario = BARBEIROS[cpf]
    elif cpf in ADMINISTRADORES:
        usuario = ADMINISTRADORES[cpf]
    else:
        print("Falha no login! Seu email, senha ou cpf podem estar incorretos, verifique suas informações e tente novamente!")
        time.sleep(2)
        return False
    
    if usuario and usuario["senha"] == senha and usuario["email"] == email:
        print("Login realizado com sucesso!")
        time.sleep(2)
        if usuario["tipo_usuario"] == "cliente":
            return fluxo_cliente(cpf)
        elif usuario["tipo_usuario"] == "barbeiro":
            return fluxo_barbeiro(cpf)
        elif usuario["tipo_usuario"] == "administrador":
            return validacao_cpf(cpf)
    else: 
        print("Falha no login! Seu email, senha ou cpf podem estar incorretos, verifique suas informações e tente novamente!")
        time.sleep(2)
        return False

def fluxo_cadastrar():
    os.system('cls') 
    print("=============================")
    print("       Crie sua conta!       ")
    print("=============================")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    cpf = input("CPF: ").strip()
    senha = input("Senha: ").strip()
    tipo_usuario = input("Deseja ofertar serviços na plataforma? [S/N] ").strip().lower()
    if tipo_usuario == "s":
        tipo_usuario = "barbeiro"
    else:
        tipo_usuario = "cliente"
    cadastrar_usuario(nome, email, cpf, senha, tipo_usuario)
    
def fluxo_login():
    os.system('cls') 
    print("=============================")
    print("            Login            ")
    print("=============================")
    cpf = input("CPF: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    login(cpf, email, senha)