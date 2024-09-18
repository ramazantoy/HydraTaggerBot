import configparser

config = configparser.ConfigParser()
config.read('config.ini')

sudo_users = [int(user_id.strip()) for user_id in config.get('Sudo', 'SudoUsers').split(',')]

print(sudo_users)


def is_sudo_user(user_id: int) -> bool:
    return user_id in sudo_users
