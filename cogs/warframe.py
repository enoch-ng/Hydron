import requests
import asyncio

try:
	import discord
	from discord.ext import commands
except ImportError:
	print("Unable to load MatchUpdates cog. Check your discord.py installation.")

PC_URL = "http://content.warframe.com/dynamic/worldState.php"
XBOX_URL = "http://content.xb1.warframe.com/dynamic/worldState.php"
PS4_URL = "http://content.ps4.warframe.com/dynamic/worldState.php"

class Notify:
	def __init__(self, bot):
		self.bot = bot

	async def loop(self):
		await self.bot.wait_until_ready()
		while not self.bot.is_closed():
			self.bot.loop.create_task(self.notifyChannel())
			await asyncio.sleep(5) # Hardcoded timer for now

	async def 

class Warframe:
	"""Cog for notifications"""

	def __init__(self, bot):
		self.bot = bot

	def get_alerts_channel(self, server):
		return self.bot.server_settings_list[server.id]["alerts_channel"]

	def make_request(self, url, matchid = ""):
		try:
			response = requests.get(url)
			response.raise_for_status() # Raise an exception if the request was unsuccessful (anything other than status code 200)
			return response
		except Exception as err:
			print(err)
			raise

	async def get_worldstate(self):
		response = self.make_request(PC_URL)

def setup(bot):
	wf = Warframe(bot)
	bot.add_cog(wf)
	#bot.loop.create_task(wf.get_worldstate())
