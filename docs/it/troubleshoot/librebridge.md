---
source_hash: 51a5c41463
source_commit: 7a18e7c
---
Sul mercato esistono molti bridge commerciali per Libre; in ordine di uscita trovi Blucon, MiaoMiao, Droplet e Bubble, per citare solo i più noti. Si basano tutti sul concetto LimiTTer e sull'implementazione blueReader: un chip di lettura NFC CR95LF e un microcontrollore BLE Nordic Semiconductor. Il primo legge il sensore e il secondo invia i dati via Bluetooth al telefono (o all'orologio Wear) ogni 5 minuti.

::: info Nota
**Finché il bridge riesce a leggere il sensore e a trasmettere i dati, puoi considerarlo funzionante.**
:::

Quando xDrip mostra letture mancanti, devi capire cosa non funziona. Non è sempre facile.

::: info
Comincia dalle cose semplici: per prima cosa riavvia il telefono.
:::

Visto che sei qui, controlla i [parametri Bluetooth di xDrip](../install/libreBT#bridge-settings) e non esitare a disattivarne qualcuno.

Poi vai in Stato del sistema e anche nella pagina BT Device. Se non sai come fare, guarda prima [qui](./systemstatus).

### Pagina di stato classica {#classis-status-page}

**Se il tuo bridge risulta come LimiTTer, probabilmente significa che non è connesso o non è riconosciuto.**

Tutti i dispositivi risultano LimiTTer finché non sono connessi; solo la connessione diretta a Libre 2 e alcuni altri bridge (ad esempio BluCon) restano indicati come LimiTTer (e ovviamente [LimiTTer](https://github.com/JoernL/LimiTTer) stesso).

<img src="./images/M-SS-CSL2.png" style="zoom:75%;" />

Controlla la versione di xDrip e assicurati che sia abbastanza recente da supportare il bridge che stai collegando.

Ci sono troppe versioni e miglioramenti in xDrip per fornire una tabella precisa delle versioni minime richieste.  
Assicurati di usare almeno la versione [ultima release](../install/download#latest-release) di xDrip e, se pensi che il tuo bridge richieda funzioni più recenti, prova ad aggiornare all'ultima [pre-release](../install/download#pre-release).

 Non disinstallare xDrip quando vuoi cambiare versione. Puoi facilmente [passare da una versione all'altra](../use/update) senza perdere dati e impostazioni.

### Pagina BT Device {#bt-device-page}

Scorri lo schermo verso sinistra per visualizzare la pagina BT Device.

<img src="./images/M-SS.png" style="zoom:75%;" />

<img src="./images/M-SS-BTLBf.png" style="zoom:75%;" />

#### Bluetooth Pairing {#bluetooth-pairing}

Se sei già passato di qui: **Bluetooth Pairing deve essere disattivato. Se l'hai cambiato per errore, tocca la riga per riportarlo in questo stato:**

<img src="./images/M-SS-BTLBc.png" style="zoom:75%;" />

#### Bluetooth Device {#bluetooth-device}

Il Bluetooth deve essere sempre connesso.

<img src="./images/M-SS-BTLBe.png" style="zoom:75%;" />

Prime azioni da eseguire se il Bluetooth non è connesso:

1. Controlla le tue [impostazioni Bluetooth](../install/libreBT#bridge-settings) e usa Riavvia Collector nella scheda classica di Stato del sistema. Se Riavvia Collector ti ha permesso di recuperare la connessione, il problema potrebbe essere nelle impostazioni Bluetooth o nelle impostazioni di risparmio energetico del telefono.  
2. Apri Impostazioni Android -> App -> xDrip: assicurati che possa funzionare in background e che non sia ottimizzato per il risparmio della batteria.  
3. Sempre in App, cerca le app di sistema Bluetooth (potrebbero essere nascoste per impostazione predefinita e disponibili nel menu a tre puntini in alto a destra): assicurati che tutti i servizi Bluetooth possano funzionare in background e non siano ottimizzati.

Se il bridge non è ancora visibile, prova con [Scansione Bluetooth](../install/libreBT#connect-bluetooth-bridge) per trovarlo.

- Se la scansione Bluetooth non lo trova, continua [qui](#bluetooth-scan-doesnt-find-the-bridge).
- Se la scansione Bluetooth ti permette di selezionarlo ma non resta connesso, continua [qui](#bridge-doesnt-stay-connected).

#### Phone Service State {#phone-service-state}

Phone Service State indica l'ultima volta che sono stati ricevuti dati dal bridge; dovrebbe essere meno di 5 minuti fa.  
Next Wake Up fa il conto alla rovescia fino ai prossimi dati attesi, poi riparte da 5 minuti.

<img src="./images/M-SS-BTLBa.png" style="zoom:75%;" />

Se hai configurato un orologio Android Wear come collector, vai alla pagina [modalità collector autonomo](../smartwatch/wear#standalone-collector-mode). Se non hai un orologio Android Wear con xDrip installato correttamente, [disattiva il collector Wear](../smartwatch/wear).

 <img src="./images/M-SS-BTLBg.png" style="zoom:75%;" />

Non cercare di collegare il bridge a uno smartwatch finché non ottieni un funzionamento affidabile con il telefono (nessuna perdita di connessione).

#### Informazioni sul bridge {#bridge-information}

Vedrai anche varie informazioni sul bridge, come l'indirizzo Mac e la versione hardware e firmware. Nota che il livello della batteria non è disponibile sui bridge Blucon e 100% significa solo che è ancora utilizzabile. 

<img src="./images/M-SS-BTLBb.png" style="zoom:75%;" />

È vivamente consigliato [aggiornare](./bridgeFW) il firmware del dispositivo all'ultima versione disponibile.

#### No Sensor Found {#no-sensor-found}

Gli errori Nessun sensore rilevato sono di solito dovuti a un cattivo posizionamento del bridge sul sensore. Alcuni bridge non hanno alcuna tolleranza riguardo alla distanza e all'angolo rispetto all'area dell'antenna del sensore. Può anche trattarsi di un problema interno del bridge, di un problema di firmware, ...  
Poiché è un messaggio persistente, controlla che l'ora indicata sia recente. Se è sempre 5 minuti fa, il sensore non viene visto. Se è successo qualche ora fa, ignoralo.

<img src="./images/M-SS-BTLBd.png" style="zoom:75%;" />

Se usi un bridge che non è sensibile al posizionamento, potrebbe avere un guasto interno o un firmware danneggiato.

- Per prima cosa resettalo e caricalo completamente.
- Prova a ricaricare o [aggiornare](./bridgeFW) il suo firmware.

Se usi un sensore diverso da Libre 1, potresti dover aggiungere un algoritmo Out Of Process (OOP).

Usa [Dimentica questo dispositivo](./systemstatus#restart-collector-forget-device) in xDrip e installa l'app del produttore per escludere un guasto del dispositivo. Contatta il produttore per assistenza.

### La scansione Bluetooth non trova il bridge {#bluetooth-scan-doesnt-find-the-bridge}

::: info Nota
È del tutto normale quando il bridge è connesso a xDrip.
:::

1. Assicurati che non sia associato a un altro telefono o a un'altra app. Se usi il bridge con un'altra app, rimuovilo dall'app o disinstalla l'app che si collega al bridge. Se hai usato il bridge su un altro telefono, spegnilo ora o rimuovi l'app che si collegava al tuo bridge.
2. Resettalo. Contatta il produttore per sapere come farlo.
3. Mettilo in carica o sostituisci la batteria.  
   Puoi fare la scansione Bluetooth con il dispositivo in carica: se riesci a collegarti solo mentre è in carica, la batteria interna potrebbe essere esaurita.

 Installa l'app del produttore per escludere un guasto del dispositivo. Contatta il produttore per assistenza. 

### Il bridge non resta connesso {#bridge-doesnt-stay-connected}

Quando fai la scansione Bluetooth, vedi e puoi selezionare il tuo bridge (di solito appare in blu come dispositivo conosciuto), ma non resta connesso: alla scansione Bluetooth successiva appare di nuovo.

##### Soluzione 1: {#solution-1}

1. Stato del sistema, Classic Status Page -> Dimentica questo dispositivo
2. Menu principale, Scansione Bluetooth -> Seleziona un dispositivo Bluetooth qualsiasi che non sia il tuo bridge
3. Attendi 10 secondi
4. Stato del sistema, Classic Status Page -> Dimentica questo dispositivo
5. Menu principale, Scansione Bluetooth -> Seleziona il tuo bridge

##### Soluzione 2: {#solution-2}

1. Stato del sistema, Classic Status Page -> Dimentica questo dispositivo
2. Metti il telefono in modalità aereo
3. Attendi 10 secondi
4. Disattiva la modalità aereo
5. Disattiva il Bluetooth
6. Attendi 10 secondi
7. Attiva il Bluetooth
8. Menu principale, Scansione Bluetooth -> Seleziona il tuo bridge

<br>

[*Ultima modifica 28/3/2022*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2022.03.27)
