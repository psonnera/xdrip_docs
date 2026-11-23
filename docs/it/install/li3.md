---
source_hash: a98504fa65
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;Li3
:::

La sorgente dati Li3, aggiunta nella release [2026.11.21](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21), collega xDrip direttamente a un dispositivo Li3. Puoi selezionarla anche con la [procedura guidata della sorgente dati](./datasource), nel gruppo Libre.

xDrip avvia una nuova sessione, o prende il controllo di una sessione in corso, con una scansione NFC. Poi riceve le letture tramite Bluetooth.

- Le letture arrivano ogni 5 minuti, oppure ogni minuto se è attivata l'opzione [Libre one minute](../use/misc).
- Quando la connessione torna dopo un'interruzione, xDrip completa le letture mancanti con la cronologia del dispositivo. Le letture già registrate non vengono mai sostituite.
- **Questa sorgente dati non può essere calibrata.** Se ci provi, xDrip mostra *This sensor cannot be calibrated.* (questo sensore non può essere calibrato)

::: warning Attenzione
Quando xDrip avvia o prende il controllo di una sessione, l'app ufficiale smette di ricevere le letture e gli allarmi.
:::

<br>

## Prima di iniziare {#before-you-start}

- Il telefono deve avere l'NFC. Senza NFC, xDrip mostra *This phone has no NFC, so it cannot start a Li3.* (questo telefono non ha l'NFC, quindi non può avviare un Li3)
- Attiva l'NFC nelle impostazioni del telefono. Se la scansione NFC di xDrip è disattivata, xDrip propone di attivarla.
- xDrip ha bisogno dell'autorizzazione alla posizione, e la localizzazione deve essere attiva, per cercare il dispositivo via Bluetooth. La schermata Li3 chiede tutto ciò che manca.
- Ti serve una connessione a internet una volta, per scaricare la credenziale dell'app.
- Se non l'hai ancora fatto, [verifica che xDrip non venga messo in sospensione](./install#make-sure-xdrip-will-not-be-put-to-sleep).

<br>

## La schermata Li3 {#the-li3-screen}

La schermata Li3 elenca i passaggi della configurazione, mostra a che punto sei e legge le scansioni NFC mentre è aperta.  
Si apre da sola quando selezioni la sorgente dati Li3 e quando tocchi Inizializza Sensore senza che nessun sensore sia avviato. Puoi aprirla anche da Stato del sistema:

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Stato del sistema  
&emsp;Li3 Status  
&ensp;&emsp;Li3 &emsp;Open
:::

Finché la configurazione non è terminata, xDrip mostra anche una notifica che apre questa schermata: *Li3 setup not finished; open System Status, Li3* (configurazione Li3 non terminata; apri Stato del sistema, Li3).

Se scansioni il dispositivo mentre è aperta un'altra schermata, xDrip apre la schermata Li3 e ti chiede di scansionarlo di nuovo lì: *Scan the device again on the Li3 screen to start it or take it over* (scansiona di nuovo il dispositivo nella schermata Li3 per avviarlo o prenderne il controllo).

<br>

## Configurazione {#setup}

#### 1. Scaricare la credenziale dell'app {#1-download-the-app-credential}

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;DOWNLOAD APP CREDENTIAL&emsp;</div>
:::

Il dispositivo si abbina con una credenziale dell'app. Se non ne è ancora stata scaricata nessuna, xDrip propone di scaricarla quando apri la schermata Li3.  
Al termine, la riga App credential sotto i pulsanti mostra *Downloaded* (scaricata). Se il download non riesce, controlla la connessione a internet e tocca di nuovo Download.

#### 2. Account ID (solo per prendere il controllo di una sessione avviata da un'app ufficiale) {#2-account-id-only-to-take-over-a-session-started-by-an-official-app}

Salta questo passaggio per avviare una nuova sessione per xDrip.

Per prendere il controllo di una sessione avviata da un'app ufficiale, xDrip ha bisogno dell'account ID di quell'app.

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;LOOK UP ACCOUNT ID&emsp;</div>
:::

Accedi con l'account che ha avviato la sessione, non con un account follower. xDrip conserva solo l'account ID, non l'email né la password.  
Se l'accesso viene rifiutato a causa di nuove condizioni d'uso, apri l'app ufficiale con questo account, accetta le condizioni e poi riprova.  
Se la ricerca non riesce, puoi inserire tu stesso l'account ID nelle [impostazioni Li3](#li3-settings).

Poi scegli l'app che ha avviato la sessione:

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;SENSOR APP: LI3 APP&emsp;</div>
:::

