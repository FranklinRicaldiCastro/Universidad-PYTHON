# Creando una lista con list()
lista = list(["Hola", "Franklin", 30, True])
lista1 = list([5, 89, 30, 56, True, False])

# Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)
#print(cantidad_elementos)

# Agregando elementos ala lista
agregando_con_append = lista.append("Hola")
#print(lista)

# Agregando un elemento ala lista en un indice especifico
lista.insert(2, "Amanecer")
#print(lista)

# Agregando varios elementos ala lista
lista.extend([False, 2023])
#print(lista)

# Eliminando un elemento (por su indice)
# -1 para eliminar el ultimo, -2 para eliminar el antepenúltimo, y asi sucesivamente
lista.pop(0)
#print(lista)

# Removiendo un elemento de la lista por su valor (Busca el valor y lo elimina)
lista.remove(30)  # Si no encuentra un parámetro lanza una excepción
#print(lista)

# Ordena la lista de menor a mayor
lista1.sort()
#print(lista1)

# Ordenando la lista alreverse (Si usamos el parametro reverse=true)
lista1.sort(reverse=True)
#print(lista1)

# Invirtiendo los elementos de una lista
lista1.reverse()
#print(lista1)

# Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista1.index(89)
print(elemento_encontrado)

# Eliminando todos los elementos de la lista
# lista.clear()
# print(lista)
