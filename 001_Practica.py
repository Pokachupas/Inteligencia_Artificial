#Aquí se esta creando una clase, que es un tipo de dato nuevo que posee características específicas

###Esta practica abarca del capítulo 2 al capítulo 6 del curso###

class Usuario:
    name = "xxxx"  #Aquí se utiliza una variable para representar una característica o "atributo" de la clase
    password = "xxxx"
    edad = 0000
    
    def __init__(self): #Este método es necesario para crear una instancia (u objeto) de la clase, un método es una acción que puede realizar cualquier objeto de la clase 
        return

    def setName(self):
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



user1 = Usuario() #Aquí user1 es una instancia de Usuario, por lo que posee los atributos y métodos de la clase Usuario
user1.setData()
user1.showData()


