from flask_cors import CORS
from flask import Flask
from Class import app as class_app
from Dependence import app as deps_app
from Month import app as month_app
import configparser
from Week import app as week_app

config = configparser.ConfigParser()
config.read('config.ini')

origins = config.get('CORS', 'origins')

app = Flask(__name__)

CORS(app, origins=origins)

# Registro de las rutas para cada uno de los servicios
app.register_blueprint(class_app, url_prefix='/Class')
app.register_blueprint(deps_app, url_prefix='/Dependence')
app.register_blueprint(month_app, url_prefix='/Month')
app.register_blueprint(week_app, url_prefix='/Week')

if __name__ == '__main__':
    app.run(debug=True, port=8786)
