---
source_hash: 09c4f80004
source_commit: 7a18e7c
---
# Libre2 Direct {#libre2-direct}

Libre2 (solo versione UE) può collegarsi direttamente a xDrip senza bridge. Questa pagina mostra come dovrebbe apparire un sistema funzionante.

Vedi qui per [imparare a configurarlo...](../install/libre2#prerequisites)

## Come dovrebbe apparire {#what-it-should-look-like}

Se la configurazione è corretta e un nuovo sensore è attivo, le pagine di stato e i log di xDrip dovrebbero apparire come mostrato qui sotto. Nota: per il funzionamento con Libre 2 direct non cambia nulla nella scheda Uploaders.


Vai in Stato del sistema di xDrip e anche nella pagina BT Device. Se non sai come fare, guarda prima [qui](./systemstatus).

## Pagina di stato classica {#classic-status-page}

<img src="./images/classic-status-connected.png" style="zoom:40%;" />

### Versione {#version}
Cambia a seconda della tua versione di xDrip

### Sorgente dati {#data-source}
Qui dovrebbe comparire LimiTTer. Anche se fuorviante, è il comportamento normale.

### Dispositivo Bluetooth {#bluetooth-device}
È l'identificativo seriale univoco del sensore. Inizia con ABBOTT...

### Stato della connessione {#connection-status}
Dovrebbe essere "connesso".

### Sensore attivato {#sensor-start}
L'ora in cui è stato avviato il sensore.

### Pulsante Riavvia Collector {#restart-collector-button}
Ferma la funzione di collector di xDrip e poi la riavvia da zero (compresa la connessione Bluetooth
 al dispositivo che era stata interrotta)

### Pulsante Dimentica questo dispositivo {#forget-device-button}
Rimuove il dispositivo Bluetooth dai dispositivi conosciuti: devi fare una scansione Bluetooth per trovarlo e associarlo
 di nuovo, oppure rifare una scansione NFC.

### Pulsante Aggiorna {#refresh-button}
Lo stato non è in tempo reale, a differenza della scheda BT Device; Aggiorna verifica lo stato della connessione.
<br>


## Pagina BT Device {#bt-device-page}

Scorri lo schermo verso sinistra per visualizzare la pagina BT Device.

<img src="./images/bt-device-connected.png" style="zoom:40%;" />

### Bluetooth Collector Status {#bluetooth-collector-status}

### Phone Service State {#phone-service-state}

Normalmente indica l'ora dell'ultima connessione.
A volte mostra XXX Blu Con XXX, ma è una fase temporanea e cambierà in Last Connect HH:MM


### Bluetooth Device {#bluetooth-device-1}

Il Bluetooth dovrebbe essere sempre connesso.

### Device Mac Address {#device-mac-address}
Dovrebbe essere una stringa di sei coppie di numeri esadecimali, unica per ogni sensore.

### Bluetooth Pairing {#bluetooth-pairing}

Dovrebbe restare "Disabled, tap to enable". Fai attenzione a NON toccarlo.  
Se lo tocchi per errore, toccalo di nuovo finché non torna disattivato.

### Slowest wake up {#slowest-wake-up}

Puoi ignorarlo. xDrip non passa il tempo ad aspettare le letture: comincia ad aspettarle dopo un certo tempo (di solito 5 minuti). Se a quel punto non arrivano dati, vedrai "Woke up early", che significa che xDrip si aspettava dati pronti ma non ce n'erano. Slowest wake up è il ritardo più lungo registrato prima di ricevere normalmente i dati.

### Next Wake up {#next-wake-up}

Dovrebbe indicare 5 minuti

<br>


# Log eventi {#event-logs}

Dal menu verticale ... in alto a destra nella schermata principale, seleziona Visualizza eventi Log

<img src="./images/event-log-normal.png" style="zoom:40%;" />

### LibreOOPAlgorithm {#libreoopalgorithm}

Dovresti vedere una serie di righe nel formato
HH:MM Creating BG time = NNN raw = RRRR
dove HH:MM è l'ora, NNN è un contatore interno del tempo (una nuova lettura ha un numero più alto della precedente) e RRRR è il valore raw letto dal sensore, in decimi di mg/dl (1000 corrisponde a 100 mg/dl o 5,5 mmol/l).
Questo indica che il sensore è connesso e che vengono ricevute letture valide.
Dovrebbe esserci una lettura ogni minuto, anche se alcune possono mancare, come è successo qui.

<br>

## Impossibile scansionare con NFC un nuovo sensore - Timeout NFC {#cannot-nfc-scan-new-sensor-nfc-timeout}
C'è un problema emergente, soprattutto in Europa, per cui non è possibile avviare il sensore con una scansione NFC. Invece del messaggio "Scansionato OK!" dopo "Scansione in corso", vedrai "Timeout lettura NFC" o "Timeout diagnostico NFC". Guarda nei log di debug. Se vedi il messaggio "Sensor type unknown, returning libre1 as failsafe" oppure "Libre sensor of type Libre1 detected", devi aggiornare sia OOP2 sia xDrip.

<img src="./images/libre2direct-failsafe-to-libre1.png" style="zoom:40%;" />

Devi scaricare una versione di OOP2 della fine di maggio 2023 e anche
aggiornare xDrip-plus a una versione del 2023-05-27 o successiva. Una nuova versione dei sensori, "C5" con firmware aggiornato, richiede queste versioni aggiornate.

## Perdi la connessione Bluetooth con un telefono Samsung? {#losing-bluetooth-connection-with-samsung-phone}
Diverse persone con un telefono Samsung hanno segnalato di perdere a volte la connessione con il sensore. Se capita anche a te, puoi provare a cambiare alcune impostazioni Bluetooth. Fai clic sul codice QR e poi scansionalo come indicato.


[<img src="./images/qr_libre2direct_samsung_30.png" style="zoom:50%;" />](./libre2direct-qr-samsung)


[*Ultima modifica 4/6/2023*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2023.05.26)
