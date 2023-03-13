from fightclubmc.configuration.config import sql
from fightclubmc.model.entity.Category import Category
from fightclubmc.model.entity.Like import Like
from fightclubmc.model.entity.Question import Question


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the like service
#

class LikeRepository():

    @classmethod
    def add(cls, userId, messageId):
        like: Like = Like(messageId, userId)
        sql.session.add(like)
        sql.session.commit()

    @classmethod
    def get(cls, userId, messageId):
        like: Like = sql.session.query(Like).filter(Like.user_id == userId).filter(Like.message_id == messageId).first()
        return like

    @classmethod
    def remove(cls, userId, messageId):
        like: Like = cls.get(userId, messageId)
        sql.session.delete(like)
        sql.session.commit()
        
    @classmethod
    def removeLikes(cls, messageId):
        likes: list = sql.session.query(Like).filter(Like.message_id == messageId).delete()
        sql.session.commit()

