const Telegraf = require('telegraf').Telegraf
require('dotenv').config();

console.log('Ukraine Info Hub Bot is running');

const bot = new Telegraf(process.env.TELEGRAF_BOT_TOKEN);

bot.start(ctx => ctx.reply('Welcome to the Ukraine Info Hub. Our mission is to connect people in need with those who can help. This bot is currently under construction.'));

bot.launch();
