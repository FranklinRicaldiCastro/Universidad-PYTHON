# LOS MÉTODOS SON:
#! DATOS.metodo()

cadena1 = "Hola soy Franklin"
cadena2 = "hola,soy,franklin"

# ?dir no es un método, es una función
# Devuelve la lista de atributos válidos del objeto pasado
atributos = dir(cadena1)
print(atributos)

# ?métodos
# Convierte a Mayúsculas
mayúscula = cadena1.upper()
print(mayúscula)

# Convierte a Minúsculas
minúscula = cadena1.lower()
print(minúscula)

# Convierte la primera letra en Mayúscula ojo solo la primera letra de la oración lo de mas a a minúsculas
primera_letra_mayúscula = cadena1.capitalize()

print(primera_letra_mayúscula)

# Buscamos un carácter dentro de una cadena, si no hay coincidencias devuelve -1
búsqueda_find = cadena1.find("a")
print(búsqueda_find)

# Buscamos un carácter de una cadena, si no hay coincidencias lanza uná excepción
# búsqueda_index = cadena1.index("d")
# print(búsqueda_index)

# Si es numérico, devolvemos true, si no devolvemos false
es_numérico = cadena2.isnumeric()
print(es_numérico)

# Si es alfanumérico devolvemos true, si no devolvemos false
es_alfanumérico = cadena2.isalpha()
print(es_alfanumérico)

# Cuenta la cantidad de veces que se encuentra una coincida.
contar_coincidencias = cadena1.count("Hola")
print(contar_coincidencias)

# ?len no es un método, es una función
# Contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)
print(contar_caracteres)

# Verificamos si una cadena empieza con (""), si es asi devuelve true
empieza_com = cadena1.startswith("Hola")
print(empieza_com)

# Verificamos si una cadena termina con (""), si es asi devuelve true
termina_com = cadena1.endswith("Franklin")
print(termina_com)

#Si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma , por el valor 2 
#Es decir remplaza un pedazo de la cadena dada, por otra dada.
cadena_nueva = cadena2.replace(",", " ")
print(cadena_nueva)

#Separar cadenas con la cadena que pasamos
cadena_separada = cadena2.split(",")
print(cadena_separada[0])