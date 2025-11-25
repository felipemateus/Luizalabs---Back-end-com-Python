# Criando listas
numeros = [1, 2, 3, 4, 5]
nomes = ["Alice", "Bob", "Carlos"]
mista = [1, "texto", 3.14, True]
vazia = []

# Acessando elementos
print(numeros[0])  # 1
print(nomes[-1])   # Carlos (último elemento)

# Adicionando elementos
numeros.append(6)
nomes.extend(["Diana", "Eva"])
numeros.insert(0, 0)  # Insere no índice 0

# Removendo elementos
numeros.remove(3)      # Remove o valor 3
ultimo = numeros.pop() # Remove e retorna o último
numeros.pop(0)         # Remove do índice 0

# Operações com listas
print(len(nomes))      # Tamanho
print(2 in numeros)    # Verifica se existe
lista_copia = nomes.copy()

# Iterando
for nome in nomes:
    print(nome)

# List comprehension
quadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Ordenação
numeros.sort()
numeros.reverse()
ordenado = sorted(nomes)  # Retorna nova lista

