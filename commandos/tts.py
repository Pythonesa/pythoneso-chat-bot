from gtts import gTTS
import os

def hablar(texto):
    tts = gTTS(text=texto, lang='es', tld='com.co')
    filename = "audio.mp3"
    tts.save(filename)
    
    os.system(f"mpv {filename}")
    
    os.remove(filename)    