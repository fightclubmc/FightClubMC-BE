import json

from flask import jsonify

from fightclubmc.model.entity.Category import Category
from fightclubmc.model.entity.Message import Message
from fightclubmc.model.entity.Question import Question
from fightclubmc.model.entity.User import User
from fightclubmc.model.repository.MessageRepository import MessageRepository
from fightclubmc.model.repository.QuestionRepository import QuestionRepository
from fightclubmc.service.MessageService import MessageService
from fightclubmc.service.UserPermissionsService import UserPermissionsService
from fightclubmc.service.UserService import UserService
from fightclubmc.utils.Constants import Constants
from fightclubmc.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the question service
#

class QuestionService():

    @classmethod
    def getQuestionsByCategory(cls, userId, categoryId):
        permissions = UserPermissionsService.hasCategoryAccess(userId, categoryId)
        questions: list[Question] = []
        result: list[dict] = []
        if permissions == 'OWN':
            questions: list[Question] = QuestionRepository.getQuestionsByCategoryOf(userId, categoryId)
        elif permissions == 'ALL':
            questions: list[Question] = QuestionRepository.getQuestionsByCategory(categoryId)
        for question in questions:
            owner: dict = UserService.getUser(question.owner_id)
            messages: list = MessageRepository.getMessages(question.question_id)
            result.append(question.toJson_Owner_Messages(owner, len(messages)))
        return jsonify(result)

    @classmethod
    def getAllQuestions(cls):
        questions: list[Question] = QuestionRepository.getAllQuestions()
        return Utils.createList(questions)

    @classmethod
    def get(cls, questionId):
        question: Question = QuestionRepository.get(questionId)
        owner = UserService.getUser(question.owner_id)
        return question.toJson_Owner(owner)

    @classmethod
    def add(cls, request):
        QuestionRepository.add(request['name'], request['owner_id'], request['category_id'])
        return Utils.createSuccessResponse(True, Constants.CREATED)
