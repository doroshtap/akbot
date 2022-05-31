import aiogram
import db
import logging
from aiogram.types import InputFile
import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram import Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import keyboard

from util import fix_str

# Объект бота
bot = Bot(token=config.TOKEN,parse_mode='HTML')
chat_zayavok_id = config.id_chat_zaivok
# Диспетчер для бота
prof = 0
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
class profit(StatesGroup):
    p = State()
@dp.message_handler(state = profit.p) #первая стадия
async def Profit(message:types.Message , state: FSMContext):
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(p = answer)#добавляю полученную инфу в класс выше
     async with state.proxy() as data:
         ad = data['ad']
         typ = data['type']
     db.make_profit(answer, ad)
     if typ == 'bank':
      await bot.send_message(config.TS_id, text=db.Log_to_TS(ad,fix_str('Оплата'),answer),reply_markup=keyboard.success(str(ad)))
     elif typ == 'refund':
      await bot.send_message(config.TS_id, text=db.Log_to_TS(ad,fix_str('Возврат'),answer),reply_markup=keyboard.success(str(ad)))
     elif typ == 'ctrahovka':
         await bot.send_message(config.TS_id, text=db.Log_to_TS(ad, fix_str('Страховка'), answer),
                                reply_markup=keyboard.success(str(ad)))

    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
    await state.finish()
class Register(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
class New_City(StatesGroup):
    city = State()
class refund(StatesGroup):
    s = State()
class Model(StatesGroup):
    q0 = State()
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    q8 = State()
    q9 = State()
    q10 = State()
    q11 = State()
    q12 = State()
    q13 = State()
    q14 = State()
@dp.message_handler(state = Model.q0)
async def answer_q1(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Возраст:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q0 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q1)
async def answer_q2(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Рост:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q1 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q2)
async def answer_q3(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Вес:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q2 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q3)
async def answer_q4(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Размер груди:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q3 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q4)
async def answer_q5(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Цвет волос:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q4 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q5)
async def answer_q6(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Национальность:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q5 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q6)
async def answer_q7(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Внешность:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q6 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q7)
async def answer_q8(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Цена за час:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q7 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q8)
async def answer_q9(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Цена за два часа:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q8 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q9)
async def answer_q10(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Цена за ночь:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q9 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q10)
async def answer_q11(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Ссылку на первое фото:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q10 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q11)
async def answer_q12(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Ссылку на второе фото:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q11 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q12)
async def answer_q13(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Ссылку на третье фото:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q12 = answer)#добавляю полученную инфу в класс выше
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q13)
async def answer_q14(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Статус:'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q13 = answer)#добавляю полученную инфу в класс выше
     #db.add_model(data.get('q0'),data.get('q1'),data.get('q2'),data.get('q3'),data.get('q4'),data.get('q5'),data.get('q6'),data.get('q7'),data.get('q8'),data.get('q9'),data.get('q10'),data.get('q11'),data.get('q12'),data.get('q13'),data.get('q14'),message.from_user.id)
     await Model.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Model.q14)
async def answer_q15(message:types.Message , state: FSMContext):
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q14 = answer)#добавляю полученную инфу в класс выше
     data = await state.get_data()
     db.add_model(data.get('q0'),data.get('q1'),data.get('q2'),data.get('q3'),data.get('q4'),data.get('q5'),data.get('q6'),data.get('q7'),data.get('q8'),data.get('q9'),data.get('q10'),data.get('q11'),data.get('q12'),data.get('q13'),data.get('q14'),message.from_user.id)

     await bot.send_message(message.from_user.id,text=fix_str('Добавлена!'))
     await state.finish()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))



@dp.message_handler(state = refund.s) #первая стадия
async def Refund(message:types.Message , state: FSMContext):
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(s = answer)#добавляю полученную инфу в класс выше
     await message.answer(fix_str('Ссылка:'))
     await message.answer('<code>' + config.refund_link + '&r=' + str(message.from_user.id) +  '&amount=' + answer+'</code>')

    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
    await state.finish()
class payment(StatesGroup):
    s = State()
@dp.message_handler(state = payment.s) #первая стадия
async def Pay(message:types.Message , state: FSMContext):
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(s = answer)#добавляю полученную инфу в класс выше
     await message.answer(fix_str('Ссылка:'))
     await message.answer('<code>' + config.payment_link + '&r=' + str(message.from_user.id) +  '&amount=' + answer+'</code>')

    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
    await state.finish()


@dp.message_handler(state = New_City.city) #первая стадия
async def city(message:types.Message , state: FSMContext):
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(city = answer)#добавляю полученную инфу в класс выше
     db.set_city(message.from_user.id,answer)
     await message.answer(fix_str('Город изменён на ') + answer)
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
    await state.finish()

