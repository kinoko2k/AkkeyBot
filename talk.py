import nextcord
print("[StartUp]モジュール「nextcord」をインポートしました")
import yaml
print("[StartUP]モジュール「yaml」をインポートしました")

client = nextcord.Client()
with open("config.yml", "r") as file:
    config = yaml.load(file)
print("[StartUP]config.ymlをロードしました")

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
