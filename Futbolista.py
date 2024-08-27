from persona import Persona
from deportista import Deportista

# Description: Clase que hereda de las clases Persona y Deportista, y que tiene como atributos propios los goles marcados, tarjetas rojas y pierna habil.
class Futbolista(Persona, Deportista):
    _listaFutbolistas = []
    
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil, deporte = "Futbol"):
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, añosPracticando)
        Futbolista._listaFutbolistas.append(self)
        
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados
        
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas
        
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil
        
    def __str__(self):
        return "Mi nombre es " + self._nombre + " soy profesional en el deporte " + self._deporte + " Tengo " + str(self._edad) + " años de edad y llevo " + str(self._añosPracticando) + " años en el deporte"