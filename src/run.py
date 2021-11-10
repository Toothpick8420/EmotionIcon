# run.py is the main driver code of the bot. It
# creates the bot and then starts the event loop

from EmotionIcon import EmotionIcon  # Import the bot

# The bot token is how the bot connects to discord
bot_token: str = "Insert bot token here"

emoticon: EmotionIcon = EmotionIcon()  # Create the bot
emoticon.run(bot_token)  # Start the event loop and connect to bot w/ token
