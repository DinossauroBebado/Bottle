"""
Intro sobre rotas no microframework bottle

"""


from bottle import run, route


@route('/')
def index():
    "Rota estatica "

    return "<h1> ola dino </h1>"


@route('/teste')
def index():
    "Outra rota estatica "

    return "<h1> ola teste </h1>"


@route('/<person>')
def index(person):
    "Rota dinamica "

    return f"<h1> ola {person} </h1>"


run(port=8080)
