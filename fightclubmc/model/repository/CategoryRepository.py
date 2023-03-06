from fightclubmc.configuration.config import sql
from fightclubmc.model.entity.Category import Category
from fightclubmc.model.entity.Question import Question


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the category service
#

class CategoryRepository():

    @classmethod
    def getCategories(cls):
        categories: list[Category] = sql.session.query(Category).all()
        return categories

    @classmethod
    def get(cls, categoryId):
        category: Category = sql.session.query(Category).filter(Category.category_id == categoryId).first()
        return category
