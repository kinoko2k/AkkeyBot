import discord
import json

def words_check(data, gid):
	for json_gid in data:
		if str(gid) == json_gid:
			return True
	return False

ConfigOpen = open("config.json", "r", encoding="utf-8")
ConfigLoad = json.load(ConfigOpen)
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
	version = ConfigLoad["version"]
	print("Bot has been launch")
	print(f"Bot version is {version}")

@client.event
async def on_message(message):
	if message.author.bot:
		return
	with open("words.json", "r", encoding="utf-8") as f:
		words_load = json.load(f)
	guild = client.get_guild(message.guild.id)
	guild_id = guild.id
	response = words_check(data=words_load, gid=guild_id)
	if response == True:
		for word in words_load[str(guild_id)]:
			if word in message.content:
				await message.delete()
				await message.channel.send(f"<@{message.author.id}>\nNGWordに設定されているキーワードです。")
				return
	else:
		return

token = ConfigLoad["token"]
client.run(token)
