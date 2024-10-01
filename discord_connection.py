import discord
import time
import os
from dotenv import load_dotenv

load_dotenv()

class Discord:
	TOKEN = os.getenv("DISCORD_TOKEN")
	GUILD = os.getenv("DISCORD_GUILD")
	CHANNEL = os.getenv("DISCORD_CHANNEL")

	intents = discord.Intents.default()
	intents.message_content = True
	
	client = discord.Client(intents=intents)
	guild = None

	messages = []
	
	@client.event
	async def on_ready():
		print(f"{Discord.client.user} has connected to discord!")
		
		Discord.guild = discord.utils.find(lambda g: g.name == Discord.GUILD, Discord.client.guilds)
		
	@client.event
	async def on_message(message):
		if message.author == Discord.client.user:
			return
		
		if message.content != None and message.content != "" and message.channel.name == Discord.CHANNEL:
			msg = {
				"username": message.author,
				"message": message.content,
			}
			
			Discord.messages.append(msg)

	def twitch_connect(self):
		self.client.run(self.TOKEN)
		
		while(self.guild == None):
			Time.delay(1)

	def reconnect(self, delay):
		time.sleep(delay)
		self.twitch_connect(self.channel)

	def twitch_receive_messages(self):
		response = messages
		messages = []
		
		return response

