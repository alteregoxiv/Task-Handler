"""
All routes of app is defined
"""

from taskHandler.app.utils.template import template

import itty3

app = itty3.App()


@app.get("/")
def index(request):
    return app.render(request , template("index.html"))


@app.post("/signup")
def signup(request):
    return app.render(request, template("info.html"))


@app.get("/validate")
def validate(request):
    is_valid = "valid"
    return app.render_json(
        request,
        data = dict(valid=is_valid),
        content_type = "application/json"
    )
