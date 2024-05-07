import os
import random  
import asyncio
from discord import Intents, Activity, ActivityType
from discord_easy_commands import EasyBot

intents = Intents.default()


channel_id = 1167879934031700088


bot = EasyBot(intents=intents)


bot_messages = [

    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    "Mensaje",
    ## 
]

async def send_random_bot_message():
    while True:
        message = random.choice(bot_messages)
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(message)
        else:
            print(f"No se pudo encontrar el canal con ID {channel_id}")

        await asyncio.sleep(800)

@bot.event
async def on_ready():
    print(f"Conectado como: {bot.user}")
    await bot.change_presence(activity=Activity(type=ActivityType.playing, name="Jugando a (Actividad)"))

    bot.loop.create_task(send_random_bot_message())

bot.run(os.environ['TOKEN'])
