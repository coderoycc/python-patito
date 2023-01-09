class Persona:
    contadorId = 0
    
    def obtenerContador():
        Persona.contadorId +=1
        return Persona.contadorId
    
    def __init__(self, nombre, apellido, edad):
        self.id = Persona.obtenerContador()
        self.nombre=nombre
        self.apellido = apellido
        self.edad = edad
        
    def __str__(self):
        return f'ID:{self.id}\nNombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}'
    
    
    