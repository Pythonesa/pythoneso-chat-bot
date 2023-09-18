import os
def reproducir_sonido(sonido):
    
    filename = f"{sonido}.mp3"
    
    os.system(f"mpv commandos/mp3s/{filename}") 