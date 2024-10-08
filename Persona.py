class Persona():
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre       # _nombre es un atributo protegido
        self._edad = edad
        self._altura = altura
        self._sexo = sexo

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getAltura(self):
        return self._altura

    def getSexo(self):
        return self._sexo
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def setEdad(self, edad):
        self._edad = edad
        
    def setAltura(self, altura):
        self._altura = altura
        
    def setSexo(self, sexo):
        self._sexo = sexo
        
    def __str__(self):
        return "Mi nombre es " + self._nombre + " Tengo " + str(self._edad) + " años de edad y mido " + self._altura