@dp.message_handler(state = Register.q1) #первая стадия
async def answer_q1(message:types.Message , state: FSMContext):
    await message.answer(fix_str('Какой опыт в скаме в общем и исключительно в антикино/эскорте?'))
    try:
     answer = message.text #добавляю текст от пользователя в переменную
     await state.update_data(q1 = answer)#добавляю полученную инфу в класс выше
     await Register.next()
    except Exception:
        await message.answer(fix_str('Вводите корректные данные!'))
@dp.message_handler(state = Register.q2)
async def answer_q2(message:types.Message , state: FSMContext):
     await message.answer(fix_str('Сколько времени готов уделять работе?'))
     try:
       answer2 = message.text #добавляю текст в переменную
       await state.update_data(q2 = answer2)#добавляю полученную инфу в класс выше
       await Register.next()
     except Exception:
         await message.answer(fix_str('Вводите корректные данные!'))



@dp.message_handler(state = Register.q3)
async def answer_q3(message:types.Message , state: FSMContext):
     try:
      answer3 = message.text #добавляю текст в переменную
      await state.update_data(q3 = answer3)#добавляю полученную инфу в класс выше
     except Exception:
         await message.answer(fix_str('Вводите корректные данные!'))
     data = await state.get_data()
     a = data.get('q1')
     b= data.get('q2')
     c = data.get('q3')

     text = fix_str('<b>Заявка от - </b>') + ' <b> @'+message.from_user.username+'</b>'+'\n'+fix_str('<b>Откуда узнал: </b> ') +a+'\n'+fix_str('<b>Опыт работы: </b> ')+b+'\n'+fix_str('<b>Сколько готов уделять работе: </b> ')+c
     await  bot.send_message(message.from_user.id, text=fix_str('Ваша заявка принята,ожидайте ответа'))
     await bot.send_message(chat_zayavok_id,text,reply_markup=keyboard.Zayvakikeys(str(message.from_user.id)))
     await state.finish() #конец


@dp.message_handler(commands="vbv")
async def VB(message: types.Message):
    txt = fix_str('Вбиверы на месте:\n')
    for i in db.get_vbivers_onwork():
        txt += "@"+i+'\n'
    await bot.send_message(message.from_user.id,text=txt)
# start
@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    if message.from_user.id in db.get_blocked():
        await message.answer(fix_str("Вы заблокированы"))
    else:
        await message.answer(fix_str("Добро Пожаловать!"), reply_markup=keyboard.Startkeys())
        if message.from_user.id in db.get_worker() and db.get_acses_level(message.from_user.id) == 0:
          await message.answer(fix_str("Начинаем Работать!"), reply_markup=keyboard.Worker_key_board())
        if message.from_user.id in db.get_worker() and db.get_acses_level(message.from_user.id) == 1:
            await message.answer(fix_str("Начинаем Работать!"), reply_markup=keyboard.Vbiver_key_board())
        if message.from_user.id == config.TS_id or db.get_acses_level(message.from_user.id) == 2:
            await message.answer(fix_str("Начинаем Работать!"), reply_markup=keyboard.TC())
