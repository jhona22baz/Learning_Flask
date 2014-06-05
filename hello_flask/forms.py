from flask_wtf import Form 
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField, SubmitField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email, InputRequired

class ContactForm(Form):
    name = TextField("Nombre", validators=[InputRequired('Please enter your name.')])
    #name = TextField("Nombre",["class ='col-sm-2'"] )
    email = TextField("Email", validators=[
           Required('Please provide a valid email address'),
           Length(min=6, message=(u'Email address too short')),
           Email(message=(u'That\'s not a valid email address.'))])
    subject = TextField("Subject",validators=[InputRequired('Por favor ingresa un asunto al correo')])
    message = TextAreaField("Message")
    submit = SubmitField("Send")