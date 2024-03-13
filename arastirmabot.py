import discord
import os
import requests
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def tehlikeli_atik(ctx):
    await ctx.send("Tehlikeli atıkların bertaraf işlemleri; yakma, kuyuya boşaltma, suya boşaltma, arazi bertarafı ve yeraltı bertarafı olarak ifade edilebilmektedir.")

@bot.command()
async def cevre_dostu(ctx):
    await ctx.send("Çevre Dostu uygulamalar ve atık azaltımı: 1.Alışverişlerinizi planlayın. 2.Dondurucunuzu kullanın. 3.Bir kompost cihazı kullanın. 4.Evde yeşillik yetiştirin.5.Kabukları saklayın. 6.Yiyeceklerinizin raf ömrünü uzatın. 7.Plastik atığını ve ambalajları azaltın. 8.Dökme, toptan ve donmuş ürünler alın.")

@bot.command()
async def en_yuksek(ctx):
    await ctx.send("Geri dönüşümün en yüksek olduğu ülke ise yüzde 83,2 ile İtalya.")

@bot.command()
async def en_yuksek(ctx):
    await ctx.send("En düşük ülkeler ise yüzde 3 ile Sırbistan ve yüzde 5,2 ile Romanya'da.")

@bot.command()
async def cevre(ctx):
    arastirma = os.listdir("arastirma")
    arastirma = random.choice(arastirma)
    with open(f'arastirma/{arastirma}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("token")
