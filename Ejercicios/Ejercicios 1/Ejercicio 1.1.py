#diferencia en porcentaje entre el curso actual y:
#-el más rápido de otros cursos
#-el más lento de otros cursos
#-el promedio de otros cursos

#promedio de duraciones de los cursos
cursos_rápido = 2.5
cursos_lento = 7
cursos_promedio = 4
este_curso = 1.5

#diferencia de duración
# ? Para calcular las diferencias en porcentaje entre la duración del curso actual y los cursos más rápidos, más lentos y promedio de otros cursos, podemos usar la siguiente fórmula:
# ? Diferencia porcentual = ((Valor 2 - Valor 1) / Valor 2) x 100%
# ? Donde Valor 1 es la duración del curso actual y Valor 2 es la duración del curso más rápido, más lento o promedio de otros cursos.
diferencia_con_rápido = ((cursos_rápido - este_curso) / cursos_rápido) * 100
diferencia_con_lento = ((cursos_lento - este_curso) * 1000 // cursos_lento) / 10
diferencia_con_promedio = (
    (cursos_promedio - este_curso) / cursos_promedio) * 100

#mostrando la diferencia de duraciones (Ejercicio A)
print("=================================================================================================")
print("Este curso dura:")
print(f'- Un {diferencia_con_rápido}% menos que el más rápido')
print(f'- Un {diferencia_con_lento}% menos que el más lento')
print(f'- Un {diferencia_con_promedio}% menos que el promedio')
print("=================================================================================================")

#duración de crudo
crudo_promedio = 5
crudo_curso = 3.5

#calculando el porcentaje de material Inservible (Tiempo de vacío removido)
tiempo_de_vacío_promedio = 100 - cursos_promedio * 1000 // crudo_promedio / 10
tiempo_de_vacío_curso = 100 - este_curso * 1000 // crudo_curso / 10

#mostrando la cantidad de espacios vacÍos que se remueven (Ejercicio B)
print(f'Un curso promedio elimina un {tiempo_de_vacío_promedio}% de tiempo vacío')
print(f'Este curso elimino el {tiempo_de_vacío_curso}% de tiempo vacío')
print("=================================================================================================")

#mostrando las diferencias si los cursos duraran 10 horas (Ejercicio C)
print(f'Ver 10 horas de este curso equivale a ver {cursos_promedio * 100 // este_curso / 10} horas de otro cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {este_curso * 100 // cursos_promedio / 10} horas de este curso')
print("=================================================================================================")