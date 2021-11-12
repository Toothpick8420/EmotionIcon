import discord  # The discord api

# For type hinting
from typing import List
from typing import TextIO
from typing import Union

class EmotionIcon(discord.Client):

    # After the bot connects and is ready to run
    async def on_ready(self) -> None:
        print("EmotionIcon: Loggin in as {0}".format(self.user))  # LOGGING

    # Called after it detects the messge is sent
    async def on_message(self, message: discord.Message) -> None:
        # Don't do anything if the message is from the bot
        if(message.author.bot):
            return

        # Split the message into strings for parsing
        msg_split: List[str] = message.content.split()

        # Gets the file path of the emote if it has one
        emote_path: str = self.getEmoteFilepath(msg_split)
        
        if(emote_path is not None):
            print("EmotionIcon: Preparing and sending emote")
            emote_path = emote_path.strip()
            await message.channel.send(file=discord.File(emote_path))
            print("EmotionIcon: Emote sent") 
        else:
            print("EmotionIcon: No emote in message")


    # Is passed a list of strings that was the message and parses it for a valid emote
    # by comparing it to our database, a text file lol, and seeing if its in there
    # FIXME: Look into how inefficent this is to do
    def getEmoteFilepath(self, message: List[str]) -> Union[str,None]:

        db: TextIO = open("../images/emotes.txt", "r")  # Database file, just a text file
        
        for name_fp in db:  # For each line in the file <emotename>:<emotefilepath>
            line: List[str] = name_fp.split(":").strip()
            emotename: str = line[0]
            emote_fp: str = line[1]
            
            # FIXME: This is the part that I think is inefficient
            for word in message:
                if(word == emotename):
                  print("EmotionIcon: Found emote {0}".format(emote_fp))
                  return emote_fp
        # No emote was found
        return None
