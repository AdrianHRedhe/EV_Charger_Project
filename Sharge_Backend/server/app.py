from server import app
from server.routes import routes_blueprint

app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run()