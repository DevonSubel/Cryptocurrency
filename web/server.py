import web
from web import form
import MT19937
import base64, datetime, hashlib, os

# token timeout, in minutes
TIMEOUT = 5		

render = web.template.render('templates/')
urls = ('/', 'index',
        '/forgot', 'forgot',
        '/register', 'register',
        '/reset', 'reset')

#Faking a user database.
user_dic = {"admin":"119ba0f0a97158cd4c92f9ee6cf2f29e75f5e05a"}
token_dic = {}

#Seed my super-secure PRNG using the OS
seed = int(os.urandom(4).encode("hex"), 16)
MT = MT19937.MT19937(seed)

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
   
	def POST(self):
		form = self.myform()

		if not form.validates():
			return render.login(form,"")

		user = form.d.username
		pw = hashlib.sha1(form.d.password).hexdigest()

		if user == "admin" and user_dic["admin"] == pw:
			return render.loggedin(user, True)
		elif user in user_dic and user_dic[user] == pw:
			return render.loggedin(user, False)
		else:
			return render.login(form,"Username/Password Incorrect")

class forgot:
	myform = form.Form(
		form.Textbox("user",
			form.notnull,
			description = "Username",
			id='forgotUser'),
		form.Button("Reset",
			description="Send"),
			id='forgotButton')

	nullform = form.Form()

	def GET(self):
		form = self.myform()
		return render.generic(form, "Enter your username to reset your password. A password reset token will be mailed to you.","")

	def POST(self):
		form = self.myform()
		msg = "Enter your username to reset your password. A password reset token will be mailed to you."
		err = ""

		if not form.validates():
			err = "Invalid form data"
			return render.generic(form, msg, err)

		user = form.d.user
         
		if user in user_dic:
			token = generate_token()
			time = datetime.datetime.now() + datetime.timedelta(minutes=TIMEOUT)
			token_dic[token] = reset_token(user, time)

			if user == "admin":
				msg = "Admin emailed reset token."
			else:
				#TODO: Email server not work, so I'll just post them to the screen for now.
				msg = web.ctx.env.get('HTTP_HOST') + "/reset?token=" + token
				return render.generic(form, msg, err)
		else:
			err = "User not found."

		return render.generic(form, msg, err)

class register:
	myform = form.Form(
		form.Textbox("user",
			form.notnull,
			description = "Username"),
		form.Password("password",
			form.notnull,
			description = "Password"),
		form.Button("Register",
			description="Register"))
			
	nullform = form.Form()
   
	def GET(self):
		form = self.myform()
		return render.generic(form, "Enter a username and password.", "")

	def POST(self):
		form = self.myform()
		msg = "ARJUN REDDY"
		err = ""

		if not form.validates():
			err = "Invalid fields."
		else:
			if form.d.user in user_dic:
				err = "User already registered."
			else:
				user_dic[form.d.user] = hashlib.sha1(form.d.password).hexdigest();
				msg = "User registered."
		return render.generic(self.nullform(), msg, err)

class reset:
	myform = form.Form(
		form.Password("password",
			form.notnull,
			description = "New Password"),
		form.Hidden("token", 
			form.notnull,
			value="", 
			description="Reset Token"),
		form.Button("Reset Password",
			description="Register"))

	nullform = form.Form()

	def GET(self):
		user_data = web.input(token="")
		token = user_data.token

		myform = form.Form(
			form.Password("password",
				form.notnull,
				description = "New Password"),
			form.Hidden("token", 
				form.notnull, 
				value=token, 
				description="Reset Token"),
			form.Button("Reset Password",
			description="Register"))
		msg = "OLA OLAA"
		err = ""

		if token not in token_dic:
			err = "Invalid token."
			return render.generic(self.nullform(), msg, err)

		if token_dic[token].timeout <= datetime.datetime.now():
			err = "Token expired."
			return render.generic(self.nullform(), msg, err)

		msg = "Reset Password for: " + token_dic[token].user
		return render.generic(myform, msg, err)

	def POST(self):
		form = self.myform()
		msg = "TO MAKE U FALL IN LOVE"
		err = ""

		if not form.validates():
			err = "Invalid form data."
			return render.generic(self.nullform, msg, err)

		#Make sure it's a valid token, and remove it once used
		if form.d.token in token_dic and token_dic[form.d.token].timeout > datetime.datetime.now():
			msg = "Password reset for user: " + token_dic[form.d.token].user
			user = token_dic[form.d.token].user
			user_dic[user] = hashlib.sha1(form.d.password).hexdigest();
			del token_dic[form.d.token]
		else:
			err = "Invalid token."

		return render.generic(self.nullform, msg, err)
   
class reset_token:
	def __init__(self, user, timeout):
		self.user = user
		self.timeout = timeout

def generate_token():
	
	#Generate a 256-bit random number as our reset tokwn
	#by concatentating 8, 32-bit integers with colons
	token = str(MT.extract_number())
	for i in range(7):
		token += ":" + str(MT.extract_number())
	return base64.b64encode(token)


if __name__ == "__main__":
	print('BEGIN')
	app = web.application(urls, globals())
	app.run()   
