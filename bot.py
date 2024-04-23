import discord
from discord.ext import commands
import random
import sifreci
import os
import requests
import time

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
    await ctx.send('İşte beni çağırmak için kodlar: /selam, /heh, /Gökhan, /Taha, /katıldı(katıldığı tarihi öğrenmek için onun ismini yaz), /Gt_Bot, /Malike(anneme özel kod), /emoji(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,PY,PRO,CAT,BJK), /sifre(rastgele şifre oluşturur), /depo, /sağol, /milliyetçi, /yakala, /tay, /yapımcı, /mem, /mem_nadirlik, /ördek, /kedi, /köpek, /tilki, /bovcx, /santıranç, /babapiro, /bruv, /Benzema, /tarih, /ters_masa, /ben_bilmem, /csgo, /mercan, /iletişim, /git, /tek_sayilar, /masayi_duzenle, /espri, /espri_nadirlik, /bilgi, /yazılım_dili, /Discord, /don_pollo, /tl, /alman_kedy, /kurallar, /komut_sayisi, /youtube, /destek, /kodland, /client, /basic, /tester, /depoyardım, /cift_sayilar, /diğerbotlar, /uzun_kelime, /guncellemeler, /takipçi_sayisi, /RobotTom, /Bot, /GitHub, /pi, /sike, /kod_uygulama, /discord_yenilikleri, /discord_sunucu, /yazılım, /tokat, /kurucu, /blackbox, /w, /python, /html, /a(C++ için), /C, /B, /D, /E, /b(C# için), /Ruby, /BASIC, /CSS, /CaseOh, /KinitoPet, /emojikitchen, /git_saver, /SQL, /Assembly, /php, /TS, /Rust, /Lua, /erlang, /MATHLAB, /Perl, /Julia, /Swift, /Go, /R, /ObjC, /Dart, /pes, /fifa, /JS, /Kotlin, /Fortran, /COBOL, /Pascal, /elixir, /Clojure, /Haskell, /OCaml, /c(F# için), /Scala, /Zig, /Lisp, /Prolog, /Nim, /Crystal, /Carbon, /ODIN, /V, /Oberon, /Eiffel, /Modula, /Ada, /PLI, /ALGOL, /Forth, /SmallTalk, /VBN, /Simula, /APL, /python_sunucu, /Eclipse, /Notepad, /Netbeans, /Apache_Tomcat, /Nginx, /sayılar, /jQuery, /Bootsrap, /PyGame, /hayal, /bildigim_yazılım, /arkadaş, /facts(2,3,4,5), /github_py, /bişey, /etkinlikler, /AmericanLife, /Scratch, /Shell, /popular_shells, /bash, /csh, /ksh, /tcsh, /zhs, /duolingo, /StarWars ve /yardim')

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
async def sayılar(ctx):
    for i in range(random.randint(1,10)):
        await ctx.send(random.randint(1,100))
        time.sleep(2)
        
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
async def emoji26(ctx):
    await ctx.send("\U0001F069")

@bot.command()
async def emoji27(ctx):
    await ctx.send("\U0001F001")

@bot.command()
async def emoji28(ctx):
    await ctx.send("\U0001F002")

@bot.command()
async def emoji29(ctx):
    await ctx.send("\U0001F003")

@bot.command()
async def emoji30(ctx):
    await ctx.send("\U0001F004")

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

@bot.command()
async def etkinlikler(ctx):
    await ctx.send("Etkinlikler: 13 Nisan, 27 Nisan etkinlikleri bulunmaktadır.")

@bot.command(name = "Bot")
async def robot(ctx):
    await ctx.send("Botlar discord'da kullanıcılara asistanlık ve yardım etmek için oluşturuldu. Python diliyle bir bot yazabilirsiniz!")

@bot.command()
async def csgo(ctx):
    await ctx.send("⚔️Super muper vor geym yeaa")

@bot.command()
async def yazılım(ctx):
    await ctx.send("Bazı yazılım dilleri: Python,C++,C#,C,Java,JavaScript,BASIC,Ruby,HTML,CSS,Shell,...")

@bot.command()
async def html(ctx):
    await ctx.send("HTML yazılım dili web sayfalarını oluşturmak için kullanılan standart metin işaretleme dilidir. Dilin son sürümü HTML5'tir. HTML, bir programlama dili olarak tanımlanamaz. Zira HTML kodlarıyla kendi başına çalışan bir program yazılamaz.")

