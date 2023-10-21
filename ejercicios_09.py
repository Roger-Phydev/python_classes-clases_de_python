### Nivel 1 ###

##1 iterar de 0 a 10 usando while y for
condition ,my_list = 0, list(range(11)) #creamos nuestra lista y condicion
for i in my_list: #usando for, nota: también puede usarse en el for directamente el range(11)
    print(i) #solo imprimimos cada elemento
while condition<11:
    print(condition)#imprimimos cada vez
    condition+=1#sumamos 1

##2 iterar de 10 a 0
condition =10 #aquí damos valor inicial de 10
for i in range(11): #aquí usamos la alternativa de usar range
    print(10-i)#lo hacemos decreciente
while condition>-1:
    print(condition)
    condition-=1 #restamos en cada ocasión

##3 triangulo de #:
for i in range(1,8):#comienza en 1 acaba en 7
    print("#"*(i))#imprime i veces #
#la versión con while es:
a = 1
while a<9:
    print("#"*a)
    a+=1

##4 pinta un cuadrado de 8x8 de # usando ciclos anidados
#Versión con while
a=1 #comenzamos en 1
b=1
while a<9:#esta será la fila
    while b<9:
        if b==1 and a>1:#cuando se resetea b (a>1), 
            print("\n# ",end="")#hace un salto de linea
        elif a*b==64:#esta condición implica a=8 y b=8
            print("#")#en la última ocasión no continua sobre la misma linea
        else:
            print("# ",end="")#en los otros casos, pinta sobre la misma linea
        b+=1#incrementa la columna
    a+=1#incrementamos la fila
    b=1#reiniciamos la columna
#versión con for:
for i in range(1,9):
    for j in range(1,9):
        if j==1 and i>1:
            print("\n# ",end="")
        elif j==8 and i==8:
            print("# ")#en la ultima línea. no continua en la misma linea
        else:
            print("# ",end="")

##5 imprimir un patrón proporcionado tabla de los cuadrados
#Versión for
for i in range(11):
    print(f"{i}x{i}={i*i}")
#versión while
a=0
while a<11:
    print(f"{a} x {a} = {a**2}")
    a+=1

##6 mostrar elementos de una lista con for:
list_1 = ['Python', 'Numpy','Pandas','Django', 'Flask']
for x in list_1:
    print(x)

##7 iterar de 0 a 100 solo pares con for
#primer método:
for i in range(0,101,2):#aquí clasificamos directo en range
    print(i)
#segundo método:
for i in range(101):
    if i%2==0:#usamos el módulo para comparar
        print(i)
#este método se puede extender a multiplos de n

##8 iterar de 0 a 100 solo impares con for:
#primer método(range):
for i in range(1,100,2):
    print(i)
#segundo método(if):
for i in range(0,101):
    if i%2==1:
        print(i)

### Nivel 2 ###
##1 usa for para iterar de 0 a 100 y sumar todo
s = 0#aquí guardamos la suma
for i in range(101):
    s+=i#sumamos a s cada uno
print(f"La suma de los primeros 100 números naturales es {s}")

##2 sumar todos los pares y luego impares de señalar cada suma
s_i = 0#suma de impares
s_p = 0#suma de pares
for i in range(101):
    if i%2==0: #si es par
        s_p+=i#se suma a los pares
    else:#si no
        s_i+=i#se suma a los impares
print(f"La suma de pares entre 0 y 100 es {s_p}, mientras que la de los impares es {s_i}")

### Nivel 3 ###
##1 extraer información de una lista muy grande
#nota: se realizó en otro archivo aparte por el peso

##2 invertir el orden de una lista usando un for
fruits = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruits)):
    fruits.insert(0,fruits[i]) #copiamos al inicio
    del fruits[i+1] #eliminamos el que copiamos
    #de esta manera, vamos pasando al inicio cada uno, inviertiendo el orden
    #la ventaja es que no recurre a crear otra lista.
print(fruits)
#la otra manera es crear otra lista:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_inv = [0,0,0,0]
for i in range(len(fruits)):
    fruits_inv[i]=fruits[len(fruits)-1-i]#invertimos el orden
print(fruits_inv)

#3 en este caso hacemos estadística sobre una cantidad MASIVA de datos,
#se anexa en otro archivo

    