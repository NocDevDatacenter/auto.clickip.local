from app import create_app
from livereload import Server

app = create_app()


def web_reloader():
    app.debug = True  # debug mode is required for templates to be reloaded
    server = Server(app.wsgi_app)
    server.watch('app/templates/**/*.*')
    server.watch('app/static/**/*.*')
    server.serve(port=5000)
