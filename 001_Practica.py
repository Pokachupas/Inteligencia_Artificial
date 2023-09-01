#Aquí se esta creando un objeto, que es un tipo nuevo de variable que posee características específicas

class Usuario:
    name = "xxxx"  #Aquí se utiliza una variable para representar una característica o "atributo" del objeto
    password = "xxxx"
    edad = 0000
    
    def __init__(self): 
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



user1 = Usuario()
user1.setData()
user1.showData()


