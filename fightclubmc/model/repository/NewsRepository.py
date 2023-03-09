from fightclubmc.configuration.config import sql
from fightclubmc.model.entity.Category import Category
from fightclubmc.model.entity.News import News
from fightclubmc.model.entity.Question import Question


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 09/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the news service
#

class NewsRepository():

    @classmethod
    def getNews(cls):
        news: list[News] = sql.session.query(News).all()
        return news

    @classmethod
    def add(cls, title, body, ownerId):
        news: News = News(title, ownerId, body)
        sql.session.add(news)
        sql.session.commit()
