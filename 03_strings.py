### Strings ###
my_string = "cadena" #siempre se definen con las comillas
my_other_string = "de caracteres"
print(len(my_string)) #muestra la longitud
print(my_string+" "+my_other_string) #se pueden concatenar
my_new_line_string = "Esto va arriba \n esto abajo" #este da un salto de línea en el str
my_tab_string = "\t aqui hubo una tabulación" #se puede poner tabulaciones en str
print(my_new_line_string)
print(my_tab_string)
#Formateo:
name, lastname, age = "Brian", "Parra", 27
print("Mi nombre es {} {}, y tengo {} años de edad".format(name,lastname,age)) #podemos hacer que se peguen directamente en el print
print("Mi nombre es %s %s, y tengo %d años de edad"%(name,lastname,age)) #esta es otra alternativa, pero aquí si importa el tipo.
# las partes %s corresponden a un dato str, %d para int, %f para float y %.n para mostrar hasta n dígitos de un dato float
print(f"Mi nombre es {name} {lastname}, y tengo {age} años de edad") #este es inferencia de datos, más simple, pero no es útil si necesita verificar formato
# Desempaquetado de caracteres:
language = "Phyton"
a , b , c , d , e , f = language #sirve para separar caracteres
print(a)
print(f) #en efecto separa las cosas
# División:
language_slice = language[1:3]#muestra desde el primer caracter (el inicial es 0) hasta el tercero sin mostrar el 3, osea [1,3)
print(language_slice)
language_slice=language[1:]#muestra todo después del primer caracter
print(language_slice)
language_slice=language[-2] #aquí cuenta desde el final dos
print(language_slice)
reversed_language = language[::-1] #se invierte la palabra
print(reversed_language)
language_slice=language[0:6:2] #aquí toma los caracteres de [0,6) pero cuenta 2 caracteres, de los cuales uno no lo pinta
print(language_slice)
#Funciones para string
print(language.capitalize())#pone en mayúscula solo la primer letra
print(language.upper()) #pone todo en mayúsculas
print(language.lower()) #pone todo en minúsculas
print(language.count("t")) #cuanta cuantas veces aparece "t" en el dato
print(language.isnumeric()) #dice si es numero o no, aqui no es
print("1".isnumeric()) #aquí, sí
print(language.lower()) #convierte todo a minúsculas
print(language.upper().isupper()) #en este caso comprueba si todo está en mayúsculas, lo cual es cierto.
print(language.startswith("Ph")) #comprueba si inicia con Ph