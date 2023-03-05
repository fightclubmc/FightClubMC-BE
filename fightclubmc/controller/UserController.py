from flasgger import swag_from
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin

from fightclubmc.service.UserService import UserService
from fightclubmc.utils.Utils import Utils


user: Blueprint = Blueprint('UserController', __name__, url_prefix=Utils.getURL('user'))


@user.route("/signin", methods=['POST'])
@cross_origin()
@swag_from('./docs/user/signin.yaml')
def signin():
    return UserService.signin(request.json)


@user.route("/session_check", methods=['GET'])
@cross_origin()
@jwt_required()
@swag_from('./docs/user/session_check.yaml')
def isExpired():
    return get_jwt_identity()


@user.route("/password_forgotten_token/<email>", methods=['PUT'])
@cross_origin()
@swag_from('./docs/user/create_password_forgotten_token.yaml')
def createPasswordForgottenToken(email):
    return UserService.createForgottenPasswordToken(email)


@user.route("/password_forgotten_token/<token>", methods=['GET'])
@cross_origin()
@swag_from('./docs/user/get_user_by_password_forgotten_token.yaml')
def getUserByPasswordForgottenToken(token):
    return UserService.getUserByPasswordForgottenToken(token)


@user.route("/change_password", methods=['PUT'])
@cross_origin()
@swag_from('./docs/user/change_password.yaml')
def changePassword():
    return UserService.changePassword(request.json)


@user.route("/get/<userId>", methods=['GET'])
@cross_origin()
@swag_from('./docs/user/get.yaml')
def get(userId):
    return UserService.getUser(userId)


@user.route("/signup", methods=['POST'])
@cross_origin()
@swag_from('./docs/user/signup.yaml')
def signup():
    return UserService.signup(request.json)




