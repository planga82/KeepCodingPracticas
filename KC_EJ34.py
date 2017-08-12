
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

class AlumnoRemoto(Alumno):

    skype = ''
    husoHorario=''

    def __init__(self, numero_matricula, nombre, apellido, correo_electronico, estatus_inscrito, skype, husoHorario):
        Alumno.__init__(numero_matricula, nombre, apellido, correo_electronico, estatus_inscrito)
        self.skype=skype
        self.husoHorario=husoHorario

class AlumnoPresencial(Alumno):
    numeroAsiento = 0

    def __init__(self, numero_matricula, nombre, apellido, correo_electronico, estatus_inscrito, numeroAsiento):
        Alumno.__init__(numero_matricula, nombre, apellido, correo_electronico, estatus_inscrito)
        self.numeroAsiento=numeroAsiento
