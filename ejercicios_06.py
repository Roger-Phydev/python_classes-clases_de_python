#nivel 1:
it_companies = {"Facebook","Google","Microsoft","Apple","IBM", "Oracle","Amazon"} #creamos
print(it_companies)
it_companies.add("Twitter")#agregamos twitter
print(it_companies)
it_companies = it_companies.union({"Nvidia","Amd","intel"})#agregamos varios al mismo tiempo
print(it_companies)
it_companies.remove("Apple") #removemos un elemento
print(it_companies)
it_companies.discard("Apple") #aqui a diferencia de remove, no dará error
#esto a pesar de que Appple ya no sea un elemento
print(it_companies)
#Nivel 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
union = A.union(B) #unimos los conjuntos
intersection = A.intersection(B)
other_union = B.union(A)
print("A = ",A,"\n","B = ",B,"\n","A U B = ",union,"\n","A int B =",intersection)
print("¿Es A un subconjunto de B? ",A.issubset(B),"\n ¿Son A y B disjuntos? ",A.isdisjoint(B))
print("A U B = ", union," B U A = ",other_union)
print("¿AUB=BUA?",union==other_union) #la union es conmutativa
diff_a = A.difference(B)
diff_b = B.difference(A)
a_b = diff_a.union(diff_b)
diff_sim = A.symmetric_difference(B)
print("A-B = ",diff_a,"\nB-A = ",diff_b,"\nAQB = ",diff_sim,"\n¿Es AQB = (A-B)U(B-A)?",diff_sim==a_b)
del A,B,diff_sim,diff_a,diff_b,a_b,union,intersection,other_union #eliminamos por completo los conjuntos
#Nivel 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
l = len(age)
print(age)
age = set(age) #lo convertimos a conjunto
L = len(age)
print(age,"\ndifieren en",l-L,"elementos") #checamos la diferencie de longitud
"""
La diferencia entre tipos:
string= una cadena de caracteres
list= un conjunto de elementos de tipos variados, pero ordenado
tuple= similar a un list, pero no permite modificar sus elementos
set= un conjunto, puede contener diversos tipos de elementos, pero no admite repeticiones
"""
#tenemos que saber cuantas palabras hay en este frase sin repetir:
frase = "I am a teacher and I love to inspire and teach people" 
words = frase.split() #separamos las palabras
words = set(words) #lo hacemos un conjunto para quitar repeticiones
words_sort = list(words)
words_sort.sort()#ordenamos las palabras sin repetir
print("En la frase:",frase,". Hay",len(words),"palabras sin repetir\nLas palabras son: ",words_sort)