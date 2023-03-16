from flask import jsonify

from fightclubmc.model.entity.Message import Message
from fightclubmc.model.repository.MessageRepository import MessageRepository
from fightclubmc.model.repository.LikeRepository import LikeRepository
from fightclubmc.service.LikeService import LikeService
from fightclubmc.service.UserService import UserService
from fightclubmc.utils.Constants import Constants
from fightclubmc.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 05/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the server service
#

class MessageService():

    @classmethod
    def getAllMessages(cls):
        messages: list[Message] = MessageRepository.getAllMessages()
        return Utils.createList(messages)

    @classmethod
    def getMessages(cls, userId, questionId):
        messages: list[Message] = MessageRepository.getMessages(questionId)
        result: list[dict] = []
        for message in messages:
            owner: dict = UserService.getUser(message.owner_id)
            result.append(message.toJson_Owner(
                owner,
                likeable=LikeService.get(userId, message.message_id) is None,
                removable=userId == message.owner_id or UserService.getUser(userId)['admin'])
            )
        return jsonify(result)

    @classmethod
    def getMessagesByCategory(cls, categoryId):
        messages: list[Message] = MessageRepository.getMessagesByCategory(categoryId)
        return Utils.createList(messages)

    @classmethod
    def add(cls, request):
        try:
            MessageRepository.add(request['question_id'], request['owner_id'], request['body'])
            UserService.addMessage(request['owner_id'])
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400
        
    @classmethod
    def removeMessage(cls, user, messageId):
        message: Message = MessageRepository.get(messageId)
        if user['admin'] or message.owner_id == user['user_id']:
            MessageRepository.removeMessage(messageId)
            LikeRepository.removeLikes(messageId)
            UserService.removeMessage(message.owner_id)
            return Utils.createSuccessResponse(False, Constants.CREATED), 200
        else:
            return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 403), 403
