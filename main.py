from rtmbot import RtmBot
from secret import SLACK_TOKEN
from rtmbot.core import Plugin

class HelloPlugin(Plugin):
    def process_message(self, data):
        if "?" in data["text"]:
            self.outputs.append([data["channel"], "Hello, World!"])

config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}

bot = RtmBot(config)
bot.start()
