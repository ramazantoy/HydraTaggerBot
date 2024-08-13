import configparser

config = configparser.ConfigParser()
config.read('config.ini')
accountID = config.getint('Credentials', 'accountID')
accountHash = config.get('Credentials', 'accountHash')
Token = config.get('Credentials', 'Token')
DebugId=config.get('Credentials', 'DebugId')