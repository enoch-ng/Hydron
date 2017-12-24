import asyncio

try:
	import discord
	from discord.ext import commands
except ImportError:
	print("Unable to load General cog. Check your discord.py installation.")

class General:
	"""General features, including automatic name changing and welcome messages"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context = True)
	async def faq(self, ctx):
		"""Displays a basic FAQ."""
		emb = discord.Embed()
		emb.set_author(name = "Frequently Asked Questions")
		emb.add_field(name = "Why am I not getting updates for matches?", value = "Make sure a channel is set through the `%smatchchannel` command. Also, make sure you've given the bot permissions to talk in that channel." % self.bot.get_prefix())
		emb.add_field(name = "What's with the nicknames? Can I set my own nickname for the bot?", value = "If the `autochangename` setting is on, the bot will automatically change its name periodically to the name of a random Dota 2 bot. To set your own nickname for the bot, disable `autochangename` and then right-click the bot and select \"Change Nickname\".")
		emb.add_field(name = "Will you periodically add new leagues to the bot?", value = "I will on my instance of the bot. If you're running your own instance of the bot, you'll have to add new leagues through the `%saddleague` command or by editing the settings.json file." % self.bot.get_prefix())
		emb.add_field(name = "How do I find out what ID a tournament comes under?", value = "You can get league IDs by calling Valve's API (https://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v1/?key=YOUR_API_KEY). In the future I hope to have some way to let people know the league IDs of upcoming tournaments more easily.")
		emb.set_footer(text = "Check @Dota2HelperBot on Twitter for development news and updates")

		try:
			await self.bot.say(embed = emb)
		except discord.HTTPException:
			await self.bot.say("I require the \"Embed Links\" permission first.")

def setup(bot):
	general = General(bot)
	bot.add_cog(general)
