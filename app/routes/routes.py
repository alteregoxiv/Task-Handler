"""
All routes of app is defined
"""

from taskHandler.app.utils.template import template
from taskHandler.app.controllers.signup_controller import email_pwd , verify_pwd , adduser

import itty3

app = itty3.App()


@app.get("/")
def index(request):
    return app.render(request , template("index.html"))


@app.post("/verify-password")
def verifypass(request):
    if 'user' not in request.POST and 'email' not in request.POST:
        app.error_404(request)
    user = request.POST['user']
    email = request.POST['email']
    hash_pwd  = email_pwd(user , email)
    print(hash_pwd)
    return app.render(request, 
                      template("verify.html",
                                user = user,
                                email = email,
                                hash = hash_pwd
                              )
                     )


@app.post("/signup")
def signup(request):
    if 'user' not in request.POST and 'email' not in request.POST and 'hash' not in request.POST and 'pass' not in request.POST:
        app.error_404(request)
    user = request.POST['user']
    email = request.POST['email']
    hash_pwd = request.POST['hash']
    passwd = request.POST['password']
    print(hash_pwd)
    print(passwd)
    if not(verify_pwd(hash_pwd, passwd)):
        return app.redirect(request , "/")
    else:
        adduser(user , email , hash_pwd)
        return app.redirect(request , "/")
    


@app.get("/validate")
def validate(request):
    is_valid = "valid"
    return app.render_json(
        request,
        data = dict(valid=is_valid),
        content_type = "application/json"
    )
