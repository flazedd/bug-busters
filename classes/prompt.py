class Prompt:
    @staticmethod
    def get_input(class_code, imports, extra):
        prompt = ''
        prompt += class_code
        prompt += '\n\nyou can use these imports only, no other imports allowed\n'
        prompt += imports
        prompt += 'give me back 1 single test case, it should only make 1 single assertion and it should pass!\n'
        # prompt += 'all the code should be inside the test case and code should be formatted with ``````\n'
        # prompt += 'only give the test case code!!!\n'
        prompt += extra
        return prompt
