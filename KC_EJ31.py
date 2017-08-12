
class Alumno:

    numero_matricula = 0
    nombre = ""
    apellido = ""
    correo_electronico = ""
    estatus_inscrito = True

    def __init__(self, numero_matricula, nombre, apellido, correo_electronico, estatus_inscrito):
        self.numero_matricula = numero_matricula
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.estatus_inscrito = estatus_inscrito
