### Sets ###
my_set = set() #conjunto vacío
my_other_set = {"Brian","Parra",27} #analogamente a lo de arriba, pero inicialmente es un diccionario, esto es por tener tipado débil
print(type(my_set),type(my_other_set)) #ya con datos, ambos son set

#Operaciones

print(len(my_other_set)) #sigue contando elementos
# ya no permite mostrar un elemento, fallaría el print(my_other_set[1])
my_other_set.add("Roger") #podemos añadir
print(my_other_set) #no es una estructura ordenada, por ello no existe 1er elemento, ni último
my_other_set.add("Roger")
print(my_other_set) #al ser un conjunto no admite elementos repetidos
print("Roger" in my_other_set)
print("Royer" in my_other_set) #sirve para saber si existe un elemento en el conjunto
my_other_set.remove("Roger")
print(my_other_set) #también borrar
my_other_set.clear()
print(my_other_set) #limpia
#la ventaja es que es más rapido que list y no admite repeticiones
del my_other_set #elimina la variable
set_1, set_2, set_3 = {"A","B","C","D"} , {"C","D","E","F"},{"E","F"}
print(set_1,set_2) #también tiene operaciones de conjuntos
print(set_1.intersection(set_2)) #intersección
print(set_1.difference(set_2)) #diferencia
print(set_1.union(set_2)) #union
print(set_1.symmetric_difference(set_2)) #diferencia simétrica
print(set_1.isdisjoint(set_3)) #saber si son disjuntos
print(set_3.issubset(set_2)) #saber si es subconjunto
print(set_2.issuperset(set_3)) #saber si contiene al otro conjunto