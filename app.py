from flasgger import Swagger
from flask_jwt_extended import JWTManager

from fightclubmc.configuration.config import app, sql
from fightclubmc.controller import UserController, ServerController

# controllers init
app.register_blueprint(ServerController.server)
app.register_blueprint(UserController.user)

# modules init
JWTManager(app)


def create_app():
    with app.app_context():
        sql.create_all()
    return app


if __name__ == '__main__':
    create_app().run()