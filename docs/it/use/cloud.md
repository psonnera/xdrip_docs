---
source_hash: 5577d64214
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_cloud_upload_grey600_48dp.png" style="width:5%;" />&ensp;Caricamento nel Cloud
:::

Il caricamento nel cloud ti permette di caricare la tua glicemia su vari servizi cloud o database.  
Puoi usarlo per condividere i dati con dispositivi diversi da xDrip e per i report. 

### API Upload (REST) {#nightscout-sync-rest-api}

::: xdripitem API Upload (REST)
&ensp;REST API è il modo standard per connettersi a Nightscout  
:::

[Nightscout](https://nightscout.github.io/) è il metodo universale per condividere i tuoi valori di glicemia, creare report e molto altro...

Dopo aver creato il tuo sito Nightscout, attiva la sincronizzazione per caricare i dati da xDrip.

::: xdripitem Abilitato<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;REST API è il modo standard per connettersi a Nightscout  
:::

Se vuoi usare Nightscout per condividere la tua glicemia, assicurati che questa opzione sia attiva se usi un telefono con SIM e piano dati. Altrimenti il caricamento avverrà solo quando sei connesso a una rete Wi-Fi, il che va bene se usi Nightscout per raccogliere dati per i report.

::: xdripitem Utilizza rete dati mobile<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Upload anche con rete dati mobile  
:::

Se usi filtri o plugin di calibrazione, puoi selezionare questa opzione per inviare a Nightscout i dati così come vengono mostrati da xDrip invece dei dati non calibrati/non filtrati.

::: xdripitem Invia Glicemia Visualizzata<span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Usa filtraggio del rumore e plugins (se abilitati) per il valore trasmesso 
:::

L'URL di base è composto dal tuo API_SECRET (o da un token) e dall'URL del tuo sito.  
L'esempio fornito nella finestra di dialogo era per un Nightscout basato su Azure.

::: xdripitem URL di base
&ensp;https://password.hostname/api/v1  
:::

Il formato dell'URL deve essere come questo:

**`https://your-API_SECRET@your-site.domain.fqd/api/v1/`**

Trovi l'API_SECRET nelle [variabili](https://nightscout.github.io/nightscout/setup_variables/#nightscout-configuration) del tuo Nightscout.

In alternativa puoi usare un [token](https://nightscout.github.io/nightscout/security/#create-authentication-tokens-for-users) admin per l'autenticazione; in quel caso sarà così:

**`https://xdrip-12ab34cd5678ef90@your-site.domain.fqd/api/v1/`**

Se usi un servizio in hosting, contatta il fornitore.

::: info Più siti
Se hai più di un sito Nightscout, xDrip può caricare su più URL Nightscout **separati da spazi**.  
***Sugli URL secondari vengono caricati solo i valori di glicemia, non i trattamenti***
:::

Se hai più dispositivi che caricano su Nightscout (sconsigliato) potresti voler scaricare anche i trattamenti da Nightscout per vedere le informazioni caricate dagli altri.

::: xdripitem Scarica dati<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Prova anche a scaricare i dati da Nightscout  
:::

::: warning Calibrazione automatica
È la stessa impostazione [Calibrazione automatica](../calibrate/advancedcal#use-treatment-bg-values) delle calibrazioni. Usala con cautela.
:::

::: xdripitem Calibrazione automatica<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Calibra automaticamente utilizzando le letture di glicemia se le condizioni sembrano giuste, senza chiedere conferma (sperimentale)  
:::

<br>

::: xdripitem Altre opzioni
:::

Se il tuo Nightscout è disponibile solo su un server locale (su un IP privato), non tentare di caricare dati su Nightscout quando non sei a casa. Ignora questa opzione per un Nightscout nel cloud.

::: xdripitem Salta upload LAN<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Per server locali con indirizzi 192.168.x.x, non caricare dati in assenza di connessione di rete locale. 
:::

Puoi caricare il livello della batteria del bridge o del sensore (se supportato).

::: xdripitem Upload livello batteria del bridge<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Invia il livello della batteria a Nightscout. Deseleziona se il sensore di batteria non funziona.
:::

::: xdripitem Carica il livello di batteria del trasmettitore OB1 G5/G6<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Invia le statistiche della batteria del trasmettitore Dexcom a Nightscout. Include tutti i dati mostrati sulla schermata Stato del Collector.
:::

Puoi caricare i [trattamenti](./mainUI#treatments) inseriti localmente nel [Care Portal](https://nightscout.github.io/nightscout/setup_variables/#careportal-careportal) di Nightscout.

::: xdripitem Carica trattamenti<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Invia i trattamenti a Nightscout. Deseleziona se il tuo careportal non funziona.
:::

Puoi impostare un avviso quando il caricamento non riesce e aggiungere altre informazioni ai dati di glicemia caricati.

::: xdripitem Allarmi in caso di errori<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Notifica e suona se il caricamento a Nightscout fallisce.
:::

::: xdripitem Aggiungi informazioni sulla sorgente dati al nome del dispositivo<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Per G5, invia il tipo di collector (es. OB1) e leggi lo stato di ricupero dati storici (per nativo) a Nightscout.
:::

##### Recuperare i dati storici su Nightscout {#backfill-data-to-nightscout}

Se hai creato da poco un sito Nightscout e vuoi caricare i tuoi dati storici dal database di xDrip, puoi usare il recupero dei dati storici.

::: xdripitem Ricupera dati storici
&ensp;Invia le letture di glicemia per lo storico
:::

Seleziona il primo giorno del periodo che vuoi caricare (fino a oggi) e tocca **DO IT!**  
A seconda della quantità di dati e della velocità della rete, il caricamento può richiedere moltissimo tempo (ore).

::: xdrip <img src="../images/BDM.png" style="zoom:75%;" />Nightscout Backfill
Choose the date for the oldest record to send to Nightscout, use with care!  


<div style="background-color: gray; color: white; text-align: center;">  &emsp;FEBRUARY 12, 2022 11:29PM&emsp;</div>  


<span style="background-color: gray; color: white; text-align: center;">  &emsp;DO IT!&emsp;</span>&emsp;CANCEL
:::

### MongoDB {#mongodb}

::: warning Attenzione
Questo metodo è deprecato per Nightscout.
:::

Puoi caricare direttamente la glicemia e lo stato del dispositivo in un database Mongo.

::: xdripitem MongoDB
&ensp;Upload diretto nel database, sconsigliato per Nightscout
:::

Il caricamento su MongoDB è deprecato da quando mLab è stata acquisita da MongoDB e molti sono migrati su Atlas: **non puoi usare un URI DNS seed `mongodb+srv`**.  
Usa questa funzione solo se gestisci un tuo database [Mongo](https://github.com/mongodb/mongo); la porta predefinita è 27017.

La struttura della [stringa di connessione URI](https://www.mongodb.com/docs/manual/reference/connection-string/#connection-string-uri-format) è:

```
mongodb://databaseusername:databasepassword@your.mongo.url/databasename
```

Per mantenere il database compatibile con Nightscout, non cambiare il nome della Collection né il nome della collection Device status rispetto ai valori predefiniti (se li cambi dovrai modificare anche le variabili corrispondenti in Nightscout, `MONGODB_COLLECTION` e `MONGO_DEVICESTATUS_COLLECTION`).

::: info
I dati caricati potrebbero non comparire nella pagina web di Nightscout, ma solo nei report di Nightscout.
:::

### InfluxDB {#influxdb}

Puoi anche caricare i dati su un [InfluxDB](https://www.influxdata.com/products/influxdb-overview/) e usare Grafana per presentarli.

::: xdripitem InfluxDB
&ensp;Se usi un database privato InfluxDB, questo dovrebbe essere abilitato
:::

Attenzione: l'URI del tuo InfluxDB sarà espresso così:

`https://host_address:port`, ad esempio per un server locale: `https://192.168.0.56:8086`

### Dex Share {#dex-share}

::: warning Il nome utente non può essere un numero di telefono
Dovresti creare un [account dipendente](https://www.dexcom.com/faqs/how-do-i-create-a-dependent-account) per avere un nome utente solo testuale.  
Dopo aver creato il nuovo account dipendente, assicurati di aver effettuato l'accesso con questo account nelle app Dexcom e ricrea tutti i follower.
:::

Quando hai un follower attivo, creato dalle app Dexcom, puoi usare xDrip per caricare su Dexcom Share.

::: xdripitem Upload in Dexcom Share Server
&ensp;Carica i dati nel server Dexcom in modo da poter utilizzare i dati con le applicazioni Dexcom
:::

::: info
Puoi caricare la tua glicemia su Dexcom Share, **non su Dexcom Clarity**.
:::

::: xdripitem Carica valori di glicemia in Dexcom Share<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Abilitare per caricare sui server Dexcom
:::

Se usi un account USA attiva questa opzione, **per qualsiasi altro paese lasciala disattivata**. 

::: xdripitem Account Dexcom basato negli USA<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Abilitare = l'account e l'app follower sono negli dagli Stati Uniti
:::

Inserisci le credenziali che usi per accedere a Clarity.

::: xdripitem Login account Dexcom
:::


::: xdripitem Password dell'account Dexcom
:::

### Tidepool {#tidepool}

::: xdripitem Tidepool
&ensp;Carica i dati in Tidepool
:::

Se hai un account [Tidepool](https://www.tidepool.org/), puoi caricare automaticamente i tuoi dati e condividerli con il tuo diabetologo.  
Se xDrip può mostrare le [informazioni sulla basale da uno stato esterno](./display#basal-information), verranno caricate anche su Tidepool.

::: xdripitem Sincronizza con Tidepool<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

Inserisci il tuo indirizzo email e la password (quelli che hai usato per la [registrazione](https://app.tidepool.org/signup/personal)).

::: xdripitem Nome utente
Il tuo nome utente per l'accesso a Tidepool, generalmente il tuo indirizzo email
:::

::: xdripitem Password
La tua password di Tidepool
:::

Al termine, verifica la connessione.

::: xdripitem Test di accesso a Tidepool
:::

Tidepool non ha bisogno di dati in tempo reale: seleziona con il cursore il periodo dopo il quale i dati vengono caricati. Il valore predefinito è 15 minuti.

::: xdripitem Età dei dati min (15)
:::

**NON** usare i server di test (lascia l'opzione non selezionata).

::: xdripitem Usa server di integrazione (test) - non utilizzare<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

Puoi scegliere di caricare solo in determinate condizioni, per risparmiare batteria e costi dei dati.

::: xdripitem Solo durante la carica<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Carica i dati solo durante la ricarica
:::

::: xdripitem Solo su WiFi<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Carica i dati solo quando connesso a una rete non contabilizzata, come Wifi
:::

Se carichi anche manualmente i dati dal microinfusore, potresti voler disattivare il caricamento dei trattamenti di xDrip per evitare duplicati.

::: xdripitem Non caricare i trattamenti<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Carica solo i dati CGM per evitare duplicati con il caricamento manuale dal micro
:::

Se il caricamento non riesce, attiva il nuovo protocollo di autenticazione.

::: xdripitem Use new Auth<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
2023 openid authentication method
:::

##### Web Deposit {#web-deposit}

Web Deposit è una semplice API di caricamento in blocco usata attualmente per la diagnostica. È nascosta dietro la modalità Engineering e non è pensata per l'uso normale.

### NightLite {#nightlite}

::: xdripitem NightLite
&ensp;Lightweight Nightscout compatible service intended for followers
:::

NightLite è un servizio follower leggero e compatibile con Nightscout, un'alternativa più semplice alla gestione di un tuo sito Nightscout se ti serve solo condividere la glicemia con i follower.

Vedi [Configurazione del follower NightLite](./nightlite) per la sequenza di installazione completa.

::: xdripitem Upload to NightLite<span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Whether to upload to the remote service
:::

::: xdripitem NightLite URL
&ensp;Contains your security key, do not disclose it. Typically entered by scanning a QR code from the dashboard.
:::

Una volta attivato, puoi mostrare un codice QR con i dati di connessione NightLite da far scansionare ai follower.

::: xdripitem Mostra Codice QR
:::

### Nocturne {#nocturne}

::: xdripitem Nocturne
&ensp;Carica su Nocturne API V4
:::

[Nocturne](https://getnocturne.dev/) è il successore moderno di Nightscout sviluppato dalla Nightscout Foundation. Se gestisci una tua istanza Nocturne, xDrip può caricare i dati direttamente su di essa.

::: xdripitem Abilita caricamento Nocturne<span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

Inserisci l'indirizzo della tua istanza Nocturne.

::: xdripitem URL istanza Nocturne
&ensp;Inserisci l'URL della tua istanza Nocturne (es. https://mynocturne.example.com)
:::

Poi autorizza xDrip con la tua istanza. In xDrip non viene memorizzata alcuna password: viene mostrato un codice, che inserisci nella pagina di approvazione della tua istanza Nocturne nel browser per completare la connessione.

::: xdripitem Connetti a Nocturne
&ensp;Autorizza xDrip+ con la tua istanza Nocturne
:::

#### Quick Connect da Nocturne {#quick-connect-from-nocturne}

Invece di digitare l'URL dell'istanza, lascia che sia Nocturne a configurare xDrip per te. Nella tua istanza Nocturne apri Connectors & Apps, poi Set Up an Uploader, e seleziona xDrip+ nell'elenco CGM Apps.

<img src="./images/M-S-N1.png" style="zoom:75%;" />

La pagina Set up xDrip+ mostra un codice QR Quick Connect.

<img src="./images/M-S-N2.png" style="zoom:60%;" />

::: warning Scansiona questo codice QR con l'app fotocamera del telefono, non con xDrip
Il codice QR Quick Connect è un link che apre xDrip sul telefono direttamente nella configurazione del connettore Nocturne. Scansionarlo con l'importatore di impostazioni [Configurazione automatica](./copysettings#auto-configure) di xDrip non funziona.
:::

xDrip mostra poi un codice di autorizzazione. Inseriscilo nel campo Enter Authorization Code della stessa pagina Nocturne e tocca Continue per completare la connessione.

#### Metodo alternativo: codice QR delle impostazioni {#alternate-method-settings-qr-code}

Se preferisci preparare tu stesso le impostazioni Nocturne, usa il configuratore qui sotto. Inserisci l'URL della tua istanza, scegli cosa caricare, poi scansiona il codice QR generato dall'interno di xDrip con [Configurazione automatica](./copysettings#auto-configure) (Camera, oppure File immagine con il PNG scaricato). xDrip elenca le impostazioni e chiede conferma prima di applicarle.

::: info A differenza del codice QR Quick Connect qui sopra, questo deve essere scansionato con xDrip, non con l'app fotocamera.
:::

Una volta importate le impostazioni, apri Impostazioni, Caricamento nel Cloud, Nocturne, tocca Connetti a Nocturne e inserisci nella tua istanza Nocturne il codice di autorizzazione mostrato da xDrip. I token di autorizzazione non fanno mai parte del codice QR.

<iframe src="./nocturne-qr.html" title="xDrip+ Nocturne QR configurator" style="width:100%; height:800px; border:1px solid #d9dee5; border-radius:8px; background:#f6f7f9;" loading="lazy"></iframe>

Puoi anche [aprire il configuratore in una pagina separata](./nocturne-qr.html){target="_blank"}.

Seleziona quali dati caricare. Le letture di glicemia sono attivate per impostazione predefinita; tutto il resto è facoltativo.

::: xdripitem Carica glicemia<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Carica i valori di glucosio del sensore CGM
:::

::: xdripitem Carica trattamenti<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Carica boli, CHO, note ed eventi del dispositivo
:::

::: xdripitem Carica calibrazioni<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Carica le calibrazioni del sensore
:::

::: xdripitem Carica misure capillare<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Carica le letture del glucometro
:::

::: xdripitem Carica battito cardiaco<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Carica i dati del battito cardiaco
:::

::: xdripitem Carica conteggio passi<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Carica i dati del conteggio passi
:::

::: xdripitem Carica stato dispositivo<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Carica il livello della batteria del telefono e lo stato di carica
:::

::: xdripitem Carica monitoraggio movimento<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Carica le classificazioni di attività riconosciute
:::

::: xdripitem Utilizza rete dati mobile<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Consenti upload su dati mobili
:::

<br>

[*Ultima modifica 6/9/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.08.19)
