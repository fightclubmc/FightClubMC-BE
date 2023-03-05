from flasgger import Swagger
from flask_jwt_extended import JWTManager

from fightclubmc.configuration.config import app, sql
from fightclubmc.controller import UserController
from fightclubmc.controller.docs.swagger import swagger_config, template

# controllers init
app.register_blueprint(UserController.user)

# modules init
Swagger(app, config=swagger_config, template=template)
JWTManager(app)


def create_app():
    with app.app_context():
        sql.create_all()
    return app


if __name__ == '__main__':
    create_app().run(host="127.0.0.1", port=1000)