import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    joke_dict = {
        "joke1": "My grandpa always said when one door closes, another one opens. Smart man but a horrible cabinet maker.",
        "joke2": "People are usually shocked when they find out I'm not a very good electrician.",
        "joke3": "I once got stuck in an elevator. Now I take steps to avoid them!",
        "joke4": "My doctor recommended I buy orthopedic insoles. I didn't think they would work, but now I stand corrected",
        }
    if message.content.startswith('$tellajoke'):
        await message.channel.send(random.choice(list(joke_dict.values())))    
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    if message.content.startswith('$help'):
        await message.channel.send("Here's a guide to all commands: $hello: This will prompt the bot to answer back with. 'hi'. $bye: This will prompt the bot to answer with the emoji 🙂. $tellajoke: This will select a random joke stored in the bot for it to answer with it. $addition: This command requires for two or more numbers (divided by spaces) to be put for the bot to sum them up so it can answer with the addition.")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    if message.author == bot.user:
        return
    if message.content.startswith('$addition'):
        try:
            numbers_str = message.content[len('$addition'):].strip().split()
            numbers = [float(num) for num in numbers_str]
            result = sum(numbers)
            await message.channel.send(f'The sum is: {result}')
        except ValueError:
            await message.channel.send('Please provide valid numbers to add, e.g., `$addition 5 10 2.5`')

client.run("")

