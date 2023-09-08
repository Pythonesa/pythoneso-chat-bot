import tkinter as tk
from pythoneso import ChatReader
import threading
import asyncio

class ChatReaderWithGUI(ChatReader):
    def __init__(self, chat_window, tts_active, *args, **kwargs):
        super().__init__(chat_window=chat_window, tts_active=tts_active, *args, **kwargs)

    async def event_message(self, message):
        author_name = message.author.name if message.author else "pythoneso"
        formatted_message = f"{author_name}: {message.content}\n"
        self.chat_window.insert(tk.END, formatted_message)
        self.chat_window.see(tk.END)
        await self.handle_commands(message)


def start_bot(chat_window, tts_active_var):
    global reader
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    reader = ChatReaderWithGUI(chat_window, tts_active=tts_active_var)
    loop.run_until_complete(reader.run())

def main():
    
    root = tk.Tk()
    root.title("Pythoneso Chat Bot")
    root.configure(bg="#1a1a1a")
    
    tts_active = tk.BooleanVar(value=True)

    def update_tts_state(*args):
        global reader
        reader.tts_active.set(tts_active.get())

    tts_active.trace_add("write", update_tts_state)

    checkbox_tts = tk.Checkbutton(root, text="TTS", variable=tts_active, bg="#1a1a1a", fg="#7f7f7f", activebackground="#1a1a1a", activeforeground="#7f7f7f")
    checkbox_tts.pack(anchor=tk.W, padx=10, pady=5)
    
    chat_window = tk.Text(root, bg="#1a1a1a", fg="#e0e0e0", font=("Hack", 14))
    chat_window.pack(fill=tk.BOTH, expand=True)

    bot_thread = threading.Thread(target=start_bot, args=(chat_window, tts_active))
    bot_thread.start()

    def on_close():
        root.destroy()
        exit(0)  

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

if __name__ == "__main__":
    main()