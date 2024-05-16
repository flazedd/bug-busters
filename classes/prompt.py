class Prompt:
    @staticmethod
    def get_input(class_code, imports, extra):
        prompt = ''
        prompt += class_code
        prompt += '\n\nyou can use these imports only\n'
        prompt += imports
        prompt += '\ngive me back 1 single test case, it should only make 1 single assertion and it should pass!\n'
        prompt += extra
        return prompt
