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
    hash_pwd  = email_pwd(email)
   
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
    
    if not(verify_pwd(hash_pwd, passwd)):
        return app.redirect(request , "/")
    else:
        adduser(user , email , hash_pwd)
        return app.redirect(request , "/")


@app.get("/forgot-password")
def forgotpwd(request):
    return app.render(request , template("forgotpwd.html"))


@app.get("/reset-password")
def resetpwd(request):
    user = request.GET['user']
    email = "prasad.biswasxiv@gmail.com"
    hash_pwd = email_pwd(email)

    return app.render_json(

                request,
                data = dict(),
                content_type = "application/json"

            )


@app.get("/validate")
def validate(request):
    is_valid = "valid"
    return app.render_json(
        request,
        data = dict(valid = is_valid),
        content_type = "application/json"
    )


@app.get("/resend-password")
def resend_pwd(request):
    if 'email' not in request.GET:
        return app.render_json(
            request,
            data = dict(),
            content_type = "application/json"
        )

    email = request.GET['email']
    hash_pwd = email_pwd(email)
    
    return app.render_json(
        request,
        data = dict(hash = hash_pwd),
        content_type = "application/json"
    )

@app.get("/tasks")
def tasks(request):
    return app.render(request , template("tasks.html"))
