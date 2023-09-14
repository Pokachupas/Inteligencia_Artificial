#Aquí se esta creando un objeto, que es un tipo de dato nuevo que posee características (atributos) y métodos específicos

###Esta practica abarca del capítulo 2 al capítulo 6 del curso###

class Usuario:
    name = "xxxx"  #Aquí se utiliza una variable para representar una característica o "atributo" del objeto
    password = "xxxx"
    edad = 0000
    
    def __init__(self):  #Este método es necesario para crea una instancia (u objeto) de la clase Usuario. Un método es un acción que puede relizar cualquier objeto de la clase.
        return

    def setName(self): #Self se utiliza para autoreferir al objeto que implementa el método
        self.name = input("Ingrese su nombre completo: ")
        self.name = self.name.title()
    
    def setPassword(self):
        self.password = input("Ingrese su password: ")
    
    def setAge(self):
        self.edad = input("Ingrese su edad: ")

    def showData(self):
        testPassword = input("Ingrese su contraseña: ")
        if testPassword == self.password:
            print(self.name + "\n" + self.password + "\n" + self.edad)
        else:
            print("Contraseña incorrecta")

    def setData(self):
        self.setName()
        self.setPassword()
        self.setAge()



user1 = Usuario() #Aquí user1 es una instancia de la clase Usuario, por lo que posee todos sus atributos y métodos.
user1.setData()
user1.showData()


