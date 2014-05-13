from bottle import get, run


@get('/')
def hello(request, response):
    return "Hello friend"

run(port=8080)