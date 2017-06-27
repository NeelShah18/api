import falcon
import json

#only for python 2

class Chinese(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        text = req.params['data']
        utf_text = unicode(text).encode('utf8')
        print(text)
        result = {
                'ans':utf_text
                }
        resp.body = json.dumps(result)

# falcon.API instances are callable WSGI apps
app = falcon.API()
# things will handle all requests to the '/things' URL path
app.add_route('/input', Chinese())