@bot.command()
async def git_saver(ctx):
    await ctx.send("Git bir yazılım dosyamızı github hesabımızdaki ddepoya otomatik olarak kaydeden uygulamadır.")

@bot.command()
async def bildigim_yazılım(ctx):
    await ctx.send("Bu botun yazarının bildiği yazılım dilleri: Python, Lua, HTML, CSS, C. Merak edenler için Lua ve C dillerinde en basit kodları yazabiliyor (Eğitim eksikliğinden)")

@bot.command()
async def pes(ctx):
    await ctx.send("eFootball (PES)")

@bot.command()
async def fifa(ctx):
    await ctx.send("En iyisi FİFA 2017")

@bot.command()
async def yazarın_site(ctx):
    await ctx.send("gtaha'nın şuanlık sadece bir tane local web sitesi vardır ve bu sitenin html kodlarını buradan bulabilirsiniz: https://github.com/gtaha23/Kodland-HTML/tree/main")

@bot.command()
async def CaseOh(ctx):
    await ctx.send("Sakin dostum... tüm pizzalar senin olabilir sakin!")

@bot.command()
async def KinitoPet(ctx):
    await ctx.send("Beni affeder misin?.... arkadaşım.... (kapanır)")

@bot.command()
async def python(ctx):
    await ctx.send("Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli yüksek seviyeli bir programlama dilidir. Girintilere dayalı basit söz dizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır.")

@bot.command()
async def Java(ctx):
    await ctx.send("Java, Sun Microsystems tarafından üretilen ve yazılım uygulamaları geliştirmeye yardımcı yazılımlar bütünüdür. Java'nın kullanım alanı gömülü aygıtlardan cep telefonlarına, kurumsal sunuculardan süper bilgisayarlara uzanmaktadır.")

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
async def SQL(ctx):
    await ctx.send("SQL, verileri yönetmek ve tasarlamak için kullanılan bir dildir. SQL, kendi bir programlama dili olmamasına rağmen birçok kişi tarafından programlama dili olarak bilinir. SQL herhangi bir veri tabanı ortamında kullanılan bir alt dildir.")

@bot.command()
async def Assembly(ctx):
    await ctx.send("Çevirme dili ya da assembly dili, bir bilgisayarda tüm işlemleri işlemci gerçekleştirir ve işlemcinin de, makine dili denen kendine has bir dili vardır. İşlemci yalnızca bu dili anlar ve bu dili kullanarak anlaşırsınız. Fakat bu dili öğrenmek ve kullanmak çok zordur.")

@bot.command()
async def php(ctx):
    await ctx.send("PHP: Hypertext Preprocessor, internet için üretilmiş, sunucu taraflı, çok geniş kullanımlı, genel amaçlı, içerisine HTML gömülebilen betik ve programlama dilidir.")

@bot.command()
async def TS(ctx):
    await ctx.send("TypeScript özgür ve açık kaynak kodlu programlama dili. Microsoft tarafından geliştirilmekte ve desteklenmekte olan TypeScript; bünyesinde barındırdığı derleyici sayesinde, yazılan kodu JavaScript koduna çevirir.")

@bot.command()
async def Rust(ctx):
    await ctx.send("Rust; açık kaynak kodlu, çoklu paradigmalı, ilk olarak Mozilla tarafından dizayn edilen ve Rust Foundation tarafından geliştirilmekte olan; performansa, güvenliğe ve eş zamanlı işlem yapabilmeye odaklanmış bir sistem programlama dilidir.")

@bot.command()
async def Lua(ctx):
    await ctx.send("Lua, ağırlıklı olarak gömülü sistemler ve istemciler için tasarlanmış hafif paralel bir programlama dilidir. Lua, ANSI C'de yazılmış olduğu için çapraz platform destekli bir dildir ve nispeten basit bir C API'sine sahiptir.")

@bot.command()
async def erlang(ctx):
    await ctx.send("Erlang, Ericsson firması tarafından 1986'da Joe Armstrong, Robert Virding ve Mike Williams önderliğinde geliştirilen genel amaçlı, eş zamanlı, dinamik, fonksiyonel ve atık toplama özelliğine sahip olan bir dildir.")

