import telebot, os, json

bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"), parse_mode=None)

def send_ad(message):
    message = json.loads(message)
    message_formated = "Novo Anúncio\n{}\n{}\nPreço: R$ {}\nAcesso em: {}".format(message['title'], message['location'], message['price'], message['url'])
    try:
        bot.send_message('@real_state_bot_br', message_formated)
        return {'messsage':'Anúncio enviado!'}
    except:
        return {'message':'Erro ao enviar mensagem para o telegram.'}