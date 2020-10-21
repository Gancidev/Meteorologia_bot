# Meteorologia_bot
Bot che permette di visionare le condizioni meteo di una qualunque(o quasi) città italiana.

# Funzionamento
Una volta che l'utente manda il comando per settare la città crea un file per salvare il settaggio, quando invece chiedo la previsione per la città di default o per una città specifica il bot farà una chiamata HTTP GET al server di OpenWeatherMap che mi ritorna una risposta Json che elaboro per comporre il messaggio sulle previsioni.

# Comandi Disponibili
1. /setta_citta {nome_città} : permette all'utente di settare una città di default.
2. /previsioni : mostra le previsioni meteo per la città di default.
3. /previsioni {nome_città} : mostra le previsioni meteo per la città specificata.
4. /help : mostra un messaggio che riassume il funzionamento del bot all'utente.

# Implementazione
Per la realizzazione è stata utilizzata la libreria telepot e le API di OpenWeatherMap che vengono richiamate da una seconda libreria requests, la risposta alle richieste è un json che viene analizzato con la libreria Json.

# Telepot
Una Libreria per Python che permette di gestire attraverso se stessa un bot di telegram fornendo delle funzioni che si appoggiano alle API di telegram stesso.
E' stata utilizzata per la gestione dei messaggi che un utente e il bot scambiano.

# API OpenWeatherMap e requests
Le API di OpenWeatherMap sono gratuite e disponibili apertamente a chiunque, basta una semplice registrazione con conferma di e-mail e una trentina di minuti prima dell'attivazione effettiva.
Le API sono richiamate attraverso il metodo GET del protocollo HTTP, quindi richiamando un semplice url al quale si passano i parametri quali: Città di interesse, Stato, linguaggio della risposta, unità di misura.
Le risposte hanno un codice di ritorno che indicano com'è andata la richiesta.

# Json
La libreria viene utilizzata per interpretare la risposta Json mandata dalle API.

# Installazione e Utilizzo
Per usufruire del bot è necessario inserire il percorso in cui esso potrà salvare i propri file di configurazione (dovuto alla città di default che ogni utente inserisce), inserire la propria API TOKEN di OpenWeatherMap e in fine aggiungere il TOKEN del bot che si può facilmente ottenere tramite il BotFather (Nick: @BotFather).
Fatti i dovuti cambiamenti basterà eseguire lo script python e il bot è pronto.
Per rendere il bot sempre attivo senza dover avere una sessione aperta sul pc remoto si può trasformare lo script in un servizio linux mediante la seguente guida: https://github.com/torfsen/python-systemd-tutorial

# Test
E' possibile testare il codice contattando il bot su telegram al nick: @Meteorologia_Bot
