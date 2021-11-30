#def app(environ, start_response):
#    status = '200 OK'
#
#    import sys
#    output = str.encode(str(sys.version_info) + '\n' + str(sys.path) + '\n' + str(sys.modules.keys()))
#    from flask import Flask
#
#    response_headers = [('Content-type', 'text/plain'),
#                        ('Content-Length', str(len(output)))]
#    start_response(status, response_headers)
#    return [output]


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    import sys
    output = '<h1>Hello, Flask! </h1>'
    output += str(sys.version_info) + '<br>' + str(sys.path) + '<br>' + str(sys.modules.keys())
    return output

