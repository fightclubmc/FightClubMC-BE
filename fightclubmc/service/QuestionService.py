import json

from flask import jsonify

from fightclubmc.model.entity.Category import Category
from fightclubmc.model.entity.Message import Message
from fightclubmc.model.entity.Question import Question
from fightclubmc.model.entity.User import User
from fightclubmc.model.repository.MessageRepository import MessageRepository
from fightclubmc.model.repository.QuestionRepository import QuestionRepository
from fightclubmc.model.repository.UserRepository import UserRepository
from fightclubmc.service.CategoryService import CategoryService
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
        category: dict = CategoryService.get(categoryId)
        questions: list = []
        result: dict = {'category': category, 'questions': []}
        if permissions == 'OWN':
            questions: list[Question] = QuestionRepository.getQuestionsByCategoryOf(userId, categoryId)
        elif permissions == 'ALL':
            questions: list[Question] = QuestionRepository.getQuestionsByCategory(categoryId)
        for question in questions:
            owner: dict = UserService.getUser(question.owner_id)
            messages: list = MessageRepository.getMessages(question.question_id)
            result['questions'].append(question.toJson_Owner_Messages(owner, len(messages)))
        return jsonify(result)

    @classmethod
    def getAllQuestions(cls):
        questions: list[Question] = QuestionRepository.getAllQuestions()
        return Utils.createList(questions)

    @classmethod
    def get(cls, userId, questionId):
        permissions: bool = UserPermissionsService.hasQuestionAccess(userId, questionId)
        if permissions:
            question: Question = QuestionRepository.get(questionId)
            owner = UserService.getUser(question.owner_id)
            return question.toJson_Owner(owner)
        else:
            return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 403), 403

    @classmethod
    def add(cls, request):
        QuestionRepository.add(request['name'], request['owner_id'], request['category_id'])
        return Utils.createSuccessResponse(True, QuestionRepository.getLastQuestion(request['owner_id']).question_id)

    @classmethod
    def changeStatus(cls, request):
        QuestionRepository.changeStatus(request['question_id'], request['status'])
        if request['status'] == 'accepted' or request['status'] == 'rejected':
            QuestionRepository.setClosed(request['question_id'], True)
        else:
            QuestionRepository.setClosed(request['question_id'], False)
        return Utils.createSuccessResponse(True, Constants.CREATED)
