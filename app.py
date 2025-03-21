import os

restaurantes = ['Pizza','Sushi']

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastro de restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def voltar_menu():
    input('\nClique uma tecla para continuar... ')
    main()

def exibir_subtitulos(nome):
    os.system('cls')
    print(nome)

def finalizar_app():
    exibir_subtitulos('Finalizando app...')

def opcao_invalida():
    print('Opção Inválida!')
    voltar_menu()

def cadastrar_restaurante():
    exibir_subtitulos('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante a ser cadastrado: ')
    restaurantes.append(nome_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulos('Listando restaurantes\n')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_menu()

def verifica_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if  opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    verifica_opcao()

if __name__ == '__main__':
    main()