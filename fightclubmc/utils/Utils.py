import datetime
import random
import smtplib

from flask import jsonify

from fightclubmc.utils.Constants import Constants
from resources.rest_service import config


class Utils():

    @classmethod
    def createList(cls, elements):
        response = []
        for element in elements:
            response.append(element.toJson())
        return response

    @classmethod
    def createFreeList(cls, elements):
        response = []
        for element in elements:
            response.append(element)
        return response

    @classmethod
    def createSuccessResponse(cls, success, param):
        return jsonify({
            "date": str(datetime.datetime.now()),
            "success": success,
            "param": param,
            "code": 200,
        })

    @classmethod
    def createWrongResponse(cls, success, error, code):
        return jsonify({
            "date": str(datetime.datetime.now()),
            "success": success,
            "error": error,
            "code": code,
        })

    @classmethod
    def getURL(cls, controllerName):
        return '/api/v_' + config['version'].replace('.', '_') + '/' + controllerName

    @classmethod
    def hash(cls, password: str):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        hashedPassword = ""
        encryptedChars = "C0yZEIipDF23djS5muGMfnV6HtcW4q9BJLXlPakrghNeK1AsU8xRwQbzYO7Tov"
        for i in range(len(password)):
            for j in range(len(chars)):
                if password[i] == chars[j]:
                    hashedPassword += encryptedChars[j]
                    break
        return hashedPassword

    @classmethod
    def unHash(cls, password: str):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        unhashedPassword = ""
        encryptedChars = "C0yZEIipDF23djS5muGMfnV6HtcW4q9BJLXlPakrghNeK1AsU8xRwQbzYO7Tov"
        for i in range(len(password)):
            for j in range(len(encryptedChars)):
                if password[i] == encryptedChars[j]:
                    unhashedPassword += chars[j]
                    break
        return unhashedPassword

    @classmethod
    def createLink(cls, length):
        letters = "ABCDEFGHILMNOPQRSTUVZYJKXabcdefghilmnopqrstuvzyjkx0123456789"
        link = ""
        for i in range(length):
            link += letters[random.randint(0, 59)]
        return link

    @classmethod
    def sendWelcomeEmail(cls, name, email):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(Constants.EMAIL, Constants.PASSWORD)
        server.sendmail(Constants.EMAIL, email, Constants.WELCOME_EMAIL.replace("{name}", name))

    @classmethod
    def sendPasswordForgottenEmail(cls, name, email, token):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(Constants.EMAIL, Constants.PASSWORD)
        server.sendmail(Constants.EMAIL, email, Constants.PASSWORD_FORGOTTEN_EMAIL
                        .replace("{name}", name).replace("{token}", token))
