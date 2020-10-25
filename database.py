#Import Databases
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#Imports Contactformulier
from flask_wtf import Form
from wtforms import TextField, IntegerField, StringField, SelectField, DateField, TextAreaField, SubmitField, BooleanField, validators
from wtforms.validators import Required, DataRequired, ValidationError

Base = declarative_base()

engine = create_engine('sqlite:///projecten.db')

class Project(Base):
   __tablename__ = 'Project'

   id = Column(Integer, primary_key=True, autoincrement=True)
   titel = Column(String(20), nullable=False)
   datum = Column(Integer, nullable=False)
   afbeeldingUrl = Column(String(50), nullable=False)
   beschrijving = Column(String(250))

class ContactForm(Form):
	firstName = TextField('First Name', [validators.DataRequired("Enter your first name")])
	lastName = TextField('Last Name', [validators.DataRequired("Enter your last name")])
	email = TextField('E-mail', [validators.DataRequired("Enter a valid email address"), validators.Email("Enter a valid email address")])
	subject = TextField('Subject', [validators.DataRequired("What's the nature of your message?")])
	message = TextAreaField('Message', [validators.DataRequired("Didn't you want to say something?")])
	submit = SubmitField('Send')

Base.metadata.create_all(engine)
