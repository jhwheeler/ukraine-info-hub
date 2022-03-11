const Telegraf = require('telegraf').Telegraf
const { Keyboard, Key } = require('telegram-keyboard')
const messages = require('./messages.json')
require('dotenv').config();

const bot = new Telegraf(process.env.TELEGRAF_BOT_TOKEN);

const ActionType = {
  Link: 'link',
  Input: 'input',
}

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

function navigate (ctx, destination) {
    const destinationValue = messages[destination]
    if (!destinationValue) {
      ctx.reply(MESSAGE_NOT_FOUND)
      return
    }

    const { message, buttons } = destinationValue
    if (!message) return

    if (buttons) {
      const keyboard = generateKeyboard(destination)
      ctx.reply(message, keyboard.inline())
      return
    }

    ctx.reply(message)
}

function handleCallback (ctx) {
  const data = JSON.parse(ctx.callbackQuery.data)
  console.log('data', data)

  const { destination, type } = data

  if (type === ActionType.Link) {
    navigate(ctx, destination)
  }

  return ctx.answerCbQuery('Loading...')
}

bot.start(init)

bot.on('callback_query', (ctx) => handleCallback(ctx))

bot.launch();

console.log('Grow Ukraine bot is connected');

