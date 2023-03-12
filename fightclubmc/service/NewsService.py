from flask import jsonify

from fightclubmc.model.entity.Category import Category
from fightclubmc.model.entity.Message import Message
from fightclubmc.model.entity.News import News
from fightclubmc.model.entity.Question import Question
from fightclubmc.model.repository.CategoryRepository import CategoryRepository
from fightclubmc.model.repository.NewsRepository import NewsRepository
from fightclubmc.model.repository.QuestionRepository import QuestionRepository
from fightclubmc.service.MessageService import MessageService
from fightclubmc.service.UserService import UserService
from fightclubmc.utils.Constants import Constants
from fightclubmc.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 09/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the news service
#


class NewsService():

    @classmethod
    def getNews(cls):
        newses: list[News] = NewsRepository.getNews()
        result: list[dict] = []
        for news in newses:
            owner: dict = UserService.getUser(news.owner_id)
            result.append(news.toJson_Owner(owner))
        return jsonify(result)

    @classmethod
    def add(cls, request):
        NewsRepository.add(request['title'], request['body'], request['owner_id'])
        users: list = UserService.getAllUsers()
        for user in users:
            Utils.sendNewsEmail(request['title'], request['body'], user['email'])
        return Utils.createSuccessResponse(True, Constants.CREATED)