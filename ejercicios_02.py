# grupo uno, simplemente declaro variables en su tipo
edad = int(27)
altura = 1.72 #ya es float
complex_variable= complex(0) #almacena un valor complejo
#ejercicio 2:
h=float(input("Dame el valor de la altura del triangulo ")) #pedimos la altura
b=float(input("Dame el valor de la base del triángulo ")) #pedimos la base
a=0.5*b*h #calculamos la altura
print("El área de tu triángulo es ",a) #devolvemos el valor
#ejercicio 3:
a=float(input("Dime cuanto mide el primer lado del triángulo ")) #pedimos los datos
b=float(input("Dime cuanto mide el segundo lado del triángulo "))
c=float(input("Dime cuanto mide el tercer lado del triángulo "))
p=a+b+c#calculamos
print("El perímetro de tu triangulo es ",p) #devolvemos
#ejercicio 4:
a=float(input("Dime la altura del triangulo "))
b=float(input("Dime la base del rectángulo "))
A=a*b
p=2*(a+b)
print("El área de tu triangulo es ",A, " y su perímetro es ",p)
#ejercicio 5:
r=float(input("Dime el radio de tu círculo "))
A=3.14*r**2
p=2*3.14*r
print("El área de tu circulo es ",A," y su circunferencia es ",p)
#ejercicio 6: Tenemos la recta y=2x-2
#para este caso es muy simple si y=0, x=1, si x=0, y=2, y la pendiente es 2
#ejercicio 7: Repetimos para los puntos (2,2) y (6,10)
m=float((10-2)/(6-2))
d=((2-6)**2+(2-10)**2)**0.5
print("pendiente: ",m," distancia: ",d)
print(m==2) #comparamos las pendientes
#ejercicio 8: calculamos solo dos valores, se hará cero para valores negativos por tener puros coef positivos:
y=(-2)**2+6*(-2)+9
print(y)
y=(-3)**2+6*(-3)+9
print(y)
#obviamos que -1 no lo satiface, pero encontramos que -3 es la solución.
#ejercicio 9: 
print("la longitud de Phyton es ",len("Phyton")," mientras que la de dragon es ",len("dragon")) #mostramos la longitud de cada uno
print("phtyon"<"dragon") #hacemos una comparación falsa
print(("on"in"phyton")and("on"in"dragon")) #vemos si "on" está en ambas palabras
print("jargon"in"I hope this course is not full of jargon") #aquí vemos si aparece la palabra en la frase en cuestión
l=len("phyton")
l=float(l)#lo reconvertimos a float
l=str(l)#lo reconvertimos a str
print(l,type(l)) #imprimimos a l junto con su tipo
#ejercicio 10: para comprobar que un número sea par es fácil, eso ocurre solo si n%2=0.
a=7//3
b=int(2.7)
print(a==b)#checamos si son iguales
print(type("10")==type(10))#checamos si son del mismo tipo
#a=int("9.8")  esto no está definido
#print(a==10) no se pudo hacer
#ejercicio 11: iniciamos pidiendo los datos
a=int(input("¿Cuántas horas trabajas a la semana? "))
b=int(input("¿Cuánto ganas por hora? "))
g=a*b#calculamos
print("Ganas ",g," a la semana")#devolvemos los datos
#Ejercicio 12: pedimos la edad
a=int(input("Dime tu edad "))
b=a*60*60*24*365
print("Has vivido ",b," segundos hasta ahora")
#Ejercicio 13: simplemente acomodamos la tabla
print(1,1,1,1,1)
print(2,1,2,4,8)
print(3,1,3,9,27)
print(4,1,4,16,64)
print(5,1,5,25,125)
#Todo funcionó :D