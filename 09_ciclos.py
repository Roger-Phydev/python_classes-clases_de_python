### Loops ###
#permite repetir codigo varias veces.
## While ##
#aquí se necesita una condición, mientras esa condición se cumpla,
#el codigo se repetirá, una vez no se cumpla, dejará de repetirse
my_condition = 0
while my_condition <10:
    print(my_condition)
    my_condition +=2 #por ello es necesario modificar la condición
    #para conseguir que en algún momento pare
#en este caso cuenta desde 0 a 10 de dos en dos
#en el momento que se cumple la condición, se mantiene ejecutando
#solo las lineas 7 a 9, cuando ya no se cumple, se saltaría a la 14
else:
    print("ya llegó a 10") #es raro, pero en python se puede usar else
    #junto con un while, y sirve para saber cuando ya no se cumple la 
    #condición
while my_condition <20:#imprime hasta 20
    my_condition+=1#porque primero sumamos y luego comprobamos
    if my_condition ==15:
        print("Mi condición es 15!")
        break #aquí detiene la ejecución
    print(my_condition) 
## For ##
#en este caso repite codigo una cantidad limitada de veces
#la cantidad esté dado por la longitud de la lista que se use
my_list = [35,24,62,52,30,30,17] #creamos esta lista
for element in my_list:#solo ejecuta para los elementos de mylist
    print(element)#imprime el elemento
#es claro que en lugar de lista podemos usar tuplas, diccionarios o conjuntos
my_tuple, my_set, my_dict = (27,1.86,"Brian","Parra","Roger"),{"Brian","Parra",27},{"Nombre":"Brian","Apellido":"Parra","Edad":27,1:"Python"}
for element in my_tuple:
    print(element)#aqui imprime por orden
for element in my_set:
    print(element)#aquí no hay orden
for element in my_dict:
    print(element)#aquí solo muestra las key
for element in my_dict.values():
    print(element)#asi se imprimen los valores
else:
    print("el bucle for terminó") #también se puede usar el else
lst = list(range(11)) #una lista de 0 hasta n-1, aquí n=11
lst_2 = list(range(2,21,2)) #lista empíeza en 2, llega hasta 20 y va de dos en dos
print(lst,lst_2)
for i in lst:
    print(i)
    if i==8:
        print("Ya llegó a 8")
        break
else: #cuando se usa break, este else tampoco se ejecuta
    print("terminó el ciclo for")
for i in lst_2:
    if i == 18:
        print("se omite")
        continue #aquí hace que continue el ciclo, pero
    #lo regresa al encabezado del for, por lo que no rompe el ciclo
    print(i) #aquí, para 18 no se imprimirá
