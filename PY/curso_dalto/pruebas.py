lista_numeros = []

numero_usuario = int(input("Porfavor introducza un número: "))

lista_numeros.append(numero_usuario)

# Le uno a lista_numero --> numero usuario, pero tambien lo puedo hacer de forma directa 
# lista_numero = int(input("Porfavor...."))

decision = input("Desea añadir más números?")

while decision == "s" or decision == "S":
    numero_usuario = int(input("Porfavor introducza otro número: "))
    lista_numeros.append(numero_usuario)
    decision = input("Desea añadir más números?")
    
print(lista_numeros)    