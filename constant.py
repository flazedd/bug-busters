import threading

RETRIES = 1  # amount of retries for getting a test suite that passes
PRINT_LOCK = threading.Lock()
MODEL = 1
JSON_NAME = 'result'

# Choose 0 for: CohereForAI/c4ai-command-r-plus
# Choose 1 for: meta-llama/Meta-Llama-3-70B-Instruct
# Choose 2 for: HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1
# Choose 3 for: mistralai/Mixtral-8x7B-Instruct-v0.1
# Choose 4 for: NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO
# Choose 5 for: google/gemma-1.1-7b-it
# Choose 6 for: mistralai/Mistral-7B-Instruct-v0.2
# Choose 7 for: microsoft/Phi-3-mini-4k-instruct
