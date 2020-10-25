from app import app
import os
from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm
from flask_mail import Mail, Message

mail=Mail(app)

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

# Contact function to control error handling and submission

def contact2():
	form = ContactForm()
	if request.method == 'POST':
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