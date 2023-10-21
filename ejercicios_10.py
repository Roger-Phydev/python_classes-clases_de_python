### Nivel 1 ###
##1 función suma de dos números:
def add_two_numbers(number_1,number_2):
    return number_1+number_2
a = add_two_numbers(12,3)
print(a)

##2 área de un circulo:
def area_of_circle(r):
    return 3.1415*r*r
a = area_of_circle(3)
print(a)

##3 suma arbitraria
def add_all_nums(*numbers):
    s=0#suma
    e=0#ayuda a saber si hay errores
    for number in numbers:
        if type(number) is float or type(number) is int:
            s+=number #en caso de que sea un número se acumula
        else:#en caso contrario detiene el ciclo y hace e=1
            e=1
            break
    if e==0:#si no hay error
        return s#devuelve s
    else:#cuando hay error
        print("there was an error, check every argument is a number") #manda un mensaje
add_all_nums(1.2,"s")
add_all_nums(3.66,True,0)
print(add_all_nums(1,12.3,13,2.1,5.6))

##4 convertir celsius a fahrenheit:
def convert_celsius_to_fahrenheit(temperature):
    return (9/5)*temperature+32
print(convert_celsius_to_fahrenheit(0))
print(convert_celsius_to_fahrenheit(20))

##5 verficar la temporada del año
def check_season(month):
    month = month.lower()#convertimos a minúsculas para facilitar cosas
    if month in ["december","january","february"]:
        print("Winter")
    elif month in ["march","april","may"]:
        print("Spring")
    elif month in ["june","july","august"]:
        print("Summer")
    elif month in ["september","october","november"]:
        print("Autumn")
    else:
        print("Oops, there was an error")
check_season("December")
check_season("MaY")
check_season("JULY")
check_season("NoVemBer")
check_season("Yeah")

##6 calcular la pendiente de ecuación lineal:
def calculate_slope(A,B,C):
    if B==0:
        return "infinity"
    else:
        return -A/B
print(calculate_slope(1,1,0))
print(calculate_slope(2,4,7))

##7 solucionando ecuaciones cuadráticas
def solve_quadratic_eqn(a,b,c):
    return [(-b)/(2*a)+((b*b-4*a*c)**0.5)/(2*a),(-b)/(2*a)-((b*b-4*a*c)**0.5)/(2*a)]
#regresamos una lista con ambas soluciones:
print(solve_quadratic_eqn(1,0,1))

##8 imprimir elementos de una lista:
def print_list(list):
    for element in list:
        print(element)
l = ["Python","it's","a","good","language"]
print_list(l)

##9 función que revierte listas usando ciclos:
def reverse_list(list):
    l_1 =[0 for i in range(len(list))] #creamos lista de igual longitud
    for i in range(len(list)):
        l_1[i]=list[len(list)-1-i] #invierte el orden
    return l_1#regresa la lista
print(reverse_list(["1",2,True]))

##10 función que pone en mayúscula el inicio de una lista
def capilize_list_items(list):
    for i in range(len(list)):
        list[i]=list[i].capitalize()
    return list
print(capilize_list_items(["hola","good","gReat"]))

##11 añadir items
def add_items(list,*items):
    for item in items:
        list.append(item)
    return list
list_1 = ["A",2]
list_1 = add_items(list_1,"B","C","D")
print(list_1)

##12 remover items
def remove_items(list,*items):
    for item in items:
        if item in list:#solo remueve si está en la lista
            list.remove(item)
    return list
list_1 = remove_items(list_1,"B",1)
print(list_1)

##13 suma de números
def sum_of_numbers(n):
    s=0 #la suma de los números
    for i in range(n):
        s+=i+1
    print(s)
sum_of_numbers(10)
sum_of_numbers(100)

##14 suma de impares hasta un número natural
def sum_of_odds(n):
    s=0
    for i in range(n):
        if (i+1)%2 ==0:
            s+=i+1
    print(s)
sum_of_odds(100)

##15 suma de pares hasta un número natural
def sum_of_even(n):
    s=0
    for i in range(n):
        if (i+1)%2 ==1:
            s+=i+1
    print(s)
sum_of_even(100)

### Nivel 2 ###
##1 ¿cuántos pares e impares hay en hasta a un número dado:
def evens_and_odds(n):
    o=0#contará impares
    e=0#contará pares
    for i in range(n+1):
        if i%2 == 0:#en caso de ser par
            e+=1#se suma al contador de pares
        else:
            o+=1#en caso contrario al de impares
    print(f"There are {e} even numbers and {o} odd numbers between 0 and {n}")
