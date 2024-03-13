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
    if count_heh > 1000:
        await ctx.send("Discordunu çökertmemimi istiyorsun?")
    else:    
        await ctx.send("he" * count_heh)

@bot.command(name='Gökhan')
async def gökhan(ctx):
    await ctx.send('Ooo kimler gelmiş! selam yazar!')

@bot.command()
async def katıldı(ctx, member: discord.Member):
    await ctx.send(f'{member.name} katıldı {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def yardım(ctx):
    await ctx.send('İşte beni çağırmak için kodlar: /selam, /heh, /Gökhan, /katıldı(katıldığı tarihi öğrenmek için onun ismini yaz), /Gt_Bot, /Malike(anneme özel kod), /emoji(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20), /sifre(rastgele şifre oluşturur), /depo, /sağol, /milliyetçi, /yakala, /tay, /yapımcı, /mem, /mem_nadirlik, /ördek, /kedi, /köpek, /tilki, /bovcx, /santıranç, /babapiro, /bruv, /Benzema, /tarih, /ters_masa, /ben_bilmem, /csgo, /mercan, /iletişim, /git, /tek_sayilar, /masayi_duzenle, /espri, /espri_nadirlik, /fenerasyon, /yazılım_dili, /dc, /don_pollo, /tl, /alman_kedy ve /yardım')

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
async def emoji11(ctx):
    await ctx.send("\U0001f362")

@bot.command()
async def emoji12(ctx):
    await ctx.send("\U0001f999")

@bot.command()
async def emoji13(ctx):
    await ctx.send("\U0001f687")

@bot.command()
async def emoji14(ctx):
    await ctx.send("\U0001F463")

@bot.command()
async def emoji15(ctx):
    await ctx.send("\U0001F364")

@bot.command()
async def emoji16(ctx):
    await ctx.send("\U0001F643")

@bot.command()
async def emoji17(ctx):
    await ctx.send("\U0001F227")

@bot.command()
async def emoji18(ctx):
    await ctx.send("\U0001F666")

@bot.command()
async def emoji19(ctx):
    await ctx.send("\U0001F256")   

@bot.command()
async def emoji20(ctx):
    await ctx.send("\U0001F435") 

@bot.command()
async def mem(ctx):
    resimler = os.listdir("resimler")
    resim = random.choice(resimler)
    with open(f'resimler/{resim}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def espri(ctx):
    espriler = os.listdir("espriler")
    espri = random.choice(espriler)
    with open(f'espriler/{espri}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def espri_nadirlik(ctx):
    await ctx.send("espri4: En yaygın espri3: Yaygın espri1: Nadir espri3: Çok Nadir")

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
async def ters_masa(ctx):
    await ctx.send("(╯°□°）╯︵ ┻━┻")

@bot.command()
async def ben_bilmem(ctx):
    await ctx.send("¯\_(ツ)_/¯")

@bot.command()
async def csgo(ctx):
    await ctx.send("⚔️Super muper vor geym yeaa")

@bot.command()
async def mercan(ctx):
    await ctx.send("Mercan! abisinin tatlış kedisi, nasılsın?")

@bot.command()
async def iletişim(ctx):
    await ctx.send("iletişim için gokhantahagpinar@gmail.com'a mail gönderebilirsiniz.")

@bot.command()
async def git(ctx):
    await ctx.send("Peki nere gideem?")

@bot.command()
async def tek_sayilar(ctx):
    await ctx.send("Tek sayilar: 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,...")

@bot.command()
async def masayi_duzenle(ctx):
    await ctx.send("┳━┳ ノ( ゜-゜ノ)")

@bot.command()
async def baldiback(ctx):
    await ctx.send("https://tenor.com/view/swedish-gif-18685828")

@bot.command()
async def yazılım_dili(ctx):
    await ctx.send("Bu bot Python yazılım dili kullanılarak yapılmıştır.")

@bot.command()
async def dc(ctx):
    await ctx.send("Discord'a hoşgeldin ben Gt_Bot!")

@bot.command()
async def don_pollo(ctx):
    await ctx.send("EL QUE QUEIRA PERDE SO TİEMPO QE ENTRA YA A Mİ PERFİL ")

@bot.command()
async def tl(ctx):
    await ctx.send("https://tenor.com/view/dolar-dolartlyekarsienflasyon-gif-18543428")

@bot.command()
async def alman_kedy(ctx):
    await ctx.send("https://tenor.com/view/bingus-gunner-german-bunker-shooting-gif-20956445")

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

@bot.command()
async def tarih(ctx):
    await ctx.send("Bu bot 21 Şubat 2024 tarihinde Gökhan Taha AĞPINAR tarafından oluşturuldu.")  

bot.run("token")
