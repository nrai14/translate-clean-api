# Translation-Service

## Description

Flask-based translation API. The service validates, cleanses, and translate English words into a target language using LibreTranslate, ensuring accurate and duplicate-free results. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

# Getting started guide 

## Installation

What are the steps required to install your project? Provide a step-by-step description of how to get the development environment running.

## Usage

Provide instructions and examples for use. Include screenshots as needed.

To add a screenshot, create an `assets/images` folder in your repository and upload your screenshot to it. Then, using the relative filepath, add it to your README using the following syntax:

    ```md
    ![alt text](assets/images/screenshot.png)
    ```

## My Experience

- What was your motivation?
- Why did I build this project? 
- What problem does it solve?
- What did I learn?

- What particular libraries? Why?
- Assumptions? Shortcuts?
- Challenges? Overcome how?

My first major challenge involved setting up the libretranslate library, which is critical for handling translations in my project. The initial plan was to install libretranslate directly into my Python environment. However, I encountered persistent issues with the installation of a dependency called PyICU, which required compiling native C++ code and configuring paths for the ICU library. Despite trying multiple fixes, including setting environment variables, reinstalling tools like pkg-config, and even forcing prebuilt wheels, the build process for PyICU kept failing.

The installation process for PyICU required deep integration with system-level libraries and C++ compilers, which are highly sensitive to configurations.

This process consumed significant time and effort without success.

I also realised that these issues were specific to my system (macOS with Homebrew), adding an additional layer of complexity.

Given the time constraints and the goal of delivering a working solution, I decided to pivot to using Docker. Docker allows me to run LibreTranslate as a standalone container, which bypasses all the installation and configuration issues. This is my first time using Docker, so I had to learn and set it up as part of the solution.

- Extra features?
- More time, what else would I implement? 

## Credits

List your collaborators, if any, with links to their GitHub profiles.

If you used any third-party assets that require attribution, list the creators with links to their primary web presence in this section.

If you followed tutorials, include links to those here as well.

## License

The last section of a high-quality README file is the license. This lets other developers know what they can and cannot do with your project. If you need help choosing a license, refer to [https://choosealicense.com/](https://choosealicense.com/).

---

🏆 The previous sections are the bare minimum, and your project will ultimately determine the content of this document. You might also want to consider adding the following sections.

## Badges

![badmath](https://img.shields.io/github/languages/top/lernantino/badmath)

Badges aren't necessary, per se, but they demonstrate street cred. Badges let other developers know that you know what you're doing. Check out the badges hosted by [shields.io](https://shields.io/). You may not understand what they all represent now, but you will in time.

## Features

If this project ends up has a lot of features, list here


## Tests

Go the extra mile and write tests for your application. Then provide examples on how to run them here.