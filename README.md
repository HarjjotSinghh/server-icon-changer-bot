# Discord Server Profile Picture Changer Bot

This Discord bot automatically changes the server profile picture of a specific server named "TGNS." every day at midnight UTC.

## Features
- Changes server profile picture daily at midnight (UTC)
- Uses random stock images from Lorem Picsum
- Targets a specific server named "TGNS."

## Prerequisites
- Node.js (v16.9.0 or higher)
- npm
- A Discord Bot Token
- Server Admin permissions for the bot

## Setup Instructions

1. Clone this repository
2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a Discord Bot:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application"
   - Go to the "Bot" section
   - Click "Add Bot"
   - Under Privileged Gateway Intents, enable necessary intents
   - Copy the bot token

4. Configure the bot:
   - Rename `.env.example` to `.env`
   - Replace `your_discord_bot_token_here` with your actual bot token

5. Invite the bot to your server:
   - Go to OAuth2 > URL Generator in the Discord Developer Portal
   - Select the following scopes:
     - `bot`
   - Select the following bot permissions:
     - `Manage Server`
   - Use the generated URL to invite the bot to your server

6. Run the bot:
   ```bash
   node index.js
   ```

## Important Notes
- Make sure the bot has the "Manage Server" permission
- The server must be named exactly "TGNS." for the bot to work
- The bot uses UTC timezone for scheduling

## License
MIT 