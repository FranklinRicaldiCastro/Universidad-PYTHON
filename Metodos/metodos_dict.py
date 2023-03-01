diccionario ={
    "nombre" : 'Franklin',
    "apellido" : 'Ricaldi Castro',
    "subs" : 1000000
}
#Keys() -> devuelve las claves (También nos sirve para iterar)
claves =diccionario.keys()
print(claves)

#get() -> devuelve el valor de una clave (Si no encuentra nada el programa continua)
valor_de_apellido =diccionario.get("apellido")
print(valor_de_apellido)

#pop() -> elimina un elemento
diccionario.pop("subs")
print(diccionario)

#items() -> para iterar el diccionario
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

#clear() -> elimina todos los elementos
#diccionario.clear()