from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import db
def Startkeys():
 btn2 = KeyboardButton('Подать Заявку')
 greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
 greet_kb.add(btn2)
 return greet_kb

def Models(id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    for i in db.get_models(id):
        keyboard.add(InlineKeyboardButton(text=i['name']+','+i['old'] ,callback_data='model/'+str(i['id'])))
    return keyboard

def Zayvakikeys(user):
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text='✅Одобрить✅',callback_data='OK'+user)
    btn2 = InlineKeyboardButton(text='❌Отклонить❌',callback_data='NO'+user)
    btn3 = InlineKeyboardButton(text='🛑Заблокировать🛑',callback_data='BLOCK'+user)
    keyboard.add(btn1,btn2,btn3)
    return keyboard
def Vbiver_key_board():
    btn1 = KeyboardButton('⛔️Заблокировать воркера⛔️')
    btn2 = KeyboardButton('🦺Ворк/Стоп ворк🦺')
    btn3 = KeyboardButton('📥Возврат📥')
    btn4 = KeyboardButton('📤Оплата📤')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    greet_kb.add(btn1, btn2, btn3, btn4)
    return greet_kb
def Worker_key_board():
    btn1 = KeyboardButton('💼Профиль💼')
    btn2 = KeyboardButton('🏙Сменить Город🏙')
    btn3 = KeyboardButton('🖥Сайты🖥')
    btn4 = KeyboardButton('✉️Чаты✉️')
    btn5 = KeyboardButton('💃Добавить модель💃')
    btn6 = KeyboardButton('💃Удалить модель💃')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    greet_kb.add(btn1, btn2,btn3,btn4,btn5,btn6)
    return greet_kb

def Worker_Profile():
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text='Сменить рефералку', callback_data='change_ref')
    keyboard.add(btn1)
    return keyboard

def Workers(access,calldata):
    keyboard = InlineKeyboardMarkup(row_width=1)
    spisok = db.Workers_Information()
    le = len(db.Workers_Information())

    for i in range(le):
        if  spisok[i]['access'] == access:
         btn = InlineKeyboardButton(text=spisok[i]['username'], callback_data=calldata+'/'+spisok[i]['user_id'])
         keyboard.add(btn)
    return keyboard

def TC():
    btn1 = KeyboardButton('⛔️Заблокировать воркера⛔️')
    btn2 = KeyboardButton('✅Разблокировать воркера✅')
    btn3 = KeyboardButton('✅Добавить вбивера✅')
    btn4 = KeyboardButton('⛔️Удалить вбивера⛔️')
    btn5 = KeyboardButton('🦺Активность воркера🦺')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    greet_kb.add(btn2, btn1, btn3, btn4,btn5)
    return greet_kb
def success(id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text='✅Успешно', callback_data='success/' + id)
    btn2 = InlineKeyboardButton(text='❌Отклонено', callback_data='notsuccess/' + id)
    keyboard.add(btn1, btn2)
    return keyboard

