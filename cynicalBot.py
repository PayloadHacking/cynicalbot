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
    elif message.content.startswith('help'):
        await client.send_message(message.channel,":mailbox_with_mail: :arrow_left:")
        await client.send_message(message.author, "Hello My Name Is Cynical , And I Am The Main Discord Bot for the Cynical Gaming Discord Server, My Mommy Is Pretty Barbie#5081 And My Daddy Is @Sorry Im Noob#7814 , My Daddy Will Make You Your Own Bot For The Low Orphaned Price Of £10 , My Commands Are - =8ball (question) =ping noob =What Does The Fox Say? =bitcoin =square (number) and i am now currently being made some more body parts! Add Me To Your Server https://discordapp.com/api/oauth2/authorize?client_id=470615664453877760&permissions=0&scope=bot Meet My Daddy In The Offical Server, My Mummy Runs Me And My Daddy Feeds me :apple: https://discord.gg/BCrGVVY")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDcwNjE1NjY0NDUzODc3NzYw.DjY3qw.VPX_Cd4lMor5FEDUIqwG3rUquag')