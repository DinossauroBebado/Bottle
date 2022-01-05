from bottle import jinja2_view, route, run, request, response


@route('/ <area>')
@jinja2_view('paginas\teste.html')
def teste(area):
    return dict(nome=area)


run(port=8080)
