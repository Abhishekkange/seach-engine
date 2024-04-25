from flask import Flask
from controllers import indexing_controller,searching_controller

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True,port=7800)