@bot.command()
async def MATHLAB(ctx):
    await ctx.send("MATLAB, çok paradigmalı sayısal hesaplama yazılımı ve dördüncü nesil programlama dilidir. Sahipli bir programlama dili olan MATLAB, MathWorks tarafından geliştirilmektedir.")

@bot.command()
async def Perl(ctx):
    await ctx.send("Perl, bir dil bilimci olup NASA'da sistem yöneticisi olarak çalışan Larry Wall tarafından geliştirilmiş bir programlama dilidir.")

@bot.command()
async def Julia(ctx):
    await ctx.send("Julia yüksek başarımlı üst düzey bir programlama dilidir. Nitelikli bir derleyici, dağıtık koşut yürütüm olanağı, sayısal hesaplamalarda yüksek doğruluk oranı ve geniş bir matematiksel işlev kütüphanesine sahip olan Julia'nın sözdizimi diğer yazılım geliştirme ortamlarında kullanılan dillerle benzerlik göstermektedir.")

@bot.command()
async def Swift(ctx):
    await ctx.send("Swift, Apple tarafından iOS ve macOS platformlarına iOS ve Mac uygulamaları geliştirmek için oluşturulan, derlenerek çalışan güçlü ve kullanımı kolay, nesne yönelimli bir programlama dili.")

@bot.command()
async def Go(ctx):
    await ctx.send("Go, Google'da 2007 yılından itibaren geliştirilmeye başlayan açık kaynak programlama dilidir. İlk web sitesi golang.org alan adına sahip olduğundan golang ismiyle anılsa da doğru adı Go'dur. Daha çok sistem programlama için tasarlanmış olup, derlenmiş ve statik tipli bir dildir. Kasım 2009'da çıkmıştır.")

@bot.command()
async def R(ctx):
    await ctx.send("R, istatistiksel hesaplama ve grafikler için yazılım ortamı olup aynı zamanda programlama dilidir. R Foundation tarafından desteklenen ve GNU Tasarısının parçası olan bir özgür yazılımdır.")

@bot.command()
async def ObjC(ctx):
    await ctx.send("Objective-C, C'nin üzerine yazılmış, yansımalı, nesne yönelimli bir programlama dilidir. ObjC, Objective C ve Obj-C olarak da anılır. Günümüzde OpenStep standardı üzerine kurulu olan macOS ve GNUstep işletim sistemlerinde kullanılmaktadır.")

@bot.command()
async def Dart(ctx):
    await ctx.send("Dart, ilk kez Google tarafından geliştirilen ve daha sonraları ECMA tarafından standart haline getirilen açık kaynaklı ve genel-amaçlı bir programlama dilidir. Dart dili kullanılarak web, sunucu, mobil uygulamalar ve IoT cihazları geliştirilebilir.")

@bot.command()
async def JS(ctx):
    await ctx.send("JavaScript, HTML ve CSS ile birlikte World Wide Web'in temel teknolojilerinden biri olan programlama dilidir. Web sitelerinin %97'sinden fazlası, web sayfası hareketleri için istemci tarafında JavaScript kullanırlar ve kullanılan kodlar genellikle üçüncü taraf kitaplıkları içerir.")

@bot.command()
async def Kotlin(ctx):
    await ctx.send("Kotlin, Java sanal makinesi üzerinde çalışan ayrıca JavaScript kaynak koduna veya LLVM ile makine koduna derlenebilen, statik tipli bir programlama dilidir. İlk geliştirme Sankt-Peterburg, Rusya merkezli JetBrains programcıları tarafından yapılmıştır. İsmi Kotlin Adası'ndan gelmektedir.")

@bot.command()
async def Fortran(ctx):
    await ctx.send("Fortran, özellikle sayısal hesaplama ve bilimsel hesaplama için uygun olan genel amaçlı, yordamsal, zorunlu programlama dilidir.")

@bot.command()
async def COBOL(ctx):
    await ctx.send("COBOL, bir programlama dili. Ticaret alanı ve özellikle iş yerlerinin yönetimiyle ilgili konularda, tüm dünyada kullanılmak üzere hazırlanmıştır. ISAM yapısına izin veren sınırlı sayıdaki dilden biridir. Sayı tipi sınırsızdır. COBOL 2002 'den beri Nesne Yönelimli Programlama'yı desteklemektedir.")

