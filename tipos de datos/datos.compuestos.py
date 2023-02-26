#Primer Tipo de dato la LISTA se puede modificar
lista = ["Franklin Ricaldi Castro", "Soy Feliz", True, 1.85]

#Segundo Tipo de dato la TUPLA y no se puede modificar
tupla = ("Franklin Ricaldi Castro", "Soy Feliz", True, 1.85)
#Esto es Valido
lista[3]= "Maquinola"
print(lista[3])

#Esto no es Valido
#tupla[3]= "Maquinola"

#Creando un conjunto (set)(No se accede a elementos por indice, no se almacena datos duplicados y no tienen un orden se pueden cambiar)
conjunto={"Franklin Ricaldi Castro", "Soy Feliz", True, 1.85}
#print(conjunto[3]) -> No puede acceder ala elemento

#creando un diccionario (dict) (La estructura es key : value y separamos con comas)
diccionario ={
    #key: value
    #clave: valor
    'nombre': "Franklin Ricaldi Castro",
    'canal de YouTube': "Soy Franklin",
    'esta emocionado': True,
    'altura': 1.62,
    'dato_duplicado': "Soy Franklin"
}

print(diccionario['altura'] + 5)