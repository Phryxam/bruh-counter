import discord

client = discord.Client()
bruh_counter = {}

@client.event
async def on_ready():

    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    if 'bruh' in msg or 'breh' in msg:
        if str(message.author.id) in bruh_counter:
            bruh_counter[str(message.author.id)] += 1 
        else:
            bruh_counter[str(message.author.id)] = 1
        await message.channel.send(message.author.name + ' has said bruh ' + str(bruh_counter[str(message.author.id)]) + ' times!');

    if 'say sike right now' in msg:
        if str(message.author.id) in sike_counter:
            sike_counter[str(message.author.id)] += 1 
        else:
            sike_counter[str(message.author.id)] = 1
        await message.channel.send(message.author.name + ' has said \"Say Sike Right Now\" ' + str(bruh_counter[str(message.author.id)]) + ' times!');


client.run('NzM1MjAyNzkzNjAxNzYxMzQx.Xxc10w.F0iYLqSI_NmkKqbjup45zYvFt_4')