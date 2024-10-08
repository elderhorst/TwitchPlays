# TwitchPlays
These are the three Python files I use that allows Twitch Chat or Youtube Chat to control your keyboard or mouse to play a game. You are welcome to use or adapt this code for your own content.

## Setup and Installation

### Dependencies
To run the code you will need to install Python 3.9 or greater.  
The python dependencies can be installed with the requirements.txt file.

1. Create the virual enviroment
```
python -m venv chatplaysenv
```

2. Activate the virual environment

Windows
```
chatplaysenv\Scripts\activate
```

MacOS / Linux
```
source chatplaysenv/bin/activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

Note: While the requirements.txt file shows all the installed pacakges, the following are the core packages this project cares about: keyboard, pydirectinput, pyautogui, pynput, requests, python-dotenv, discord

### Environment variables
In the same directory as the file you are running create a file names `.env` (with no file extension) using the following template:

```
# Set to True which sources you want to listen to for the input.
LISTEN_ON_TWITCH = True
LISTEN_ON_YOUTUBE = False
LISTEN_ON_DISCORD = False

# Twitch Settings
# Replace this with your Twitch username. Must be all lowercase.
TWITCH_CHANNEL = "YOUR_USERNAME"

# Youtube Settings
# Replace this with your Youtube's Channel ID. Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings.
YOUTUBE_CHANNEL_ID = "YOUTUBE_CHANNEL_ID_HERE"

# If you're using an Unlisted stream to test on Youtube, replace "None" below with your stream's URL in quotes.
# Otherwise you can leave this as "None"
YOUTUBE_STREAM_URL = None

# Discord Settings
DISCORD_TOKEN = "BOT_TOKEN"
DISCORD_GUILD = "GUILD_SERVER_NAME"
DISCORD_CHANNEL = "CHANNEL_NAME"
```

## Running
Once Python is set up, simply change the Twitch username, Youtube channel ID, or Discord information in the .env file, and you'll be ready to go.

```
python TwitchPlays_TEMPLATE.py
```

## Credits

This code is originally based off Wituz's Twitch Plays template, then expanded by DougDoug and DDarknut with help from Ottomated for the Youtube side. For now I am not reviewing any pull requests or code changes, this code is meant to be a simple prototype that is uploaded for educational purposes. But feel free to fork the project and create your own version!
