const fs = require('fs').promises
const { Api, TelegramClient } = require('telegram')
const { StringSession } = require('telegram/sessions')
const input = require('input')
require('dotenv').config();

const {
  TELEGRAM_API_ID,
  TELEGRAM_API_HASH,
  TELEGRAM_PHONE_NUMBER,
} = process.env

const SESSION_KEY_FILE = './sessionKey.txt'

const apiId = parseInt(TELEGRAM_API_ID, 10);

async function getSavedSessionKey () {
  const data = await fs.readFile(SESSION_KEY_FILE, 'utf8')
  return data
}

async function login (client) {
  console.log('Loading interactive login');

  await client.start({
    phoneNumber: TELEGRAM_PHONE_NUMBER,
    phoneCode: async () => await input.text('Code:'),
      onError: (err) => console.log(err),
  });
  console.log('You are now connected');

  // Save session key to avoid login every time
  fs.writeFile(SESSION_KEY_FILE, client.session.save())
}

async function search (client) {
  const query = await input.text('Query:')

  const ONE_DAY = 86400; // seconds
  const NUMBER_OF_DAYS = 7; // how many days to search back

  const res = await client.invoke(new Api.messages.SearchGlobal({
    flags: 1,
    folderId: 0,
    q: query,
    filter: new Api.ChannelMessagesFilterEmpty(),
    minDate: (Date.now()/1000) - (ONE_DAY * NUMBER_OF_DAYS),
    offsetRate: 0,
    offsetPeer: new Api.InputPeerEmpty(),
    offsetId: 0,
    limit: 10,
  }));

  const filteredResults = res.messages.reduce((filtered, messageObject) => {
    const { scam, message, fromId, peerId } = messageObject

    const userId = fromId ? fromId.userId : peerId.userId

    if (!scam) {
      filtered.push({
        message,
        userId,
      })
    }

    return filtered
  }, [])

  console.log(`Search result for '${query}'`, filteredResults);

  search();
}

async function init () {
  const sessionKey = await getSavedSessionKey()

  const client = new TelegramClient(
    new StringSession(sessionKey),
    apiId,
    TELEGRAM_API_HASH,
    { connectionRetries: 5 }
  );

  if (!client.session.save()) await login(client);

  search(client);
}

init()

