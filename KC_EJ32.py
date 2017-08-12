
from datetime import datetime

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


class Modulo:

    listaAlumnos = []
    fecha_Inicio = datetime.now()
    fecha_fin = datetime.now()

    def __init__(self,listaAlumnos,fecha_Inicio,fecha_fin):
        self.listaAlumnos = listaAlumnos
        self.fecha_Inicio = fecha_Inicio
        self.fecha_fin = fecha_fin

    def agregarAlumno(self,alumno):
        self.listaAlumnos.append(alumno)

    def dameAlumno(self, nombre, apellido):
        for alumno in self.listaAlumnos:
            if alumno.nombre == nombre and alumno.apellido == apellido:
                return alumno
        return None

    def dameAlumno(self, nombre, apellido):
        for alumno in self.listaAlumnos:
            if alumno.nombre == nombre and alumno.apellido == apellido:
                return alumno
        return None

    def alumnosInscritos(self):
        resultado = []
        for alumno in self.listaAlumnos:
            if alumno.estatus_inscrito:
                resultado.append(alumno)
        return resultado
