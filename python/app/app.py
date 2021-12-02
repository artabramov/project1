from flask import Flask, request
from tasks import post_request, get_response

app = Flask(__name__)
app.debug = True

@app.route('/post/<string:value>')
def post_task(value):
    task = post_request.delay(value)
    output = 'id: ' + str(task.id)
    return output

@app.route('/get/<string:id>')
def get_task(id):
    output = str(get_response(id))
    return output

@app.route('/')
def hello():
    import sys
    output = '<h1>Hello, Flask!</h1>'
    output += 'APP: ' + str(sys.version_info) + '<br>' + str(sys.path) + '<br>' + str(sys.modules.keys()) + '<br>'
    output += 'REQUEST: ' + str(request.args) + '<br>'
    return output

