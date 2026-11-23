---
source_hash: 4a69400131
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_open_in_app_grey600_48dp.png" style="width:5%;" />&ensp;Impostazioni Inter-app
:::

<br>

Impostazioni Inter-app offre due modi per far comunicare xDrip con altre app: la trasmissione locale (interna a questo telefono) e il web service (interno ed esterno).

### Trasmissione locale {#local-broadcast}

Trasmetti localmente fa inviare a xDrip messaggi interni che possono essere usati da altre app come Nightwatch o AAPS.

::: xdripitem Trasmetti localmente <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Abilita trasmissione locale di dati in modo da altre applicazioni (ad es. NightWatch) possano importare nuovi valori
:::

Se usi plugin di calibrazione o il filtraggio, puoi scegliere di trasmettere i dati grezzi o quelli filtrati/calibrati.

::: xdripitem Invia Glicemia Visualizzata <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Usa filtraggio del rumore e plugins (se abilitati) per il valore trasmesso
:::

Per sicurezza puoi anche bloccare la trasmissione dei dati rumorosi. Per impostazione predefinita, solo i dati con rumore estremo non vengono trasmessi.

::: xdripitem Blocco rumore
&ensp;Livello a quale i dati rumorosi non dovrebbero essere trasmessi perché potrebbe confondere le app riceventi
:::

Le app e i telefoni recenti dovrebbero accettare il broadcast compatibile. Non togliere la spunta.

::: xdripitem Broadcast compatibile <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Invia trasmissioni senza usare il vecchio modello di permesso
:::

Puoi indicare un ricevitore identificato se vuoi che xDrip invii i messaggi solo a un'app specifica. Uno degli usi più comuni è quando xDrip è la sorgente dati di [AAPS](https://androidaps.readthedocs.io/en/latest/Configuration/xdrip.html#identify-receiver).

::: xdripitem Identifica ricevitore
&ensp;Invia dati solo al package nominato
:::

##### Ricezione da NSClient. {#receiving-from-nsclient}

Con questa funzione xDrip può anche ricevere messaggi: puoi attivare o disattivare la ricezione di dati e trattamenti da altre app che li trasmettono.

::: xdripitem Accetta Glucosio <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Usa i dati di glicemia ricevuti dall'app NSClient
:::

::: xdripitem Accetta trattamenti <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Processa i trattamenti ricevuti dall'app NSClient
:::

Puoi attivare o disattivare (**disattivalo con AAPS!!!**) il suono riprodotto dopo l'aggiornamento del profilo di xDrip.

::: xdripitem Importa Suoni <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Suona durante l'importazione di dati significativi come i profili
:::

Fai attenzione quando accetti calibrazioni da altre app.

::: xdripitem Accetta calibrazione <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Utilizza le calibrazioni ricevute da altre applicazioni
:::

### Web Service {#web-service}

