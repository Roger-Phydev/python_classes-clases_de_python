### Condicionales ###
# En general, los condicionales comprueban si alguna condición se cumple
# para esta condición se usa al menos una variable de condición:
my_condition = True
if my_condition: # if condición : (my condition es igual a my condition == True en este caso porque ya es booleano)
    print("Es verdad") #codigo que realiza si se cumple la condición
#para que algo se ejecute con el condicional, debe tener un tabulador
#de distancia respecto a la izquierda, si está pegado a la izquierda,
#ese código se ejecuta sin importar la condición
if my_condition == False:
    print("Es Falso") #no se imprime al no cumplir la condición
my_condition=5*2
if my_condition:
    print("si se cumplió") #aquí no ejecuta al no ser booleano
if my_condition >9:
    print("se cumplió") #aqui si se cumple
my_condition=2*3
if my_condition >10:
    print("la condición es mayor a 10")
else: #el else se ejecuta cuando no se cumpla la condición
    print("la condición es menor o igual que 10")
my_condition=-5
if my_condition < 10 and my_condition > 5:
    print("la condición está entre 5 y 10")
if my_condition<5 and my_condition>-5:
    print("la condición está entre -5 y 5")
elif my_condition>=5: #esta es una segunda condición que se verifica si no se cumple la primera
    print("la condición es mayor a 5")
elif my_condition<-5: #pueden haber más de un caso
    print("la condición es menor a -5")
else:
    print("la condición es -5")
my_string = "mi cadena"
my_second_string = ""
if my_string: #esto comprueba si no es vacía
    print("mi cadena de texto no es vacía")
if not my_second_string: #así se comprueba si es vacía
    print("esta otra es vacía")