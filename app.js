const bot = require('./bot.js')
const express = require('express')
const { webhookCallback } = require('grammy')
require('dotenv').config()

const { TELEGRAM_BOT_TOKEN, GOOGLE_CLOUD_REGION, GOOGLE_CLOUD_PROJECT_ID } = process.env

// FUNCTION_TARGET is reserved Google Cloud Env
const domain =
  `https://${GOOGLE_CLOUD_REGION}-${GOOGLE_CLOUD_PROJECT_ID}.cloudfunctions.net/${process.env.FUNCTION_TARGET}`
const webhookUrl = `https://${domain}/${TELEGRAM_BOT_TOKEN}`
const app = express()

app.use(express.json())
app.use(`/${TELEGRAM_BOT_TOKEN}`, webhookCallback(bot, "express"))

app.listen(process.env.PORT, async () => {
  await bot.api
    .setWebhook(webhookUrl)
    .then(async () => {
      console.log(
        `Bot API Webhook has been set to ${webhookUrl}`
      )
      await bot.init()
    })
    .catch((error) => {
      console.log("Bot API Webhook setting failed:", error)
    })
})

exports.telegramBotWebhook = (req, res) => {
    bot.handleUpdate(req.body, res);
};
