from flask import Flask
from pymemcache.client.base import Client

from time import gmtime, strftime
from utils import *

app = Flask (__name__)

client = Client(('localhost', 11211), serde=JsonSerde())

@app.route('/')
def hello_world():
	return '{}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

@app.route('/<n>')
def fibo(n):
	if client.get(n) is None:
		print(n)
		result = fib(int(n))
		print(type(result))
		client.set(str(n),str(result))
		return 'Твоё число Фибоначе {}! Оно только что посчитано'.format(result)

	else:
		result = client.get(str(n))
		return 'Твоё число Фибоначе {}! Оно взято из кэша'.format(result)



if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8080)
