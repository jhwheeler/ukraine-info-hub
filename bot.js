const Telegraf = require('telegraf').Telegraf
const { Keyboard, Key } = require('telegram-keyboard')
const messages = require('./messages.json')
require('dotenv').config();

const bot = new Telegraf(process.env.TELEGRAF_BOT_TOKEN);

const MESSAGE_NOT_FOUND = "Sorry, I don't understand your message. Please try something else."

function generateKeyboard (node) {
  const buttons = messages[node].buttons
    .map(button => Key.callback(button.message, JSON.stringify(button.action)))

  return Keyboard.make([buttons])
}

function init (ctx) {
  const welcomeMessage = 'Welcome to the Grow Ukraine Chat Bot'
  const keyboard = generateKeyboard('root_message')

  ctx.reply(welcomeMessage, keyboard.inline())
}

bot.start(init)

bot.on('callback_query', (ctx) => {
  const data = JSON.parse(ctx.callbackQuery.data)
  console.log('data', data)

  if (data.type === 'link') {
    const destination = messages[data.destination]
    if (!destination) {
      ctx.reply(MESSAGE_NOT_FOUND)
      return
    }

    const { message } = destination
    if (!message) return

    ctx.reply(message)
  }

  return ctx.answerCbQuery('Loading...')
})

bot.launch();

console.log('Grow Ukraine bot is connected');

