from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    import sys
    output = '<h1>Hello, Flask! </h1>'
    output += str(sys.version_info) + '<br>' + str(sys.path) + '<br>' + str(sys.modules.keys()) + '<br>'

    for arg in request.args:
        output += str(arg) + '<br>'
    
    return output

