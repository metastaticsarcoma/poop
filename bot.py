import discord
import bot_logic
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

@client.event
async def on_message(message):
    joke_dict = {
            "joke1": "My grandpa always said when one door closes, another one opens. Smart man but a horrible cabinet maker.",
            "joke2": "People are usually shocked when they find out I'm not a very good electrician.",
            "joke3": "I once got stuck in an elevator. Now I take steps to avoid them!",
            "joke4": "My doctor recommended I buy orthopedic insoles. I didn't think they would work, but now I stand corrected",
            }
    random_value = random.choice(list(joke_dict.values()))
    if message.author == client.user:
        return
    if message.content.startswith('$tellajoke'):
        await message.channel.send(random_value)
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)    

client.run("")