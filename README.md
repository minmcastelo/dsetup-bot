# Discord Bot Template

A basic template for creating a Discord bot.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white)

## Useful Links for Building the Bot

+ **[Python](https://www.python.org/downloads/)** required to run the bot’s code
+ **[Git](https://git-scm.com/install/)** used to clone and manage the project repository
+ **[Discord Development Portal](https://discord.com/developers/applications)** where you create and configure your Discord application

## How to Install

### 1. Install Python Packages
Make sure you have Python installed. Then run the command below to install the necessary libraries:
```sh
pip install discord.py python-dotenv
```

### 2. Download the Project
Use the following commands to clone the repository and access the project folder:
```sh
git clone https://github.com/minmcastelo/dsetup-bot awesome-bot
cd awesome-bot
```
If you want, you can download the repository as a Zip file from GitHub.

### 3. Set Up the Bot Token
After opening the project, find the **.env** file and add your bot’s token to the variable shown below:
```sh
DISCORD_TOKEN="YOUR_BOT_TOKEN"
```

>[!NOTE]
> You can also use the **.env** file to store API keys for any additional services your bot may use. This helps keep sensitive information organized and protected.
