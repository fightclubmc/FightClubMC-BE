from flasgger import swag_from
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin

from fightclubmc.service.ServerService import ServerService
from fightclubmc.service.UserService import UserService
from fightclubmc.utils.Utils import Utils


server: Blueprint = Blueprint('ServerController', __name__, url_prefix=Utils.getURL('server'))


@server.route("/get", methods=['GET'])
@cross_origin()
def signin():
    return ServerService.get()