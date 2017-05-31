
# -*- coding: utf-8 -*-

import web
from pyicloud import PyiCloudService

email = 'YOUR_APPLE_ID_EMAIL'
password = 'YOUR_APPLE_PASSWORD'

# Uncomment this section to find your device ID
#api = PyiCloudService(email, password)
#print api.devices

deviceid = 'YOUR_DEVICE_ID'

urls = (
  '/', 'Index'
)


app = web.application(urls, globals())

render = web.template.render('templates/')
	
class Index(object):
	def GET(self):
		form = web.input(q="")
		request = form.q
		api = PyiCloudService(email, password)
		if (request == "location"):
			location = api.devices[deviceid].location()
			response = str(location).replace("u'", "'")
		if (request == "ping"):
			response = api.devices[deviceid].play_sound()
		print response
		return render.index(response = response)
        
if __name__ == "__main__":
	app.run()
