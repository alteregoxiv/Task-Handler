"""
All routes of app is defined
"""

from taskHandler.app.utils.template import template
from taskHandler.app.controllers.signup_controller import (
    email_pwd,
    verify_pwd,
)
from taskHandler.app.controllers.user_controller import (
    adduser,
)

import itty3

app = itty3.App()

############# Custom 404 Error Handler ##################
def my_error_404(request):
    return app.render(
                      request,
                      template('error404.html'),
                      status_code=404
            )

app.error_404 = my_error_404
#########################################################

############# View Serving Routes ######################

@app.get("/")
def index(request):
    args = dict()
    args['signup'] = request.GET.get('signup', 'unknown')
    args['verification'] = request.GET.get('verification', 'unknown')
    args['user'] = request.GET.get('user', 'valid')
    return app.render(request,
                      template("index.html", **args)
                     )


@app.post("/verify-password")
def verifypass(request):
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
    user = request.POST['user']
    email = request.POST['email']
    hash_pwd = request.POST['hash']
    passwd = request.POST['password']
    
    if not verify_pwd(hash_pwd, passwd):
        return app.redirect(request , "/?signup=failed")
    else:
        adduser(user , email , hash_pwd)
        return app.redirect(request, "/tasks")


@app.get("/forgot-password")
def forgotpwd(request):
    return app.render(request , template("forgotpwd.html"))


@app.post("/change-password")
def changepwd(request):
    user = request.POST['user']
    hash_pwd = request.POST['hash']
    pwd = request.POST['password']
    newpwd = request.POST['newpassword']
    
    return app.redirect(request , "/")


@app.get("/tasks")
def tasks(request):
    return app.render(request , template("tasks.html"))


#########################################################

############## JSON Serving Routes ######################

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
    email = request.GET['email']
    hash_pwd = email_pwd(email)
    
    return app.render_json(
        request,
        data = dict(hash = hash_pwd),
        content_type = "application/json"
    )


@app.get("/reset-password")
def resetpwd(request):
    user = request.GET['user']
    email = "prasad.biswasxiv@gmail.com"
    hash_pwd = email_pwd(email)

    return app.render_json(
                request,
                data = dict(hash = hash_pwd),
                content_type = "application/json"
    )
