import asyncio
from aiohttp import web
from functools import partial

@asyncio.coroutine
def handle(repo, request):
	pass

@asyncio.coroutine
def info(repo, request):
	pass


@asyncio.coroutine
def init(loop, repos, port):
	app = web.Application(loop = loop)
	for repo in repos:
		app.router.add_route('POST', repo._hook, partial(handle, repo))
		app.router.add_route('GET', repo._hook, partial(info, repo))
	srv = yield from loop.create_server(app.make_handler(),
                                        '0.0.0.0', port)
	print("Server started at: {}:{}".format('0.0.0.0', port))
	return srv


def serve(config):
	
	loop = asyncio.get_event_loop()
	loop.run_until_complete(init(loop, config._repos, config._port))
	try:
		loop.run_forever()
	except KeyboardInterrupt:
		pass