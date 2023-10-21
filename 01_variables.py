#vamos a ver variables
my_string_variable = "My String Variable" #una variable string
#nota: cuando se nombran variables suele comenzarse con minúsculas
#cada que se inicia una nueva palabra, la primera letra será mayúscula
#debería ser myVariable, pero en phyton se habitúa usar guiones
#bajos, y todo en minúsculas. Quedando lo que se escribió
print(my_string_variable)#imprimirá lo que escribimos arriba
my_int_variable=18
print(my_int_variable) #lo mismo pero con int
my_bool_variable= True
print(my_bool_variable)
my_int_to_str_variable=str(my_int_variable)#convierte entero a str
print(my_int_to_str_variable)#imprimimos
print(type(my_int_to_str_variable))#imprimimos el tipo
#aunque lo anterior en apariencia es lo mismo, en cuanto a operaciones no lo es
print(my_string_variable,my_int_variable,my_bool_variable)#se puede juntar todo
#print,int o type son funciones precargadas del sistema.
print(len(my_int_to_str_variable)) #por ejemplo, len cuanta la extensión de variables str
print("Este es el número que elegí: ",my_int_variable) #se puede mezclar texto y valores
#variables en una linea:
name,last_name, alias, age = "Brian Rogelio", "Parra Hernández", "Roger", "27"
#se asignan valor en el orden señalado, separando con comas, pero NO es aconsejable abusar de esto
print("Hello, my name is",name,last_name,",my alias is",alias,"and I'm",age,"years old")
#se puede hacer por separado con cualquier nombre:
name_1=str(input("What's your name? "))
last_name_1=str(input("What about your last name?"))
alias_1=str(input("do you have an alias? Tell me what is "))
age_1=int(input("How old are you?"))
print("check this out: Hello, my name is",name_1,last_name_1,",my alias is",alias_1,"and I'm",age_1,"years old")
#también podríamos usar las variables sin el sufijo 1, solo se reasignaría su valor.
