# TwitchPlays
These are the three Python files I use that allows Twitch Chat or Youtube Chat to control your keyboard or mouse to play a game. You are welcome to use or adapt this code for your own content.

## Setup and Installation

### Dependencies
To run the code you will need to install Python 3.9.  
Additionally, you will need to install the following python modules using Pip:  
python -m pip install keyboard  
python -m pip install pydirectinput  
python -m pip install pyautogui  
python -m pip install pynput  
python -m pip install requests
python -m pip install python-dotenv

### Environment variables
In the same directory as the file you are running create a file names `.env` (with no file extension) using the following template:

```
# Replace this with your Twitch username. Must be all lowercase.
TWITCH_CHANNEL = 'dougdougw' 

# If streaming on Youtube, set this to False
STREAMING_ON_TWITCH = True

# If you're streaming on Youtube, replace this with your Youtube's Channel ID
# Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings
YOUTUBE_CHANNEL_ID = "YOUTUBE_CHANNEL_ID_HERE"

# If you're using an Unlisted stream to test on Youtube, replace "None" below with your stream's URL in quotes.
# Otherwise you can leave this as "None"
YOUTUBE_STREAM_URL = None
```

Once Python is set up, simply change the Twitch username (or Youtube channel ID) in TwitchPlays_TEMPLATE.py, and you'll be ready to go.

This code is originally based off Wituz's Twitch Plays template, then expanded by DougDoug and DDarknut with help from Ottomated for the Youtube side. For now I am not reviewing any pull requests or code changes, this code is meant to be a simple prototype that is uploaded for educational purposes. But feel free to fork the project and create your own version!
