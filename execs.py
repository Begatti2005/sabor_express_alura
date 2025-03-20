import os

def verifica_numero():
    try:
        num1 = int(input('Escreva um número: '))
        print(num1)
        if num1 %2 == 0:
            print('Par')
        else:
            print('Impar')
    except:
        input('Digite uma tecla para continuar...')
        verifica_numero()

def verifica_idade():
    idade = int(input('Idade:'))
    if idade <= 12:
        print('Criança')
    elif idade >= 13 and idade <= 18:
        print('Jovem')
    else:
        print('Adulto')

def verifica_senha():
    user_correto = 'caick'
    senha_correta = '1234'
    user = str(input('User: ')) 
    senha = str(input('Senha: '))

    if user == user_correto and senha == senha_correta:
        print('Acesso Concedido')
    else:
        print('Acesso Negado')

def verifica_coordenadas():
    x = float(input('Coordenada X:'))
    y = float(input('Coordenada Y:'))

    if x > 0 and y > 0:
        print('Primeiro Quadrante')
    elif x < 0 and y > 0:
        print('Segundo Quadrante')
    elif x < 0 and y < 0:
        print('Terceiro Quadrante')
    elif x > 0 and y < 0:
        print('Quarto Quadrante')
    else:
        print('Eixo de Origem')

def lista_informacao():
    lista = [1,2,3,4,5,6,7,8,9,10]
    try:
        print()
        for numero in lista:
            print(numero)
    except:
        print('off')

    lista_nomes = ['Caick', 'Ana', 'Laura', 'Murillo']
    try:
        print()
        for nome in lista_nomes:
            print(nome)
    except:
            print('off')

    lista_ano_nasc = [2005, 2025]
    try:   
        print()
        for ano in lista_ano_nasc:
            print(ano)
    except:
        print('off')
  
def soma_impares():
    numeros = [1,2,3,4,5,6,7,8,9,10]

    result = 0

    for numero in numeros:
        if numero %2 != 0:
            result = numero + result
    print(result)

def descrescente():
    
    for i in range(10,0,-1):
        print(i)

def tabuada():
    num1 = float(input('Insira um número:'))
    multiplo = 0

    while multiplo < 11:
        result = num1 * multiplo
        multiplo = multiplo + 1
        print(f'{result:.2f}')

def soma_lista():
    lista_numeros = [1,2,3,4,5]
    result = 0

    try:
        for numero in lista_numeros:
            result = numero + result
    
        print(result)
    except:
        print('Lista inválida, digite novamente')
        input('Clique uma tecla para continuar...')

def divisao():
    lista_valores = [15, 20, 25, 30]
    soma_valores = 0

    try:
        for valor in lista_valores:
            soma_valores += valor
        media = soma_valores / len(lista_valores)
        print(f"Média dos valores: {media}")
    except ZeroDivisionError:
        print("A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    verifica_numero()

if __name__ == '__main__':
    main()