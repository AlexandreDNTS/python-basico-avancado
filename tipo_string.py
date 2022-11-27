"""
tipos strings

Em python um dado é considerado um string sempre que:
- estiver entre áspas simples ou dupla -> 'uma string', '234', 'a', ' True', '42.3'
"uma string", "234", "a", "True", "42.3"
"""
nome = 'francimar alexandre'
print(nome)
print(type(nome))

nome = 'francimar \nalexandre'  # '\n' pula uma linha
print(nome)
print(nome.upper())  # transforma os caracteres em maiúsculo
print(nome.lower())  # transforma os caracteres em minúsculo
print(nome.split())  # transforma em uma lista
print(type(nome))
print(nome[0:9])  # vai imprimir do caracter 0 até o 9° caracter
# vai do primeiro elemento até o ultimo elemento e inverte eles
print(nome[::-1])