# Обработка сообщений
@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text == fix_str('Подать Заявку'):
        if db.make_zaivka(msg.from_user.id, msg.from_user.username):
            await msg.answer(fix_str("Напиши откуда ты узнал про нашу команду:"))
            await Register.q1.set()
        else:
            await msg.answer(fix_str("Вы уже подавали заявку"))

    if db.get_acses_level(msg.from_user.id) == 0:
     if msg.text == fix_str('💃Добавить модель💃'):
      await bot.send_message(msg.from_user.id, text=fix_str('Введите имя модели:'))
      await Model.q0.set()
     if msg.text == fix_str('💃Удалить модель💃'):
         await bot.send_message(msg.from_user.id, text=fix_str('Модели:'),
                                reply_markup=keyboard.Models(msg.from_user.id))
     if msg.text == fix_str('💼Профиль💼'):
        photo = InputFile("img1.jpg")
        data = db.get_Worker_information(msg.from_user.id)
        rank = str(data[0]['rank'])
        referalka = str(data[0]['promocode'])
        profit = str(data[0]['profit_sum'])
        city = str(data[0]['city'])
        await bot.send_photo(chat_id=msg.chat.id, photo=photo,caption=fix_str('<b>Профиль:</b>\n')+fix_str('<b>💼Ранг - ')+rank+fix_str('</b>\n<b>💰Заработано - ')+
                             profit+fix_str(' ₽ </b>\n<b>🏙Город - ')+city+fix_str('</b>\n<b>🔴Рефералка - ')+referalka+'</b>')
     if msg.text == fix_str('✉️Чаты✉️'):
        await msg.answer(fix_str('<b>Выплаты: </b>')) +str(config.channel_viplot)+fix_str('\n<b>Чат: </b>') + config.chat_workerov_link)
     if msg.text == fix_str('🏙Сменить Город🏙'):
        await msg.answer(fix_str("Напиши название города:"))
        await New_City.city.set()
     if msg.text == fix_str('🖥Сайты🖥'):
        st = ''
        for i in range(len(config.links)):
            st  =st+'<code>'+config.links[i]+'?&ref='+db.get_referal(msg.from_user.id)+'&city='+db.get_city(msg.from_user.id)+'</code>\n'
        await msg.answer(fix_str("<b>Твои ссылки:</b> \n")+st)
    elif db.get_acses_level(msg.from_user.id) == 1 and  msg.from_user.id != config.TS_id:
        if msg.text ==fix_str('⛔️Заблокировать воркера⛔️'):
            await msg.answer(fix_str("Воркеры:"),reply_markup=keyboard.Workers(0,'zablokirovat'))
        if msg.text == fix_str('🦺Ворк/Стоп ворк🦺'):
            if db.work_nowork(msg.from_user.id) == 1:
             await bot.send_message(config.chat_workerov_id,text=fix_str('<b>🦺Вбивер @')+ msg.from_user.username+fix_str(' работает🦺')+'</b>')
            else :
                await bot.send_message(config.chat_workerov_id,
                                       text=fix_str('<b>🦺Вбивер @') + msg.from_user.username + fix_str(' отошёл🦺') + '</b>')
        if  msg.text == fix_str('📥Возврат📥'):
            await msg.answer(fix_str('Введите сумму:'))
            await refund.s.set()
        if  msg.text == fix_str('📤Оплата📤'):
            await msg.answer(fix_str('Введите сумму:'))
            await payment.s.set()
    if  msg.from_user.id == config.TS_id:
        if msg.text == fix_str('⛔️Заблокировать воркера⛔️'):
            await msg.answer(fix_str("Воркеры:"), reply_markup=keyboard.Workers(0,'zablokirovat'))
        if msg.text == fix_str('⛔️Удалить вбивера⛔️'):
            await msg.answer(fix_str("Вбиверы:"), reply_markup=keyboard.Workers(1,'udalitvbivera'))
        if msg.text == fix_str('✅Разблокировать воркера✅'):
            await msg.answer(fix_str("Заблокированные:"), reply_markup=keyboard.Workers(-1,'razblokirovat'))
        if msg.text == fix_str('✅Добавить вбивера✅'):
            await msg.answer(fix_str("Воркеры:"), reply_markup=keyboard.Workers(0,'addvbiver'))
        if msg.text == fix_str('🦺Активность воркера🦺'):
            await msg.answer(fix_str("Воркеры:"), reply_markup=keyboard.Workers(0, 'stata'))




