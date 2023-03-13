from flask_jwt_extended import JWTManager

from fightclubmc.configuration.config import app, sql
from fightclubmc.controller import UserController, ServerController, CategoryController, QuestionController, \
    MessageController, LikeController, NewsController
from fightclubmc.service.QuestionService import QuestionService

# controllers init
app.register_blueprint(MessageController.message)
app.register_blueprint(CategoryController.category)
app.register_blueprint(QuestionController.question)
app.register_blueprint(ServerController.server)
app.register_blueprint(LikeController.like)
app.register_blueprint(UserController.user)
app.register_blueprint(NewsController.news)

# modules init
JWTManager(app)


def create_app():
    with app.app_context():
        sql.create_all()
    return app


if __name__ == '__main__':
    create_app().run()