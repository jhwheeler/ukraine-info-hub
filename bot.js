const { Bot, InlineKeyboard } = require('grammy')
const messages = require('./messages.json')
require('dotenv').config();

const bot = new Bot(process.env.TELEGRAM_BOT_TOKEN);

const ActionType = {
  Link: 'link',
  Input: 'input',
}

const MESSAGE_NOT_FOUND = "Sorry, I don't understand your message. Please try something else."

function generateKeyboard (node) {
  let keyboard = new InlineKeyboard()

  for (const button of messages[node].buttons) {
    keyboard = keyboard.text(button.message, JSON.stringify(button.action))
  }

  return keyboard
}

function init (ctx) {
  const welcomeMessage = 'Welcome to the Grow Ukraine Chat Bot'
  const keyboard = generateKeyboard('root')

  ctx.reply(welcomeMessage, { reply_markup: keyboard })
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
      ctx.reply(message, { reply_markup: keyboard })
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

  return ctx.answerCallbackQuery('Loading...')
}

bot.start()
bot.command('start', init)

bot.on('callback_query:data', (ctx) => handleCallback(ctx))

console.log('Grow Ukraine bot is connected');

