#las actividades son variadas asi que las iré anotando:
#1:
print("Día 2 de 30 días programando en Phyton") #listo, esto se imprimirá
first_name = "Brian"
last_name = "Parra"
full_name = "Brian Rogelio Parra Hernández"
country = "México"
city = "CDMX"
age = 27
year = 2023
is_married = False #declaramos las variables solicitadas
is_true , is_light_on = True, False #declaramos varias variables en una sola línea como se pide
print(first_name,type(first_name))
print(last_name,type(last_name))
print(full_name,type(full_name))
print(country,type(country))
print(city,type(city))
print(age,type(age))
print(year,type(year))
print(is_married,type(is_married))
print(is_true,type(is_true))
print(is_light_on,type(is_light_on)) #imprimimos los datos con su tipo
print("tu nombre tiene",len(first_name),"caracteres de largo") #con esto sabemos la longitud del nombre
q=abs(len(first_name)-len(last_name)) #la diferencia absoluta entre nombre y apellido
print("mientras que tu apellido tiene",len(last_name),"caracteres, difiriendo en",q, "caracteres entre ambos")#nos dice cuantos caracteres difieren
#2:
num_one , num_two = 5, 4 #declaramos lo que se pide
print("los números son:", num_one, "and ", num_two)#los imprimimos
total = num_one + num_two #definimos el total
diff = num_one - num_two #definimos la diferencia
product = num_one*num_two #producto
division = num_one/num_two #división
remainder = num_two%num_one #resto
exp = num_one**num_two #exponenciación
floor_division = num_one//num_two #y función piso
print("y da en total:","\n" ,"suma: ",total, "resta: ", diff,"producto: ", product, "cociente: ", division, "con resto: ", remainder, "exponenciación ", exp, " y con división entera: ", floor_division) #lo imprimimos todo
#3: el radio de un círculo es 30m
r=30
area_of_circle = 3.1416*r**2 #calculamos el área
circum_of_circle = 2*3.1416*r #calculamos el perímetro
print("Área:",area_of_circle,"m^2 Circunferencia:",circum_of_circle,"m")#lo imprimimos
r=float(input("Dame el valor del radio del círculo en metros"))#recibimos el valor del radio
area = 3.1416*r**2 #calculamos su área
print("el area de tu circulo es:",area,"m^2") #le devolvemos su valor de area
#4 pregutamos los datos
nombre = input("dime tu nombre")
apellido = input("dime tu apellido")
pais = input("¿De dónde eres?")
edad = input("¿Cuántos años tienes")
print("hola",nombre,apellido,"de",pais,"con",edad,"años de edad")# se los devolvemos
help("keywords")#nos informará de palabras reservadas


