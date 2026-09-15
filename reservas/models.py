from mongoengine import Document, StringField


class Reserva(Document):
    nombre_miembro = StringField()
    clase = StringField()
    fecha = StringField()
