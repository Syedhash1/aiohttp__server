from aiohttp import web

def setup(app):
    app.add_routes([web.get("/api/v1/yesterday", yesterday)])


def yesterday(request):
    yesterdays_date = "2020-20-08"
    return web.json_response({"yesterday": yesterdays_date})


if __name__ == "__main__":
    app = web.Application()
    setup(app)
    web.run_app(app, port=2224, host="0.0.0.0")

