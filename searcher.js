const { Api, TelegramClient } = require('telegram')
const { StringSession } = require('telegram/sessions')
const input = require('input')
require('dotenv').config();

const {
  TELEGRAM_API_ID,
  TELEGRAM_API_HASH,
  TELEGRAM_PHONE_NUMBER
} = process.env

const apiId = parseInt(TELEGRAM_API_ID, 10);

const stringSession = new StringSession('');

(async () => {
  async function login () {
    console.log('Loading interactive login');
    await client.start({
        phoneNumber: TELEGRAM_PHONE_NUMBER,
        phoneCode: async () => await input.text('Code:'),
        onError: (err) => console.log(err),
    });
    console.log('You are now connected');

    // TODO: Save this string to avoid logging in again
    console.log(client.session.save())
  }

  async function search () {
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

    console.log(`Search result for '${query}'`, res);

    search();
  }


  const client = new TelegramClient(
    stringSession,
    apiId,
    TELEGRAM_API_HASH,
    { connectionRetries: 5 }
  );

    await login();


    search();
})();


