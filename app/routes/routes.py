import itty3

app = itty3.App()

from taskHandler.app.utils.template import template


@app.get("/")
def index(request):
    return app.render(request , "MIJN")

