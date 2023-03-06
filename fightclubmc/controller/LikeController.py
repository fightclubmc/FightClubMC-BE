from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin
from fightclubmc.service.CategoryService import CategoryService
from fightclubmc.service.LikeService import LikeService
from fightclubmc.service.MessageService import MessageService
from fightclubmc.service.QuestionService import QuestionService
from fightclubmc.utils.Utils import Utils


like: Blueprint = Blueprint('LikeController', __name__, url_prefix=Utils.getURL('like'))


@like.route("/add", methods=['POST'])
@cross_origin()
def add():
    return LikeService.add(request.json)


@like.route("/remove", methods=['DELETE'])
@cross_origin()
def remove():
    return LikeService.remove(request.args.get("user_id"), request.args.get("message_id"))


