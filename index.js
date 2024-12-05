const { Client, GatewayIntentBits, Events } = require('discord.js');
const cron = require('node-cron');
const fetch = require('node-fetch');
require('dotenv').config();

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
    ]
});

async function getRandomImage() {
    try {
        const response = await fetch('https://picsum.photos/512');
        if (!response.ok) throw new Error('Failed to fetch image');
        return response.url;
    } catch (error) {
        console.error('Error fetching random image:', error);
        return null;
    }
}

async function changeServerIcon() {
    try {
        const guild = client.guilds.cache.find(g => g.name === "TGNS.");
        if (!guild) {
            console.error('Could not find the server "TGNS."');
            return;
        }

        const imageUrl = await getRandomImage();
        if (!imageUrl) return;

        const imageResponse = await fetch(imageUrl);
        const buffer = await imageResponse.arrayBuffer();

        await guild.setIcon(Buffer.from(buffer));
        console.log('Successfully changed server icon');
        return true;
    } catch (error) {
        console.error('Error changing server icon:', error);
        return false;
    }
}

client.on(Events.MessageCreate, async (message) => {
    // Check if the message mentions the bot and includes the word "change"
    if (message.mentions.has(client.user) && message.content.toLowerCase().includes('change')) {
        // Check if the user has the MANAGE_GUILD permission
        if (!message.member.permissions.has('ManageGuild')) {
            await message.reply('You need the "Manage Server" permission to use this command.');
            return;
        }

        await message.reply('Changing server profile picture...');
        const success = await changeServerIcon();

        if (success) {
            await message.reply('Server profile picture has been changed successfully!');
        } else {
            await message.reply('Failed to change server profile picture. Please check the logs for more details.');
        }
    }
});

client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);

    // Schedule the icon change for midnight every day
    cron.schedule('0 0 * * *', () => {
        changeServerIcon();
    }, {
        timezone: "UTC"
    });

    // Change icon immediately when bot starts (optional)
    changeServerIcon();
});

client.login(process.env.DISCORD_TOKEN); 