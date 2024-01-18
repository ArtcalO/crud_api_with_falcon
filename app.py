from wsgiref.simple_server import make_server
import falcon

class CRUD(object):

	def get():


if __name__=="main":
	api = falcon.API()
	
	api.add_route("/", CRUD())

	with make_server("",8080) as api:
		api.serve_forever()