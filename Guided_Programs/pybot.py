import discord 
from discord.ext import commands

DISCORD_GUILD = "Your server name here"

TOKEN = 'Your token here'
GUILD = DISCORD_GUILD

bot= commands.Bot(command_prefix= "$", intents=discord.Intents.all())

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name==GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.event
async def on_message(message):
    contents= message.content
    if message.author== bot.user:
        return

    if contents in message.content.lower():
        await bot.process_commands(message)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.command()
async def todo(ctx, *args):
    response= ""

    for arg in args:
        response= response +", " + arg

    await ctx.channel.send(response)

#WHEN = time(12, 47, 0)

#@tasks.loop(seconds=10)
#async def schedule_message():
#    await bot.wait_until_ready()
#    channel= bot.get_channel(1022213906292281444)
#    await channel.send("Class is starting!")

#async def background():
#    now= datetime.now()
#    if now.time() > WHEN:
#        tomorrow= datetime.combine(now.date() + time.delta(days=2), time(0))
#        seconds= (tomorrow-now).total_seconds()
#        await asyncio.sleep(seconds)
#    while True:
#        now= datetime.now()
#        target_time= datetime.combine(now.date(), WHEN)
#        seconds_til_target= (target_time-now).total_seconds()
#        await asyncio.sleep(seconds_til_target)
#        await schedule_message()
#        tomorrow= datetime.combine(now.date() +time.delta(days=2), time(0))
#        seconds= (tomorrow-now).total_seconds()
#        await asyncio.sleep(seconds)
    

        

bot.run(TOKEN)
