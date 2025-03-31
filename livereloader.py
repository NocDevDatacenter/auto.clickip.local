from app import create_app
from livereload import Server
from flask_assets import Environment, Bundle


def register_assets():
    app = create_app()

    assets = Environment(app)
    scss = Bundle(
        "scss/styles.scss",
        filters="libsass",
        output="css/styles.css"
    )
    assets.register("scss_all", scss)

    if app.config.get("FLASK_ENV") == 'development':
        assets.auto_build = True
        assets.debug = True
        scss.build()


def web_reloader():
    app = create_app()
    app.debug = True

    register_assets()

    server = Server(app.wsgi_app)

    server.watch('app/templates/**/*.*', delay=0.5)
    server.watch('app/static/**/*.*', delay=0.5)
    server.watch('app/static/scss/**/*.scss', lambda: app.extensions['assets']['scss_all'].build())

    port = app.config.get('APLICATION_PORT', 5000)
    server.serve(port=port, restart_delay=1)


if __name__ == '__main__':
    web_reloader()
