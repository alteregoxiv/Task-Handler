from sys import path
path.append

from app.utils.template import template

import itty3

app = itty3.App()

@app.get("/")
def index(request):
    return app.render(request , "MIJN")

if __name__=="__main__":
    app.run(
            debug=True)

