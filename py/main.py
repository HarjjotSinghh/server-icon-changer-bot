import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
import io
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime, timezone

# Load environment variables
load_dotenv()

# Set up bot with required intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


async def get_random_image():
    """Fetch a random image from Lorem Picsum"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://picsum.photos/512") as response:
                if response.status != 200:
                    raise Exception("Failed to fetch image")
                image_data = await response.read()
                return image_data
    except Exception as error:
        print(f"Error fetching random image: {error}")
        return None


async def change_server_icon():
    """Change the server icon of the specified server"""
    try:
        # Find the specific server by name
        guild = discord.utils.get(bot.guilds, name="TGNS.")
        if not guild:
            print('Could not find the server "TGNS."')
            return False

        # Get and set the new icon
        image_data = await get_random_image()
        if not image_data:
            return False

        await guild.edit(icon=image_data)
        print("Successfully changed server icon")
        return True
    except Exception as error:
        print(f"Error changing server icon: {error}")
        return False


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

    # Set up scheduler for midnight UTC
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        change_server_icon, CronTrigger(hour=0, minute=0, timezone=timezone.utc)
    )
    scheduler.start()

    # Change icon immediately when bot starts (optional)
    await change_server_icon()


@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message mentions the bot and includes the word "change"
    if bot.user in message.mentions and "change" in message.content.lower():
        # Check if the user has the Manage Server permission
        if not message.author.guild_permissions.manage_guild:
            await message.reply(
                'You need the "Manage Server" permission to use this command.'
            )
            return

        # Process the change request
        await message.reply("Changing server profile picture...")
        success = await change_server_icon()

        if success:
            await message.reply("Server profile picture has been changed successfully!")
        else:
            await message.reply(
                "Failed to change server profile picture. Please check the logs for more details."
            )

    await bot.process_commands(message)


# Start the bot
bot.run(os.getenv("DISCORD_TOKEN"))
