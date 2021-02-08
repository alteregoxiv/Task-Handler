"""
App setup and firing wsgi server
"""

from app.setup import setup

setup()

from app.routes.routes import app
 
if __name__=="__main__":
    app.run(
        debug = True,
        static_url_path = '/static/',
        static_root = 'app/statics'
    )