@bot.command()
async def Pascal(ctx):
    await ctx.send("Pascal bilgisayar programlama dili pek çok öğrenciye bilgisayar programlamayı öğreten ve çeşitli versiyonları bugün hâlâ yaygın olarak kullanılmaya devam eden en önemli programlama dillerinden biridir. İlk Macintosh işletim sisteminin çoğu ve TeX Pascal ile yazılmıştır.")

@bot.command()
async def elixir(ctx):
    await ctx.send("Elixir, fonksiyonel, eş zamanlı, genel amaçlı Erlang Sanal Makinesi üzerinde çalışan bir dildir. Erlang üzerine kurulmuş bir dil olduğu için dağıtık, arızalara dayanıklı sistemler yazılır iken Erlang ile aynı soyut yaklaşımları paylaşabilmektedir.")

@bot.command()
async def Clojure(ctx):
    await ctx.send("Clojure, Lisp programlama dilinin lehçelerinden bir tanesidir. Clojure genel amaçlı bir programlama dilidir ve fonksiyonel programlamayı temel alıp, paralel zamanlı programlamayı kolaylaştırır. Clojure JVM, JavaScript ve CLR gibi farklı platformlarda çalışabilmektedir.")

@bot.command()
async def Haskell(ctx):
    await ctx.send("Haskell, isim babası matematikçi Haskell Curry olan arı işlevsel programlama dilidir. Haskell'i birçok programlama dilinden ayıran özellikleri tembel değerlendirme, monadlar ve tür sınıflarıdır. Haskell, Miranda dilinin semantikleri üzerine kuruludur. Akademide ve endüstride yoğun olarak kullanılmaktadır.")

@bot.command()
async def OCaml(ctx):
    await ctx.send("Ocaml, Fransız Ulusal Bilişim ve Uygulamaları Araştırma Kurumu'nda Xavier Leroy tarafından geliştirilen, ücretsiz ve özgür bir lisans altında sunulan, ML programlama dilleri ailesine mensup, hem yorumlanan hem de derlenip doğal makine koduna dönüştürülebilen gelişmiş bir fonksiyonel programlama dilidir.")

c = "F#"
@bot.command()
async def c(ctx):
    await ctx.send("F# Microsoft Research tarafından geliştirilen ve .NET Framework üzerinde çalışan fonksiyonel programlama dilidir.")

@bot.command()
async def Scala(ctx):
    await ctx.send("Scala, hem nesne yönelimli programlamayı hem de fonksiyonel programlamayı destekleyen, statik olarak yazılmış güçlü bir genel amaçlı programlama dilidir. Kısa ve öz olacak şekilde tasarlanan Scala'nın tasarım kararlarının çoğu Java eleştirilerini ele almayı amaçlıyor.")

@bot.command()
async def Zig(ctx):
    await ctx.send("Zig, Andrew Kelley tarafından tasarlanan zorunlu, genel amaçlı, statik olarak yazılan, derlenmiş bir sistem programlama dilidir.")

@bot.command()
async def Lisp(ctx):
    await ctx.send("Lisp, kullanımda olan en eski ve en güçlü programlama dillerinden biridir. John McCarthy'in 1958'de icat ettiği dilden türetilmiş birçok dile verilen genel ad olmakla birlikte, günümüzde çoğunlukla ANSI Common Lisp'in kısa adı olarak kullanılır. Diğer yaygın lehçeleri Emacs Lisp, Scheme ve AutoCAD'in Autolisp'idir.")

@bot.command()
async def Prolog(ctx):
    await ctx.send("Prolog, Yapay zekâ uygulamalarında kullanılan dördüncü nesil bilgisayar dili ailesinden olan bir mantık programlama dilidir. 1970'li yılların başlarında Fransa'nın Aix-Marseille Üniversitesi'nde Alain Colmerauer ve çalışma grubu tarafından icat edilmiştir. Fransızca Programmation en Logique kelimesinden gelmektir.")

@bot.command()
async def Nim(ctx):
    await ctx.send("Nim, Andreas Rumpf tarafından tasarlanan ve geliştirilen, genel amaçlı, çok paradigmalı, statik tipli, derlenen bir programlama dilidir.")

@bot.command()
async def Crystal(ctx):
    await ctx.send("Crystal genel kullanım amaçlı, nesne tabanlı, açık kaynak kodlu programlama dili. Sözdizimi olarak Ruby programlama dilini örnek alan, performans olarak C programlama dili kadar hızlı olmayı hedefleyen Crystal, ilk kararlı sürümünü 2014 yılında yayımlamıştır.")

