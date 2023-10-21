### Functions ###
#sirven para resolver problemas concretos
#ayudan a minimizar errores
def my_function (): #forma general de definir funciones
    print("Esto es una funcion")
#a partir de que se crea, se puede usar 
my_function ()
def sum_two_values(first_number,second_number):
    print(first_number+second_number)
sum_two_values(3,10)
def product_two_values_return(value_1,value_2):
    return value_1*value_2
result_1 = product_two_values_return(5,10)
result_2 = sum_two_values(25,25)
print(result_1) #aquí está el resultado del return
print(result_2) #aquí no imprime, porque la función
#no regresa nada
def print_full_name(name,last_name):
    print(f"{name} {last_name}")
print_full_name("Brian","Parra")
print_full_name(last_name="Parra",name="Brian")
#no es necesario meter los parámetros en el orden dado
#siempre que se nombren todos, y se igualen, pueden
#introducirse en cualquier orden.
def print_name_with_default(name,last_name,alias = "not alias available"):
    print(f"{name} {last_name} known as {alias}")
#poniendo valores en la definición, se asigna un valor 
#por defecto, osea, cuando no se meta valor a ese 
#parámetro, toma el valor señalado:
print_name_with_default("Brian","Parra")#sin alias
print_name_with_default("Brian","Parra","Roger")
def print_texts(*texts):#el * significa que hay tantos parámetros como se quiera, crea una lista
    for text in texts:
        print(text.upper(),end="")#todo seguido
    print("")#salto de línea al final

print_texts("Hola")
print_texts("Python","funciona","bien")