from flask import Flask
from datetime

# define a variable to hold you app
app = Flask(app)

# define your resource endpoints
app.route('/')
def index_page():
    return "Hello world"

app.route('/time', methods=['GET'])
def get_time():
    return str(datetime.datetime.now())


if __name__ == '__main__':
    app.run()