import configparser

config = configparser.ConfigParser()
config.read('env.ini')
api_key = config.get("Github", "api-key")
