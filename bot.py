import discord
from discord.ext import commands
import random
import sifreci
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def selam(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    if count_heh > 3000:
        await ctx.send("Discordunu çökertmemimi istiyorsun?")
    else:    
        await ctx.send("he" * count_heh)

@bot.command()
async def gökhan(ctx):
    await ctx.send("Ooo kimler gelmiş! selam yazar!")

@bot.command()
async def katıldı(ctx, member: discord.Member):
    await ctx.send(f'{member.name} katıldı {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def yardım(ctx):
    await ctx.send('İşte beni çağırmak için kodlar: /selam , /heh , /gökhan , /katıldı(katıldığı tarihi öğrenmek için onun ismini yaz) , /Gt_Bot , /Malike(anneme özel kod) , /emoji(1,2,3,4,5,6,7,8,9,10) , /sifre(rastgele şifre oluşturur) , /depo , /sağol /milliyetçi , /yakala , /tay , /yapımcı , /mem , /mem_nadirlik , /ördek , /kedi , /köpek , /tilki , /bovcx , /santıranç , /babapiro , /bruv , /Benzema ve /yardım ')

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
async def mem(ctx):
    resimler = os.listdir("resimler")
    resim = random.choice(resimler)
    with open(f'resimler/{resim}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem_nadirlik(ctx):
    await ctx.send("Kod memes3 nadirlik: En yaygın  Kod memes2 nadirlik: Yaygın  Kod memes nadirlik: Nadir  Kod memes4 nadirlik: Destansı  Kod memes5: Efsanevi Kod memes6:Çok nadir")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('ördek')
async def ördek(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def gelkedi():
    url = 'https://api.thecatapi.com/v1/images/search'
    res = requests.get(url)
    data = res.json()
    print(data)
    print(data[0])
    return data[0]["url"]


@bot.command()
async def kedi(ctx):
    image_url = gelkedi()
    await ctx.send(image_url)

def Dogs():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('köpek')
async def köpek(ctx):
    image_url = Dogs()
    await ctx.send(image_url)

def fox():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command('tilki')
async def tilki(ctx):
    image_url = fox()
    await ctx.send(image_url)

@bot.command()
async def sifre(ctx):
    await ctx.send(sifreci.gen_pass(10))

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

@bot.command()
async def Benzema(ctx):
    await ctx.send("15💀☠️💀")

@bot.command()
async def santıranç(ctx):
    await ctx.send("What the heeeeeeeeeell")

@bot.command()
async def bovcx(ctx):
    await ctx.send("O mey gat BOVCXXX")
    
bot.run("token")