evens_and_odds(100)

##2 el factorial de un natural:
def factorial(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
print(factorial(5))

##3 checar si está vacío:
def is_empty(a):
    if not a:#si está vacío
        print("It's empty")
    else:
        print("it's not empty")
a = ["a"]
b=[]
is_empty(a)
is_empty(b)

##4 estadística básica en listas:
def calculate_mean(list): #promedio
    s=0#suma
    for element in list:#suma de todo
        s+=(element)/(len(list))
    return s
def calculate_median(list):
    list.sort() #ordenamos
    if len(list)%2 == 0:#si hay una cantidad par de elementos
        return (list[len(list)//2] + list[(len(list)//2 )-1])/2 #promediamos los de enmedio
    else:
        return list[len(list)//2+1]#si no, es el elemento de enmedio
def calculate_mode(lst):
    elements = set(lst)#evitamos repeticiones
    elements = list(elements) #lo hacemos lista
    num = [0  for i in range(len(elements))]#lista para guardar cuantas veces aparece
    for i in range(len(elements)):#para cada número
        for items in lst:#ve en la lista
            if items == elements[i]:#si concuerda
                num[i]+=1#añade 1 a las apariciones
    order = num.copy()
    order.sort()#creamos uno ordenado de las apariciones
    m = order[len(num)-1] #será la cantidad más grande de apariciones
    n=(len(num)-order.index(m)) #es la cantidad que aparece m =cantidad de modas
    mode = set()
    initial = 0
    for i in range(n): #buscaremos todos los elementos que aparezcan la mayor cantidad de veces
        j=num.index(m,initial)#comienza a buscar desde el lugar indicado
        mode.add(elements[j])#añade el número correspondiente de la lista de elementos
        initial=j+1 #ahora empezaremos a buscar después de esta aparición
    return mode
def calculate_range(list):
    list.sort()#ordenamos
    return list[len(list)-1]-list[0] #el rango es la diferencia entre el máximo y el mínimo
def calculate_variance(list):
    m=calculate_mean(list)#calculamos el promedio
    v=0#la varianza:
    for i in range(len(list)): #suma de desviación del promedio al cuadrado
        v+=(list[i]-m)**2
    return v
def calculate_std(list):
    return (calculate_variance(list))**0.5#es la raíz de la varianza
Proof = [1,2,1,1,2,3,2,0,0]
print(f"Tengo la lista {Proof} y su estadística es:")
print(f"Promedio: {calculate_mean(Proof)} || Mediana: {calculate_median(Proof)}")
print(f"Moda: {calculate_mode(Proof)} || Rango: {calculate_range(Proof)}")
print(f"Varianza: {calculate_variance(Proof)} || Desviación estándar: {calculate_std(Proof)}")

### Nivel 3 ###
##1 checar si algo es primo
def is_prime(n):
    i=2 #empezamos por 2
    while n%i != 0:#mientras i no sea divisor
        i+=1#incrementamos i
    if i==n:#si al final i llega a n+1
        print("It's a prime") #es primo
    else:
        print("It's not a prime")#si se queda antes, hubo otro divisor no trivial y no es primo
is_prime(11)

##2 ver si todos los elementos en una lista son únicos.
def are_items_unique(lst):
    lst_1 = set(lst)
    if len(lst_1) == len(lst): #habrá elementos únicos si al convertir a conjunto siguen habiendo los mismos
        print("There are unique elements in the list")
    else:
        print("There are repeated elements in the list")
A = [1,2,3,4,5]
B = [1,1,3,4,5]
are_items_unique(A)
are_items_unique(B)

##3 ver si todos los elementos de una lista son del mismo tipo
def are_items_same_type(lst):
    for i in range(1,len(lst)):
        if type(lst[0]) != type(lst[i]):#solo es necesario ver si coinciden con el del primero
            print("There are at least two elements of different type")#señalamos que no son del mismo tipo
            break #y rompe el for
    else:
        print("All elements are the same type") #en caso de que concluya el for, todos son del mismo tipo
A=[1,2,3,4] #mismo tipo
B=[1,2,True] #diferente tipo
are_items_same_type(A)
are_items_same_type(B)

##4 verifica si algo es una variable de python aceptable
a="blade runner"
def is_correct_variable(a):
    if a.isidentifier():#si es un nombre válido
        print("Yes, it's a valid variable name")
    else:
        print("No, try with another name")
is_correct_variable(a)

##5 vamos a trabajar con una cantidad de datos masivos, se realiza aparte.