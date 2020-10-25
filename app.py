from flask import Flask, render_template, request, session, current_app, jsonify, redirect, url_for
from flask_wtf import Form
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Project
# from database import ....
import os
from flask_mail import Mail, Message
from forms import ContactForm
from wtforms import TextField, IntegerField, StringField, SelectField, DateField, TextAreaField, SubmitField, BooleanField, validators
from wtforms.validators import Required, DataRequired, ValidationError

engine = create_engine('sqlite:///projecten.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__, static_url_path='/static')
app.config["DEBUG"] = True

app.config['SECRET_KEY'] = 'any secret string'

app.config.update(
    DEBUG=True,
    #EMAIL SETTINGS
    MAIL_SERVER = '',
    MAIL_PORT = 587,
    MAIL_USE_SSL = False,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = '',
    MAIL_PASSWORD = ''
    )

mail=Mail(app)

@app.route('/')
def home():
    return render_template('landingspagina.html')

@app.route('/About')
def portfolio():
    return render_template('about.html')

@app.route('/CV')
def CVpagina():
    return render_template('cv.html')

#@app.route('/Contact')
#def contact():
#    return render_template('contact.html')

@app.route('/productoverzicht')
def productoverzicht():
    projecten = session.query(Project).all()
    return render_template('productoverzicht.html', projecten = projecten)

@app.route('/portoverzicht')
def portoverzicht():
    return render_template('portoverzicht.html')

@app.route('/fashoverzicht')
def fashoverzicht():
    return render_template('fashoverzicht.html')

@app.route('/nieuwproject')
def nieuwProject():
    return render_template('nieuwProject.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Onjuiste inloggegevens, probeer opnieuw'
        else:
            return redirect(url_for('projecten'))
    return render_template('login.html', error=error)

@app.route('/projecten')
def projecten():
    projecten = session.query(Project).all()
    print(projecten)
    return render_template('projecten.html', projecten = projecten)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        print('email:' + request.form['email'])
        if form.validate() == False:
            flash('You must enter something into all of the fields')
            return render_template('contact.html', form = form)
        else:
            msg = Message(form.subject.data, sender='[SENDER EMAIL]', recipients=['[RECIPIENT EMAIL]'])
            msg.body = """
            From: %s %s <%s>
            %s
            """ % (form.firstName.data, form.lastName.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html',
            title = 'Contact Us',
            form = form)

@app.route('/createProject/', methods = ['POST'])
def createProject():
  if request.method == 'POST':
      nieuwProject = Project(titel = request.form['titel'], datum = request.form['datum'], afbeeldingUrl = request.form['afbeeldingUrl'])
      session.add(nieuwProject)
      session.commit()
      return redirect(url_for('projecten'))

@app.route('/projecten/<int:poject_id>/edit/', methods = ['GET','POST'])
def editProject():
    editedProject = session.query(Project).filter_by(id=project_id).one()
    if request.method == 'POST':
        if request.form['titel']:
           editedProject.title = request.form['titel']
           return redirect(url_for('projecten', project_id=project_id))
        else:
           return render_template('editProject.html', project = editedProject, project_id = project_id)

@app.route('/projecten/<int:poject_id>/delete/', methods = ['GET','POST'])
def deleteProject(project_id):
   projectToDelete = session.query(Project).filter_by(id=project_id).one()
   if request.method == 'POST':
       session.delete(projectToDelete)
       session.commit()
       return redirect(url_for('projecten', project_id=project_id))
   else:
       return render_template('deleteProject.html',project = projectToDelete)

if __name__ == '__main__':
    app.run(debug=True)