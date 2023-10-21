#1 concatenación:
print("30"+" Days"+" of"+" Phyton")#concatenamos
print("Coding "+"for "+"all") #concatenamos
#2 operaciones
company = "Coding For All" #asginamos valor inicial
print(company) #lo imprimimos
print(len(company)) #imprimimos su longitud
print(company.upper())#con mayúsculas
print(company.lower())#con minúsculas
print(company.capitalize(), company.title(),company.swapcase()) #usamos varias operaciones: solo la inicial en mayúscula, como título e intercambiar mayúsuclas y minúsculas
print(company[0:7]) #solo mostramos la primer palabra
print(company.find("Coding")>-1) #muestra si hay coding por lo menos una vez en la frase, si no hubiera lo izquierdo sería -1
print(company.replace("Coding","Phyton")) #remplazamos una palabra por la otra
print("Phyton for Everyone".replace("Everyone","All")) #reemplazamos
print(company.split()) #separa la cadena en varios string usando el espacio para separar
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(",")) #lo mismo pero usando la coma para separar.
print(company[0]) #muestra la letra en posición cero de company
print(company.rindex("l"))#muestra el indice final, pues l es la última letra y rindex busca la posición más alta en que aparece una l, debe ser 13 pues su longitud es 14 y el 0 cuenta
print(company[10]) #muestra el caracter en la posición 10
print(company[0],company[7],company[11])#creamos un acrónimo
a = "Phyton For Everyone"
print(a[0],a[7],a[11]) #repetimos para Phyton for  evryone
print(company.index("C"))#muestra el indice donde aparece C por primera vez
print(company.index("F"))#lo mismo para F
print("Phyton for all people".rindex("l")) #muestra el indice donde aparece por última vez l
print("You cannot end a sentence with because because because is a conjunction".find("because"))
print("You cannot end a sentence with because because because is a conjunction".rindex("because")) #buscamos indices de 1a y ultima aparicion
print("You cannot end a sentence with because because because is a conjunction"[31:47+len("because")]) #solo imprimimos because [x3] usando lo anterior
print(company.startswith("Coding"))
print(company.startswith("coding"))#vemos si inicia con Coding o coding
b = "        coding for all         "#vamos a remover los espacios
print(b)
print(b.index("c"))
print(b.rindex("l"))#vemos donde inicia y acaba
print(b[8:22])#quedando así
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier()) #señala si son nombres adecuados para variable, el de arriba no, el de abajo sí
c=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(c[0]," ",c[1]," ",c[2]," ",c[3]," ",c[4])#ponemos de corrido
print("I am enjoying this challenge.\nI just wonder what is next.") #separamos la frase
print("Name\tAge\tCountry\tCity\nAsbeneh\t250\tFinland\tHelsinki")#formamos una tabla usando saltos de línea y tabuladores
print("radius = 10\narea=3.14*radius**2\nThe area of a circle with radius 10 is 314 meters square.")#escribimos lo solicitado
p,q = 8,6 #definimos nuestras variables
print(f"{p}+{q}={p+q}")#hacemos la tabla pedida
print(f"{p}-{q}={p-q}")
print(f"{p}*{q}={p*q}")
print(f"{p}/{q}={p/q}")
print(f"{p}%{q}={p%q}")
print(f"{p}//{q}={p//q}")
print(f"{p}**{q}={p**q}")