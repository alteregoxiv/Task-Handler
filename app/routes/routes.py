from taskHandler.app.utils.template import template

import itty3

app = itty3.App()

@app.get("/")
def index(request):
    return app.render(request , "MIJN")

