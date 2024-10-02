import discord
import threading
import time
from dotenv import load_dotenv

load_dotenv()

class Discord:
	client = None

	def discord_connect(self, token, guild, channel):
		intents = discord.Intents.default()
		intents.message_content = True
		
		self.client = ChatRecordingClient(intents, guild, channel)
		
		bot = threading.Thread(target=self.run_bot, args=(token,), daemon=True)
		bot.start()
		
	def run_bot(self, token):
		self.client.run(token)

	def reconnect(self, delay):
		time.sleep(delay)
		self.discord_connect(self.channel)

	def twitch_receive_messages(self):
		# This should be using locks
		response = self.client.messages
		self.client.messages = []
		
		return response

class ChatRecordingClient(discord.Client):
	guild_name = ""
	channel_name = ""
	
	guild = None
	
	messages = []
	
	def __init__(self, intents, guild_name, channel_name):
		self.guild_name = guild_name
		self.channel_name = channel_name
		
		discord.Client.__init__(self, intents=intents)
	
	async def on_ready(self):
		print(f"{self.user} has connected to discord!")
		
		self.guild = discord.utils.find(lambda g: g.name == self.guild_name, self.guilds)
		
	async def on_message(self, message):
		if message.author == self.user:
			return
		
		if message.content != None and message.content != "" and message.channel.name == self.channel_name:
			msg = {
				"username": message.author.name,
				"message": message.content,
			}
			
			self.messages.append(msg)
