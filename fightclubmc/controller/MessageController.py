from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin

from fightclubmc.service.MessageService import MessageService
from fightclubmc.service.QuestionService import QuestionService
from fightclubmc.utils.Utils import Utils


message: Blueprint = Blueprint('MessageController', __name__, url_prefix=Utils.getURL('message'))


@message.route("/get/question/<questionId>", methods=['GET'])
@cross_origin()
@jwt_required()
def get(questionId):
    return MessageService.getMessages(questionId)


