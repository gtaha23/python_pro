import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def gökhan(ctx,a):
    await ctx.send("merhaba gökhan!" * int(a))

@bot.command()
async def taha(ctx,a):
    await ctx.send("merhaba taha!" * int(a))

@bot.command()
async def katıldı(ctx, member: discord.Member):
    await ctx.send(f'{member.name} katıldı {discord.utils.format_dt(member.joined_at)}')
    
@bot.command()
async def ekle(ctx, sol: int, sağ: int):
    await ctx.send(sol + sağ)
    
@bot.command(name='Gt_Bot')
async def bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Bu bot havalıya benziyor.')
    
bot.run("token")
