import os
import replicate

class NamedObject:
    def __init__(self, name):
        self.name = name

class ChatBot():
    def __init__(self):
        os.environ['REPLICATE_API_TOKEN'] = 'r8_Tf397zdT0UvvywyakHa9YM7VWPMnBfL1pqScs'
        self.conversation = """\
        """

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
        return reply

    def new_conversation(self, id):
        self.conversation = ''

    def get_remote_llms(self):
        return [NamedObject('meta-llama/Meta-Llama-3-70B-Instruct'),
                NamedObject('meta-llama/Meta-Llama-3-70B-Instruct')]

    def switch_llm(self):
        pass


# os.environ['REPLICATE_API_TOKEN'] = 'r8_Tf397zdT0UvvywyakHa9YM7VWPMnBfL1pqScs'
#
# def main():
#     conversation = ''
#     while True:
#         # Get user input
#         user_input = input(">")
#
#         # Add user input to conversation
#         conversation += f"[INST] {user_input} [/INST]\n"
#
#         obj = {
#             "prompt": conversation
#         }
#
#         # Generate response
#         output = replicate.run(
#             "meta/meta-llama-3-70b-instruct",
#             input=obj
#         )
#
#         reply  = "".join(output)
#         print(f'Reply is: \n\n {reply}')
#         # Add AI's response to conversation
#         conversation += f"{reply}\n"
#
# if __name__ == "__main__":
#     main()

