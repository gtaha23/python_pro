import discord
from discord.ext import commands

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
    await ctx.send("he" * count_heh)

@bot.command()
async def gökhan(ctx):
    await ctx.send("Ooo kimler gelmiş! selam yazar!")

@bot.command()
async def katıldı(ctx, member: discord.Member):
    await ctx.send(f'{member.name} katıldı {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def yardım(ctx):
    await ctx.send('İşte beni çağırmak için kodlar: /selam , /heh , /gökhan , /katıldı(katıldığı tarihi öğrenmek için onun ismini yaz) , /Gt_Bot ve /yardım ')

@bot.command(name='Gt_Bot')
async def robot(ctx):
    await ctx.send('Bu bot havalıya benziyor.')

bot.run("Token")
