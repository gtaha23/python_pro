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
    await ctx.send('İşte beni çağırmak için kodlar: /selam , /heh , /gökhan , /katıldı(katıldığı tarihi öğrenmek için onun ismini yaz) , /Gt_Bot , /Malike(anneme özel kod) , /emoji(1,2,3,4) , /sifre(rastgele şifre oluşturur) , /depo , /sağol ve /yardım ')

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
async def sifre(ctx):
    await ctx.send(yeni.gen_pass(10))

@bot.command()
async def depo(ctx):
    await ctx.send("https://github.com/gtaha23/python_pro/blob/main/bot.py bağlantısı sizi depoya yölendirebilir!")

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

bot.run("token")
