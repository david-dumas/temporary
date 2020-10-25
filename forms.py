from flask_wtf import Form
from wtforms import TextField, IntegerField, StringField, SelectField, DateField, TextAreaField, SubmitField, BooleanField, validators
from wtforms.validators import Required, DataRequired, ValidationError

# Form models

class ContactForm(Form):
	firstName = TextField('First Name', [validators.DataRequired("Enter your first name")])
	lastName = TextField('Last Name', [validators.DataRequired("Enter your last name")])
	email = TextField('E-mail', [validators.DataRequired("Enter a valid email address"), validators.Email("Enter a valid email address")])
	subject = TextField('Subject', [validators.DataRequired("What's the nature of your message?")])
	message = TextAreaField('Message', [validators.DataRequired("Didn't you want to say something?")])
	submit = SubmitField('Send')