@dp.callback_query_handler(lambda call: True)
async def zayavki(callback_query: types.CallbackQuery, state: FSMContext):

    data = db.get_zaivky()
    new = []
    new1 = []
    new2 = []
    for i in range(len(data)):
        new.append('OK'+str(data[i]['id']))
        new1.append('NO' + str(data[i]['id']))
        new2.append('BLOCK' + str(data[i]['id']))
    for i in range(len(new)):
        if callback_query.data == new[i] and (config.TS_id == callback_query.from_user.id):
            if db.add_new_worker(data[i]['id'],data[i]['username']) == True :
             await bot.send_message(data[i]['id'],text=fix_str('Вы приняты!'),reply_markup=keyboard.Worker_key_board())
             break
            else:
               continue
        if callback_query.data == new1[i]:
            await bot.send_message(data[i]['id'], text=fix_str('Вам Отказано'))
            break
        if callback_query.data == new2[i]:
            await bot.send_message(data[i]['id'], text=fix_str('Вы Заблокированы'))
            db.block(data[i]['id'])
            break
        data = db.get_zaivky()
    users = db.get_worker()
    if callback_query.data.split('/')[0] in ['addvbiver','stata','zablokirovat','razblokirovat','udalitvbivera']:
     for i in range(len(users)):
        if callback_query.data == 'addvbiver/' + str(users[i]):
            db.make_vbiver(users[i])
            await callback_query.message.edit_text(text=fix_str('Воркеры:'), reply_markup=keyboard.Workers(0,'addvbiver'))
        elif callback_query.data == 'stata/' + str(users[i]):
            stats =  db.stats(users[i])
            usr =db.Worker_username(users[i])
            txt = '<b>Статистика переходов</b> @')+usr+':\n'
            txt += '<b>За день: </b>')+str(stats[0])+'\n'
            txt+= '<b>За неделю: </b>')+str(stats[1])+'\n'
            txt +='<b>За месяц: </b>') +str(stats[2])
            await bot.send_message(callback_query.from_user.id,text=txt, reply_markup=keyboard.Workers(0,'stata'))
        elif callback_query.data =='zablokirovat/'+str(users[i]):
            db.block(users[i])
            await callback_query.message.edit_text(text=fix_str('Воркеры'), reply_markup=keyboard.Workers(0,'zablokirovat'))
        elif callback_query.data =='razblokirovat/'+str(users[i]):
            db.unblock(users[i])
            await callback_query.message.edit_text(text=fix_str('Заблокированные:'),reply_markup=keyboard.Workers(-1,'razblokirovat'))
        elif callback_query.data == 'udalitvbivera/' + str(users[i]):
            db.block(users[i])
            await callback_query.message.edit_text(text=fix_str('Вбиверы:'), reply_markup=keyboard.Workers(1,'udalitvbivera'))
        users = db.get_worker()


    ad = db.adverts()
    if callback_query.data.split('/')[0] == 'vbit':
     for i in range(len(ad)):
       if callback_query.data =='vbit/'+str(ad[i]):
         if db.Status_of_advert(db.adverts()[i]) == 0:

            await bot.send_message(callback_query.from_user.id, text=db.Log_to_vbiver(ad[i]))
            db.addvbiver_to_advert(ad[i], callback_query.from_user.id)
         else:
             await bot.answer_callback_query(callback_query.id, text=fix_str('Кто-то уже взял этот лог'), show_alert=True)
       ad = db.adverts()

    if callback_query.data.split('/')[0] == 'model':
        for i in db.get_models(callback_query.from_user.id):
            if callback_query.data == 'model/'+str(i['id']):
                db.delete_model(i['id'])
                await callback_query.message.edit_text( text=fix_str('Модели:'),
                                       reply_markup=keyboard.Models(callback_query.from_user.id))
    if callback_query.data.split('/')[0] in ['pay', 'refund', 'ctrahovka', 'success', 'notsuccess']:
      for i in range(len(db.adverts())):
        if callback_query.data == 'pay/' + str(ad[i]):
            db.adverts2(ad[i], 'bank')
            async with state.proxy() as data:
                data['ad'] = ad[i]
                data['type'] = 'bank'
            await bot.send_message(callback_query.from_user.id,text=fix_str('Введите профит:'))
            await profit.p.set()
        elif callback_query.data == 'refund/' + str(ad[i]):
            db.adverts2(ad[i], 'refund')
            async with state.proxy() as data:
                data['ad'] = ad[i]
                data['type'] = 'refund'
            await bot.send_message(callback_query.from_user.id, text=fix_str('Введите профит:'))
            await profit.p.set()
        elif callback_query.data == 'ctrahovka/' + str(ad[i]):
            async with state.proxy() as data:
                data['ad'] = ad[i]
                data['type'] = 'ctrahovka'
            db.adverts2(ad[i],'ctrahovka')
            await bot.send_message(callback_query.from_user.id, text=fix_str('Введите профит:'))
            await profit.p.set()
        elif callback_query.data == 'success/'+str(ad[i]) and callback_query.from_user.id == config.TS_id:
            if db.adverts1(ad[i]) == 'bank':
                tx  = db.add_profit(ad[i],config.procent_vbiver_bank,config.procent_worker_bank)
            elif db.adverts1(ad[i]) == 'refund':
                tx = db.add_profit(ad[i], config.procent_vbiver_refund, config.procent_worker_refund)
            elif db.adverts1(ad[i]) == 'ctrahovka':
                tx = db.add_profit(ad[i], config.procent_vbiver_ctrahovka, config.procent_worker_ctrahovka)


            res = fix_str('❗️<b>Новая Оплата</b>❗️\n\n')
            res += fix_str('     👨‍💻<b>Вбивер:</b> @') + tx[1][1]+ '\n\n'
            res += fix_str('     🦺<b>Воркер: </b> @') + tx[1][0] + '\n\n'
            res += fix_str('     💰<b>Профит: ') + str(tx[0][0]) + fix_str('</b>₽\n\n')
            await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await  bot.send_message(callback_query.from_user.id, text=fix_str("Отправлено в выплаты"))
            await  bot.send_message(config.channel_viplot,text=res)
            db.delete_advert(ad[i])
        elif callback_query.data == 'notsuccess/'+str(ad[i])  and callback_query.from_user.id == config.TS_id:
            await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await  bot.send_message(callback_query.from_user.id, text=fix_str("Отклонено"))

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)