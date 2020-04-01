import discord
from datetime import date

client = discord.Client()

channels = [671617756004876328, 624038275245539349]
@client.event
async def on_ready():
    print('Logged in as {0.user} - may the chaos commence.'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    today = date.today()
    if message.channel.id in channels and [today.day, today.month] == [1,4]:
      m = message.content
      a = message.author.mention
      c = message.channel.name

      await message.channel.send(f"From {a} in #{c}: {m}")

client.run(open("token").read())
