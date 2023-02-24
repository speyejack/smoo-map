from aiohttp import web
import asyncio
import json

request = "{\"API_JSON_REQUEST\":{\"Token\":\"SECRET_TOKEN_12345\",\"Type\":\"Status\"}}"
response = ""

async def index(request):
    return web.FileResponse("./index.html")

async def sand_map(request):
    return web.FileResponse("./SandWorldHomeStage.png")
    # return web.FileResponse("./sand.png")

async def send_reply(request):
    # print("Got request")
    return web.json_response(response)

async def run_update_info(app):
    app['get_info'] = asyncio.create_task(get_info())
    yield
    app['get_info'].cancel()
    await app['get_info']

def create_app():
    app = web.Application()

    app.cleanup_ctx.append(run_update_info)
    app.add_routes([web.get('/', index)])
    app.add_routes([web.get('/map', sand_map)])
    app.add_routes([web.get('/info.json', send_reply)])
    return app
    # web.run_app(app)


async def get_info():
    print("getting info")
    while True:
        reader, writer = await asyncio.open_connection(
            '127.0.0.1', 1030)
        writer.write(request.encode())
        await writer.drain()

        data = await reader.read(1000)
        data = data.decode('utf-8')
        if not data:
            continue
        data = json.loads(data)
        global response
        response = data
        # print(response)
        writer.close()
        await writer.wait_closed()
        await asyncio.sleep(0.1)



# with asyncio.runners() as runner:
#     runner.run(handle_reqs)
#     runner.run(get_info)
app = create_app()
web.run_app(app, port=33556)
