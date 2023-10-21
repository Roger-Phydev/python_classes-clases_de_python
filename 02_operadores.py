### Operadores ###
"""
Para algunos casos resulta utilen usar descripciones de tipo iterativo, en cuyo caso:
x p= n es una estrucutura que equivale a x=x p n, con p un operador que ya conocemos. Por ejemplo:
x +=5 equivale a x=x+5, lo mismo aplica con -,*,/,%,//,**, etc.
"""
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 % 4)
print(3 // 4)
print(3 ** 4)
#en algunos casos estas operaciones se pueden usar con str, + une cadenas:
print("Hola"+" "+"Mundo")
#pero no se puede mezclar tipos:
#print("Mide"+" "+5) no funcionaría, pero se puede agregar str:
print("Mide"+" "+str(5))
#también la multiplicación por enteros funciona, a veces forzando
print("hola "*10)
print("Ja "*int(3.4))

### Operadores Comparativos ###
# Cuando se necesita comparar datos, se usan distintos operadores
print(3<4)
print(3<=4)
print(3>4)
print(3>=4)
print(3==4) #compara si son iguales
print(3!=4) #compara si son distintos
print(3<4<7)
print(3<4<2)
print("Hello">"Phyton") #compara la ordenación alfabética distinguiendo también entre mayúsculas y minúsculas:
print("A">"Z")
print("a">"A")

### Operadores Lógicos ###
# Se trata de operadores que actúan sobre variables booleanas
print((3>4) and ("Hola">"Phyton")) #solo da True si ambas son True
print((3>4) or ("Hola">"Phyton")) #solo da False si ambas son False
print(not("Hola">"Phyton")) #invierte, osea que False->True y True->False
