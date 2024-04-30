# CSE3000

Name: Reinier Schep<br>
Student number: 5512743<br>
Follow these steps to run the experiment.<br>
It works on Windows 11. <br>

This repo makes use of the api for huggingface written by Soulter which can be found [here](https://github.com/Soulter/hugging-chat-api)

## Instructions

1. Make sure you have Gradle (version 8.7 or higher) installed. You can download Gradle from [here](https://gradle.org/install/).

2. Clone this repository.

3. Make a new virtual environment with `python3 -m venv venv`.

4. Activate your new virtual env with `source venv/Scripts/activate` (windows).

5. Install the requirements with `pip install -r requirements.txt`

6. Execute `touch config.py`

7. Paste this in `config.py` with your actual email and password for huggingface \
`EMAIL = "YOUR_EMAIL"` \
`PASSWORD = "YOUR_PASSWORD"`

7. Run ```python3 main.py``` to run the experiment.

