from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin

from fightclubmc.service.QuestionService import QuestionService
from fightclubmc.utils.Utils import Utils


question: Blueprint = Blueprint('QuestionController', __name__, url_prefix=Utils.getURL('question'))


@question.route("/get/<categoryId>/category", methods=['GET'])
@cross_origin()
@jwt_required()
def getQuestionsByCategory(categoryId):
    return QuestionService.getQuestionsByCategory(get_jwt_identity()['user_id'], categoryId)


@question.route('/get/<questionId>', methods=['GET'])
@cross_origin()
@jwt_required()
def get(questionId):
    return QuestionService.get(questionId)