Documentazione originale [qui](https://github.com/NightscoutFoundation/xDrip/blob/master/Documentation/technical/Local_Web_Services.md).

::: warning Attenzione
Se hai un'altra app che usa la porta 17580 (come Diabox), devi disattivare questa funzione.  
Nota che il servizio non è disponibile in http sicuro e le app [Fitbit](../smartwatch/smartwatch#fitbit) recenti potrebbero non accettarne i dati.
:::

Il web service apre un servizio web locale sul dispositivo per permettere ad altri dispositivi (smartwatch) e app di riceverne i dati.  
Il server web risponde alle richieste all'indirizzo `127.0.0.1` porta `17580`

::: xdripitem xDrip Web Service <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Opera un server web locale per interagire con smartwatch Fitbit ed altri
:::

Per impostazione predefinita il web service è disponibile solo sul tuo dispositivo; puoi aprirlo perché altri dispositivi della rete possano accedervi. Assicurati di avere davvero bisogno di questa funzione e di comprenderne le implicazioni per la sicurezza. Assicurati di aver impostato uno Shared Secret.

::: xdripitem Apri Web Service <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Accetta connessioni da qualsiasi rete invece che solo all'interno di questo dispositivo. Ci sono implicazioni di sicurezza per abilitarlo! La password Shared Secret sarà richiesta se impostata. 
:::

::: xdripitem xDrip Web Service Segret
&ensp;Shared Secret per il servizio web aperto (dovrebbe corrispondere all'API segret di Nightscout)
:::

#### Opzione Apri Web Service {#open-option}

Il servizio ha un'opzione `Apri Web Service`. Se è attiva, le connessioni possono arrivare da qualsiasi interfaccia di rete invece di essere limitate alla sola rete di loopback interna al dispositivo. Di solito attivare questa opzione espone la connessione wifi / lan / bluetooth pan del dispositivo, ma è possibile che venga esposta anche tramite la rete cellulare, se l'operatore supporta gli indirizzi IP pubblici.

Fai molta attenzione ad attivare questa opzione, perché rende accessibili funzioni potenti, ad esempio l'interfaccia tasker. È meglio usarla insieme all'opzione di autenticazione descritta qui sotto.

#### Autenticazione {#authentication}

Per motivi di sicurezza (chiunque sulla rete può accedere a questo servizio) dovresti proteggerlo con una password; se hai un sito Nightscout, usa il tuo API_SECRET.

Se `xDrip Web Service Segret` è impostato su qualcosa di diverso da una stringa vuota (il valore predefinito), le richieste che arrivano dalle reti aperte non di loopback devono fornire un header http `api-secret` contenente l'hash SHA1 della stessa password segreta, altrimenti la connessione viene rifiutata. Le informazioni sul rifiuto vengono salvate nel Registro eventi e restituite nella risposta http. Quando una connessione viene rifiutata, viene impostato il codice di risultato 403 (forbidden).

Inoltre, se un client fornisce l'header `api-secret`, la richiesta viene rifiutata anche se il secret di xDrip non è impostato. Questa funzione serve a garantire ai dispositivi client che si stanno collegando all'istanza di xDrip giusta (usando secret diversi). Può essere importante, ad esempio, quando si usa un loop.

L'autenticazione non è richiesta sull'interfaccia di rete locale di loopback (127.0.0.1)

```
api-secret: 915858afa2278f25527f192038108346164b47f2
```

Qui sopra è mostrato l'header http per la password `Abc`

#### Endpoint Pebble di Nightscout {#nightscout-pebble-endpoint}

`/pebble` emula lo stesso URL di Nightscout: con un quadrante che lo supporta, puoi inserire l'indirizzo nel quadrante, ad esempio impostando l'endpoint dei dati del quadrante Pebble Nightscout su:

```
http://127.0.0.1:17580/pebble
```

#### Endpoint sgv.json {#sgvjson-endpoint}

`/sgv.json` emula `/api/v1/entries/sgv.json?count=24` di Nightscout

```
http://127.0.0.1:17580/sgv.json
```

Il primo record contiene un'indicazione sulle unità usate: `units_hint` sarà `mgdl` o `mmol` per indicare la preferenza dell'utente, ma i valori vengono sempre inviati in mgdl

Puoi accedere anche all'endpoint dei passi aggiungendo un parametro alla query

```
http://127.0.0.1:17580/sgv.json?steps=1234
```

In questo caso cerca il numero `steps_result` nel primo record della risposta json: 200 indica successo, qualsiasi altro valore indica che l'impostazione dei passi non è riuscita. Il valore dei passi deve essere il contapassi cumulativo attuale del dispositivo.

Puoi accedere anche all'endpoint della frequenza cardiaca aggiungendo un parametro alla query

```
http://127.0.0.1:17580/sgv.json?heart=123
```

In questo caso cerca il numero `heart_result` nel primo record della risposta json: 200 indica successo, qualsiasi altro valore indica che l'impostazione dei bpm non è riuscita. Il valore deve essere la frequenza cardiaca attuale in bpm del dispositivo.

Puoi combinare i due come in una normale query string:

```
http://127.0.0.1:17580/sgv.json?steps=1234&heart=123
```

C'è anche l'opzione `brief_mode=Y`, che puoi usare per escludere alcuni campi dai risultati e ridurre la dimensione della risposta.

C'è anche l'opzione `no_empty=Y`, che puoi usare perché un insieme di dati vuoto restituisca `""` invece di `"[]"`

C'è anche l'opzione `all_data=Y`, che puoi usare per ottenere in più i dati della sessione del sensore precedente.

C'è anche l'opzione `sensor=Y`, che puoi usare per ottenere i dati sull'età del sensore

C'è anche l'opzione `collector=Y`, che puoi usare per ottenere i messaggi di avviso del collector. Se il messaggio è vuoto non viene restituito nulla.

Puoi accedere anche all'endpoint tasker aggiungendo un parametro alla query

```
http://127.0.0.1:17580/sgv.json?tasker=osnooze
```

cerca `tasker_result` nella prima riga della risposta json per sapere se l'operazione è riuscita o no.

`OSNOOZE` è la sospensione opportunistica, che puoi richiamare anche quando nessun avviso sta suonando

`SNOOZE` è la sospensione tasker tradizionale, che invia la sospensione ai follower e usa più cpu

#### Endpoint treatments.json {#treatmentsjson-endpoint}

`/treatments.json` emula `/api/v1/treatments.json?count=24` di Nightscout

```
http://127.0.0.1:17580/treatments.json
```

#### Endpoint status.json {#statusjson-endpoint}

Implementa un piccolo sottoinsieme dei dati che potresti ricevere dallo status.json di Nightscout

```
http://127.0.0.1:17580/status.json
```

I risultati hanno questo aspetto:

```
{"thresholds":{"bgHigh":9.4,"bgLow":3.9}}
```

Le soglie alta e bassa impostate nell'app, espresse nelle unità locali.

#### Endpoint Libre 2 {#libre-2-endpoint}

`/Libre2ConnectCode.json` restituisce il buffer di sblocco Bluetooth e l'indirizzo MAC del dispositivo.

È usato da [whole house](./sync#whole-house).

```
http://127.0.0.1:17580/Libre2ConnectCode.json
```

#### Endpoint Tasker {#tasker-endpoint}

L'endpoint `/tasker` ti permette di inviare richieste all'interfaccia tasker via http. Così un quadrante che supporta solo endpoint web (ad es. FitBit) può inviare una richiesta di sospensione come questa:

```
http://127.0.0.1:17580/tasker/SNOOZE
```

#### Endpoint dei passi {#steps-endpoint}

`/steps` permette di impostare i dati attuali del contapassi

```
http://127.0.0.1:17580/steps/set/1234
```

Deve essere il contapassi cumulativo attuale del dispositivo che misura i passi, non un dato storico.

#### Endpoint della frequenza cardiaca {#heart-endpoint}

`/heart` permette di impostare la frequenza cardiaca attuale in bpm

```
http://127.0.0.1:17580/heart/set/123/1
```

Deve essere la frequenza cardiaca attuale in BPM del dispositivo di misura, non un dato storico. Il primo parametro sono i BPM e il secondo la precisione. Se non sei sicuro del parametro di precisione, impostalo semplicemente a 1.

<br>

### Servizio di Trasmissione API {#broadcast-service-api}

Questo servizio permette di trasmettere i valori di xDrip tramite un'API e può essere usato da app esterne come [WatchDrip+](https://bigdigital.home.blog/2022/06/16/watchdrip-a-new-application-for-xdrip-watch-integration) (attiva la funzione per WatchDrip+).

::: xdripitem Servizio di Trasmissione API <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Abilita la comunicazione tra xDrip e applicazioni terze parti utilizzando la nuova API
:::

::: xdripitem Abilita il trasferimento dell'IoB nelle API <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Abilita la segnalazione dei valori IoB nell'endpoint Web Service API utilizzato da alcuni smartwatch
:::

::: xdripitem Recupera IoB dall'app compagno <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Recupera il valore IoB dall'app compagno in esecuzione sullo stesso dispositivo, come l'app Omnipod 5
:::

<br>

### Google Health Connect {#google-health-connect}

Puoi condividere informazioni con Google Health.

::: xdripitem Google Health Connect
&ensp;Invia e ricevi dati da Google Health Connect e Google Fit
:::

Devi avere installato sul dispositivo [Health Connect](https://play.google.com/store/apps/details?id=com.google.android.apps.healthdata&hl=en&gl=US), disponibile per Android 8 e successivi.

::: xdripitem Usa Health Connect <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Richiede Android 8+ e Google app compagno oppure Android 14+
:::

Puoi poi decidere di usare i dati in entrata e di consentire quelli in uscita.

xDrip può condividere passi, frequenza cardiaca e glicemia con Google Health.

::: xdripitem Ottieni dati da Health Connect <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Invia dati a Health Connect <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

::: xdripitem Gestione permessi
&ensp;Apri le impostazioni di Health Connect per gestire manualmente i permessi
:::

Su alcune versioni di Android (in particolare 15 e 16) xDrip non può aprire direttamente la propria schermata dei permessi di Health Connect. Apre allora l'app Health Connect: vai in *Autorizzazioni app* e seleziona xDrip per gestirli. Se Health Connect non si può aprire affatto, un messaggio ti chiede di aprire tu stesso l'app Health Connect e di gestire lì i permessi di xDrip.

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
