const Telegraf = require('telegraf').Telegraf
const { Keyboard, Key } = require('telegram-keyboard')
const flow = require('./bot-flow.json')
require('dotenv').config();

const bot = new Telegraf(process.env.TELEGRAF_BOT_TOKEN);

const backKeyboard = Keyboard.make(['Back'])

function main (ctx) {
  const welcomeMessage = 'Welcome to the Grow Ukraine Chat Bot'

  const { root } = flow
  const options = Object.keys(root.options)

  const buttons = options.map(option => Key.callback(option, options[option]))
  const keyboard = Keyboard.make([buttons])

  ctx.reply(welcomeMessage, keyboard.inline())
}

bot.start(main)

bot.on('callback_query', (ctx) => {
  const { data } = ctx.callbackQuery
  console.log('data', data)
  return ctx.answerCbQuery(data.toString())
})

bot.launch();
console.log('Grow Ukraine bot is connected');

