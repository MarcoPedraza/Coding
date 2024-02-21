#Creando una lista se pueden modificar
lista = ["Lucas Dalto","Soy Dalto",True,1.85]

#Creando una tupla no se puede modificar
tupla = ("Lucas Dalto","Soy Dalto",True,1.85)


lista[3] = "Maquinola"

print(lista)
print(lista[0])

#Creando un conjunto (set) ; se pueden intercambiar
    # No puedo sacar valores individualmente y no se pueden repetir valores
conjunto = {"Lucas Dalto","Soy Dalto",True,1.85}

# Para ver cuales son los elementos del set tenemos que recorrerlo con un bucle

diccionario = {
    "Nombre" : "Dalto",
    "Canal" : "Soy Dalto",
    "esta emocionado" : True,
    "dato duplicado" : "Soy Dalto"
}

print(diccionario["Canal"])

