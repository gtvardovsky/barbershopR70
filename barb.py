# - coding: utf-8 --
import telebotç
from telebot import types
TOKEN = '558806392:AAG9RMUkpApca1ka4MmOJyvEqEtf6vQdsjw'
bot = telebot.TeleBot(TOKEN)
i = 1
massPict = ['https://i.imgur.com/WiHYxNP.jpg', 'https://i.imgur.com/4xrFbyp.jpg','https://i.imgur.com/zxWlexE.jpg','https://i.imgur.com/BhgRWja.jpg','https://i.imgur.com/o9UESD4.jpg']

keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard.row('Записаться','Цены')
keyboard.row('Как доехать', 'О барбершопе')
keyboard.row('💈Специальное предложение💈')

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        '\n\nДобро пожаловать в мужскую парикмахерскую R70 💈\n\n☎️ 242-666\n📍 Пушкинская 235 \n↘️ Группа вк\nhttps://vk.com/r70_barbershop\n\nЗдесь вы сможете:\n\n- Записаться онлайн\n- Узнать о специальных предложениях\n- Узнать цены на наши услуги\n- Узнать как до нас добраться\n- Узнать о нас побольше',
        reply_markup = keyboard,
        disable_web_page_preview = True
        )

@bot.message_handler(content_types = ['text'])
def message(message):
    if (message.text == 'Записаться'):
        keyboardZap = types.InlineKeyboardMarkup()
        url_button1 = types.InlineKeyboardButton(text = "Запись онлайн", url = "https://n121609.yclients.com/")
        url_button2 = types.InlineKeyboardButton(text = "Группа Вк", url = "https://vk.com/r70_barbershop")
        keyboardZap.add(url_button1,url_button2)
        bot.send_message(
            message.chat.id,
            'Переходи по любой ссылке, выбирай удобное время, услугу и мастера 💈\n\nБудем рады тебя видеть👊😎',
            reply_markup = keyboardZap,
            disable_web_page_preview = True
        )
    if (message.text == 'Цены'):
        bot.send_message(
            message.chat.id,
            '💈Наши услуги💈\n\n- Мужская стрижка + мытьё головы + укладка = 500Rub\n\n- Мужской маникюр + экспресс уход за кожей рук = 300Rub\n\n- Бритьё/оформление усов и бороды = 400Rub\n\n- Укладка волос = 150Rub\n\n- Камуфляж седых волос = 500Rub\n\n- Восстанавливающие и увлажняющие маски для лица = 150Rub',
            reply_markup = keyboard
        )
    if (message.text == '💈Специальное предложение💈'):
        bot.send_message(
            message.chat.id,
            'В честь открытия нашей мужской парикмахерской R70 мы дарим тебе скидку в размере 10% на любую услугу или товар 🔥\n\nА если ты придёшь к нам на стрижку 2 раза за месяц, то третья обойдётся тебе всего за 100 рублей 😎',
            reply_markup = keyboard
        )
    if (message.text == 'Как доехать'):
        keyboardNavigator = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text = "Показать на карте", url = "https://goo.gl/ky6ofz")
        keyboardNavigator.add(url_button)
        bot.send_message(
            message.chat.id,
            'Мы находимся по адресу улица Пушкинская 235',
            reply_markup = keyboardNavigator
        )
    if message.text == 'О барбершопе':
        kb = types.InlineKeyboardMarkup()
        kb.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in ['▶']])
        bot.send_message(message.chat.id,
                         '<a href="https://i.imgur.com/GxoDlWn.jpg">В детстве я не любил парикмахерские, в которые меня водила мама. Разговоры пухленьких парикмахерш о кредитах, ноготочках и своих "проблемах" раздражали меня, но главной проблемой была стрёмная стрижка. Никто не понимал какую прическу я хочу и не мог подобрать что-то интересное.\n\nСо временем ничего не изменилось. Я ходил во многие Ижевские парикмахерские, но везде чего-то не хватало. В одном месте уровень навыков мастера был слишком низким, а интерьер крутым и работа с клиентами была на высоте. В другом были хорошие мастера, слишком простой интерьер и ужасная организация. В третьем все было здорово, но цена не позволяла посещать данный салон больше одного раза в месяц и всегда ходить с идеальной причёской.\n\nЯ решил, что в будущем открою свою парикмахерскую для мужчин, возьму все самое лучшее и добавлю своих фишек.\n\nПрошло много лет, и я наконец-то открыл такое заведение, где подстригаюсь сам</a>',
                         reply_markup = kb,
                         parse_mode = "HTML")


@bot.callback_query_handler(func = lambda c: True)
def inline(c):
    global i
    global massPict
    kb = types.InlineKeyboardMarkup()
    if c.data == '▶':
        if (i != 4):
            kb.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in ['◀','▶']])
        else:
            kb.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in ['◀']])
        bot.edit_message_text(
            chat_id = c.message.chat.id,
            message_id = c.message.message_id,
            text = '<a href="{pict}">В детстве я не любил парикмахерские, в которые меня водила мама. Разговоры пухленьких парикмахерш о кредитах, ноготочках и своих "проблемах" раздражали меня, но главной проблемой была стрёмная стрижка. Никто не понимал какую прическу я хочу и не мог подобрать что-то интересное.\n\nСо временем ничего не изменилось. Я ходил во многие Ижевские парикмахерские, но везде чего-то не хватало. В одном месте уровень навыков мастера был слишком низким, а интерьер крутым и работа с клиентами была на высоте. В другом были хорошие мастера, слишком простой интерьер и ужасная организация. В третьем все было здорово, но цена не позволяла посещать данный салон больше одного раза в месяц и всегда ходить с идеальной причёской.\n\nЯ решил, что в будущем открою свою парикмахерскую для мужчин, возьму все самое лучшее и добавлю своих фишек.\n\nПрошло много лет, и я наконец-то открыл такое заведение, где подстригаюсь сам</a>'.format(pict = massPict[i]),
            reply_markup = kb,
            parse_mode = 'HTML')
        i = i + 1

    if c.data == '◀':
        if (i != 0):
            kb.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in ['◀','▶']])
        else:
            kb.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in ['▶']])
        i = i - 1
        bot.edit_message_text(
            chat_id = c.message.chat.id,
            message_id = c.message.message_id,
            text = '<a href="{pict}">В детстве я не любил парикмахерские, в которые меня водила мама. Разговоры пухленьких парикмахерш о кредитах, ноготочках и своих "проблемах" раздражали меня, но главной проблемой была стрёмная стрижка. Никто не понимал какую прическу я хочу и не мог подобрать что-то интересное.\n\nСо временем ничего не изменилось. Я ходил во многие Ижевские парикмахерские, но везде чего-то не хватало. В одном месте уровень навыков мастера был слишком низким, а интерьер крутым и работа с клиентами была на высоте. В другом были хорошие мастера, слишком простой интерьер и ужасная организация. В третьем все было здорово, но цена не позволяла посещать данный салон больше одного раза в месяц и всегда ходить с идеальной причёской.\n\nЯ решил, что в будущем открою свою парикмахерскую для мужчин, возьму все самое лучшее и добавлю своих фишек.\n\nПрошло много лет, и я наконец-то открыл такое заведение, где подстригаюсь сам</a>'.format(pict = massPict[i]),
            reply_markup = kb,
            parse_mode = 'HTML')

bot.polling()
