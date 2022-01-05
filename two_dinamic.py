
"""
Intro sobre rotas dinamicas com resposta no microframework bottle

"""
from bottle import run, route, request


@route('/', method="GET")
def index():

    return """
        <form  action = "/" method = "post" >
        Username : <input name = "username" type = "text" />
        Password : <input name = "password" type = "text" />
        <input value = "Login" type = "submit"/>
        </form>"""


@route('/', method="POST")
def index():
    username = request.forms.get("username")
    password = request.forms.get("password")

    print(username, password)

    return f"""
    <h1> Info </h1>
    </br>
    <h4> Nome : {username} </h4>
    </br>
    <h4> Senha : {password} </h4>  
    """


run(port=8080)
