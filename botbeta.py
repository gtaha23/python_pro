import discord

import random

import sifreci

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)
    
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

    elif message.content.startswith('$emoji1'):
        await message.channel.send("\U0001f600")
    elif message.content.startswith('$emoji2'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$emoji3'):
        await message.channel.send("\U0001F606")
    elif message.content.startswith('$emoji4'):
        await message.channel.send("\U0001F923")
    elif message.content.startswith('$emoji5'):
        await message.channel.send("\U0001f875")
    elif message.content.startswith("$emoji6"):
        await message.channel.send("\U0001F835")

    elif message.content.startswith("$görüşürüz"):
        await message.channel.send("Görüşürüz!")

    elif message.content.startswith("$gokhan2308"):
        await message.channel.send("Nasılsın yazar!")

    elif message.content.startswith("$yardım"):
        await message.channel.send("İşte kodlarım: $merhaba, $nasılsın, $bende iyiyim, $emoji(1,2,3,4,5,6), $görüşürüz, $gokhan2308,$şifre, $yardım")

    elif message.content.startswith("$şifre"):
        await message.channel.send(sifreci.gen_pass(10))

    else:
        await message.channel.send("Lütfen tekrarlar mısınız, sistemim algılayamadı")

client.run("token")
