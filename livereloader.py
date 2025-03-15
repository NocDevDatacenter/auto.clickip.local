from app import create_app
from livereload import Server
from flask_assets import Environment, Bundle

app = create_app()


def register_assets(app):
    assets = Environment(app)

    scss = Bundle(
        "scss/styles.scss",
        filters="libsass",
        output="css/styles.css"
    )

    assets.register("scss_all", scss)
    assets.auto_build = True
    assets.debug = True

    scss.build()


def web_reloader():
    app.debug = True

    register_assets(app)

    server = Server(app.wsgi_app)
    server.watch('app/templates/**/*.*')
    server.watch('app/static/**/*.*')
    server.serve(port=5000)
