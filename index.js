const discord = require("discord.js")
const asyncio = require("asyncio")
const config = require("./config.json")
const client = new discord.Client()

client.on("ready", () => {
	console.log(`[StartUp]${config.version}で実行中`);
})

client.on("message", async message => {
	if(message.author.bot) {
		return;
	}
	if(message.content.match(/おは/)) {
		message.channel.send("おはよう...うちはもうちょっと寝てるわ...")
	}
	if(message.content.match(/おや/)) {
		message.channel.send("おやすみーあ、まだ起きてるから電機はそのままで...")
	}
	if(message.content.match(/@everyone/)) {
		message.channel.send("うるさいなぁ...今寝てたんだけど?")
	}
	if(message.content.match(/@here/)) {
		message.channel.send("ちょっとうるさい...やっと寝れそうだったのに...")
	}
	if(message.content.match(/http:/)) {
		message.reply("そのURLもしかしてhttp?\n接続保護されないから注意してね!")
	}
});

client.login(config.token)
