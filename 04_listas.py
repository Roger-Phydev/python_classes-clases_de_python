### Listas ###
#lo de adentro es una lista
#cada elemento se separa por una coma
my_list = ["Phyton",2.3,False,0,2.3] #también es válido usar []
my_other_list = [27,1.82,"Brian","Parra"]
print(type(my_list)) #tienen su tipo propio: list
print(type(my_other_list))
print(len(my_list)) #tambien se puede medir la cantidad de objetos en su interior
print(my_list[0]) #poniendo entre [] el número de lugar, se accede a ese lugar, se inicia por 0
print(my_list[-1]) #señala el ultimo elemento, si hay n elementos, a partir de n da error y menos de -n-1 también falla
# OPERACIONES
print(my_list.count("Phyton")) #cuenta cuantas veces aparece el argumento
print(my_list.count(2.3))#funciona también con variables float, int etc.
edad,altura,nombre,apellido = my_other_list #igual, separa cada entrada a una variable
print(altura)#lo anterior se llama desempaquetar = "unpack"
print(my_list+my_other_list)#se puede concatenar
my_other_list.append("Xbox") #se agrega un elemento
print(my_other_list)
my_other_list.insert(1,"Morado")#agrega antes de la posición indicada
print(my_other_list)
my_other_list.remove("Morado") #remueve lo que se le señala
print(my_other_list)
my_list.remove(2.3) #pero solo elimina una vez
print(my_list) #u es el primero de izq a derecha
print(my_list.pop()) #muestra lo eliminado
my_pop_element = my_list.pop(2) #podemos asignar el valor eliminado en posicion dada
print(my_list)
print(my_pop_element)
del my_list[1] #aqui no importa que hay en posicion 2 (como en pop), solo se elimina
print(my_list)
my_new_list = my_list.copy()#copia el objeto
my_new_list.insert(0,"Es")
my_list.clear() #simplemente limpía la lista
print(my_list)
print(my_new_list)
my_new_list.reverse()#invierte el orden
print(my_new_list)
my_new_list.sort() #ordena usando criterios en el argumento
print(my_new_list) #en este caso ordena por la primer letra
my_new_list.append(4.66)
sub_list = my_new_list[1:3] #crea una sublista, con los elementos 1 y 2 de la original
print(my_new_list)
print(sub_list)