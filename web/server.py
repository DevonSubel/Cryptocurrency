import web
import base64, datetime, hashlib, os
import sys
sys.path.append("../")
import blockChain
from driver import *
import threading

# token timeout, in minutes
TIMEOUT = 5		

render = web.template.render('templates/')
urls = ('/', 'index')

driver = Driver("../sampleInput.json", 3)
driver.run()

class index(object):
	def GET(self):
		global driver
		while True:
			threading.Timer(5.0, driver.getBCImg()).start()
			return render.ledger("/static/blockchain1.jpg")
  
if __name__ == "__main__":
	print('SERVER BEGIN')
	
	app = web.application(urls, globals())
	app.run()   
