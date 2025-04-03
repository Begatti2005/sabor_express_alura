import os

restaurantes = [{'nome':'Praça', 'categoria':'Japoensa', 'estado':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'estado':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'estado':False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    
    # Teste do GIT - V2

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/Desativar restaurante')
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
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante,'categoria':categoria,'estado':False}
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso')
    voltar_menu()

def estado_restaurante():
    os.system('cls')
    exibir_subtitulos('Alternando o estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante['estado'] = not restaurante['estado']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['estado'] else f'O restaurante {nome_restaurante} foi desativado'
            print(mensagem)
            restaurante_encontrado = True

    if not restaurante_encontrado:
        print('Restaurante não foi encontrado\nDigite o nome corretamente')
        input('Digite uma tecla para continuar...')
        estado_restaurante()

    voltar_menu()

def listar_restaurantes():
    exibir_subtitulos('Listando restaurantes\n')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        estado_restaurante = 'Ativado' if restaurante['estado'] else 'Desativado'
        print(f'- {nome_restaurante} | {categoria_restaurante} | {estado_restaurante}')

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
            estado_restaurante()
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