#import libraries
import discord
import os
import random
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv

#Initialize the variables

load_dotenv()
client = discord.Client()
token = str(os.getenv('TOKEN'))

#Intializing the Bot with callable object on_ready
@client.event
async def on_ready():
    print("Logeed in as a bot {0.user}".format(client))

#Code to set up bot responses with callable object on_message
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')
    #if else condition for bot to respond to certain user messages
    if message.author == client.user:
        return
    #if else condition where channel == random and bot responds if user message is equal to the input by the user
    if channel == "random":
        if user_message.lower() == "hello world" or user_message.lower() == "hi":
            #await keyword to run the onbject message
            await message.channel.send(f'Hello!')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "tell me a joke":
            jokes = [" Can someone please shed more\
light on how my lamp got stolen?",
                     "Why is she called llene? She\
stands on equal legs.",
                        "What do you call a gazelle in a \
lions territory? Denzel."]
            #run the object randomly selecting one of the jokes to output
            await message.channel.send(random.choice(jokes))
        elif user_message == "Tell me about my server!":
            #run the object to output server info
            await message.channel.send(f"Your EC2 Data:\nRegion: {ec2_metadata.region}\nIP Address: {ec2_metadata.public_ipv4}\nAvailability: {ec2_metadata.availability_zone}\nServer instance:  {ec2_metadata.instance_type}")



#Function client takes the token as an argument
client.run(token)         

