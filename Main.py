from cadastroElogin import fluxo_cadastrar, fluxo_login
from menu import menu, menu_sac
import os
from pesquisa import painel_busca


def main():
    chave = False
    os.system('cls') 
    opc = 0
    while opc != 5:
        opc = menu()
        if opc == 1:
            painel_busca(chave)
        elif opc == 2:
            fluxo_login()
        elif opc == 3:
            fluxo_cadastrar()
        elif opc == 4: 
            menu_sac()
        elif opc == 5:
            print("Adeus!")
        else:
            print("Opção inválida!")

main()

