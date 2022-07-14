<h1 align="center">
  Aiogram bot template
</h1>

<p align="center">
  ✈️ 🐍 📃
</p>

<p align="center">
  A simple template for an asynchronous telegram bot with webhooks to be hosted on the Heroku server.
</p>

<p align="center">
  
   <a href="https://github.com/AlexanderKorataev/aiogram-bot-template/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
  </a>
  
  <a href="https://www.python.org/downloads/release/python-3105">
    <img src="https://img.shields.io/badge/python-v3.10.5-green.svg" alt="Python: v3.10.5" />
  </a>
  
  <a href="https://t.me/aiogram_bot_template_bot">
    <img src="https://img.shields.io/badge/Telegram-bot-blue" alt="Telegram: bot" />
  </a>
  
![photo_2022-07-13_17-04-20](https://user-images.githubusercontent.com/87244069/178807124-c2e5b9fd-350c-4277-ad0f-bac777b8ddb5.jpg)

## Running on your PC 🚀

1. **Clone the GitHub repository.**

   ```shell
   git clone https://github.com/AlexanderKorataev/aiogram-bot-template.git
   ```
  
2. **Create a virtual environment.**

   ```shell
   python -m venv venv
   ```
   and activate
   ```shell
    . venv/bin/activate
    ```
  
3. **Install dependencies from requirements.txt.**

   ```shell
   pip install -r requirements.txt
   ```
  
4. **Create environment variables TOKEN and DEBUG.**
  
5. **Run the bot script.**
   ```shell
   python polling.py
   ```

## Dispatch to Heroku ☁
  
1. **Create a new application on Heroku and configure**

   ### In the settings
   - Add a buildpack *heroku/python*
   - Add config vars DEBUG, TOKEN and HEROKU_APP_NAME
  
2. **Clone the GitHub repository.**

   ```shell
   git clone https://github.com/AlexanderKorataev/aiogram-bot-template.git
   ```
  
3. **Create your Github repository and connect it to Heroku in the Deploy section.**

## File system 📁

| folder       | purpose                                                                          |
| ------------ | -------------------------------------------------------------------------------- |
| handlers     | handlers of commands and messages sent to the telegram bot                       |
| keyboards    | bot keyboards                                                                    |
| plugins      | plugins for adding functionality to the bot                                      |
| settings     | project settings                                                                 |
