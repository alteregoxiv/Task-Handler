"""
All routes of app is defined
"""

from taskHandler.app.utils.template import template
from taskHandler.app.controllers.signup_controller import email_pwd

import itty3

app = itty3.App()


@app.get("/")
def index(request):
    return app.render(request , template("index.html"))


@app.post("/verify-password")
def signup(request):
    if 'user' not in request.POST and 'email' not in request.POST:
        app.error_404(request)
    user = request.POST['user']
    email = request.POST['email']
    hash_pwd  = email_pwd(user , email)
    return app.render(request, 
                      template("info.html",
                                user = user,
                                email = email,
                                hash = hash_pwd
                              )
                     )


@app.get("/validate")
def validate(request):
    is_valid = "valid"
    return app.render_json(
        request,
        data = dict(valid=is_valid),
        content_type = "application/json"
    )
