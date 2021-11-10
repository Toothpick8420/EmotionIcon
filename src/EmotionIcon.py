import discord  # The discord.py api

class EmotionIcon(discord.Client):

    # After the bot connects and is ready to run
    async def on_ready(self):
        print("EmotionIcon: Loggin in as {0}".format(self.user))  # LOGGING 
