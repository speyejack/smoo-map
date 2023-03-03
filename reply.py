from aiohttp import web
import asyncio
import json
import sys

request = "{\"API_JSON_REQUEST\":{\"Token\":\"SECRET_TOKEN_12345\",\"Type\":\"Status\"}}"
response = ""

if len(sys.argv) < 2:
    print("Missing parameters")
    print("Usage: reply.py {server_ip} (server_port) (local_serve_port)")

server_ip = sys.argv[1]
server_port = 1030
local_serve_port = 33556

if len(sys.argv) >= 3:
    server_port = int(sys.argv[2])

if len(sys.argv) >= 4:
    local_serve_port = int(sys.argv[3])

async def index(request):
    return web.FileResponse("./index.html")

async def get_map(request):
    stage = None
    # print("Attempting map get")
    for player in response['Players']:
        if "Home" in player['Stage']:
            stage = player['Stage']


    if not stage:
        print("Map request when no appropriate player location could be found. Defaulting to Mushroom Kingdom.")
        stage = "PeachWorldHomeStage"

    filename = "./maps/" + stage + ".png"
    # print(f"Getting file {filename}")
    return web.FileResponse(filename)

async def get_view_matrix(request):
    return web.json_response({
        "SandWorldHomeStage": [[ 9.94226977e-05,  2.42626562e-02,  1.30726135e+03],
                               [ 2.44168997e-02, -5.98239291e-05,  1.06235817e+03],
                               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "PeachWorldHomeStage": [[-3.42906143e-02,  8.95028507e-05,  9.44332098e+02],
                                [ 3.37708646e-05,  3.42327570e-02,  1.09828936e+03],
                                [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "CapWorldHomeStage" : [[-2.29886940e-02,  2.29009424e-02,  8.23556189e+02],
                               [ 2.27482304e-02,  2.31328824e-02,  7.73800352e+02],
                               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "WaterfallWorldHomeStage": [[-3.38215720e-02,  3.42714219e-02,  9.53179055e+02],
                                    [ 3.40258988e-02,  3.43686595e-02,  9.48856710e+02],
                                    [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "LakeWorldHomeStage" : [[-6.68966292e-02, -3.39799288e-04,  4.63485895e+02],
                                [ 3.96529413e-05,  6.67899784e-02,  1.00668366e+03],
                                [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "ForestWorldHomeStage" : [[-3.74726789e-02, -7.37209801e-06,  9.77907726e+02],
                                  [-2.25564147e-04,  3.73025810e-02,  1.28494918e+03],
                                  [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "CloudWorldHomeStage": [[-6.31062690e-02, -6.58900201e-05,  1.02252890e+03],
                                [-1.28315883e-03,  6.26014521e-02,  1.14842984e+03],
                                [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "ClashWorldHomeStage": [[-6.06231653e-02, -1.04772227e-04,  1.09430610e+03],
                                [ 4.86723430e-04,  6.02856120e-02,  8.03473059e+02],
                                [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "CityWorldHomeStage": [[-4.47079319e-02,  2.73429137e-05,  1.02487125e+03],
                               [-3.25686013e-05,  4.46198531e-02,  8.88866317e+02],
                               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "SnowWorldHomeStage": [[-5.82491062e-02,  5.98959366e-05,  1.07669332e+03],
                               [ 2.35527251e-05,  5.80195573e-02,  8.37841922e+02],
                               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "SeaWorldHomeStage": [[-3.40443049e-02,  1.89689671e-04,  1.02915924e+03],
                              [ 3.71263983e-05,  3.41050834e-02,  1.64954665e+03],
                              [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "LavaWorldHomeStage": [[ 6.35325390e-05,  3.54400088e-02,  1.12216141e+03],
                               [ 3.46685553e-02, -6.38950757e-04,  1.01999375e+03],
                               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "BossRaidWorldHomeStage": [[-3.15764534e-02,  2.80949845e-04,  1.23777163e+03],
                                   [-2.99710854e-04,  3.08114401e-02,  3.35373875e+02],
                                   [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "SkyWorldHomeStage": [[-1.29601393e-02, -1.09502459e-04,  9.12553404e+02],
                              [-3.27542923e-06,  1.28180272e-02,  1.24845544e+03],
                              [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "MoonWorldHomeStage": [[-2.19710964e-02, -7.74056331e-05,  9.67069307e+02],
                               [-2.32316366e-05,  2.18941589e-02,  1.02173222e+03],
                               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "Special1WorldHomeStage": [[-3.41307548e-02, -1.16788590e-05,  8.10260704e+02],
                                   [ 2.01918596e-04,  3.41116814e-02,  1.03053478e+03],
                                   [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
        "Special2WorldHomeStage": [[-2.58975695e-02, -4.78757602e-05,  1.13413227e+03],
                                   [ 1.47396353e-04,  2.60619214e-02,  1.73145572e+03],
                                   [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]]
    })

async def send_reply(request):
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
    app.add_routes([web.get('/view', get_view_matrix)])
    app.add_routes([web.get('/index.html', index)])
    app.add_routes([web.get('/map', get_map)])
    app.add_routes([web.get('/info.json', send_reply)])
    return app
    # web.run_app(app)


async def get_info():
    while True:
        reader, writer = await asyncio.open_connection(
            server_ip, server_port)
        writer.write(request.encode())
        await writer.drain()

        tot_data = bytearray()
        data = ""
        while True:
            data = await reader.read(1000)
            tot_data += data
            data = data.decode('utf-8')

            try:
                out_json = json.loads(tot_data)
                data = out_json
                break
            except json.decoder.JSONDecodeError:
                pass
        if not data:
            continue
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
web.run_app(app, port=local_serve_port)
