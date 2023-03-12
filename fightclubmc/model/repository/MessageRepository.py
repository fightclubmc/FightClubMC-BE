from sqlalchemy import text, asc, desc

from fightclubmc.configuration.config import sql
from fightclubmc.model.entity.Like import Like
from fightclubmc.model.entity.Message import Message
from fightclubmc.model.entity.Question import Question


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the message repository
#

class MessageRepository():

    @classmethod
    def getMessages(cls, questionId):
        messages: list[Message] = sql.session.query(Message).filter(Message.question_id == questionId).all()
        return messages

    @classmethod
    def get(cls, messageId):
        message: Message = sql.session.query(Message).filter(Message.message_id == messageId).first()
        return message

    @classmethod
    def getAllMessages(cls):
        messages: list[Message] = sql.session.query(Message).all()
        return messages

    @classmethod
    def getMessagesByCategory(cls, categoryId):
        messages: list[Message] = sql.session.query(Message).from_statement(
            text(
                "SELECT messages.* FROM messages "
                "JOIN questions "
                "ON questions.question_id = messages.question_id "
                "WHERE questions.category_id = :categoryId"
            )
        ).params(categoryId=categoryId).all()
        return messages

    @classmethod
    def add(cls, questionId, ownerId, body):
        message: Message = Message(questionId, ownerId, body)
        sql.session.add(message)
        sql.session.commit()

    @classmethod
    def addLike(cls, messageId):
        like: Like = cls.get(messageId)
        like.likes += 1
        sql.session.commit()

    @classmethod
    def removeLike(cls, messageId):
        like: Like = cls.get(messageId)
        like.likes -= 1
        sql.session.commit()