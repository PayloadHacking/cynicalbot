import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('=What Does The fox Say?'):
        msg = 'ningningningningningningningningningningningningningningningningningningningningningning {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('=ping'):
        await client.send_message(message.channel,"pong")
    elif message.content.startswith('noob'):
        await client.send_message(message.channel,"i know you are")
    elif message.content.startswith('diss'):
        await client.send_message(message.channel,"Im Better than You ledgend Mods And Your PP bot , i mean like , musci cmon man , lets go ahed and have a bot diss , oh yeah i forgot you cant im sorry for taking a piss on that base of yours , this is just what you shitty phantom deserver , all you do is play music, phh please thats just basic , go suck on my moderation commands or maybe even my camel toe")
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDcwNjE1NjY0NDUzODc3NzYw.DjY3qw.VPX_Cd4lMor5FEDUIqwG3rUquag')