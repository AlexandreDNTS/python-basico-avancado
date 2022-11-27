"""
tipo booleano

Duas constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

"""

ativo = False

print(ativo)
print(type(ativo))

# operações básicas

# negação (not)

"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. 
"""

print(not ativo)
logado = False

# or (ou)

"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and)

"""
Também é uma operação binária, ou seja, depende de dois valores, ambos valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
print(ativo and logado)
