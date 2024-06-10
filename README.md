# CSE3000

Name: Reinier Schep<br>
Student number: 5512743<br>
Follow these steps to run the experiment.<br>
It works on Windows 11. <br>

To run this experiment you need to obtain an API key from [replicate](https://replicate.com/)
which costs you money based on the usage. Also, this repository already contains all the generated data from the experiment,
so if you want to generate new data, you first need to delete the old data, or just use run numbers higher than 10. 
This repository contains full data for runs 1 to 6 and partial data for runs 7 to 10. 

## Instructions

1. Make sure you have Gradle (version 8.7 or higher) installed. You can download Gradle from [gradle](https://gradle.org/install/).
1. Make sure you have Python 3.10 installed, other versions won't work. 
1. Clone this repository. 
1. Make a new virtual environment with `python3 -m venv venv`. 
1. Activate your new virtual env with `source venv/Scripts/activate` (windows).
1. Install the requirements with `pip install -r requirements.txt`
1. Run `touch ./config/config.py` to create config.py.
1. Paste this in `config.py` with your actual API key from [replicate](https://replicate.com/)  \
`REPLICATE_KEY = "YOUR_REPLICATE_API_KEY"` (Making use of their service costs money!)
2. `./config/constant.py` contains some constants which change the behaviour of the experiment. 
3. Make sure to change the run inside the subsequent files to how many runs and which runs you want to generate.
1. Run ```python improve.py``` to generate all the test suites.
2. Run ```python stats.py``` to calculate all the statistics.
3. The files that start with 'visualize' and end in '.py' are used to generate visualizations based on the data generated.
