import discord
from discord.ext import commands

import random

import yeni

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def selam(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def gökhan(ctx):
    await ctx.send("Ooo kimler gelmiş! selam yazar!")

@bot.command()
async def katıldı(ctx, member: discord.Member):
    await ctx.send(f'{member.name} katıldı {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def yardım(ctx):
    await ctx.send('İşte beni çağırmak için kodlar: /selam , /heh , /gökhan , /katıldı(katıldığı tarihi öğrenmek için onun ismini yaz) , /Gt_Bot , /Malike(anneme özel kod) , /emoji(1,2,3,4,5,6,7,8,9,10) , /sifre(rastgele şifre oluşturur) , /depo , /sağol /milliyetçi , /yakala , /tay , /yapımcı ve /yardım ')

@bot.command(name='Gt_Bot')
async def robot(ctx):
    await ctx.send('Bu bot havalıya benziyor.')

@bot.command(name='Malike')
async def annem(ctx):
    await ctx.send('Çok güzel bir isim! acaba kim.')

@bot.command()
async def emoji1(ctx):
    await ctx.send("\U0001f600")

@bot.command()
async def emoji2(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def emoji3(ctx):
    await ctx.send("\U0001F606")

@bot.command()
async def emoji4(ctx):
    await ctx.send("\U0001F923")

@bot.command()
async def emoji5(ctx):
    await ctx.send("\U0001F945")

@bot.command()
async def emoji6(ctx):
    await ctx.send("\U0001f756")

@bot.command()
async def emoji7(ctx):
    await ctx.send("\U0001f875")

@bot.command()
async def emoji8(ctx):
    await ctx.send("\U0001f985")

@bot.command()
async def emoji9(ctx):
    await ctx.send("\U0001f578")

@bot.command()
async def emoji10(ctx):
    await ctx.send("\U0001f786")    

@bot.command()
async def mem1(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1209932750581399685/1214958213795942410/Kod_memes.png?ex=65fb0103&is=65e88c03&hm=b698c27c218f0e233bc02a1b6560a90248482b79621c98045dcfa6c64abec75f&")

@bot.command()
async def mem2(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1209932750581399685/1214960216458928139/Kod_memes2.png?ex=65fb02e0&is=65e88de0&hm=e97a524e2cc850a91bbe7fbe195b3f331c92983c1801570447294d86915d9272&")

@bot.command()
async def mem3(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1209932750581399685/1214962112758026312/Kod_memes3.png?ex=65fb04a4&is=65e88fa4&hm=f0a4977b11fc21a8ff805fe7bb5703f6e456c0003bbce701b8c27873f06785fd&")
    
@bot.command()
async def sifre(ctx):
    await ctx.send(yeni.gen_pass(10))

@bot.command()
async def depo(ctx):
    await ctx.send("https://github.com/gtaha23/python_pro bağlantısı sizi depoya yölendirebilir!")

@bot.command()
async def yapımcı(ctx):
    await ctx.send("https://github.com/gtaha23/gtaha23/blob/main/README.md bağlantısı sizi Yapımcıya yölendirebilir!")

@bot.command()
async def sağol(ctx):
    await ctx.send("Size hizmet etmek bir zevkti!")

@bot.command()
async def mamaci(ctx):
    await ctx.send("Demek gizli kodu buldun! aramıza hoşgeldin.")

@bot.command()
async def milliyetçi(ctx):
    await ctx.send("Yaşasın ırkımız, Çin'e bedel kırkımız, Söylenir türkümüz dağlarda dağlara ")   

@bot.command()
async def yakala(ctx, count_yakala = 5):
    await ctx.send("Yakala chat" * count_yakala)

@bot.command()
async def tay(ctx):
    await ctx.send("İşte efsane 2021 üçlüsü: Taha, Ahmet, Yavuz")

@bot.command()
async def babapiro(ctx):
    await ctx.send("Uyyy birowl sıtar bir nümara")

@bot.command()
async def bruv(ctx):
    await ctx.send("Oi bruv can ı get a bo'o o'wa'er")

@bot.command()
async def hamster(ctx):
    await ctx.send("Hamstır şit o yeee")

@bot.command()
async def Bjk(ctx):
    await ctx.send("ÇARŞI 1903 OOO BJK HEY HEY HEY")

bot.run("token")
