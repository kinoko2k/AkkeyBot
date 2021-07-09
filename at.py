# -*- coding: utf-8 -*-

import discord
import requests
import json

client = discord.Client()

def token_check(token):
	api_url = "https://discord.com/api/v6/auth/login"
	header = {"Authorization": token}
	response = requests.get(api_url, headers=header)
	if response.status_code == 200:
		return True
	else:
		return False

ConfigOpen = open("config.json", "r",  encoding="utf-8")
ConfigLoad = json.load(ConfigOpen)

@client.event
async def on_message(message):
	if message.author.bot:
		return
	token_message = message.content
	try:
		response = token_check(token_message)
	except UnicodeEncodeError:
		return
	if response == True:
		await message.delete()
		await message.channel.send(f"<@{message.author.id}>\n有効なTokenのみが書かれたメッセージだったため削除しました。\nTokenを送るには文章を含める必要があります。")
	elif response == False:
		return

login_token = ConfigLoad["token"]
client.run(login_token)
