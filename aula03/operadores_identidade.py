lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 is lista2)      # False - objetos diferentes na memória
print(lista1 is lista3)      # True - mesma referência
print(lista1 is not lista2)  # True - não são o mesmo objeto

# Exemplo 2: Strings (objetos imutáveis)
str1 = "hello"
str2 = "hello"
str3 = "world"

print(str1 is str2)          # True - Python otimiza strings iguais
print(str1 is str3)          # False