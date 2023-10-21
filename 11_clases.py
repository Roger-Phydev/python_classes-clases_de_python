### Clases ###
#Sirve como conjunto universal para delimitar usos o contexto de ciertos objetos
class MyEmptyPerson: #así se define una clase, cuando es una clase suele usarse cammel case
    #lo anterior son normas de buena práctica de programación
    pass #esto equivale a null, no hace nada
print(MyEmptyPerson())

class Person():
    def __init__(self,name,last_name,alias = "Sin alias") -> None:#esto sirve como constructor de clase
        #lo anterior da característica
        self.name = name# aquí self.name significa que person tiene la propiedad "name" y su valor es el de name
        self.last_name = last_name#se almacenan los datos
        self.__alias = alias #aquí alias está en PRIVADO, no se puede modificar
        self.full_name = f"{name} {last_name} ({alias})"
    def walk (self): #esta es una función, para póder usar los guardado
        #se debe poner self como parámetro
        print(f"{self.full_name} está caminando")
    def get_alias(self):#para poder acceder al alias, se debe crear una función aparte
        return self.__alias 
my_person = Person(name="Brian",last_name="Parra",alias="Roger")
print(my_person.name)
print(my_person.last_name)
print(my_person.full_name)
my_person.walk()
my_person.full_name = "Brian Parra (Elver Galarga)"
my_person.walk()#se puede modificar los valores (características) después de construirlo
print(my_person.get_alias())
#dicho de otra manera, una clase es algo que almacena
#características (valores) y acciones (funciones) de algo
