#nivel 1
my_tuple = tuple() #creamos una tupla vacía
names_brothers, names_sisters = ("Brian","Eber","Carlos","José"),("Isis","Brenda") #una tupla con nombres
sibilings = names_brothers+names_sisters #las unimos
print(names_brothers,names_sisters,sibilings)
print("tengo ",len(sibilings)," familiares")
family_members = list(sibilings) #convertimos a lista
family_members.append("Felix") #agregamos a papá y mamá
family_members.append("María")
family_members = tuple(family_members) #lo volvemos tupla
print(family_members)
#nivel 2
sibilings, parents = family_members[0:6],family_members[6:8] #desempaquetamos lo pedido
print(sibilings,parents)
fruits = ("Mango","Watermelon","Lemon","orange","Banana","Dragonfruit")
vegetables = ("Pumkin","Lettuce","Corn","Carrot","Onion")
animal = ("Lamb","Beef","Chicken","Turkey","Pork")#creamos la tuplas pedidas
food_stuff_tp = fruits+vegetables+animal #creamos la union de ellas
print(food_stuff_tp)
print(len(food_stuff_tp))
a = food_stuff_tp[3:13] #recortamos los elementos de enmedio
b= food_stuff_tp[0:3]+food_stuff_tp[13:16] #recortamos los primeros 3 elementos y los últimos 3
print(a,b)
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden') #copiado

print("¿Islandia está entre los países nórdicos? ",bool(nordic_countries.index("Iceland"))) #si está en la tupla
print("¿Polonia está entre los países nórdicos? ",bool(nordic_countries.index("Estonia"))) #no está