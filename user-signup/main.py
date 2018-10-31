from flask import Flask, request, redirect, render_template
import cgi
import os
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route("/")
def display_signup_form():
	return render_template('signup.html')

def valid_un(un):
	if len(un) > 3:
		return True
	else:
		return False

def valid_pw_len(pw):
	if len(pw) > 7:
		return True
	else:
		return False

def have_num(pw):
    return any(i.isdigit() for i in pw)

def have_letter(pw):
    return any(i.isalpha() for i in pw)


	
@app.route("/", methods=['POST'])
def validate_form():
	un = request.form['user_name']
	pw = request.form['password']
	verify_pw = request.form['verify_password']

	un_error = ''
	pw_error = ''


	

	if not valid_un(un):
		un_error = 'User name must be at least 4 characters of more.'
	
	if not valid_pw_len(pw):
		pw_error = pw_error + 'Password must be 8 or more characters. '

	if not have_num(pw):
		pw_error = pw_error + 'Password must contain at least 1 number. '

	if not have_letter(pw):
		pw_error = pw_error + 'Password must contain at least on letter. '

	if pw != verify_pw:
		pw_error = pw_error + 'Passwords do not match. '

	
		
	if not un_error and pw_error == '':
		welcome_message = un
		return redirect('/welcome?welcome_message={0}'.format(welcome_message))

	else:
		return render_template('signup.html', user_name=un, user_name_error=un_error, password_error=pw_error)


@app.route("/welcome")
def valid_info():
	welcome_message = request.args.get('welcome_message')
	return '<h1>Welcome, {0}! To the world of tomorrow!</h1>'.format(welcome_message)

app.run()