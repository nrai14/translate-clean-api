# Translatate-Clean-API (ReadMe Documentation)

## Description

Flask-based translation API. The service validates, cleanses, and translate English words into a target language using LibreTranslate, ensuring accurate and duplicate-free results. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Credits](#credits)
- [License](#license)

# Getting started guide 

## Installation

The following are required to be installed on your system to get the development environment running:

* Node.js (version 16 or later) and npm
* Python (version 3.10 or later) and pip
* Docker

### Step 1: Clone the Repository 
- In the terminal run:
* git clone git@github.com:nrai14/translate-clean-api.git
* then "cd" into the folder

### Step 2: Install Node.js Dependencies 
* npm install

### Step 3: Install Python Dependencies
- In the terminal run:
* python3 -m venv venv 
* source venv/bin/activate (for Mac) or venv/Scripts/activate (for Windows)
* pip install -r requirements.txt 

### Step 4: Start the LibreTranslate API
- In the terminal run:
* docker-compose up -d
(this will create the containerised LibreTranslate on port 5002)
* docker-compose ps
(checks the service is running)
(verify it's running with curl http://localhost:5002 - you should see a response)



## Usage

### Step 1: Run the Flask Backend
* In the terminal enter: source venv/bin/activate
* In the terminal enter: flask run 
(the backend will be available at http://127.0.0.1:5000)

### Step 2: Prepare the Input File
* Place words you wish to translate within the Excel file - data/wordsToTranslate.xlsx
* Ensure words are only the first column 
* If you want to see how this API works, the data/wordsToTranslate.xlsx is already filled with data to try

### Step 3: Run the Node.js wrapper
* Open a split terminal 
* In the split terminal enter: - npm run start 
(this runs the wrapper, processes translations, and saves the result as an .xlsx file in the results folder)

### Step 4: Check results
* Open the results/translatedWords.xlsx file to view the translations
* Each target langauge will have its own sheet

## Step 5: Stop Service 
- When you're finished, run this in the terminal:
* docker-compose down 

### Things to note:
* There could be excel file compatibility issues - e.g. on macOS, if the file doesn't open immediately, please use Google Sheets
* For any set up issues, please see [Troubleshooting](#troubleshooting)



## My Experience

### What was my motivation?

I embarked on this project to push my technical skills to the next level. Having worked with Python, JavaScript and Java in the past, I wanted to challenge myself by incorporating new tools like Docker and integrating multiple APIs into a cohesive application. My goal was to gain hands-on experience with setting up Flask backends, using Node.js wrappers, and tackling real-world issues like batch processing, error handling, and scalability.

This project was also an opportunity to revisit foundational skills I learned during Makers Academy, such as test-driven development and Agile practices, while exploring new technologies that are relevant in today’s software development landscape.

### Why did I build this project? 

The core reason for building this project was to enhance my understanding of full-stack development and API integrations. By using tools like Flask, Node.js, and LibreTranslate, I created a functional pipeline for translating and managing data across multiple languages. This gave me experience working with:

* Python libraries like Flask, Pandas, and SpellChecker for efficient backend processes.
* Docker to containerise and manage the LibreTranslate API.

### What problem does it solve?

This project automates the otherwise tedious task of translating large datasets into multiple languages. It’s designed for scenarios where businesses or users need batch translations efficiently, with spell-checking and data cleaning included. It bridges the gap between raw user input and structured, high-quality translations stored in a sharable format (Excel).

### What did I learn?

This project was a blend of revisiting old knowledge and learning new skills:

Revisited Skills: Makers Academy principles like Agile development, clean coding, and TDD came in handy. I also solidified my understanding of Python and Node.js while working on API integrations.

New Skills:
* Docker: Setting up and troubleshooting a local Docker container to host LibreTranslate.
* Batch Processing: Implementing efficient batch processing for translating large datasets.
* Flask Debugging: Overcoming issues like port conflicts and environmental variable persistence.
* Spell Checker Integration: Handling real-world edge cases like invalid words and preparing data for translation.

### What particular libraries? Why?

* Flask: Lightweight framework for building the backend.
* SpellChecker: To clean and correct input words before translation.
* Pandas: Initially used for Excel processing before transitioning to ExcelJS.
* ExcelJS: For efficient handling of Excel files in Node.js.
* Docker: To containerise and deploy LibreTranslate for local API calls.
* LibreTranslate: Translation API for handling multilingual requests.
* Node.js: To test a scalable wrapper for batch translation.

### Assumptions 

* Design Assumptions
- Assumed input would be mostly single words in English
- Believed LibreTranslate's batch processing would work without modification
- Assumed Docker would handle API hosting seamlessly

* Mistaken Assumptions
- Somehow embarrassingly overlooked the translate-wrapper.ts and went down a rabbit hole of using xlwings/pandas to manually extract data
- Thought LibreTranslate would process a bulk list of words without adapting its input format

### Pragmatic Shortcuts 

- Assumed a basic spell-checker is sufficient for this project
- Using LibreTranslate instead of perhaps implementing my own translation logic (this would definitely take a much longer time)



### What challenges did I experience? How did I overcome them? 

My first major challenge involved setting up the LibreTranslate library, which was critical for handling translations in my project. Initially, I tried installing LibreTranslate directly into my Python environment. However, I encountered persistent issues with the installation of a dependency called PyICU, which required compiling native C++ code and configuring paths for the ICU library. Despite trying multiple fixes, including setting environment variables, reinstalling tools like pkg-config, and even forcing prebuilt wheels, the build process for PyICU kept failing.

This process was complicated by the fact that the installation required deep integration with system-level libraries and C++ compilers, which are highly sensitive to system configurations. On macOS, for instance, managing dependencies through tools like Homebrew added another layer of complexity, as it introduced version mismatches and path issues. The situation was further exacerbated by the fact that these problems were specific to my system, making generalised solutions ineffective.

Recognising that this path was consuming significant time without yielding results, I pivoted to using Docker. Docker allowed me to run LibreTranslate as a standalone container, completely bypassing the need for system-level installations and configurations. While this solved the immediate problem, it presented a new challenge: I had never used Docker before.

I had to quickly learn:

- The basics of Docker containers.
- How to pull and run the official LibreTranslate image.
- How to manage Docker networks and ports to integrate it with my Flask backend.
- Ultimately, this pivot was successful, and it not only resolved the dependency issues but also taught me a valuable new skill.

Another challenge arose when implementing batch processing for translations. The initial implementation processed each word one by one, resulting in high latency due to the overhead of individual API calls. This was inefficient and not scalable. To address this, I implemented a batching mechanism that sent them to the LibreTranslate API in a single request. This change significantly improved the performance of the translation process. 

Finally, integrating a spell-checking API added its own complexity. It was important to ensure that the spell checker did not interfere with valid words, especially in a multilingual context. After exploring various libraries, I selected pyspellchecker for its simplicity and efficiency. Incorporating it required cleansing words of special characters, converting them to lowercase, and ensuring that incorrectly spelled words were flagged and corrected before translation.

These challenges collectively pushed me to:

- Deepen my understanding of API integration.
- Strengthen my debugging and troubleshooting skills.
- Learn entirely new tools like Docker.
- Improve my ability to pivot and adapt to constraints.
- Each obstacle turned into an opportunity to enhance both the functionality of the project and my technical skills.

### Extra features?

- Performance Logging 
- Error Handling
- Self-Hosting with Docker (no need for API keys/quotas imposed + No external dependencies + Unlimited requests)

### If I had more time, what else would I implement? 

* Advanced batch processing - perhaps something that could configure batch sizes/dyanmic handling to optimise translation time for very, very large datasets 
* Front-End Interfact - add simple UI ot allow users to upload files and select target langauge directly. This would make user experience more convenient by removing the need for manual setup 
* Enhanced spell checking - there might be more advanced spell-checking functionality with other APIs
* Custom target language - allow users to choose what langauge they wish to translate to
* Progress tracking - with large datasets, it might be useful for users to see real-time progress on the status of their request (perhaps have a countdown completion timer)
* More detailed mocking external APIs - API timeouts/netowrk errors/weird response formats/error codes
* Load and Performance testing - see if my app can handle even larger payloads/many requests without crashing 
* More advanced ReadMe - with further time, perhaps expanding this ReadMe with ways developers can contribute/customise the project for their own needs would be great



## Troubleshooting

### Possible hiccups 

* If any import problem/issues show up, dependencies might not work correctly. Please check and make sure the path to the interpreter/virtual environment is set up correctly 
* Issues with opening .xlsx file - Mac users may experience this, please first try opening with Google sheets
* If opening with Google sheets is unsuccessful please try the following curl command:

curl -X POST http://localhost:5002/translate \
-H "Content-Type: application/json" \
-d '{"q":"hello","source":"en","target":"es"}'

* The above should return this if it's all working:
{"translatedText":"hola"}

* For the above, if you receive "curl: (52) Empty reply from server" then LibreTranslate has not been set up correctly in a Docker container. Please use "docker ps" to show all running containers and their IDs. Then use "docker restart CONTAINER ID". Please try the curl command again. 
* Note: sometimes in the split terminal, where you are running the "npm run start" being in the virtual environment causes issues. Run "deactivate" if you see you are in "venv" in the split terminal
* Occasionally, if you have multiple containers (non-active) running, Docker might not have the space to run properly. There is an option to run "docker container prune" in the terminal to remove all stopped containers to reclaim space. 
* For further issues, please feel free to email me on: nishadrai14@gmail.com and I'll be more than happy to assist. 


## Testing 

- This project uses Pytest for testing - covers both API endpoints and utility functions. 
- Important for confidence when making changes in the future
- In the command (if not already done so):
* pip install -r requirements.txt 
(Because we need Pytest)
* PYTHONPATH=. pytest
(Runs all tests, navigates to the project's root directory and executes)
- Test results will be displayed in the terminal 
- Uses requests-mock to simulate LibreTranslate API during testing (ensures tests don't dpeend on the external API being available)

## Credits

* https://flask.palletsprojects.com/en/stable/ (Flask Documentation)
* https://tedboy.github.io/flask/quickstart/quickstart4.html (Flask Routing)
* https://docs.docker.com/desktop/setup/install/mac-install/ (Docker Setup Documentation)
* https://www.boot.dev/lessons/6f30791a-eeb5-4485-900c-6c8c0b760f8a (Docker Tutorial)
* https://www.codecademy.com/resources/docs/python/regex/sub (For writing cleanse_method)
* https://pyspellchecker.readthedocs.io/en/latest/ (psyspellchecker documentation)
* https://github.com/LibreTranslate/LibreTranslate (LibreTranslate GitHub Repo)
* https://chatgpt.com/share/674daca7-a1ec-8006-b85f-0bb076f82fdc (Conversation with ChatGPT on optimising processing time)
* https://www.geeksforgeeks.org/time-perf_counter-function-in-python/ (Logging timing for processes)
* https://coding-boot-camp.github.io/full-stack/github/professional-readme-guide (For writing a banging ReadMe document)


## License

MIT License

Copyright (c) [2024] [Nishad Rai]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Features

* Spell Check and Cleaning (remove special characters and correct misspellings)
* Translation API Integration (POST requests to LibreTranslate's API which is containerised with Docker)
* Error Handling (returns error responses for validation and API errors)
* Batch translations (for faster processing)
* Logging and Performance monitoring (measures + logs time for cleaning words. Provides insights into bottlenecks)


## Tests

