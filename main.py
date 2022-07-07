import discord
import time
client = discord.Client()


@client.event
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'ping':
        await message.channel.send('pong')

    if message.author == client.user:
        return
    if message.content.startswith('說'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦？")
      else:
        await message.channel.send(tmp[1])
   
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
            await message.channel.send("你要改成什麼啦？")
        else:
            game = discord.Game(tmp[1]) 
            await client.change_presence(status=discord.Status.idle, activity=game)
    if message.content.startswith('跟我打聲招呼吧'):
        channel = message.channel
       
        await channel.send('那你先跟我說你好')
        def checkmessage(m):
            return m.content == '你好' and m.channel == channel
		
        msg = await client.wait_for('message', check=checkmessage)
        await channel.send('嗨, {.author}!'.format(msg))
    if message.content == '群組':
        guilds = await client.fetch_guilds(limit=150).flatten()
       
        for i in guilds:
        
            await message.channel.send(i.name)

client.run('OTgyNjA0OTIyMDA2Njc1NDU3.GAOPmv.fMN95MAtGwc2JjSiqtSLfpa-a-9jTu_2l_5-VQ')