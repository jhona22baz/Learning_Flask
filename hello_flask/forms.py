from flask_wtf import Form 
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField, SubmitField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email, InputRequired

class ContactForm(Form):
    name = TextField("Nombre", validators=[InputRequired('Please enter your name.')])
    
    email = TextField("Email", validators=[
           Required('Please provide a valid email address'),
           Length(min=6, message=(u'Email address too short')),
           Email(message=(u'That\'s not a valid email address.'))])
    subject = TextField("Subject",validators=[InputRequired('Please provide a subject')])
    message = TextAreaField("Message",validators = [InputRequired('I need to know your message')])
    submit = SubmitField("Send")