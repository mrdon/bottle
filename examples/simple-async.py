from asyncio import coroutine, sleep
from bottle import get, run


@get('/')
@coroutine
def hello(request, response):
    yield from sleep(1)
    return "Hello friend"

run(port=8080)