import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info' , 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info' , 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('commmon info' , 'password')
        return password
