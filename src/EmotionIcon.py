import discord  # The discord api

# For type hinting
from typing import List
from typing import TextIO


class EmotionIcon(discord.Client):

    # After the bot connects and is ready to run
    async def on_ready(self) -> None:
        print("EmotionIcon: Loggin in as {0}".format(self.user))  # LOGGING

    # Called after it detects the messge is sent
    async def on_message(self, message: discord.Message) -> None:
        if(message.author.bot):
            return
        # Split the message into strings
        msg_split: List[str] = message.content.split()

        emote_path: str = self.getEmoteFilepath(msg_split).strip()
        if(emote_path == "Error"):
            print("EmotionIcon: No emote sent")
            return

        await message.channel.send(file=discord.File(emote_path))

    def getEmoteFilepath(self, message: List[str]) -> str:
        db: TextIO = open("../images/emotes.txt", "r")
        for name_fp in db:
            line: List[str] = name_fp.split(":")
            for word in message:
                if not (word == line[0]):
                    continue
                print("EmotionIcon: Found emote {0}".format(line[1].strip()))
                return line[1]

        return "Error"
