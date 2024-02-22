import discord

import random

import yeni

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")

    elif message.content.startswith('$nasılsın'):
        await message.channel.send("İyiyim! sen?") 

    elif message.content.startswith('$bende iyiyim'):
        await message.channel.send("Harika!")    

    elif message.content.startswith("$bye"):
        await message.channel.send("Görüşürüz!")

    elif message.content.startswith("gokhan2308"):
        await message.channel.send("Nasılsın yazar!")
    
    elif message.content.startswith("alper"):
        await message.channel.send(yeni.gen_pass(10))

    else:
        await message.channel.send("Lütfen tekrarlar mısınız, sistemim algılayamadı)")

    client.run("TOKEN")
