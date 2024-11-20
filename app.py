from flask import Flask
from rutas.rutas_personajes import bp_personajes

app = Flask(__name__)

app.register_blueprint(bp_personajes)

if __name__ == "__main__":
    app.run(debug=True)
