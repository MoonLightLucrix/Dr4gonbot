import os
from sys import *
from telegram.ext import *
from telegram import *
import requests
import re
from datetime import *

#def getUrl():
#	contents=requests.get('https://www.twitch.tv/dr4gon_89')
#	url=contents['url']
#	return url

#def info(bot,update):
#	url=getUrl()
#	chat_id=update.message.chat_id
#	bot.send_message(chat_id=chat_id, text="Ciao ragazzi, sono Seby alias Dr4gon_89! Sono un appassionato di tutte le tipologie (o quasi) di videogiochi da sempre, non mi definisco un pro player ma gioco per divertirmi e e per divertire, cosa aspetti? metti follow e diventa anche tu un Dragone!")

def start(update,context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Ciao ragazzi, sono Seby alias Dr4gon_89! Sono un appassionato di tutte le tipologie (o quasi) di videogiochi da sempre, non mi definisco un pro player ma gioco per divertirmi e e per divertire, cosa aspetti? metti follow e diventa anche tu un Dragone!")

def help(update,context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="\t\t<b>Comandi</b>\n\n/start - presentazione\n\n/twitch - link al canale twitch\n\n/discord - link discord\n\n/donazioni - fai una donazione\n\n/regole - Elenco di regole del gruppo e del canale\n\n/badoo - Bellissima foto ricordo di Badoo", parse_mode=ParseMode.HTML)

def creepyBadoo(update,context):
	context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("./Photo/Badoo1.JPG","rb"))

def setPoll(update,context):
	game_list=["The Witcher 2: Assassins of Kings", "South Park: The Fractured but whole", "Bloodborne", "Final Fantasy VI"]
	now=datetime.now()+timedelta(seconds=6)
	context.bot.send_poll(chat_id=update.effective_chat.id, question="Che gioco volete stasera?", options=game_list, is_anonymous=False, open_period=int(10))
	print(chat_id)

def twitch(update,context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="https://www.twitch.tv/dr4gon_89")

def discord(update,context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="https://discord.gg/FpQWCS3")

def donazioni(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Prova a fare anche tu una donazione <a href="https://www.paypal.com/paypalme/Dr4gon89">clicca qui</a>', parse_mode=ParseMode.HTML)

def rules(update,context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="<b>Regole\n\n-Non si possono spammare altri gruppi\n-Sono severamente vietati gli spoiler di ogni genere\n-Non si possono spammare altri canali </b>(Quindi Jessica ti po' stuiari u mussu)<b>\n-Sono vietate ogni forma di bestemmia </b>porco Yevon<b>\n-È severamente vietato parlare bene di Dota o LoL in questo gruppo, possono essere usati solo ed esclusivamente per tirargli merda\n-Cerchiamo di mantenere un comportamento di pace e rispettiamoci tra di noi!\n\nBuona Permanenza!!</b>", parse_mode=ParseMode.HTML)

#def msgProva(context: CallbackContext):
#	context.bot.send_message(chat_id=context.job.context, text="Prova")

#def efMsgProva(update: Update, context:CallbackContext):
#	context.job_queue.run_once(msgProva,1,context=update.message.chat_id)


def main(args):
    updater = Updater(token='1338167655:AAGdCx4L-0R4YKhcPMdYxOs1kaGgSCe30Vk',use_context=True)
    dp = updater.dispatcher
    #jq = updater.job_queue
    #job_prova=jq.run_once(msgProva,2)
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',help))
    #dp.add_handler(CommandHandler('setPoll',setPoll))
    dp.add_handler(CommandHandler('twitch',twitch))
    dp.add_handler(CommandHandler('discord',discord))
    dp.add_handler(CommandHandler('donazioni',donazioni))
    dp.add_handler(CommandHandler('badoo',creepyBadoo))
    dp.add_handler(CommandHandler('regole',rules))
    #dp.add_handler(CommandHandler('jqueue',efMsgProva))
    updater.start_polling()
    updater.idle()

if __name__=='__main__':
	main(argv)
