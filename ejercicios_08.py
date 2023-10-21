#Nivel 1:
#1 señalar si cumple con la edad
age = int(input("enter your age: "))#solicitamos la edad
if age>17: #si es mayor de edad, puede aprender a conducir
    print("You're old enogh to learn to drive")
elif age<18 and age>0:#si es positivo, señalamos lo que falta
    d=18-age
    print(f"You need {d} year(s) to learn to drive")
else: #si no es el caso, señalamos que pudo ocurrir algo mal
    print("You might have done a mistake")
#2 comparar edades
my_age = 27
your_age = int(input("Enter your age: "))
diff = your_age - my_age #calculamos la diferencias
if diff>0: #este el caso cuando es más grande
    if diff>1:
        print(f"You're {diff} years older than me")
    else: #este el caso cuando es solo por un año
        print("You're a year older than me")
elif diff<0:#aquí es más chico
    if diff<-1: 
        print(f"You're {-1*diff} years younger than me")
    else: #la diferencia es un año
        print("You're a year younger than me")
else: #este es el caso donde la edad es la misma
    print("You and me are the same age")
#3 comparando números
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: ")) #recibimos los números
if a>b:
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{b} is greater than {a}")
else:
    print("The numbers are the same")
# Nivel 2:
#1 codigo que califica estudiantes
cal = int(input("Enter the score: ")) #pedimos la calificación
if cal>=0 and cal<50:#separamos los rangos
    print("Grade: F")
elif cal>49 and cal<60:
    print("Grade: D")
elif cal>59 and cal<70:
    print("Grade: C")
elif cal>69 and cal<80:
    print("Grade: B")
elif cal>79 and cal<101:
    print("Grade: A")
else: #si se sale de esto, señalamos que debió ocurrir un error
    print("There should be a mistake")
#2 programa que señala la temporada del año:
month = str(input("Enter the month: ")) #pedimos el mes
month = month.lower() #convertimos todo a minúsculas para que no
#importe como haya escrito, solo que sean las letras correctas:
spring = ["march","april","may"]#creamos las listas de meses
summer = ["june","july","august"]
autumn = ["september","october","november"]
winter = ["december","january","february"]
if month in spring:
    print("It's Spring")
elif month in summer:
    print("It's Summer")
elif month in autumn:
    print("It's Autumn")
elif month in winter:
    print("It's Winter")#mostramos el mensaje en cada caso
#3 programa que añade elementos a una lista
fruits = ['banana', 'orange', 'mango', 'lemon'] #comenzamos con nuestra lista
print(f"I've got this list of fruits {fruits} please, add someone else")
fruit = str(input("What fruit do you want to add? "))
if fruit in fruits: #si está en la lista
    print("Sorry, that fruit is already in the list")#informamos
else: #cuando no esté
    fruits.append(fruit)#la agregamos
    print(f"Now the list is: {fruits}")# e imprimimos la nueva lista
#Nivel 3:
#comprobar información en un diccionario personal:
person={
    'first_name': 'Brian',
    'last_name': 'Parra',
    'age': 27,
    'country': 'Mexico',
    'is_marred': False,
    'skills': ['Electronics', 'Arduino', 'Advanced math', 'QFT', 'Python',"Statistics"],
    'address': {
        'Street': 'José María Morelos y Pavón',
        'zipcode': '01840'
    }
    } #tenemos el diccionario personal
if "skills" in person.keys(): #si está skills
    print(person['skills'][len(person['skills'])//2]) #imprimimos el termino medio
if "skills" in person.keys() and "Python" in person['skills']: 
    print("This person knows how to use Phyton")#si está skills y phyton en skills
    #imprimimos que sabe usar Python
if "Electronics" in person['skills'] and "Arduino" in person['skills']:
    print("It's a robotic entusiast")
elif "QFT" in person['skills']:
    print("It's a particles physicist")
elif "Advanced math" in person['skills'] and "Statistics" in person['skills'] and "Python" in person['skills']:
    print("It's a data scientist")
elif "Arduino" in person['skills'] and "Python" in person['skills']:
    print("It's a programmer")
else:
    print("we don't know its title")
if person['is_marred']==True:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He's married")
else:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He's not married")