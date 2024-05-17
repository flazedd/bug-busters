import threading
from classes.java_implementation import JavaImplementation

RETRIES = 2  # amount of retries for getting a test suite that passes
PRINT_LOCK = threading.Lock()
MODEL = 0
JSON_NAME = 'result'
SLEEP = 2
ORACLES = [JavaImplementation()]

# Choose 0 for: CohereForAI/c4ai-command-r-plus
# Choose 1 for: meta-llama/Meta-Llama-3-70B-Instruct works
# Choose 2 for: HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1 dead?
# Choose 3 for: mistralai/Mixtral-8x7B-Instruct-v0.1
# Choose 4 for: NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO
# Choose 5 for: google/gemma-1.1-7b-it
# Choose 6 for: mistralai/Mistral-7B-Instruct-v0.2
# Choose 7 for: microsoft/Phi-3-mini-4k-instruct


# as of may 16
# Choose 0 for: CohereForAI/c4ai-command-r-plus works somewhat
# Choose 1 for: meta-llama/Meta-Llama-3-70B-Instruct works
# Choose 2 for: HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1 server response contains error 404
# Choose 3 for: mistralai/Mixtral-8x7B-Instruct-v0.1 works
# Choose 4 for: NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO model is overloaded
# Choose 5 for: 01-ai/Yi-1.5-34B-Chat stupid
# Choose 6 for: google/gemma-1.1-7b-it works
# Choose 7 for: mistralai/Mistral-7B-Instruct-v0.2 works
# Choose 8 for: microsoft/Phi-3-mini-4k-instruct works