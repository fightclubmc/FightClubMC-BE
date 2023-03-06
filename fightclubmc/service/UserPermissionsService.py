from fightclubmc.model.repository.CategoryRepository import CategoryRepository
from fightclubmc.model.repository.QuestionRepository import QuestionRepository
from fightclubmc.model.repository.UserRepository import UserRepository
from fightclubmc.service.CategoryService import CategoryService


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user service
#


class UserPermissionsService():

    @classmethod
    def hasCategoryAccess(cls, userId, categoryId):
        if CategoryRepository.get(categoryId).private:
            if cls.isStaffer(userId):
                return "ALL"
            else:
                return "OWN"
        else:
            return "ALL"

    @classmethod
    def hasQuestionAccess(cls, userId, questionId):
        return cls.isStaffer(userId) and QuestionRepository.get(questionId).owner_id == userId

    @classmethod
    def isStaffer(cls, userId) -> bool:
        return UserRepository.getUserById(userId).admin
