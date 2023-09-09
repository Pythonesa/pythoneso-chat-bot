from twitchio.ext import commands
from commandos.hola import obtener_saludo
from commandos.tts import hablar
from commandos.abrazo import obtener_abrazo_nadie, obtener_abrazo_auto, obtener_abrazo
from commandos.odio import odio_sin_blanco, odio_dirigido, odio_auto

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
    
@commands.command(name='comandos')
async def comandos(ctx):
    await ctx.send(f"Comandos disponibles: !hola  !abrazo  !decir")