@bot.command()
async def Carbon(ctx):
    await ctx.send("Carbon, Google tarafından C++ Ardıl Dili olarak oluşturulmuş deneysel bir genel amaçlı programlama dilidir. İlk olarak 2022 yılının Temmuz ayında Carruth Chandler tarafından CppNorth konferansında halka sunuldu.")

@bot.command()
async def ODIN(ctx):
    await ctx.send("Odin, yüksek performanslı, modern sistemler ve veri odaklı programlamaya yönelik özel bir tür sistem tipine sahip genel amaçlı bir programlama dilidir.")

@bot.command()
async def V(ctx):
    await ctx.send("V, Haziran 2019'da Alex Medvedniko tarafından açık kaynaklı bir proje olarak yayınlanan genel amaçlı, statik olarak yazılmış derlenen bir programlama dilidir. Performans, güvenlik ve hızlı derleme için tasarlanmıştır.")

@bot.command()
async def Oberon(ctx):
    await ctx.send("Oberon Pascal dilinin mucidi Niklaus Wirth ve Martin Gutknecht tarafından, 1985-1988 yılları arasında, Zürih'te Eidgenossische Technische Hochschule'de geliştirilmiştir. Nesneye yönelik yapıda bir dildir. Aynı zamanda yordamsal ve blok-yapısal bir dildir.")

@bot.command()
async def Eiffel(ctx):
    await ctx.send("Eiffel, Bertrand Meyer ve Eiffel Software tarafından tasarlanan nesne yönelimli bir programlama dilidir. Meyer, dili 1985 yılında ticari yazılım geliştirmenin güvenilirliğini artırmak amacıyla tasarladı; ilk versiyonu 1986'da kullanıma sunuldu. 2005'te Eiffel, ISO standartlaştırılmış bir dil haline geldi.")

@bot.command()
async def Modula(ctx):
    await ctx.send("Modula 1975'te Niklaus Wirth tarafından İsviçre'de geliştirilmiş olan programlama dilidir. Pascal'ın ardılı olarak bilinen Modula, adını sahip olduğu modüler programlama özelliğinden almıştır. Kısa ömürlü bir dil olup gelişimini Modula-2 adı altında sürdürmüştür.")

@bot.command()
async def Ada(ctx):
    await ctx.send("Ada, yapısal, statik tipli, zorunlu, geniş spektrumlu ve nesne yönelimli bir üst düzey bilgisayar programlama dilidir. Pascal ve diğer dillerin genişletilmiş halidir. Gömülü design-by-contract, güçlü yazımı, açık eşzamanlı, senkronize mesaj geçişi, korunmuş objeli ve belirsiz bir dildir.")

@bot.command()
async def PLI(ctx):
    await ctx.send("PL/I, başlangıçta IBM tarafından geliştirilen, prosedürel, zorunlu bir bilgisayar programlama dilidir. Bilimsel, mühendislik, işletme ve sistem programlama için tasarlanmıştır. 1960'lı yıllarda tanıtıldığı günden bu yana akademik, ticari ve endüstriyel kuruluşlar tarafından sürekli kullanılmaktadır.")

@bot.command()
async def ALGOL(ctx):
    await ctx.send("ALGOL, ilk olarak 1958 yılında geliştirilen bir zorunlu bilgisayar programlama dili ailesidir. ALGOL diğer birçok dili büyük ölçüde etkilemiş ve Association for Computing Machinery tarafından")

@bot.command()
async def Forth(ctx):
    await ctx.send("Forth, Charles H. Chuck Moore tarafından tasarlanan ve ilk kez 1970 yılında diğer programcılar tarafından kullanılan prosedürel, birleştirmeli, yığın odaklı bir programlama dili ve etkileşimli geliştirme ortamıdır.")

@bot.command()
async def SmallTalk(ctx):
    await ctx.send("Smalltalk, Alan Kay önderliğinde aralarında Adele Goldberg, Dan Ingalls, Ted Kaehler'in bulunduğu bir grup tarafından Xerox PARC'ta geliştirilmiş nesne yönelimli bir programlama dilidir.")

@bot.command()
async def Simula(ctx):
    await ctx.send("Simula, 1960'lı yıllarda Ole-Johan Dahl ve Kristen Nygaard tarafından Oslo'daki Norveç Bilgi İşlem Merkezi'nde geliştirilen Simula I ve Simula 67 adında iki programlama dilidir. Sözdizimsel olarak, ALGOL 60'ın oldukça sadık bir üst kümesidir.")

