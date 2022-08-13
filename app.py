from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Avanti Palestra scoppia che la vittoria é nostra"

if __name__ == '__main__':
    app.run()