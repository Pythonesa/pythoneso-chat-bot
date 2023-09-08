import secrets_1
from twitchio.ext import commands

from comandos import comandos, hola, abrazo, decir

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
    
    async def event_ready(self):
        print(f"Bot has connected to Twitch as {self.nick}")

    async def event_message(self, message):
        author_name = message.author.name if message.author else "Usuario Desconocido"
        formatted_message = f"{author_name}: {message.content}\n"
        self.chat_window.insert(tk.END, formatted_message)
        self.chat_window.see(tk.END)
        await self.handle_commands(message)