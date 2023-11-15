import sqlite3

import requests
from pyrogram import Client
from pyrogram import types, filters



database = sqlite3.connect('database_WTB_parser.db', check_same_thread=False)
sql = database.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS messages
                (user_id INTEGER,
                 message_text TEXT)''')
database.commit()

CHANNEL_ID = ['Crypto Taverna OTC', '2TOP OTC', 'OTC ICOBOG', 'Accounts & Social Media Market', 'криптапиражок 🍰 | OTC', 'OTC | SWOP TOKY', 'OTC Bull Market', 'OTC Market ICO/Whitelist - SCrypt',
              'OTC MARKET | INVESTORS HUB', 'Magic Eden | OTC Market', 'OTC | 9RSxTAF', 'TVS OTC', '++4Plus++OTC|ICO|IDO|Coinlist account', 'ENJOY OTC 🤝', 'Media OTC', 'Official Crypto Pro Marketplace',
              'NFT OTC HUB', "Sell Buy Accounts OTC'", 'Topclub OTC', 'OTC BOX', 'OTC | Aquatorium', 'CRYPTO SPACE | OTC', 'Publish OTC [NFT | WL | CRYPTO]', 'CRYPTO MARKET | OTC',
              'OTC • TRUST', 'OTC 37', 'Offerum OTC Market']

app = Client(
    "Parser_WTB",
    api_id=,
    api_hash=""
)

header = {
        'authorization': ''
    }


@app.on_message(filters=filters.group)
def my_handler(client: Client, message: types.Message):
    if message.chat.title not in CHANNEL_ID:
        return

    # rules eu binance scam russia

    # verify

    # print(message.text)



    try:

        if 'wtb' in message.text.lower() and 'wl' in message.text.lower() and 'channel' not in message.text.lower() and 'канал' not in message.text.lower() and 'rules' not in message.text.lower() and 'работ' not in message.text.lower():

            sql.execute(
                f'''SELECT user_id FROM messages WHERE user_id = {message.from_user.id} AND message_text = "{message.text}"''')
            de = sql.fetchone()
            print(de)

            # print(message.text)

            if de == None:

                sql.execute('''INSERT INTO messages VALUES (?,?)''', (message.from_user.id, message.text))
                database.commit()

                print(message.chat.id, message.from_user.id)
                # Как-то обработать сообщение с канала, например, напечатать его текст
                print(message.text + '\n\n')

                payload = {'content': f'{message.text}\n\n'
                                      f'TG Username: **@{message.from_user.username}**'}

                if message.from_user.username == None:
                    pass
                else:
                    requests.post('https://discord.com/api/v9/channels/?/messages', data=payload, headers=header)

    except Exception as e:
        print(e)
        pass

app.run()
