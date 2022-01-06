import time
from aiogram import Bot, Dispatcher, executor, types
import main
import json
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
def crypta(crp):
    url = f'https://min-api.cryptocompare.com/data/price?fsym={crp}&tsyms=USD'
    header = {
        'user-agent': UserAgent().random
    }

    answer = requests.get(url, headers=header)
    soup = BeautifulSoup(answer.text, 'lxml')
    return json.loads(soup.text)["USD"]

TOKEN = '5013239788:AAEburkdTg___aWDeT0xk7sh6K6aXe6-I3M'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup=main.menu)
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Запустить бота':
        btc, eth, doge, ltc = [42834.69], [3341.32], [0.1561], [133.53]
        while True:
            b_tc, e_th, d_oge, l_tc = crypta('BTC'), crypta('ETH'), crypta('DOGE'), crypta('LTC')
            btc.append(b_tc)
            eth.append(e_th)
            doge.append(d_oge)
            ltc.append(l_tc)
            print(btc, eth, doge, ltc, sep='----')
        #BTC
            if btc[0] > btc[-1]:
                persents_btc = ((btc[0] - btc[-1]) / btc[0]) * 100
                await bot.send_message(message.from_user.id, f'Курс BTC {btc[-1]} USD\n'
                                                             f'Курс BTC упал на {str(persents_btc)[:7]}%\n'
                                                             f'----------------')
            elif btc[0] < btc[-1]:
                persents_btc = ((btc[-1] - btc[0]) / btc[-1]) * 100
                await bot.send_message(message.from_user.id, f'Курс BTC {btc[-1]} USD\n'
                                                             f'Курс BTC вырос на {str(persents_btc)[:7]}%\n'
                                                             f'----------------')
            else:
                await bot.send_message(message.from_user.id, f'Курс BTC остался без изменений'
                                                             f'----------------')
        #ETH
            if eth[0] > eth[-1]:
                persents_eth = ((eth[0] - eth[-1]) / eth[0]) * 100
                await bot.send_message(message.from_user.id, f'Курс ETH {eth[-1]} USD\n'
                                                             f'Курс ETH упал на {str(persents_eth)[:7]}%\n'
                                                             f'----------------')
            elif eth[0] < eth[-1]:
                persents_eth = ((eth[-1] - eth[0]) / eth[-1]) * 100
                await bot.send_message(message.from_user.id, f'Курс ETH {eth[-1]} USD\n'
                                                             f'Курс ETH вырос на {str(persents_eth)[:7]}%\n'
                                                             f'----------------')
            else:
                await bot.send_message(message.from_user.id, f'Курс ETH остался без изменений'
                                                             f'----------------')
        #DOGE
            if doge[0] > doge[-1]:
                persents_doge = ((doge[0] - doge[-1]) / doge[0]) * 100
                await bot.send_message(message.from_user.id, f'Курс DOGE {btc[-1]} USD\n'
                                                             f'Курс DOGE упал на {str(persents_doge)[:7]}%\n'
                                                             f'----------------')
            elif doge[0] < doge[-1]:
                persents_doge = ((doge[-1] - doge[0]) / doge[-1]) * 100
                await bot.send_message(message.from_user.id, f'Курс DOGE {doge[-1]} USD\n'
                                                             f'Курс DOGE вырос на {str(persents_doge)[:7]}%\n'
                                                             f'----------------')
            else:
                await bot.send_message(message.from_user.id, f'Курс DOGE остался без изменений'
                                                             f'----------------')
        #LTC
            if ltc[0] > ltc[-1]:
                persents_ltc = ((ltc[0] - ltc[-1]) / ltc[0]) * 100
                await bot.send_message(message.from_user.id, f'Курс LTC {ltc[-1]} USD\n'
                                                             f'Курс LTC упал на {str(persents_btc)[:7]}%\n'
                                                             f'----------------')

            elif ltc[0] < ltc[-1]:
                persents_ltc = ((btc[-1] - btc[0]) / btc[-1]) * 100
                await bot.send_message(message.from_user.id, f'Курс LTC {ltc[-1]} USD\n'
                                                             f'Курс LTC вырос на {str(persents_ltc)[:7]}%\n'
                                                             f'----------------')
            else:
                await bot.send_message(message.from_user.id, f'Курс LTC остался без изменений'
                                                             f'----------------')
            await bot.send_message(message.from_user.id, '----Курсы криптовалют меняються----')
            time.sleep(30)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


