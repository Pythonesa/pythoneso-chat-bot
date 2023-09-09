from twitchio.ext import commands
from commandos.hola import obtener_saludo
from commandos.tts import hablar

@commands.command(name='hola')
async def hola(ctx):
    saludo = obtener_saludo(ctx.author.name)
    await ctx.send(saludo)
        
@commands.command(name="abrazo")
async def abrazo(ctx, *, nick: str = None):
    if not nick:
        await ctx.send("No puedes abrazar al aire, ¿lo sabes verdad?")
        return
    elif nick.lower() == ctx.author.name.lower():
        await ctx.send(f"Eh, no lo sé {ctx.author.name}, es raro que te abrazes a ti mism@, ¿estás bien?")
    else:
        await ctx.send(f"¡{ctx.author.name} abraza a {nick}!")
    
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