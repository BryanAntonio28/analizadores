from flask import Flask, render_template, request
from ply import lex

app = Flask(__name__)

def procesarCadena(entrada):
    # Implementa tu lógica para procesar la cadena de entrada
    # Para fines de demostración, asumamos que el procesamiento convierte la cadena a mayúsculas
    cadenaProcesada = entrada.upper()
    return cadenaProcesada

def checkSintaxisCorrect(entrada):
    if entrada != "":
        return True
    return "Error de sintaxis"

tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION'
)

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f'Caracter erroneo: {t.value[0]}')
    t.lexer.skip(1)

analizadorLexico = lex.lex()

def analizarLexico():
    codigoFuente = "2 + 1"
    analizadorLexico.input(codigoFuente)

    for token in analizadorLexico:
        print(token)

@app.route("/", methods=["GET", "POST"])
def homepage():
    cadenaProcesada = None
    analizarLexico()

    if request.method == "POST":
        entrada = request.form.get("entrada")
        cadenaProcesada = procesarCadena(entrada)

    return render_template("index.html", title="Lenguajes y Automatas II", cadenaProcesada=cadenaProcesada)

@app.route("/analisis_sintactico.html")
def analisisSintactico():
    return render_template("analisis_sintactico.html")

@app.route("/analisis_lexico.html")
def analisisLexico():
    return render_template("analisis_lexico.html")

if __name__ == "__main__":  # Corrección: Cambiar _name a __name__
    app.run(debug=True)