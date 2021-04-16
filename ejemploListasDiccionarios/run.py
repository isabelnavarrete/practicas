from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def holamundo():
    lista = [23,45,34,45,23,5,23]
    diccionario = {'nombre': 'marta', 'edad': 20, 'curso': 'Java'}
    mezclado = {'nombres': ['Alvaro', 'Bernardo', 'Cecilia', 'Daniel'], 'edades': [23, 45, 34, 23], 'cursos': ['Java', 'Python', 'PHP', 'CSS']}
    mezcladoLD= [{'nombre':'marta', 'edad':24, 'curso':'Java'}, {'nombre':'fernando', 'edad':21, 'curso':'HTMl'}, {'nombre':'Victoria', 'edad':24, 'curso':'PHP'}, {'nombre':'Laura', 'edad':23, 'curso':'Java'}, {'nombre':'Jesus', 'edad':80, 'curso':'PHP'}]
    return render_template('index.html', lista=lista, diccionario=diccionario, mezclado=mezclado, mezcladoLD=mezcladoLD)


app.run(host="0.0.0.0", port=8080, debug=True)

