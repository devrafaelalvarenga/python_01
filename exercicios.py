# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
''' 
def somar(num_1 = int, num_2 = int) -> int: # Função que recebe dois números inteiros e retorna a soma deles
    return num_1 + num_2

def obtem_numero_inteiro(mensagem = str) -> int: # Função que solicita um número inteiro ao usuário
    while True: 
        try:
            return int(input(mensagem))
        except ValueError: # Tratamento de erro para caso o usuário digite um valor inválido
            print('Digite um número inteiro válido.')

if __name__ == "__main__":  # Executa o código abaixo apenas se este arquivo for executado diretamente
    num_1 = obtem_numero_inteiro('Digite o primeiro número inteiro: ')
    num_2 = obtem_numero_inteiro('Digite o segundo número inteiro: ')
    resultado = somar(num_1, num_2)
    print(f'A soma dos números é: {resultado}')    
'''
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
'''
def dividir(num_1 = int, num_2 = int) -> int: # Função que recebe dois números inteiros e retorna o resto da divisao deles
    return num_1 % num_2

def obtem_numero_inteiro(mensagem = str) -> int: # Função que solicita um número inteiro ao usuário
    while True: 
        try:
            return int(input(mensagem))
        except ValueError: # Tratamento de erro para caso o usuário digite um valor inválido
            print('Digite um número inteiro válido.')

if __name__ == "__main__":  # Executa o código abaixo apenas se este arquivo for executado diretamente
    num_1 = obtem_numero_inteiro('Digite um número inteiro: ')
    num_2 = 5
    resultado = dividir(num_1, num_2)
    print(f'O resto da divisão do numero {num_1} por {num_2} dos números é: {resultado}')
'''

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
''''
def multiplicar(num_1 = int, num_2 = int) -> int: # Função que recebe dois números inteiros e retorna a multiplicação dos valores
    return num_1 * num_2

def obtem_numero_inteiro(mensagem = str) -> int: # Função que solicita um número inteiro ao usuário
    while True: 
        try:
            return int(input(mensagem))
        except ValueError: # Tratamento de erro para caso o usuário digite um valor inválido
            print('Digite um número inteiro válido.')

if __name__ == "__main__":  # Executa o código abaixo apenas se este arquivo for executado diretamente
    num_1 = obtem_numero_inteiro('Digite um número inteiro: ')
    num_2 = obtem_numero_inteiro('Digite o segundo número inteiro: ')
    resultado = multiplicar(num_1, num_2)
    print(f'O resultado da multiplicação do numero {num_1} por {num_2} dos números é: {resultado}')
'''
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
'''
def dividir_inteiro(num_1 = int, num_2 = int) -> int: # Função que recebe dois números inteiros e retorna a divisão inteira dos valores
    return num_1 // num_2

def obtem_numero_inteiro(mensagem = str) -> int: # Função que solicita um número inteiro ao usuário
    while True: 
        try:
            return int(input(mensagem))
        except ValueError: # Tratamento de erro para caso o usuário digite um valor inválido
            print('Digite um número inteiro válido.')

if __name__ == "__main__":  # Executa o código abaixo apenas se este arquivo for executado diretamente
    num_1 = obtem_numero_inteiro('Digite um número inteiro: ')
    num_2 = obtem_numero_inteiro('Digite o segundo número inteiro: ')
    resultado = dividir_inteiro(num_1, num_2)
    print(f'O resultado da divisão inteira do numero {num_1} por {num_2} dos números é: {resultado}')
'''
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
'''
calcular_expoente = pow # Função que recebe dois números inteiros e eleva um número a uma potência

def obtem_numero_inteiro(mensagem=str) -> int: # Função que solicita um número inteiro ao usuário
    while True:
        try:
            return int(input(mensagem))
        except ValueError:  # Tratamento de erro para caso o usuário digite um valor inválido
            print('Digite um número inteiro válido.')


if __name__ == "__main__":  # Executa o código abaixo apenas se este arquivo for executado diretamente
    num_1 = obtem_numero_inteiro('Digite um número inteiro: ')
    expoente = 2
    resultado = calcular_expoente(num_1, expoente)
    print(f'O calculo do numero {num_1} ao quadrado é: {resultado}')
'''

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
