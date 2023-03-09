from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin

from fightclubmc.service.CategoryService import CategoryService
from fightclubmc.service.MessageService import MessageService
from fightclubmc.service.NewsService import NewsService
from fightclubmc.service.QuestionService import QuestionService
from fightclubmc.utils.Utils import Utils


news: Blueprint = Blueprint('NewsController', __name__, url_prefix=Utils.getURL('news'))


@news.route("/get", methods=['GET'])
@cross_origin()
def get():
    return NewsService.getNews()


@news.route("/add", methods=['POST'])
@cross_origin()
def add():
    return NewsService.add(request.json)


