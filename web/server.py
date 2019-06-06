import web
from web import form
import base64, datetime, hashlib, os

# token timeout, in minutes
TIMEOUT = 5		

render = web.template.render('templates/')
urls = ('/', 'index',
        '/forgot', 'forgot',
        '/register', 'register',
        '/reset', 'reset')

class index:
	print('IGOR')
	myform = form.Form(
		form.Textbox("username",
			form.notnull,
			description="Username",
			id='usernameBox'),
		form.Password("password",
			form.notnull,
			description="Password",
			id='passwordBox'),
		form.Button("Login",
			id='loginButton')
			)

	def GET(self):
		form = self.myform()
		return render.login(form, "/static/blockchain1.jpg")
  

if __name__ == "__main__":
	print('BEGIN')
	app = web.application(urls, globals())
	app.run()   
