import vk_api, random, requests, json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = ''

def read_message(text):
    types       = ['voice', 'text', 'photo']
    type        = random.choice(types)
    try:
        second_word = text.split(' ')[1].lower()
    except:
        second_word = ''
    finally:
        first_word  = text.split(' ')[0].lower()
        random_int  = random.randint(0, 100)
        if first_word == 'кос' or first_word == 'кос,':
            kos_listen(' '.join(text.split(' ')[1:]))
            if second_word:
                if second_word == 'фото': type = 'photo'
                if second_word == 'гс':   type = 'voice'
                if second_word == 'текст': type = 'text'
            random_int = 1
        if random_int >= 10: type = 'no'
        # print(random_int, type)
        return type

def kos_listen(text):
    print('kos_listen:', text)

def send_voice_on_server(url):
    rnd   = str(random.randint(0, 34))
    audio = open(f'C:/python-projects/vk_bots/kos/voices/{rnd}.mp3', 'rb')
    send  = requests.post(url['upload_url'], files = {'file': audio}).json()
    return send['file']

def main():

    replies = [
        "АРМ",
        "Флёпа, засранец!",
        "За Кожина и Мошкина - АРМ логистов",
        "Как у Вас с процессом написания диплома?",
        "Аа касательно диплома, что?",
        "Сейчас работаю над новым АРМ",
        "Я сейчас себя очень плохо чвствую",
        "Очень плохо!",
        "Два?",
        "Один?",
        "Пять?",
        "Что здесь вообще происходит?",
        "Биг бойс плэйнг виз дипломс",
        "Ни кому это не нужно",
        "Твоя подружка дрочит, на мой диплом у клуба",
        "Насилуют! АРМ-логистов носилуют! Совсем ахуели!",
        "5 дипломов спиздили АРМа",
        "сучьё",
        "падонки",
        "вот засранец",
        "могу яишницу приготовить",
        "Я смотрю вы к защите не готовитесь?",
        "завтра - Краков",
        "студент, лишенный головного мозга, отказывается от АРМ-диплома",
        "честно говоря, я в ахуе",
        "у нас так всё просто, посмотришь на поросёнка - он тебя понимает",
        "пойдём со мной...",
        "я расскажу тебе сказку",
        'ганглии головного мозга, голожаберных молюсков Тритонии',
        'Ты! В жопе оказался!',
        "мудачьё"
    ]

    photo_album = [
        'photo-202781313_457239031',
        'photo-202781313_457239032',
        'photo-202781313_457239033',
        'photo-202781313_457239034',
        'photo-202781313_457239035',
        'photo-202781313_457239036',
        'photo-202781313_457239037',
        'photo-202781313_457239038',
        'photo-202781313_457239039'
    ]

    bot_session = vk_api.VkApi(token = token)
    bot_api     = bot_session.get_api()
    group_id    = '202781313'
    longpoll    = VkBotLongPoll(bot_session, group_id)

    for event in longpoll.listen():


        # ЕСЛИ ПРИШЛО НОВОЕ СООБЩЕНИЕ
        if (event.type == VkBotEventType.MESSAGE_NEW):

            def send_message():
                bot_api.messages.send(
                    random_id   =   random.getrandbits(32),
                    peer_id     =   event.obj.message['peer_id'],
                    message     =   message,
                    attachment  =   attachment
                    )

            message_text = event.object.message['text']
            from_id      = event.object.message['from_id']
            message      = ''
            attachment   = ''

            message_type = read_message(message_text)
            if message_type == 'no':
                ...
            if message_type == 'text':
                message    = random.choice(replies)
                send_message()
            if message_type == 'photo':
                message    = random.choice(replies)
                attachment = random.choice(photo_album)
                send_message()
            if message_type == 'voice':

                # Загрузка аудио файла на сервер
                url = bot_api.docs.getMessagesUploadServer(
                    type    = 'audio_message',
                    peer_id = event.obj.message['peer_id']
                )

                # Отправка аудио файла на сервер
                file = send_voice_on_server(url)

                # Сохранение файла
                save = bot_api.docs.save(file = file)
                owner_id = save['audio_message']['owner_id']
                audio_id = save['audio_message']['id']

                # формирование названия файла
                attachment = 'save: ', f'doc{owner_id}_{audio_id}'
                send_message()

        print(f'{from_id} написал: "{message_text}" type: {message_type}')

if __name__ == '__main__': main()

        #
        #     if event.from_me:
        #         print('От меня для: ', end='')
        #     elif event.to_me:
        #         print('Для меня от: ', end='')
        #
        #     if event.from_user:
        #         print(event.user_id)
        #     elif event.from_chat:
        #         print(event.user_id, 'в беседе', event.chat_id)
        #     elif event.from_group:
        #         print('группы', event.group_id)
        #
        #     print('Текст: ', event.text)
        #     print()
        #
        # elif event.type == VkEventType.USER_TYPING:
        #     print('Печатает ', end='')
        #
        #     if event.from_user:
        #         print(event.user_id)
        #     elif event.from_group:
        #         print('администратор группы', event.group_id)
        #
        # elif event.type == VkEventType.USER_TYPING_IN_CHAT:
        #     print('Печатает ', event.user_id, 'в беседе', event.chat_id)
        #
        # elif event.type == VkEventType.USER_ONLINE:
        #     print('Пользователь', event.user_id, 'онлайн', event.platform)
        #
        # elif event.type == VkEventType.USER_OFFLINE:
        #     print('Пользователь', event.user_id, 'оффлайн', event.offline_type)
        #
        # else:
        #     print(event.type, event.raw[1:])
