from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, RadioField
from wtforms import validators
from flask_wtf.csrf import CSRFProtect

class userForm(FlaskForm):
    matricula = IntegerField('Matricula', [
        validators.DataRequired(message='La matricula es requerida')
    ])

    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo nombre es requerido')
    ])

    apellido = StringField('Apellido', [
        validators.DataRequired(message='El campo apellido es requerido')
    ])

    correo = EmailField('Correo', [
        validators.DataRequired(message='El campo correo es requerido'),
        validators.Email(message='Pon un correo válido')  
    ])


class CinepolisForm(FlaskForm):
    nombre = StringField('Nombre', [
        validators.DataRequired(message="Campo requerido"),
        validators.Length(min=2, max=50, message="Nombre muy corto o muy largo")
    ])

    compradores = IntegerField('Cantidad Compradores', [
        validators.DataRequired(message="Camopo requerido"),
        validators.NumberRange(min=1, max=100, message="Compradores inválidos")
    ])

    tarjeta = RadioField(
        'Tarjeta Cinéco',
        choices=[('si', 'Sí'), ('no', 'No')],
        default='no',
        validators=[validators.DataRequired(message="Elige si o no")]
    )

    boletos = IntegerField('Cantidad de Boletos', [
        validators.DataRequired(message="Pon cantidad de boletos"),
        validators.NumberRange(min=1, max=999, message="Boletos inválidos")
    ])
