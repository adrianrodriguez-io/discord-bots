import discord
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()

token = os.environ.get("token")

serverid = 123
channelid = 456

def get_random_message():

    #messages array from 0 to 5
    messages = [
        ' fancy a dashboard?',
        ' share your data project !',
        ' join a discussion !',
        ' ask a question and receive feedback !',
        ' share any data resource you want with the rest !',
        ' glad you join !'
    ]

    rng = np.random.default_rng()
    i = rng.integers(len(messages), size=1)[0]
    
    message = messages[i]

    return message

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):
  guild = client.get_guild(serverid)
  channel = guild.get_channel(channelid)
  await channel.send(f'Welcome {member.mention} !'+get_random_message())

client.run(token)