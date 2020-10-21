# Meteorologia_bot

Bot che permette di visionare le condizioni meteo di una qualunque(o quasi) città italiana.

# Comandi Disponibili

1. /setta_citta {nome_città} : permette all'utente di settare una città di default.
2. /previsioni : mostra le previsioni meteo per la città di default.
3. /previsioni {nome_città} : mostra le previsioni meteo per la città specificata.
4. /help : mostra un messaggio che riassume il funzionamento del bot all'utente.

# Implementazione

Per la realizzazione è stata utilizzata la libreria telepot e le API di OpenWeatherMap che vengono richiamate da una seconda libreria requests.

# Telepot

Una Libreria per Python che permette di gestire attraverso se stessa un bot di telegram fornendo delle funzioni che si appoggiano alle API di telegram stesso.
E' stata utilizzata per la gestione dei messaggi che un utente e il bot scambiano.

# API OpenWeatherMap e requests

Le API di OpenWeatherMap sono gratuite e disponibili apertamente a chiunque, basta una semplice registrazione con conferma di e-mail e una trentina di minuti prima dell'attivazione effettiva.
Le API sono richiamate attraverso il metodo GET del protocollo HTTP, quindi richiamando un semplice url al quale si passano i parametri quali: Città di interesse, Stato, linguaggio della risposta, unità di misura.
Le risposte hanno un codice di ritorno che indicano com'è andata la richiesta.

# Test
E' possibile testare il codice contattando il bot su telegram al nick: @Meteorologia_Bot
