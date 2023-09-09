import secrets_1
from twitchio.ext import commands

from commandos.comandos import comandos, hola, abrazo, decir, odio

class ChatReader(commands.Bot):

    def __init__(self, chat_window=None, tts_active=None):
        super().__init__(
            token=secrets_1.irc_token,
            prefix='!',
            initial_channels=['pythonesa']
        )

        self.chat_window = chat_window
        self.tts_active = tts_active
        
        self.add_command(comandos)
        self.add_command(hola)
        self.add_command(abrazo)
        self.add_command(decir)
        self.add_command(odio)
    
    async def event_ready(self):
        print(f"Bot has connected to Twitch as {self.nick}")
