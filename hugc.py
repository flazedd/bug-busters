from utility import credentails

# # Log in to huggingface and grant authorization to huggingchat
# cookie_path_dir = "./cookies/"  # NOTE: trailing slash (/) is required to avoid errors
# sign = Login(config.MAIL, config.PASSWORD)
# cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
#
# # Create a chatbot connection
# chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
chatbot = credentails.get_chatbot()

# New a conversation (ignore error)
id = chatbot.new_conversation()
chatbot.change_conversation(id)

# Intro message
print('[[ Welcome to HuggingChat. Let\'s talk! ]]')
print('\'q\' or \'quit\' to exit')
print('\'c\' or \'change\' to change conversation')
print('\'n\' or \'new\' to start a new conversation')
print('\'m\' or \'model\' to change model')


def new_conv():
	id = chatbot.new_conversation()
	chatbot.change_conversation(id)
	print(f"This is a new chat, my name is {chatbot.active_model}")

while True:
	user_input = input('> ')
	s = user_input.lower()
	print("User input received...\n\n")
	if s == '':
		pass
	elif s in ['q', 'quit']:
		break
	elif s in ['c', 'change']:
		print('Choose a conversation to switch to:')
		print(chatbot.get_conversation_list())
	elif s in ['n', 'new']:
		print('Clean slate!')
		new_conv()
	elif s in ['m', 'model']:
		l = chatbot.get_remote_llms()
		for i in range(0, len(l)):
			print(f"Choose {i} for: {l[i].name}")
		print("Choosing a new model will start a new conversation")
		selection = input('> ')
		try:
			selection = int(selection)
			if 0 <= selection < len(l):
				# print(f"Current model: {chatbot.active_model}")
				chatbot.switch_llm(selection)
				# print(f"Switched to this model: {chatbot.active_model}")
				new_conv()
		except Exception as e:
			print(f"Invalid input supplied: {selection}")
	elif s in ['g', 'get']:
		print(f"You're talking to {chatbot.active_model}")
	else:
		print(chatbot.chat(user_input))
