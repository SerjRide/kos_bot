import vk_api, random, sys
from vk_api.longpoll import VkLongPoll, VkEventType

token = 'ba56658e915221087b77700935e370a4ba6e3df42f413c096551d09760a51b090b98b8dc9d4138b5ba063'

# Подключение к сообществу
vk = vk_api.VkApi(token = token)
vk._auth_token()

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

# 101 - игорировать сообщение
# 201 - вложение фото
def current_answer(text):
    if 'кос фото' in text.lower(): return 201
    if 'кос' in text.lower(): return 'АаааРМ!'
    return 101

def get_longpoll_data(group_id):
    long_pull = vk.method('groups.getLongPollServer', {"group_id": group_id})
    print(long_pull)

# Возвращает данные подключения к Longpoll VkApi
longpoll = vk_api.VkBotLongPoll(vk, 202781313)
vk_session = vk.get_api()
longpoll_key    = '3P8esmZwgex9k4zeSG3vEYLbji4VVTQM7a'
longpoll_server = 'https://lp.vk.com/wh202781313'
longpoll_link   = 'https://lp.vk.com/wh202781313?act=a_check&key=3P8esmZwgex9k4zeSG3vEYLbji4VVTQM7a&wait=25&mode=2&ts=1'
#get_longpoll_data(202781313)

# Постоянная проверка новых сообщений в беседе ботом
while True:
    params   = {"offset": 0, "count": 20, "filter": "all"}
    messages = vk.method('messages.getConversations', params)

    # если есть сообщения
    if messages['count'] > 0:

        # текст последнего сообщения
        in_msg_text = messages['items'][0]['last_message']['text']

        # пользователь, приславший это сообщение
        user_id = messages['items'][0]['last_message']['from_id']

        #print(messages['count'])
        # отправить сообщение

        if current_answer(in_msg_text) != 101:
            params = {
                "user_id": user_id,
                "message": current_answer(in_msg_text),
                'random_id': random.randint(1, 1000)
            }
            # отправить фото
            if current_answer(in_msg_text) == 201:

                '''
                Механизм загрузки фото с нуля
                '''
                # uploader = vk_api.upload.VkUpload(vk)
                # album = 'C:/python-projects/vk_bots/kos/photos/'
                # photo = in_msg_text.split(' ')[-1]
                # img = uploader.photo_messages(f'{album}{photo}.jpg')
                # media_id = str(img[0]['id'])
                # owner_id = str(img[0]['owner_id'])
                # params["message"] = 'Я'
                # params["attachment"] = 'photo' + owner_id + '_' + media_id
                # print(f'photo {photo} == {"photo" + owner_id + "_" + media_id}')
                '''
                Механизм загрузки фото, которые уже хранятся на сервере
                '''
                get_random = random.randint(0, 7)
                params["message"] = 'Я'
                params["attachment"] = photo_album[get_random]

            vk.method('messages.send', params)

        #print(user_id, ':', in_msg_text, ':', )
