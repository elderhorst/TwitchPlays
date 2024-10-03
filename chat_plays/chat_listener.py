import concurrent.futures
import keyboard
import os
import pyautogui
from chat_plays import discord_connection
from chat_plays import twitch_connection
from chat_plays import youtube_connection
from chat_plays.TwitchPlays_KeyCodes import *
from dotenv import load_dotenv

class ChatListener:
	last_time = time.time()
	connections = []
	message_queue = []
	active_tasks = []
	pyautogui.FAILSAFE = False
	
	def __init__(self, message_rate, max_queue_length, max_workers):
		self.MESSAGE_RATE = message_rate
		self.MAX_QUEUE_LENGTH = max_queue_length
		self.MAX_WORKERS = max_workers
		
		self.thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=self.MAX_WORKERS)
	
	def run(self, handle_message):
		self.load_enviroment_variables()
		self.countdown()
		self.setup_connections()
		self.loop(handle_message)
	
	def load_enviroment_variables(self):
		load_dotenv()

		self.LISTEN_ON_TWITCH = os.environ.get("LISTEN_ON_TWITCH")
		self.LISTEN_ON_YOUTUBE = os.environ.get("LISTEN_ON_YOUTUBE")
		self.LISTEN_ON_DISCORD = os.environ.get("LISTEN_ON_DISCORD")

		self.TWITCH_CHANNEL = os.environ.get("TWITCH_CHANNEL")

		self.YOUTUBE_CHANNEL_ID = os.environ.get("YOUTUBE_CHANNEL_ID")
		self.YOUTUBE_STREAM_URL = os.environ.get("YOUTUBE_STREAM_URL")

		self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
		self.DISCORD_GUILD = os.getenv("DISCORD_GUILD")
		self.DISCORD_CHANNEL = os.getenv("DISCORD_CHANNEL")
		
	# Count down before starting, so you have time to load up the game
	def countdown(self):
		countdown = 5
		while countdown > 0:
			print(countdown)
			countdown -= 1
			time.sleep(1)
			
	def setup_connections(self):
		if self.LISTEN_ON_TWITCH == "True":
			twitch = twitch_connection.Twitch()
			twitch.twitch_connect(self.TWITCH_CHANNEL)
			self.connections.append(twitch)

		if self.LISTEN_ON_YOUTUBE == "True":
			youtube = youtube_connection.YouTube()
			youtube.youtube_connect(self.YOUTUBE_CHANNEL_ID, self.YOUTUBE_STREAM_URL)
			self.connections.append(youtube)

		if self.LISTEN_ON_DISCORD == "True":
			discord = discord_connection.Discord()
			discord.discord_connect(self.DISCORD_TOKEN, self.DISCORD_GUILD, self.DISCORD_CHANNEL)
			self.connections.append(discord)
			
	def loop(self, handle_message):
		while True:

			self.active_tasks = [t for t in self.active_tasks if not t.done()]

			self.check_for_messages()

			messages_to_handle = self.get_messages_to_handle()

			# If user presses Shift+Backspace, automatically end the program
			if keyboard.is_pressed('shift+backspace'):
				exit()

			if not messages_to_handle:
				continue
			else:
				for message in messages_to_handle:
					if len(self.active_tasks) <= self.MAX_WORKERS:
						self.active_tasks.append(self.thread_pool.submit(handle_message, message))
					else:
						print(f'WARNING: active tasks ({len(self.active_tasks)}) exceeds number of workers ({self.MAX_WORKERS}). ({len(self.message_queue)} messages in the queue)')
		
	def check_for_messages(self):
		# Check for new messages in all active connections
		new_messages = []
		
		for connection in self.connections:
			new_messages.extend(connection.twitch_receive_messages())
		
		# Update the message queue
		if new_messages:
			self.message_queue += new_messages; # New messages are added to the back of the queue
			self.message_queue = self.message_queue[-self.MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages
			
	def get_messages_to_handle(self):
		messages_to_handle = []
		if not self.message_queue:
			# No messages in the queue
			self.last_time = time.time()
		else:
			# Determine how many messages we should handle now
			r = 1 if self.MESSAGE_RATE == 0 else (time.time() - self.last_time) / self.MESSAGE_RATE
			n = int(r * len(self.message_queue))
			if n > 0:
				# Pop the messages we want off the front of the queue
				messages_to_handle = self.message_queue[0:n]
				del self.message_queue[0:n]
				self.last_time = time.time()
				
		return messages_to_handle
