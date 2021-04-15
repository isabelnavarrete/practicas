from flask import Flask, render_template
app = Flask(__name__)


"""listas"""
@app.route('/<string:slug>/')
def holamundo (slug):
    lista = ['Alvaro', 'Bernardo', 'Cecilia', 'Daniel']
    diccionario = {'nombre': 'marta', 'edad': 20, 'curso': 'Java'}
    mezclado = {'nombres': ['Alvaro', 'Bernardo', 'Cecilia', 'Daniel'], 'edades': [23, 45, 34, 23], 'cursos': ['Java', 'Python', 'PHP', 'CSS']}
    return render_template('index.html', lista=lista, diccionario=diccionario, mezclado=mezclado, slug=slug)


"""diccionario"""
""""@app.route('/view')
def diccionario ():
    diccionario = {'nombre': 'marta', 'edad': 20, 'curso': 'Java'}
    return render_template('post_view.html', diccionario=diccionario)"""
