from flask import Flask, render_template

server = Flask(__name__)

messages = [
{'username':'stepa','text':'Привет'},
{'username':'stepan','text':'Пока'},
{'username':'stepik','text':'Привет и пока'}
]

@server.route('/')
def hello():
    return '''Hello, World!
    <br>
    <a target="_blank" href=/index>Index</a>'''

@server.route('/get_messages')

def get_messages():
    return{
    'messages': messages
}

@server.route('/index')
def index():
    name = 'Stepa'
    return render_template("index.html")


@server.route('/day-<num>')
def day(num):
    return render_template(f"day-{num}.html")


server.run()