@bot.command()
async def APL(ctx):
    await ctx.send("APL 1960'larda Kenneth E. Iverson tarafından geliştirilmiş bir programlama dilidir. Adını A Programming Language adlı kitaptan almıştır. Çok boyutlu dizilerin ana ekseni oluşturduğu dilde çoğu işlev ve işleç belirli simgelerle tanımlanmaktadır. Hesap çizelgeleri ve işlevsel programlamayı etkilemiştir.")

@bot.command()
async def VBN(ctx):
    await ctx.send("Visual Basic .Net, görsel programlama dillerinden olan Visual Basic'in son sürümüdür. Görsellik yanında .Net kütüphanesiyle birliktelik içindedir. Bu kütüphane eski visual basic için tasarlanmış API lerin sınıflanmış halidir.")

@bot.command()
async def Eclipse(ctx):
    await ctx.send("Eclipse, açık kaynak kodlu ve özgür bir tümleşik geliştirme ortamıdır. Ana odak noktası Java ve Java ile ilişkili teknolojiler olsa da, esnek yapısı sayesinde C ve Python gibi farklı diller için de kullanılmaktadır.")

@bot.command()
async def Notepad(ctx):
    await ctx.send("Notepad++, Windows işletim sistemi içerisine gömülü olarak gelen Notepad yazılımının yerine kullanılmak üzere C++ ile saf Win32 API ve STL ile geliştirilmiş GPL ile dağıtılan açık kaynak kodlu bir kaynak kod düzenleyicisidir.")

@bot.command()
async def NetBeans(ctx):
    await ctx.send("NetBeans, Oracle tarafından geliştirilen bir Java geliştirme ortamıdır ve ücretsiz olarak dağıtılmaktadır. Özellikle kullanıcı arayüzü tasarımında sağladığı kolaylıklardan dolayı tercih edilmektedir. Henüz Eclipse kadar popüler olmasa da popülerliği giderek artmaktadır.")

@bot.command()
async def Apache_Tomcat(ctx):
    await ctx.send("Apache Tomcat, Apache Yazılım Vakfı tarafından geliştirilmiş açık kaynak bir Java Servlet Container uygulamasıdır.")

@bot.command()
async def Nginx(ctx):
    await ctx.send("Nginx; yüksek eş zamanlı çalışma kabiliyeti, yüksek performans ve düşük hafıza kullanımına odaklanılarak tasarlanmış bir Web sunucusudur. Aynı zamanda ters vekil sunucusu, yük dengeleyici ve HTTP ön belleği olarak da kullanılabilir.")

@bot.command()
async def jQuery(ctx):
    await ctx.send("jQuery, John Resig tarafından 2006 yılında geliştirilmiş ve şu an geniş bir jQuery ekibi tarafından gelişimi sürdürülen bir açık kaynak JavaScript kütüphanesidir.")

@bot.command()
async def Bootstrap(ctx):
    await ctx.send("Bootstrap, HTML, CSS ve JavaScript kullanılarak yazılmış, açık kaynaklı ve ücretsiz bir front-end kütüphanesidir. Eski Twitter çalışanları Mark Otto ve Jacob Thornton tarafından oluşturulan bu kütüphane, geliştiricilere duyarlı web siteleri oluşturabilme imkanı sağlar.")

@bot.command()
async def PyGame(ctx):
    await ctx.send("PyGame python'un oyun yapmak için kullanılan bir kütüphanedir. Daha pratik ve kısa oyunlar için pgzero kullanılır.")

@bot.command()
async def Delphi(ctx):
    await ctx.send("Delphi, Object Pascal'ı temel alan bir olaya dayalı programlama dili ve masaüstü, mobil, web ve konsol yazılımları için tümleşik geliştirme ortamıdır. Delphi, 2008 yılından beri Embarcadero Technologies tarafından geliştirilmektedir.")

@bot.command()
async def Scratch(ctx):
    await ctx.send("Scratch, ABD’de bulunan MIT’in (Massachusetts Teknoloji Enstitüsü) geliştirdiği, 8-16 yaş arası çocukların kullanımına göre tasarlanmış ve basit bir arayüze sahip bir programlama dilidir.[2] Geleneksel programlama dillerinin aksine kullanıcı, istediği fonksiyonları fareyle tıklayıp sürükleyerek animasyonlar, oyunlar yaratabilir.")

