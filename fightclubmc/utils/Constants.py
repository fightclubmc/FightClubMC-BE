
#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the constants
#

class Constants():

    NOT_FOUND: str = "This resource was not found"
    CREATED: str = "Created"
    FULL_SLOTS = "You can't add more"
    ALREADY_CREATED = "This resource was already created"
    INVALID_REQUEST: str = "Invalid request"

    FRONTEND_URL = ''

    WELCOME_EMAIL: str = "Hey {name}! \n Benvenuto nella nostra piattaforma"
    PASSWORD_FORGOTTEN_EMAIL: str = "Hey {name}! \n Ecco il link per recuperare la tua password: " + FRONTEND_URL + "/recovery_password?token={token}"

    PAGE_NOT_FOUND = 'This page was not found. See our documentation'
    PAGE_METHOD_NOT_ALLOWED = 'Method not allowed. See our documentation'
    PAGE_UNKNOWN_ERROR = 'Unknown error'
