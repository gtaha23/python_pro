import discord
import os
import requests
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def yardim(ctx):
    await ctx.send("İşte beni çağırmak için kodlar: ?tehlikeli_atik, ?cevre_dostu, ?en_yuksek, ?en_dusuk, ?tarih, ?cevre, ?yenilenemez, ?hava_kirliligi, ?toprak_kirliligi, ?isik_kirliligi, ?gurultu_kirliligi, ?goruntu_kirliligi, ?cevre_cesitleri ve ?yardim")

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
async def en_dusuk(ctx):
    await ctx.send("En düşük ülkeler ise yüzde 3 ile Sırbistan ve yüzde 5,2 ile Romanya'da.")

@bot.command()
async def tarih(ctx):
    await ctx.send("Bu bot bir araştırma için Gökhan Taha AĞPINAR tarafından 13.03.2024 tarihinde oluşturulmuştur.")

@bot.command()
async def yenilenebilir(ctx):
    await ctx.send("Yenilenebilir enerji kaynakları: Jeotermal, Rüzgar enerjisi, Güneş enerjisi, Hidroelektrik, Biokütle, Biogaz,...")

@bot.command()
async def en_kirli(ctx):
    await ctx.send("Saraybosna Aralık ayında dünyanın havası en kirli şehirleri listesinin başında. IQAir verilerine göre, hava kirliliğinde Saraybosna'yı, Hindistan'ın Kalküta, Sırbistan'ın başkenti Belgrad, Bangladeş'in başkenti Dakka ve Pakistan'ın Lahor şehirleri izliyor.")

@bot.command()
async def yenilenemez(ctx):
    await ctx.send("Yenilenemez enerji kaynakları: Kömür, Doğalgaz, Petrol,...")

@bot.command()
async def hava_kirliligi(ctx):
    await ctx.send("Hava kirliliği, havanın doğal bileşiminin çeşitli nedenlerle değişmesi, havada katı, sıvı ve gaz şeklindeki yabancı maddelerin insan sağlığına, canlı hayatına, ekolojik dengeye ve eşyalara zararlı olabilecek derişim ve sürede bulunmasıdır.")

@bot.command()
async def toprak_kirliligi(ctx):
    await ctx.send("Toprak kirliliği, katı, sıvı ve radyoaktif artık ve kirleticiler tarafından toprağın fiziksel ve kimyasal özelliklerinin bozulmasıdır. Topraklarda meydana gelecek tüm olumsuz değişimler insan yaşamını kuvvetle etkileyecek güce sahiptir.")

@bot.command()
async def isik_kirliligi(ctx):
    await ctx.send("Işık kirliliği, ışığın canlıları rahatsız edecek şekilde yanlış kullanılmasıdır. Yanlış yönde, yanlış miktarda, yanlış yerde, aydınlatılması gerekmeyen yerde ışık kullanımı hem ekonomik kayıp hem de rahatsız edici bir durumdur.")

@bot.command()
async def gurultu_kirliligi(ctx):
    await ctx.send("Gürültü kirliliği veya diğer adıyla ses kirliliği, insan veya hayvan yaşamını olumsuz etkileyen, dengesini bozan her türlü insan, hayvan ya da makine kaynaklı ses oluşumudur.")

@bot.command()
async def goruntu_kirliligi(ctx):
    await ctx.send("Görüntü kirliliği, insan faaliyetleri ve çevresini tahrip etmesi ile oluşan çirkin görüntü ve düzensizlikleri ifade eder.")

@bot.command()
async def cevre_cesitleri(ctx):
    await ctx.send("Çevre kirliliği çeşitleri genel olarak; hava kirliliği, su kirliliği, toprak kirliliği, gürültü kirliliği ve görüntü kirliliği olarak sınıflandırılır.")

@bot.command()
async def cevre(ctx):
    arastirma = os.listdir("arastirma")
    arastirma = random.choice(arastirma)
    with open(f'arastirma/{arastirma}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("token")