@bot.command()
async def Shell(ctx):
    await ctx.send("Kabuk programlama (İngilizce: shell programming), Unix ve benzeri sistemlerde sistem yönetimini sağlayan komutlar ve bu komutları işlemeye yarayan kontrol mekanizmalarının bulunduğu programlama şeklidir.")

@bot.command()
async def popular_shells(ctx):
    await ctx.send("En çok bilinen kabuklar: bash(Bourne Again Shell), csh(C-Shell), ksh, sh, tcsh, zsh.")

@bot.command()
async def bash(ctx):
    await ctx.send("Bash, Brian Fox tarafından GNU Projesi için Bourne kabuğuna özgür yazılım alternatifi olarak yazılmış, Unix ve benzeri işletim sistemlerinde kullanılan komut satırı kabuğu ve bu kabuğun betik dilidir. GNU Tasarısı'nın parçasıdır ve birçok GNU/Linux dağıtımında ön tanımlı kabuk olarak gelir.")

@bot.command()
async def csh(ctx):
    await ctx.send("C Shell, 1970'lerin sonlarında Berkeley'deki California Üniversitesi'nde yüksek lisans öğrencisiyken Bill Joy tarafından yaratılan bir Unix kabuğudur. Joy'un ilk olarak 1978'de dağıttığı Berkeley Software Distribution'ın 2BSD sürümünden başlayarak geniş çapta dağıtıldı.")

@bot.command()
async def ksh(ctx):
    await ctx.send("KornShell(ksh), 1980'lerin başında David Korn tarafından Bell Laboratuvarlarında geliştirilen ve 14 Temmuz 1983'te USENIX'te duyurulan bir Unix kabuğudur. İlk geliştirme, Bourne kabuğu kaynak koduna dayanıyordu.")

@bot.command()
async def sh(ctx):
    await ctx.send("Unix shell (tr. Unix kabuğu), Unix benzeri işletim sistemleri için bir komut satırı kullanıcı arabirimi sağlayan bir komut satırı yorumlayıcısı veya kabuğudur. Kabuk, hem etkileşimli bir komut dili hem de bir komut dosyası dilidir ve işletim sistemi tarafından sistemin kabuk komut dosyalarını kullanarak yürütülmesini kontrol etmek için kullanılır.")

@bot.command()
async def tcsh(ctx):
    await ctx.send("Tcsh, C kabuğuna(csh) temelli ve geriye dönük uyumlu bir Unix kabuğudur.")

@bot.command()
async def zsh(ctx):
    await ctx.send("Zsh(Z kabuğu), etkileşimli oturum açma kabuğu ve kabuk betikleri oluşturmak için komut yorumlayıcısı olarak kullanılabilen bir Unix kabuğudur. Bash, ksh ve tcsh'nin bazı özelliklerinin yanı sıra, birçok iyileştirme içeren, genişletilmiş bir Bourne kabuğudur.")

@bot.command()
async def plankalkül(ctx):
    await ctx.send("Plankalkül icat edilmiş ilk programlama dilidir. 1940'larda Konrad Zuse tarafından tasarlanmış, ancak 1972'ye kadar kamuya açıklanmamış ve 1998'e kadar kullanılmamıştır.")

@bot.command()
async def duolingo(ctx):
    await ctx.send("İngilizce dersini yapmayı unutma, yoksa aileni kaçırırım...")

@bot.command()
async def StarWars(ctx):
    await ctx.send("https://youtu.be/Bv1LVYtdGGo?list=RDBv1LVYtdGGo Bunu izlemelisin dostum!")

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
async def ohio(ctx):
    await ctx.send("https://tenor.com/view/spam-spongebob-meme-mr-krabs-mr-krabs-meme-table-gif-7910338758662995384")

@bot.command()
async def komut_sayisi(ctx):
    await ctx.send("Şuanda 175 komut vardır.(İlerideki hedef 180)")

@bot.command()
async def pi(ctx):
    await ctx.send("İlk 1000 basamağı: 3,1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 2164201989")

@bot.command()
async def guncellemeler(ctx):
    await ctx.send("En son güncelleme: 1 tane yeni komut eklendi 🥳 ve komut sayısı 175 oldu 📢.")
 
