# Discord Server Profile Picture Changer Bot (Python Version)

This Discord bot automatically changes the server profile picture of a specific server named "TGNS." every day at midnight UTC. This is the Python implementation using discord.py.

## Features
- Changes server profile picture daily at midnight (UTC)
- Uses random stock images from Lorem Picsum
- Targets a specific server named "TGNS."
- Manual change command via bot mention

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A Discord Bot Token
- Server Admin permissions for the bot

## Setup Instructions

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the bot:
   - Copy `.env.example` to `.env`
   - Replace the token in `.env` with your Discord bot token

5. Invite the bot to your server:
   - Go to Discord Developer Portal
   - Select your application
   - Go to OAuth2 > URL Generator
   - Select the following scopes:
     - `bot`
   - Select the following bot permissions:
     - `Manage Server`
   - Use the generated URL to invite the bot

6. Run the bot:
   ```bash
   python main.py
   ```

## Usage
- The bot will automatically change the server icon at midnight UTC
- To manually change the icon, mention the bot with the word "change" (e.g., "@BotName change")
- Only users with "Manage Server" permission can use the manual change command

## Important Notes
- Make sure the bot has the "Manage Server" permission
- The server must be named exactly "TGNS." for the bot to work
- The bot uses UTC timezone for scheduling

## License
MIT 