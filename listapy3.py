minha_lista = [1, 2, 3, 4, 5]
#usando um loop for para percorrer a lista e imprimir elemento 

for i in range(len(minha_lista)):
    print("O elemento", i+1, "da lista é:", minha_lista[i])
    
# criando uma lista de númeors 
numeros = [1, 2, 3, 4, 5]

#usando um loop for para percorrer a lista e imprimir cada elemento 
for numero in numeros:
    print(numero, " - Com for")

#usando um loop para percorrer a lista e imprimir cada elemento 
i = 0
while i < len(numeros):
    print(numeros[i], " - Com While")
    i += 1