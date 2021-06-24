'''
Module : Software for Digital Innovation 
Assessment : ICA-2 (Freedom Of Information)
Project Name : Freedom Of Information

@author: Mohana Kamanooru
email : A0223038@live.tees.ac.uk
'''   

#########################################################
# Configuration details - Development Environment
#########################################################

class Config:
    '''set base flask configurations
    '''
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    TEMPLATES_AUTO_RELOAD = True 


#########################################################
# Configuration details - Configuration Object
#########################################################

class DevConfig(Config):
    '''set base Development configurations
    '''
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    
#########################################################
# Configuration details - Testing / Pre-Prod Environment
#########################################################

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'Testing'


#########################################################
# Configuration details - Production Environment
##########################################################

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

