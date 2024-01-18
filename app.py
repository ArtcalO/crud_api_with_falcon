from wsgiref.simple_server import make_server
import falcon

class CRUD:

	def on_get(self,req, resp):
		response.status = falcon.HTTP_200
		resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
		resp.text = (
			'\nTwo things awe me most, the starry sky '
			'above me and the moral law within me.\n'
			'\n'
			'	~ Immanuel Kant\n\n'
		)

api = falcon.App()
crud = CRUD()
api.add_route("/", crud)

if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()