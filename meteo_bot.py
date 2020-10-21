#!/usr/bin/python
# -*- coding: latin-1 -*-
import time
import os
import telepot
from telepot.loop import MessageLoop
from pprint import pprint
import requests
import json

def handle(msg):
    #percorso alla cartella dedicata al bot (di cui ha bisogno per salvare i settaggi)
    percorso="/home/user/path/meteo_bot/"
    content_type, chat_type, chat_id = telepot.glance(msg)
    print ("\n")
    pprint(msg)

    if msg['text']=='/start':
        bot.sendMessage(chat_id,"Benvenuto nel Meteorologia_Bot, il bot che ti fornisce le previsioni meteo in tempo Reale.")

    elif msg['text'][:12]=='/setta_citta':
        r=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+msg['text'][13:]+',IT&lang=IT&units=metric&appid={INSERT YOUR API TOKEN}')
        x=r.text
        y=json.loads(x)
        if y['cod']==200:
            file=open(percorso+'info/'+str(chat_id)+'.txt','w')
            file.write(msg['text'][13:])
            file.close()
            bot.sendMessage(chat_id,"Citta' -"+msg['text'][13:]+"- settata, adesso ti basta inviare il comando /previsioni per avere le previsioni della tua citta'")
        else:
            bot.sendMessage(chat_id,"La citta' -"+msg['text'][13:]+"- non e' stata trovata.")

    elif msg['text']=='/help':
        help="Ecco una lista di quello che so fare:\n 1) /setta_citta - Per impostare una citta' predefinita;\n 2) /previsioni {citta (facoltativo se eseguito il comando 1)} - Per conoscere le previsioni per la citta' scelta;\n 3) /help - Per ricevere questo messaggio di aiuto;"
        help=help+"\n\n Per utilizzare il bot puoi lanciare il comando /previsioni seguito dalla citta' di tuo interesse, oppure lanciare prima il comando per settarne una di default e poter usare solo /previsioni."
        bot.sendMessage(chat_id,help)

    elif msg['text'][:11]=='/previsioni':
        if msg['text'][12:]=="":
            try:
                file=open(percorso+'info/'+str(chat_id)+'.txt','r')
                citta_settata=file.read()
                r=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+citta_settata+',IT&lang=IT&units=metric&appid={INSERT YOUR API TOKEN}')
                x=r.text
                y=json.loads(x)
                testo="Previsioni per "+y['name']+":\n"
                testo=testo+"  Condizioni: "+y['weather'][0]['description'].capitalize()+"\n"
                testo=testo+"  Temperatura Attuale: "+str(y['main']['temp'])+" C"+"\n"
                testo=testo+"  Temperatura (min/max): "+str(y['main']['temp_min'])+" C / "+str(y['main']['temp_max'])+" C\n"
                testo=testo+"  Umidita': "+str(y['main']['humidity'])+"%\n"
                testo=testo+"  Vento: "+str(y['wind']['speed'])+" m/s\n"
                bot.sendMessage(chat_id,testo)
            except IOError:
                bot.sendMessage(chat_id,"Per poter utilizzare il comando /previsioni senza specificare una citta' devi prima settarne una con il comando /setta_citta {nome_citta'}")

        else:
            r=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+msg['text'][12:]+',IT&lang=IT&units=metric&appid={INSERT YOUR API TOKEN}')
            x=r.text
            y=json.loads(x)
            testo="Previsioni per "+y['name']+":\n"
            testo=testo+"  Condizioni: "+y['weather'][0]['description']+"\n"
            testo=testo+"  Temperatura Attuale: "+str(y['main']['temp'])+" C\n"
            testo=testo+"  Temperatura (min/max): "+str(y['main']['temp_min'])+" C / "+str(y['main']['temp_max'])+" C\n"
            testo=testo+"  Umidita': "+str(y['main']['humidity'])+"%\n"
            testo=testo+"  Vento: "+str(y['wind']['speed'])+" m/s\n"
            bot.sendMessage(chat_id,testo)
    else:
        bot.sendMessage(chat_id,"Non sono riuscito a interpretare il comando, usa /help per sapere come utilizzarmi")

TOKEN = '{INSERT YOUR TELEGRAM BOT TOKEN}'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
