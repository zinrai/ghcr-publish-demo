import falcon
import json

class HelloWorldResource:
    def on_get(self, req, resp):
        data = {'message': 'Hello, World!'}

        resp.body = json.dumps(data, ensure_ascii=False)
        resp.status = falcon.HTTP_200

app = falcon.App()

hello_world_resource = HelloWorldResource()
app.add_route('/hello', hello_world_resource)

if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    print('Server started on http://127.0.0.1:8000')
    httpd.serve_forever()
