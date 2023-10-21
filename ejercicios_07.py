dog = {}#creamos un diccionario vacío con el nombre pedido
dog = dict.fromkeys(("name","color","breed","legs","age")) # le agregamos las claves pedidas
print(dog) #lo mostramos
students = {"first name":[],"last name":[], "gender":[],"age":[],"marital status":[],"skills":[],"country":[],"city":[],"address":[]}
print(students)#creamos el diccionario especificando que sus valores son listas
print(len(students)) #vemos su longitud: 9
print(type(students["skills"])) #muestra el tipo: lista
students["skills"] = ["science","history","coding"] #modificamos esta lista
print(students) #vemos la modificación
keys = list(students.keys()) #obtenemos una lista con las claves
values = list(students.values()) #obtenemos una lista con los valores
print(keys,values)
students = list(students.items()) #lo convertimos a una lista de tuplas
print(students)
del students[5] #borramos el elemento 5
print(students)
del dog #borramos un diccionario por completo