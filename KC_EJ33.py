
from datetime import datetime, date, time, timedelta
import calendar

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

    def imprime(self):
        if self.estatus_inscrito:
            matriculado = 'Matriculado'
        else:
            matriculado = 'No matriculado'
        print('Matricula: ' + self.numero_matricula +
              ', Nombre:' + self.nombre +
              ' , Apellido' + self.apellido +
              ', Correo: ' + self.correo_electronico +
              ' ' + matriculado)

class Modulo:
    listaAlumnos = []
    fecha_Inicio = datetime.now()
    fecha_fin = datetime.now()

    def __init__(self,fecha_Inicio,fecha_fin):
        self.listaAlumnos = []
        for i in range(10):
            alumno = Alumno('Matricula' + str(i), 'Nom' + str(i), 'Ap' + str(i), 'correo' + str(i) + '@gmail.com', True)
            self.listaAlumnos.append(alumno)

        for i in range(11, 20):
            alumno = Alumno('Matricula' + str(i), 'Nom' + str(i), 'Ap' + str(i), 'correo' + str(i) + '@gmail.com',
                            False)
            self.listaAlumnos.append(alumno)
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

    def dameAlumnoMatricula(self, matricula):
        for alumno in self.listaAlumnos:
            if alumno.numero_matricula == matricula:
                return alumno
        return None

    def alumnosInscritos(self):
        resultado = []
        for alumno in self.listaAlumnos:
            if alumno.estatus_inscrito:
                resultado.append(alumno)
        return resultado

    def imprimeTodosAlumnos(self):
        for alumno in self.listaAlumnos:
            alumno.imprime()

    def imprimeAlumnoPorMatricula(self,matricula):
        a = self.dameAlumnoMatricula(matricula)
        a.imprime()



modulo = Modulo(datetime.now(), datetime.now() + timedelta(days=60))
modulo.imprimeTodosAlumnos()
matricula = raw_input("Matricula Alumno: ")
modulo.imprimeAlumnoPorMatricula(matricula)