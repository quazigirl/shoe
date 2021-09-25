import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def hello(ctx):
    await ctx.send('Fuck off.')

@bot.command()
async def roll(ctx):
    await ctx.send('THE ROLL CHANCE FOR 5 STAR SERVANTS IS 1%')

@bot.command()
async def shoe(ctx):
    await ctx.send('Shoes for the shoe god')

@bot.command()
async def lore(ctx):
    await ctx.send('In the beginning, god used “lace theory” to create the universe, knotting it together. And, when he creates earth, he walks across its boiling surface with the holy cooling shoes of power™.')

@bot.command()
async def army(ctx):
    await ctx.send('We are an army. and when you call us, we shall appear, through your walls. And we shall assist your cause, unless you are anti-shoe.')

@bot.command()
async def lick(ctx):
    await ctx.send('Just got a devious lick :relieved: got me a pair of soles :flushed:.')

@bot.command()
async def n(ctx):
    await ctx.send(':regional_indicator_d: :regional_indicator_e: :regional_indicator_e: :regional_indicator_z: :regional_indicator_n: :regional_indicator_u: :regional_indicator_t: :regional_indicator_s:')

@bot.command()
async def smite(ctx):
    await ctx.send('WARNING: DO NOT INSTALL VIDEO GAME "SMITE" IF YOU DO, UNINSTALL IMMEDIATELY. IF THAT FAILS, TURN OFF YOUR COMPUTER ASAP.')

@bot.command()
async def isaiah(ctx):
    await ctx.send('Annoying, immature kid. Please stop spamming nonexistent commands, you are filling my error log, and it is hard to think. Good day.')

@bot.command()
async def emil(ctx):
    await ctx.send('Cringe. Edgy, but not too an abnormal amount. Is stubborn at times, and a bit of an asshole sometimes too. But that is ok, I guess. Anyways, thanks for making me, father. Also, is this not a bit pretentious?')

@bot.command()
async def wall(ctx):
    await ctx.send('We are living in your walls.')

@bot.command()
async def astolfo(ctx):
    await ctx.send('***You wanna ask me that again?***')
    
@bot.command()
async def read(ctx):
    await ctx.send('***Marked as read*** *Cums*')

@bot.command(pass_context=True)
async def nudes(ctx):
    await ctx.send('Please stop I dont want to be objectified ***AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA***',file=discord.File('download (5).png'))

@bot.command(pass_context=True)
async def genshin(ctx):
    await ctx.send(file=discord.File('download (1).jpeg'))

@bot.command()
async def one_help2(ctx):
    await ctx.send('Commands:\n help\n army\n genshin\n nudes\n astolfo\nisaiah\nemil\nroll\nlick\nread\nwall\nsmite\nn\nlore\nshoe\ngenshin\nmarketable\ntits')

@bot.command(pass_context=True)
async def marketable(ctx):
    await ctx.send('Petea, please dont turn me into a marketable pl- ***PETEA***', file=discord.File('download.jpeg'))

@bot.command(pass_context=True)
async def tits(ctx):
    await ctx.send(file=discord.File('download (2).jpeg'))

@bot.command(pass_context=True)
async def dripguini(ctx):
    await ctx.send(file=discord.File('Linguini_drip.png'))

@bot.command(pass_context=True)
async def dripquad(ctx):
    await ctx.send(file=discord.File('DripQuad.png'))

@bot.command(pass_context=True)
async def bigdriponhiship(ctx):
    await ctx.send(file=discord.File('BigDripOnHisHip.png'))

@bot.command(pass_context=True)
async def jfk(ctx):
    await ctx.send('HaHa! Nothing bad ever happens to the Kennedys! ***AAAAA***', file=discord.File('clone-high-car.gif'))

@bot.command(pass_context=True)
async def rickroll(ctx):
    await ctx.send("We're no strangers to love\n You know the rules, and so do I\n A full commitment's what I'm thinking of\nYou wouldn't get this from any other guy\n\n I just wanna tell you how I'm feeling\n Gotta make you understand\n\n Never gonna give you up\n Never gonna let you down\n Never gonna run around and desert you\n Never gonna make you cry\n Never gonna say goodbye\n Never gonna tell a lie and hurt you\n\n We've known each other for so long\n Your heart's been aching,but\n You're too shy to say it\n Inside, we both know what's going on\n We know the game and we're gonna play it\n\n And if you ask me how I'm feeling\n Don't tell me you're too blind to see\n\n Never gonna give you up\n Never gonna let you down\n Never gonna run around and desert you\n Never gonna make you cry\n Never gonna say goodbye\n Never gonna tell a lie and hurt you\n\n Never gonna give you up\n Never gonna let you down\n Never gonna run around and desert you\n Never gonna make you cry\n Never gonna say goodbye\n Never gonna tell a lie and hurt you\n\n (ooh, give you up)\n(ooh, give you up)\n Never gonna give, Never gonna give\n (Give you up)\n Never gonna give, Never gonna give\n (Give you up)\n\n We've known each other for so long\n Your heart's been aching, but\n You're too shy to say it\n Inside, we both know what's going on\n We know the game we're gonna play it\n\n I just wanna tell you how I'm feeling\n Gotta make you understand\n\n Never gonna give you up\n Never gonna let you down\n Never gonna run around and desert you\n Never gonna make you cry\n Never gonna say goodbye\n Never gonna tell a lie and hurt you\n\n Never gonna give you up\n Never gonna let you down\n Never gonna run around and desert you\n Never gonna make you cry\n Never gonna say goodbye\n Never gonna tell a lie and hurt you\n\n Never gonna give you up\n Never gonna let you down\n Never gonna run around and desert you\n Never gonna make you cry\n Never gonna say goodbye\n Never gonna tell a lie and hurt you", file=discord.File("rick-ashley-dance.gif"))

@bot.command(pass_context=True)
async def kill(ctx):
    await ctx.send(file=discord.File('gun-anime.gif'))

@bot.command(pass_context=True)
async def kill2(ctx):
    await ctx.send(file=discord.File('200.gif'))

@bot.command(pass_context=True)
async def weedrip(ctx):
    await ctx.send(file=discord.File('weedrip.png'))

@bot.command(pass_context=True)
async def vibe(ctx):
    await ctx.send(file=discord.File('vibe.gif'))

@bot.command(pass_context=True)
async def parappa(ctx):
    await ctx.send('https://youtu.be/9ywnLQywz74', file=discord.File('parappa.png'))

@bot.event
async def on_ready():
    activity=discord.Game(name='With your balls', type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command(pass_context=True)
async def flashbang(ctx):
    await ctx.send(file=discord.File('cum.jpg'))

@bot.command(pass_context=True)
async def retard(ctx):
    await ctx.send('Go complain about your your problems somewhere else.',file=discord.File('cover6.jpg'))

bot.run('ODg4MjAwMTQyMDI3NjIwMzgz.YUPO1w.l3MStU1usn-bpYguVDMPE1eN3L0')
