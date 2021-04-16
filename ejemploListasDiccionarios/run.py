from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def holamundo():
    lista = ['Alvaro', 'Bernardo', 'Cecilia', 'Daniel']
    diccionario = {'nombre': 'marta', 'edad': 20, 'curso': 'Java'}
    mezclado = {'nombres': ['Alvaro', 'Bernardo', 'Cecilia', 'Daniel'], 'edades': [23, 45, 34, 23], 'cursos': ['Java', 'Python', 'PHP', 'CSS']}
    return render_template('index.html', lista=lista, diccionario=diccionario, mezclado=mezclado)

app.run(host="0.0.0.0", port=8080, debug=True)


