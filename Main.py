from flask import Flask
from Class import app as class_app
from Dependence import app as deps_app
from Month import app as month_app
from Week import app as week_app

app = Flask(__name__)

# Registro de las rutas para cada uno de los servicios
app.register_blueprint(class_app, url_prefix='/Class')
app.register_blueprint(deps_app, url_prefix='/Dependence')
app.register_blueprint(month_app, url_prefix='/Month')
app.register_blueprint(week_app, url_prefix='/Week')

if __name__ == '__main__':
    app.run(debug=True, port=8786)
