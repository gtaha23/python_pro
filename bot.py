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

@bot.command(name='Taha')
async def gökhan(ctx):
    await ctx.send('Ooo kimler gelmiş! selam yazar!')

@bot.command()
async def katıldı(ctx, member: discord.Member):
    await ctx.send(f'{member.name} katıldı {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def yardim(ctx):
    await ctx.send('İşte beni çağırmak için kodlar: /selam, /heh, /Gökhan, /Taha, /katıldı(katıldığı tarihi öğrenmek için onun ismini yaz), /Gt_Bot, /Malike(anneme özel kod), /emoji(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,PY,PRO,CAT,BJK), /sifre(rastgele şifre oluşturur), /depo, /sağol, /milliyetçi, /yakala, /tay, /yapımcı, /mem, /mem_nadirlik, /ördek, /kedi, /köpek, /tilki, /bovcx, /santıranç, /babapiro, /bruv, /Benzema, /tarih, /ters_masa, /ben_bilmem, /csgo, /mercan, /iletişim, /git, /tek_sayilar, /masayi_duzenle, /espri, /espri_nadirlik, /bilgi, /yazılım_dili, /Discord, /don_pollo, /tl, /alman_kedy, /kurallar, /komut_sayisi, /youtube, /destek, /kodland, /client, /basic, /tester, /depoyardım, /cift_sayilar, /diğerbotlar, /uzun_kelime, /guncellemeler, /takipçi_sayisi, /RobotTom, /Bot, /GitHub, /pi, /sike, /kod_uygulama, /discord_yenilikleri, /discord_sunucu, /yazılım, /tokat, /kurucu, /blackbox, /w, /python, /html, /a(C++ için), /C, /B, /D, /E, /b(C# için), /Ruby, /BASIC, /CSS, /CaseOh, /KinitoPet, /emojikitchen, /git_saver ve /yardim')

@bot.command()
async def tester(ctx):
    await ctx.send("Bu botun tester'ı olmak için gokhan2308 adlı hesap ile iletişime geçebilirsiniz.")

@bot.command(name='Gt_Bot')
async def robot(ctx):
    await ctx.send('Bu bot havalıya benziyor.')

@bot.command()
async def bilgi(ctx):
    await ctx.send("Bu bot Gökhan Taha AĞPINAR tarafından Kodland'ın Python pro kursu ve yazılımcılıkta bir başlangıç için yapılmıştır.")

@bot.command(name='Malike')
async def annem(ctx):
    await ctx.send('Çok güzel bir isim! acaba kim.')

@bot.command(name = 'Gökhan')
async def baba(ctx):
    await ctx.send("Ne ara kahraman isimlerini saymaya başladık?")

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
async def emoji21(ctx):
    await ctx.send("\U0001F493")

@bot.command()
async def emoji22(ctx):
    await ctx.send("\U0001F460")

@bot.command()
async def emoji23(ctx):
    await ctx.send("\U0001F687")

@bot.command()
async def emoji24(ctx):
    await ctx.send("\U0001F479")

@bot.command()
async def emoji25(ctx):
    await ctx.send("\U0001F987")

@bot.command()
async def emojiPY(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/1139439539224580116.webp?size=128&quality=lossless")

@bot.command()
async def emojiPRO(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/1139490575377235998.webp?size=128&quality=lossless")

@bot.command()
async def emojiCAT(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/1215757648927129701.webp?size=128&quality=lossless")

@bot.command()
async def emojiBJK(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/1216744301451804742.webp?size=128&quality=lossless")

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

@bot.command(name = "GitHub")
async def gh(ctx):
    await ctx.send("GitHub insanların yazılım dili kodlarını paylaşıp yazılımlar hakkında bilgi edindiği bir platformdur.")

@bot.command()
async def ben_bilmem(ctx):
    await ctx.send("¯\_(ツ)_/¯")

@bot.command(name = "Bot")
async def robot(ctx):
    await ctx.send("Botlar discord'da kullanıcılara asistanlık ve yardım etmek için oluşturuldu. Python diliyle bir bot yazabilirsiniz!")

@bot.command()
async def csgo(ctx):
    await ctx.send("⚔️Super muper vor geym yeaa")

@bot.command()
async def yazılım(ctx):
    await ctx.send("Bazı yazılım dilleri: Python,C++,C#,C,Java,JavaScript,BASIC,Ruby,HTML,CSS,...")

@bot.command()
async def html(ctx):
    await ctx.send("HTML yazılım dili web sayfalarını oluşturmak için kullanılan standart metin işaretleme dilidir. Dilin son sürümü HTML5'tir. HTML, bir programlama dili olarak tanımlanamaz. Zira HTML kodlarıyla kendi başına çalışan bir program yazılamaz.")

@bot.command()
async def git_saver(ctx):
    await ctx.send("Git bir yazılım dosyamızı github hesabımızdaki ddepoya otomatik olarak kaydeden uygulamadır.")

@bot.command()
async def yazarın_site(ctx):
    await ctx.send("gtaha'nın şuanlık sadece bir tane local web sitesi vardır ve bu sitenin html kodlarını buradan bulabilirsiniz: https://github.com/gtaha23/Kodland-HTML-web/tree/main")

@bot.command()
async def CaseOh(ctx):
    await ctx.send("Sakin dostum... tüm pizzalar senin olabilir sakin!")

@bot.command()
async def KinitoPet(ctx):
    await ctx.send("Beni affeder misin?.... arkadaşım.... (kapanır)")

@bot.command()
async def python(ctx):
    await ctx.send("Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli yüksek seviyeli bir programlama dilidir. Girintilere dayalı basit söz dizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır.")

a = "C++"
@bot.command()
async def a(ctx):
    await ctx.send("C++, Bell Laboratuvarlarından Bjarne Stroustrup tarafından 1979 yılından itibaren geliştirilmeye başlanmış, C'yi kapsayan ve çok paradigmalı, yaygın olarak kullanılan, genel amaçlı bir programlama dilidir.")

@bot.command()
async def C(ctx):
    await ctx.send("C programlama dili, UNIX işletim sistemini geliştirmek için B dili kullanılarak üretilen bir programlama dilidir.")

@bot.command()
async def B(ctx):
    await ctx.send("B programlama dili Ken Thompson ve Dennis Ritchie tarafından takriben 1969 yılında geliştirilmiş bir programlama dilidir.")

@bot.command()
async def D(ctx):
    await ctx.send("D programlama dili, C++ dilinden daha yüksek seviyede ve hedef alınan işletim sistemiyle donanımlara göre uygulama yazılmasını kolaylaştıran bir sistem ve uygulama dilidir.")

@bot.command()
async def E(ctx):
    await ctx.send("E, Mark S. Miller, Dan Bornstein, Douglas Crockford, Chip Morningstar ve Electric Communities'teki diğerleri tarafından 1997'de oluşturulmuş, güvenli dağıtılmış bilgi işlem için nesne yönelimli bir programlama dilidir.")

b = "C#"
@bot.command()
async def b(ctx):
    await ctx.send("C#; Microsoft tarafından .NET Teknolojisi için geliştirilen modern bir programlama dilidir. Sözdizimi C-like bir deneyim sunar. Microsoft tarafından geliştirilmiş olsa da ECMA ve ISO standartları altına alınmıştır. C programlama dilinde bir tam sayı değişkeni 1 artırmak için değişkenden sonra ++ eki kullanılır.")

@bot.command()
async def Ruby(ctx):
    await ctx.send("Ruby, nesneye yönelik, dinamik, reflektif ve esnek bir programlama dilidir. Ruby dili, Yukihiro Matsumoto tarafından Japonya'da tasarlanmaya ve geliştirilmeye başlanmıştır.")

@bot.command()
async def BASIC(ctx):
    await ctx.send("BASIC 1964'te John George Kemeny ve Thomas Eugene Kurtz tarafından New Hampshire, ABD'de icat edilmiş, günümüzde de çeşitli türevleri kullanılmakta olan yüksek düzey bir programlama dili. Farklı türevleri birçok işletim sisteminin parçası olarak sunulmuştur. BASIC öğrenmesi ve yazılımları kolay olan bir dildir.")

@bot.command()
async def CSS(ctx):
    await ctx.send("Cascading Style Sheets, HTML'e ek olarak metin ve format biçimlendirme alanında fazladan olanaklar sunan bir işaretleme dilidir.")

@bot.command()
async def mercan(ctx):
    await ctx.send("Mercan! abisinin tatlış kedisi, nasılsın?")

@bot.command()
async def diğerbotlar(ctx):
    await ctx.send("Diğer botlar @Momoşko ve @Araştırmabot'dur ve şuanda @Araştırmabot üzerinde çalışılıyor.")

@bot.command()
async def iletişim(ctx):
    await ctx.send("iletişim için gokhantahagpinar@gmail.com'a mail gönderebilirsiniz.")

@bot.command()
async def kurallar(ctx):
    await ctx.send("Kurallar: 1.Saygılı olun 2.Botu boşyere kullanmayın 3.Yazılımcı olmak için botunuzu kurucuya gösterin 4.Botu geliştirmek için fikirlerinizi lütfen söyleyin")

@bot.command()
async def w(ctx):
    await ctx.send("https://tenor.com/view/gigachad-chad-gif-20773266")


@bot.command()
async def komut_sayisi(ctx):
    await ctx.send("Şuanda 91 komut vardır.(İlerideki hedef 95)")

@bot.command()
async def pi(ctx):
    await ctx.send("İlk 1000 basamağı: 3,1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 2164201989")

@bot.command()
async def guncellemeler(ctx):
    await ctx.send("En son güncelleme: 5 tane emoji ve /git_saver komutu eklendi 🥳 ve komut sayısı 91 oldu 📢.")
 
@bot.command()
async def discord_yenilikleri(ctx):
    await ctx.send("Discord sunucumuzdaki yenilikler: 5 tane yeni emoji ve /git_saver komutları geldi ve /yardım diyerek bunları görebiliriz!")

@bot.command()
async def discord_sunucu(ctx):
    await ctx.send("İşte Gt_Bot™'nin sunucusu! : https://discord.gg/Zewtmpwu")

@bot.command()
async def kurucu(ctx):
    await ctx.send("Kurucu: @gokhan2308")

@bot.command()
async def tokat(ctx, member: discord.Member):
    await ctx.send(f'{member.name} tokatlandı ')

@bot.command()
async def git(ctx):
    await ctx.send("Peki nere gideem?")

@bot.command()
async def uzun_kelime(ctx):
    await ctx.send("'Çekoslovakyalalılaştıramadıklarımızdanmısınız' kelimesi en uzun kelimedir.") 

@bot.command()
async def kod_uygulama(ctx):
    await ctx.send("Yazarımın kullandığı uygulama: Microsoft Visual Studio Code (VS Code)")

@bot.command()
async def tek_sayilar(ctx):
    await ctx.send("Tek sayılar: 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,...")

@bot.command()
async def cift_sayilar(ctx):
    await ctx.send("Çift sayılar: 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,...")

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
async def youtube(ctx):
    await ctx.send("https://www.youtube.com/channel/UCQe6Kt2hyfFhaDL3lhwM9PQ kanalı bu botun sahibinindir")

@bot.command()
async def destek(ctx):
    await ctx.send("https://www.youtube.com/channel/UCQe6Kt2hyfFhaDL3lhwM9PQ ve https://github.com/gtaha23 hesaplarını takip ederek bize destek edebilirsiniz.")
 
@bot.command()
async def blackbox(ctx):
    await ctx.send("Blackbox AI bir yazılım yapay zekadır ve size kod yazmada yardım eder. Bu botta birkaç deneme yapıldı 😅")

@bot.command()
async def RobotTom(ctx):
    await ctx.send("https://hub.kodland.org/en/project/226311")

@bot.command(name = "Discord")
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
async def sike(ctx):
    await ctx.send("https://media.discordapp.net/attachments/756505124293312524/1137832647809302598/sike.gif?ex=660081bb&is=65ee0cbb&hm=e6b640725aefeec0fe02e55da066751c0c3c389fa7514e5cd6c6ae1ed7e36040&")

@bot.command()
async def kodland(ctx):
    await ctx.send("https://media.discordapp.net/attachments/1188018611252629554/1188018611428802590/k_2.gif?ex=65fe830d&is=65ec0e0d&hm=2712d9d8137b8e5715ac55a65023baaa44607f9d7ae77cf7817af549141091c6&")

@bot.command()
async def depo(ctx):
    await ctx.send("https://github.com/gtaha23/python_pro bağlantısı sizi depoya yölendirebilir!")

@bot.command()
async def yapımcı(ctx):
    await ctx.send("https://github.com/gtaha23/gtaha23/blob/main/README.md bağlantısı sizi Yapımcıya yölendirebilir!")

@bot.command()
async def depoyardım(ctx):
    await ctx.send("https://github.com/gtaha23/python_pro/blob/main/README.md işinizi görecektir.")

@bot.command()
async def sağol(ctx):
    await ctx.send("Size hizmet etmek bir zevkti!")

@bot.command()
async def takipçi_sayisi(ctx):
    await ctx.send("Yapımcının takipçi sayısı: 0")

@bot.command()
async def client(ctx):
    await ctx.send("Client sınıfı basit bir discord botu oluşturmak için idealdir")

@bot.command()
async def emojikitchen(ctx):
    await ctx.send("https://www.google.com/search?client=opera&q=emoji+kitchen&sourceid=opera&ie=UTF-8&oe=UTF-8")

@bot.command()
async def basic(ctx):
    await ctx.send("Python basic: python yazılım dilinde basit işler yapmak için bir kurstur( oyun yapabilirsiniz :) )")

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