@bot.command()
async def discord_yenilikleri(ctx):
    await ctx.send("Discord sunucumuzdaki yenilikler: 1 yeni komut geldi ve /yardım diyerek bunu görebiliriz!")

@bot.command()
async def github_py(ctx):
    await ctx.send("Yazarın python kodlarını bu github deposundan bulabilirsiniz: https://github.com/gtaha23/python_pro")

@bot.command()
async def facts(ctx):
    await ctx.send("Bir bulutun ağırlığı yaklaşık bir milyon tondur")

@bot.command()
async def facts2(ctx):
    await ctx.send("Zürafaların yıldırım çarpması olasılığı insanlara göre 30 kat daha fazladır.")    

@bot.command()
async def facts3(ctx):
    await ctx.send("Tek yumurta ikizleri aynı parmak izlerine sahip değildir.")

@bot.command()
async def facts4(ctx):
    await ctx.send("Dünyanın dönüş hızı değişiyor.")

@bot.command()
async def facts5(ctx):
    await ctx.send("Beyniniz sürekli kendini yiyor.")

@bot.command()
async def version(ctx):
    await ctx.send("Bu botun versiyonu: v1.21 (Bot oluşturulduğundan beri)")

@bot.command()
async def data_science(ctx):
    await ctx.send("Veri bilimi, iş için anlamlı öngörüler ayıklamak amacıyla veriler üzerinde gerçekleştirilen çalışmaların adıdır1. Matematik, istatistik, yapay zeka ve bilgisayar mühendisliği gibi alanların ilke ve uygulamalarını bir araya getirerek büyük miktardaki verileri analiz eden, disiplinler arası bir yaklaşımdır1. Veri bilimcileri, ne olduğu, neden olduğu, ne olacağı ve sonuçlarla neler yapılabileceğini sormalarına ve bu soruları cevaplamalarına yardımcı olan analizleri yaparlar.")

@bot.command()
async def hayal(ctx):
    await ctx.send("Bu botun yazarının asıl hayali kendi programlama dilini oluşturmak. Bize destek olursanız çok seviniriz!")

@bot.command()
async def discord_sunucu(ctx):
    await ctx.send("İşte Gt_Bot™'nin sunucusu! : https://discord.gg/Zewtmpwu")

@bot.command()
async def python_sunucu(ctx):
    await ctx.send("Python sunucumuza katılmayı unutmayın! İşte Linki: https://discord.gg/9k2sUHk2")

@bot.command()
async def Atatürk(ctx):
    await ctx.send("Ulu önder Mustafa Kemal Atatürk. Ruhu şad olsun o7")

@bot.command()
async def arkadaş(ctx):
    await ctx.send("Yapımcımın bazı arkadaşları: JR, Ariyonix, eotra, Shenhe, Semih Vatansever,...")

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
async def bişey(ctx):
    await ctx.send("“Bir şey” kelimesi, Türkçe dilinde genellikle belirli bir konu veya nesne üzerine odaklanmayı gerektiren durumlarda kullanılır. İki ayrı kelimeden oluşur: “bir” ve “şey”. “Bir”, Türkçede belirli bir miktar veya sayıyı ifade eder ve genellikle çoğunlukla tek olan nesne veya durumları vurgulamak için kullanılır.")

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

@bot.command(name = "AmericanLife")
async def al(ctx):
    await ctx.send("AmericanLife ingilizce öğrenmek için bulunan birçok kursların yalnızca bir tanesi. Eğer samimi bir atmosferde öğrenmek isterseniz AmericanLife tam size göre.")

@bot.command()
async def AI(ctx):
    await ctx.send("Yapay zekâ ya da kısaca YZ, (İngilizce: Artificial intelligence ya da kısaca AI), insanlar da dahil olmak üzere hayvanlar tarafından, doğal zekânın aksine makineler tarafından görüntülenen zekâ çeşididir. İlk ve ikinci kategoriler arasındaki ayrım genellikle seçilen kısaltmayla ortaya çıkar. Güçlü yapay zeka genellikle Yapay genel zekâ (İngilizce: Artificial General Intelligence kelimelerinin kısaltılmışı olarak: AGI) olarak etiketlenirken, doğal zekayı taklit etme girişimleri yapay biyolojik zeka (İngilizce: Artificial Biological Intelligence: ABI) olarak adlandırılır.")

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
    await ctx.send("Yapımcının takipçi sayısı: 2")

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
