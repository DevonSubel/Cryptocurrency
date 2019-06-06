import web
import base64, datetime, hashlib, os

# token timeout, in minutes
TIMEOUT = 5		

render = web.template.render('templates/')
urls = ('/', 'index')

class index:
	def GET(self):
		return render.ledger("/static/blockchain1.jpg")
  
if __name__ == "__main__":
	print('SERVER BEGIN')
	app = web.application(urls, globals())
	app.run()   