::: xdripitem Which app started this session?
&ensp;Li3 app  
&ensp;Multi-sensor app
:::

#### 3. Scansionare il dispositivo {#3-scan-the-device}

Con la schermata Li3 aperta, scansiona il dispositivo con il telefono. xDrip ti pone una di queste domande:

| Dispositivo              | Account ID impostato                                               | Nessun account ID                                                |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Nuovo                 | **Start Sensor**: xDrip riceve le letture. L'app ufficiale può riprendere il dispositivo in seguito con lo stesso account. | **Start Sensor**: la sessione è per xDrip solo su questo telefono. **Il dispositivo non potrà mai passare a un'app ufficiale e andrà perso se reinstalli xDrip.** |
| Sessione in corso | **Take over Li3**: l'app ufficiale smette di ricevere le letture e gli allarmi. | Funziona solo per una sessione avviata da xDrip su questo telefono. Per una sessione avviata da un'app ufficiale, cerca prima il suo account ID. |

Senza account ID, puoi toccare *Look up account ID* oppure *Scan anyway* per proseguire senza.

Premi Ok, poi **scansiona di nuovo il dispositivo entro cinque minuti** per confermare.  
Quando funziona, xDrip mostra *Li3 ready, connecting by Bluetooth* (Li3 pronto, connessione via Bluetooth).

Se il dispositivo rifiuta il comando, controlla che l'app e l'account ID siano quelli con cui è stata avviata la sessione.  
Se xDrip usa già questo dispositivo, non viene inviato nulla. Per abbinarlo di nuovo, tocca Dimentica questo dispositivo nella schermata Li3, poi scansionalo.

#### 4. Attendere la prima lettura {#4-wait-for-the-first-reading}

Un dispositivo nuovo non invia letture durante più o meno la prima ora.

<br>

## Impostazioni Li3 {#li3-settings}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;&ensp;Impostazioni Meno Usate  
&emsp;&emsp;&emsp;Altre opzioni  
&emsp;&emsp;&emsp;&emsp;Li3
:::

::: xdripitem Account ID
&ensp;Needed to take over a session in progress. Leave empty to start a new session for xDrip on this phone only.
:::

Look up account ID, nella schermata Li3, lo compila per te.

::: xdripitem Official app
&ensp;The app the account uses
:::

Li3 app (predefinita) o Multi-sensor app. È la stessa scelta del pulsante Sensor app nella schermata Li3.

::: xdripitem Smooth Li3 readings <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Average recent readings to make them smoother
:::

Le impostazioni NFC che non si applicano a Li3 (età del sensore, giorni di scadenza, multiblocco, any tag, streaming Bluetooth Libre 2) sono nascoste mentre Li3 è la sorgente dati.

<br>

## Stato {#status}

La schermata Li3 e Stato del sistema → Li3 Status mostrano:

- **Device** (dispositivo)
- **Stage** (fase): cosa sta facendo xDrip in quel momento, ad esempio:
    - *No device; scan one with NFC* (nessun dispositivo; scansionane uno con l'NFC)
    - *No app credential; tap Download on the Li3 screen* (nessuna credenziale dell'app; tocca Download nella schermata Li3)
    - *Looking for the device; keep the phone near it* (ricerca del dispositivo; tieni il telefono vicino)
    - *Lost the device; trying again soon* (dispositivo perso; nuovo tentativo a breve)
    - *Connected; waiting for a reading* (connesso; in attesa di una lettura)
    - *Session ended; scan a new device with NFC* (sessione terminata; scansiona un nuovo dispositivo con l'NFC)
- **Last error** (ultimo errore)
- **Reading not stored** (lettura non registrata), quando xDrip ha rifiutato una lettura: nessun valore valido, l'ora di inizio della sessione sembra sbagliata, oppure il dispositivo ha segnalato la lettura come inaffidabile
- **Started** (avviato) e **Sensor life** (durata del sensore) (oppure *Expired*, scaduto)
- **Last reading** (ultima lettura)
- **App credential** (credenziale dell'app)

#### Dimenticare il dispositivo {#forget-device}

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;DIMENTICA QUESTO DISPOSITIVO&emsp;</div>
:::

xDrip smette di comunicare con questo dispositivo. Per usarlo di nuovo, scansionalo con l'NFC.  
Una sessione avviata senza account può tornare solo a xDrip su questo telefono.

#### Copiare la diagnostica {#copy-diagnostics}

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;COPY DIAGNOSTICS&emsp;</div>
:::

Copia le informazioni di diagnostica negli appunti. Incollale quando chiedi aiuto.

<br>

[*Ultima modifica 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
