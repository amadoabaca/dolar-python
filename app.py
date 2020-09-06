#importFlask
from flask import Flask, render_template
import dolar

#instancia de flask en app
app = Flask(__name__)

# generar ruta con @app.route
@app.route("/")

#la ruta responde con una funcion
def index():
    return render_template("index.html", pDolar = dolar.decimeDolar())

#validar que este en este modulo
if __name__ == "__main__":
    app.run(debug=True, port=3000)