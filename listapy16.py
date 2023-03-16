list = []
trocado = True 
num = int(input("quantos elementos queres?"))

for i in range(num):
    val = float(input("entre com o numero: "))
    list.append(val)

while trocado:
    trocado = False 
    for i in range(len(list)- 1):
        if list[i] > list[i + 1]:
            trocado = True 
            list[i], list[i+1], list[i]
            
print("\nOrdenado:")
print(list)