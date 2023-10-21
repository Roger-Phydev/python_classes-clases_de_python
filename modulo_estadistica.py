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