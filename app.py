from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.config["SECRET_KEY"] = "algo"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/animales")
def animales():
    return render_template("animales.html")

@app.route("/vehiculos")
def vehiculos():
    return render_template("vehiculos.html")

@app.route("/maravillas")
def maravillas():
    return render_template("maravillas.html")

@app.route("/acercade")
def about():
    return render_template("acercade.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/registrame", methods=("GET", "POST"))
def registrame():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]
        contrasena = request.form["password"]

if __name__ == "__main__":
    app.run(debug=True)
