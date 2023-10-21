#repaso
list_empty = [] #empezamos definiendo una lista vacía
list = [1.2,6.32,"Hola","feliz cumpleaños",14.6,2.3,6] #creamos otra con más de 5 elementos
print(len(list))
print(list[0],list[3],list[6]) #mostramos el primer, medio y final elemento
mixed_data_types = ["Brian",27,1.82,"single","Mexico city"]
it_companies = ["Facebook","Google","Microsoft","Apple","IBM", "Oracle","Amazon"]#creamos lo que se pide
#operaciones
print(mixed_data_types)
print(it_companies) #imprimimos las listas
print(len(it_companies)) #averiguamos cuantas compañias hay
print(it_companies[0],it_companies[3],it_companies[6]) #imprimimos la 1a, intermedia y ultima compañia
it_companies[5]="Amd" #modificamos una entrada
print(it_companies)#vemos la modificación
it_companies.append("Nvidia") #agregamos uno a la lista
it_companies.insert(3,"Intel") #insertamos uno en mitad
it_companies[6]=it_companies[6].upper()#hacemos esta entrada toda en mayúsculas
print(it_companies[0],"#;",it_companies[1],"#;",it_companies[2],"#;",it_companies[3],"#;",it_companies[4],"#;",it_companies[5],"#;",it_companies[6],"#;",it_companies[7],"#;",it_companies[8])
#mostramos todos enlazados con la cadena pedida
print(bool(it_companies.count("Nvidia"))) #verificamos si Nividia está en la lista
it_companies.sort() #ordenamos la lista
it_companies.reverse() #la invertimos
print(it_companies) #lo mostramos
it_companies_1 = it_companies[0:3]#cortamos los primeros 3 elementos
it_companies_2 = it_companies[len(it_companies)-3:len(it_companies)]#cortamos los tres últimos
it_companies_3 = it_companies[3:len(it_companies)-2] #las de enmedio
print(it_companies_1) #mostramos como queda
print(it_companies_2)
print(it_companies_3)
del it_companies[0] #eliminamos la primera compañia
del it_companies[int(len(it_companies)/2)-1] #la de enmedio
del it_companies[len(it_companies)-1] #la última
print(it_companies)#mostramos
it_companies.clear() #borramos la lista
print(it_companies)
del it_companies #la borramos
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] #definimos
back_end = ['Node','Express', 'MongoDB']
complete = front_end+back_end #las juntamos
print(front_end)
print(back_end)
print(complete)
#ejercicios nivel 2:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() #ordenamos
print("mínimo: ",ages[0],"máximo: ",ages[9]) #mostramos el máximo y mínimo despues de ordenar
ages.insert(0,19)
ages.append(26) #agregamos el mínimo y máximo de nuevo, sin perder el orden
#al ser 12 elementos (usando print(len(ages)) ), su mediana es el promedio de las entradas 5 y 6
print(ages)
print("la mediena es: ",(ages[5]+ages[6])/2)
p=(ages[0]+ages[1]+ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9]+ages[10]+ages[11])/12
print("el promedio es: ",p)#mostramos el promedio
print("el rango es: ",ages[11]-ages[0]) #el rango = diferencia entre max y min
a = ages[0]-p
b = ages[11]-p
print("comparando cantidades: ",abs(a-b))#vemos la diferencia