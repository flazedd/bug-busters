from hugchat import hugchat
from hugchat.login import Login

from config import config


def get_chatbot():
    # Log in to huggingface and grant authorization to huggingchat
    cookie_path_dir = "./cookies/"  # NOTE: trailing slash (/) is required to avoid errors
    sign = Login(config.MAIL, config.PASSWORD)
    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
    # cookies = sign.login()

    # Create a chatbot connection
    return hugchat.ChatBot(cookies=cookies.get_dict())
