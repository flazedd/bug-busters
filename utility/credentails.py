import os
import replicate

#=> "Let's break this problem down step by step.\n\nStep 1: S...

# from hugchat import hugchat
# from hugchat.login import Login
#
# from config import config
#
#
# def get_chatbot():
#     # Log in to huggingface and grant authorization to huggingchat
#     cookie_path_dir = "./cookies/"  # NOTE: trailing slash (/) is required to avoid errors
#     sign = Login(config.MAIL, config.PASSWORD)
#     cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
#     # cookies = sign.login()
#
#     # Create a chatbot connection
#     return hugchat.ChatBot(cookies=cookies.get_dict())

import os
import replicate

import config.config


class NamedObject:
    def __init__(self, name):
        self.name = name


class ReturnObject:
    def __init__(self, text):
        self.text = text

    def wait_until_done(self):
        pass


class ChatBot():
    def __init__(self):
        os.environ['REPLICATE_API_TOKEN'] = config.config.REPLICATE_KEY
        self.conversation = """\
        """
        self.active_model = 'meta-llama/Meta-Llama-3-70B-Instruct'

    def chat(self, message: str):
        # Add user input to conversation
        self.conversation += f"[INST] {message} [/INST]\n"

        obj = {
            "prompt": self.conversation
        }

        # Generate response
        output = replicate.run(
            "meta/meta-llama-3-70b-instruct",
            input=obj
        )

        reply = "".join(output)
        self.conversation += f"{reply}\n"
        return ReturnObject(reply)

    def new_conversation(self):
        self.conversation = ''
        return 1

    def change_conversation(self, id):
        pass

    def get_remote_llms(self):
        return [NamedObject('meta-llama/Meta-Llama-3-70B-Instruct'),
                NamedObject('meta-llama/Meta-Llama-3-70B-Instruct')]

    def switch_llm(self, id):
        pass

    def get_conversation_list(self):
        return 'Dummy value'


def get_chatbot():
    return ChatBot()
