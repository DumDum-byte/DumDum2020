#config
import discord
import flask
import os

client = discord.Client()

#login
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#commands

#hello
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("bruh hello"):
        await message.channel.send("Hello, Im dumdum Nice to meet you Onee Chans")
    
    if message.content.startswith("bruh help"):
        await message.channel.send("Hello, dumdum is currently devloping me wait a while")

    if message.content.startswith("bruh tell me my name"):
        await message.channel.send("Are you eve")    
    










client.run(os.getenv('secret'))
