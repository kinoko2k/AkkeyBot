import discord
print("[StartUp]モジュール「discord」をインポートしました")
import json
print("[StartUP]モジュール「json」をインポートしました")

client = discord.Client()
with open("config.json", "r") as file:
    config = json.load(file)
print("[StartUP]config.jsonをロードしました")

@client.event
async def on_ready():
    version = config["version"]
    print("Bot has been launch")
    print(f"Bot version is {version}")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if "おは" in message.content:
        await message.channel.send("おはよう...うちはもうちょっと寝てるわ...")
        return
    elif "おや" in message.content:
        await message.channel.send("おやすみーあ、まだ起きてるから電機はそのままで...")
        return
    elif "@everyone" in message.content:
        await message.channel.send("うるさいなぁ...今寝てたんだけど?")
        return
    elif "@here" in message.content:
        await message.channel.send("ちょっとうるさい...やっと寝れそうだったのに...")
        return
    else:
        pass

client.run(config["token"])