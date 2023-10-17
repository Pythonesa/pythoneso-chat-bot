from twitchio.ext import commands
from commandos.hola import obtener_saludo
from commandos.tts import hablar
from commandos.abrazo import obtener_abrazo_nadie, obtener_abrazo_auto, obtener_abrazo
from commandos.odio import odio_sin_blanco, odio_dirigido, odio_auto
from commandos.alcohol import obtener_alcohol_solo, obtener_invitar_alcohol
from commandos.sonidos import reproducir_sonido

@commands.command(name='hola')
async def hola(ctx):
    saludo = obtener_saludo(ctx.author.name)
    await ctx.send(saludo)
        
@commands.command(name="abrazo")
async def abrazo(ctx, *, nick: str = None):
    if not nick:
        await ctx.send(obtener_abrazo_nadie(ctx.author.name))
        return
    elif nick.lower() == ctx.author.name.lower():
        await ctx.send(obtener_abrazo_auto(ctx.author.name))
    else:
        await ctx.send(obtener_abrazo(ctx.author.name, nick))
        
        
#Comando sugerido por DHardySD
@commands.command(name="odio")
async def odio(ctx, *, nick: str = None):
    if not nick:
        await ctx.send(odio_sin_blanco(ctx.author.name))
        return
    elif nick.lower() == ctx.author.name.lower():
        await ctx.send(odio_auto(ctx.author.name))
    else:
        await ctx.send(odio_dirigido(ctx.author.name, nick))
        
        
@commands.command(name='alcohol')
async def alcohol(ctx, *, nick: str = None):
    if not nick or nick.lower() == ctx.author.name.lower():
        await ctx.send(obtener_alcohol_solo(ctx.author.name))
    else:
        await ctx.send(obtener_invitar_alcohol(ctx.author.name, nick))


@commands.command(name='youtube')
async def youtube(ctx):
    await ctx.send(f"Mira las clases grabadas: https://www.youtube.com/@pythonesa")
    

@commands.command(name='github')
async def github(ctx):
    await ctx.send(f"Mirá los ejercicios y código de las clases además de otros proyectos en el repo de GitHub: https://github.com/Pythonesa")
    

@commands.command(name='redes')
async def redes(ctx):
    await ctx.send(f"Únete a la comunidad de discord: https://discord.gg/QkBvKDKHSw =================== Mira las clases grabadas: https://www.youtube.com/@pythonesa =================== Síganla en twitter: https://twitter.com/pythonesamar y también en facebook: https://www.facebook.com/pythonesa")
    
    
@commands.command(name='discord')
async def discord(ctx):
    await ctx.send(f"Unete a la comunidad de discord: https://discord.gg/QkBvKDKHSw")
    
    
@commands.command(name='streams')
async def streams(ctx):
    await ctx.send(f"Martes y Jueves hacemos streams con Python y los viernes con Java. Podés ver los horarios en la agenda de Twitch.")
    
@commands.command(name='decir')
async def decir(ctx, *, texto: str = None):
    if not texto:
        await ctx.send(f"{ctx.author.name}, ¿no sabes que decir? ¡Intentalo de nuevo!")
        return
    txt = f"{ctx.author.name} dice {texto}"
    if ctx.bot.tts_active.get():
        hablar(txt)
    else:
        await ctx.send(f"TTS desactivado: {txt}")
        

@commands.command(name='latigo')
async def latigo(ctx):
    if ctx.bot.reproducir_sonidos.get():
        reproducir_sonido("latigo")
    
@commands.command(name='comandos')
async def comandos(ctx):
    await ctx.send(f"Comandos disponibles: !hola !abrazo !decir !odio !youtube !github !redes !discord !streams !alcohol !latigo")