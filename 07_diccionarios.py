### Dictionaries ###
my_dict = dict()#se crea en blanco
my_other_dict = {"Nombre":"Brian","Apellido":"Parra","Edad":27} #también, aunque se parezca a set
# los puntos señalan que los dos datos están relacionados, se separa con coma
my_dict = {#También se puede acomodar con más formato
    "Nombre":"Brian",
    "Apellido":"Parra",
    "Edad":27,
    "Lenguajes":{"Phyton","Swift","Kotlin"}, #en este caso tenenmos un set como valor
    1:1.82
}
#un diccionario es una estructura donde podemos tener datos "clave"-"valor" relacionados
print(my_dict)
print(len(my_dict)) #su longitud es la cantidad de claves
print(my_dict["Lenguajes"]) #muestra los valores asociados a una clave
my_dict["Nombre"] = "Pablo" #se puede modificar
print(my_dict["Nombre"])
my_dict["Calle"] = "Av. José María Morelos y Pavón"#asi se puede agregar un nuevo campo
print(my_dict)
# Operaciones:
del my_dict["Calle"] #podemos eliminar una clave y sus valores
print(my_dict)
print("Parra" in my_dict)
print("Apellido" in my_dict) #búsqueda por clave
print("Parra" in my_dict["Apellido"]) #búsqueda de valores en clave
print(my_dict.items()) #listado de items
print(my_dict.keys()) #solo muestra las claves en una lista
print(my_dict.values()) #muestra los valores 
print(my_dict.fromkeys(("Apellido",1))) #crea un diccionario nuevo pero sin valores
#lo anterior reutiliza un diccionario, aunque también puede crear un diccionario nuevo sin campos así:
keys = ["Hora","Lugar","Año"] #puede crearse a partir de una lista
my_new_dict = dict.fromkeys(keys)#crea diccionario sin valores
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict) #crea un dic con las mismas claves pero sin valores
my_new_dict = dict.fromkeys(my_dict,["Brian","Parra"]) 
print(my_new_dict) #añade lo que va después de la como en todas las entradas
print(list(my_new_dict)) #cuando se transforma en lista, solo aparecen las claves
print(list(my_new_dict.values())) #aunque también se puede hacer con los valores
#en lo anterior, my_new_dict.values() NO es una lista, es de tipo "dict values"
my_dict.clear#borra todo el diccionario