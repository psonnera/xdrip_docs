---
source_hash: 32e9d6dee6
source_commit: 9eea450
---
Finché non è selezionata una sorgente dati della glicemia, xDrip mostra la procedura guidata della sorgente dati. Puoi attivarla o disattivarla dal [menu goccia di sangue](../use/mainUI#blood-drop-menu), poi con Pulsante Assistente Sorgente.

<img src="./images/ChooseDataSource.png" style="zoom:50%;" />

Scorri verso il basso finché non trovi il tuo sensore o il tuo caso d'uso.

## G6, G7, 1, 1+ {#g6-g7-1-1}

Se colleghi xDrip direttamente al sensore ([G6, G7, 1, 1+](./g6)), **non potrai** usare l'app del produttore né caricare i dati su Clarity (puoi usare [Nightscout](https://nightscout.github.io/) o [Tidepool](../use/cloud#tidepool)). Potresti riuscire a condividere i dati tramite i server [Share](../use/cloud#dex-share), ma la condivisione deve essere prima configurata con le app del produttore.

<img src="./images/DS-DxDrip.png" style="zoom:50%;" />

Se usi le app del produttore (G6, G7, 1+), puoi collegare xDrip come [Share follower](./dexshare), purché sia stato configurato un follower con le app del produttore.

<img src="./images/DS-DShare.png" style="zoom:50%;" />

Se usi [BYODA](./byod) (solo G6) e hai attivato Broadcast to xDrip, non ti serve una connessione di rete per avere i dati in xDrip. Usa la sorgente dati Inter-app broadcast

<img src="./images/DS-BYOD.png" style="zoom:45%;" />

Puoi aggiungere xDrip alla tua configurazione attuale e selezionare [Companion App](./companion) per far leggere a xDrip la glicemia dalle notifiche dell'app del produttore (G6, G7, 1, 1+, Stelo). Nota che con l'app del produttore Stelo fornisce letture ogni 15 minuti.

<img src="./images/DS-DComp.png" style="zoom:50%;" />

Ed è possibile anche se usi [CamAPS](./companion), sempre con la sorgente dati Companion App

<img src="./images/DS-GCAPS.png" style="zoom:50%;" />

## Libre {#libre}

xDrip si collega direttamente ai Libre 2/2+ UE; puoi usare i Libre 1 e i 14 giorni USA con un dispositivo bridge. Gli altri sensori Libre 2 e 3 non sono supportati direttamente.

Puoi collegare i Libre 2/2+ UE a xDrip aggiungendo [OOP2](../use/OOP). **Non puoi** usare l'app del produttore per gli allarmi (solo per le scansioni NFC) né caricare i dati sui server del produttore (usa [Nightscout](https://nightscout.github.io/) o [Tidepool](../use/cloud#tidepool)). Usa la sorgente dati [Libre Bluetooth](./libreBT).

<img src="./images/DS-L2EU.png" style="zoom:50%;" />

Poiché i Libre 1 non hanno il Bluetooth, devi aggiungere un dispositivo [bridge](./libreBT). Usa la sorgente dati [Libre Bluetooth](./libreBT).  
Alcuni di questi bridge funzionano anche con i Libre 2/2+ UE. Verifica che il tuo sensore non richieda un [OOP](../use/OOP).

<img src="./images/DS-LBT.png" style="zoom:50%;" />

Dalla release 2026.11.21 il gruppo Libre include anche la sorgente dati [Li3](./li3), che collega xDrip direttamente a un dispositivo Li3 tramite NFC e Bluetooth.

Per i sensori non supportati (Libre 2/2+ non UE e Libre 3/3+) puoi anche usare Diabox o Juggluco, e poi [trasmettere](./libre2patch) i dati a xDrip, che li riceverà con la sorgente dati [Libre 2 patched](./libre2patch) (**non** l'app modificata stessa).

<img src="./images/DS-LOther.png" style="zoom:50%;" />

Puoi seguire un CGM Libre 2/2+ o un Libre 3/3+ con xDrip tramite la sorgente dati [Web Follower](./webfollower).

<img src="./images/DS-L3Web.png" style="zoom:50%;" />

## Guardian e MiniMed {#guardian-and-minimed}

Con un [microinfusore 640G/670G](./640_670) devi ricevere i dati glicemici dal microinfusore usando un glucometro collegato al telefono con un cavo OTG.

<img src="./images/DS-M6xx.png" style="zoom:50%;" />

Puoi aggiungere xDrip alla tua configurazione attuale e selezionare [Companion App](./companion) per far leggere a xDrip la glicemia dalle notifiche dell'app del produttore.

<img src="./images/DS-MComp.png" style="zoom:50%;" />

Puoi seguire i dati del sensore quando sono condivisi tramite [Carelink](./carelinkfollow), ma il produttore potrebbe rendere spesso inutilizzabile questa funzione.

<img src="./images/DS-MFoll.png" style="zoom:50%;" />

## [Aidex](./aidex) {#aidex}

Puoi ricevere in xDrip i dati dall'app del produttore.

Puoi aggiungere xDrip alla tua configurazione attuale e selezionare [Companion App](./companion) per far leggere a xDrip la glicemia dalle notifiche dell'app del produttore.

## Sibionics {#sibionics}

L'[app modificata](https://t.me/s/kubarev_modz) ti permette di usare xDrip con la sorgente dati [Inter-app broadcast](./640_670).

## CareSens Air {#caresens-air}

Puoi ricevere in xDrip i dati dall'app del produttore con la sorgente dati [CareSens Air](./caresens) (o Inter-app broadcast).

<img src="./images/DS-CareSens.png" style="zoom:50%;" />

<br>

## Connessione Bluetooth a un sensore o a un bridge {#bluetooth-connection-to-a-sensor-or-a-bridge}

Quando colleghi xDrip direttamente a un sensore, è xDrip a gestire la connessione Bluetooth, o la connessione al dispositivo Bluetooth che invia i dati del tuo sensore (chiamato bridge). 

::: warning Attenzione
**NON** provare a collegarti da Impostazioni Android -> Connessioni -> Bluetooth! 
:::

<img src="./images/Install26.png" style="zoom:100%;" />

Se il tuo bridge è associato ad Android, dissocialo prima di continuare.

<img src="./images/Install27.png" style="zoom:100%;" />

::: warning Un dispositivo alla volta
Sensori e bridge possono collegarsi a un solo smartphone (o tablet) alla volta, e a una sola app alla volta.  
Dovresti disinstallare l'app del produttore per collegare xDrip al tuo sensore o bridge.  
Se un altro dispositivo è collegato al tuo sensore o bridge, spegnilo o disattiva l'altra app prima di provare a collegarti con xDrip.  
**Non puoi collegarti a due telefoni o app. Con un'eccezione per Dex G6/G7/1 e 1+: il secondo dispositivo può essere solo un ricevitore/microinfusore collegato o un orologio BlueJay.**
:::

<br>

Ora dovresti vedere la procedura guidata di selezione della sorgente dati.

<img src="./images/ChooseDataSource.png" style="zoom:50%;" />

Se non la vedi, tocca questo pulsante per visualizzarla.

<img src="./images/Install12.png" style="zoom:75%;" />

Se il pulsante non è visibile, puoi mostrarlo con una pressione prolungata sull'icona di xDrip, attivando `Pulsante Assistente Sorgente`.

<img src="../images/UImenu.png" style="zoom:75%;" />

<br>

## Selezione del sensore {#sensor-selection}

I sensori inutilizzati e obsoleti sono stati rimossi da questa documentazione.

### I seguenti sensori sono supportati direttamente da xDrip: {#the-following-sensors-are-supported-directly-by-xdrip}

- [G6, G7, 1 e 1+](./g6)  
  <img src="./images/Dex.png" style="zoom:54%;" />    <img src="./images/Install31.png" style="zoom:50%;" />
- [Libre (con bridge)](./libreBT)  
  <img src="./images/Libre.png" style="zoom:54%;" />    <img src="./images/Bridge.png" style="zoom:50%;" />
- Libre con smartwatch SWR50 modificato  
  <img src="./images/Libre.png" style="zoom:54%;" />    <img src="./images/LibreAlarm.png" style="zoom:51%;" />
- [Libre 2 (solo UE)](./libre2)  
  <img src="./images/Libre.png" style="zoom:54%;" />    <img src="./images/Bridge.png" style="zoom:50%;" />
- [Medtrum A6](./medtrum)  
  <img src="./images/Other.png" style="zoom:54%;" />    <img src="./images/Medtrum.png" style="zoom:53%;" />
- [CareSens Air](./caresens)  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/CareSensAir.png" style="zoom:54%;" />

### I seguenti sensori e funzioni sono supportati con un'app compagno: {#the-following-sensors-and-features-are-supported-with-a-companion-app}

- [Libre 2 (solo UE)](./libre2patch)  
  <img src="./images/Libre.png" style="zoom:51%;" />    <img src="./images/Libre2Patch.png" style="zoom:53%;" />
- [Eversense](./eversense)  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/Eversense.png" style="zoom:53%;" />
- [Microinfusori 640G/670G](./640_670)  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/640670.png" style="zoom:53%;" />
- [Build your own app (BYODA)](./byod) per sensori G6  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/640670.png" style="zoom:53%;" />
- [Aidex](./aidex)  
  <img src="./images/SmartGuide.png" style="zoom:53%;" />
- [Companion App](./companion) per G6, G7, 1, 1+, CamAPS ed Eversense  
  Vedi più sotto.

<br>

## Modalità follower {#follower-mode}

- [xDrip Sync](./xdripfollower) (richiede i Google Play Services)  
  <img src="./images/XDripSyncFollower.png" style="zoom:53%;" />
- [Nightscout](./nightscoutfollower)  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/Nightscout.png" style="zoom:53%;" />
- [Dex Share](./dexshare)  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/DexShare.png" style="zoom:53%;" />
- [Libre Web Follower](./webfollower)  
  Vedi più sotto.
- [CareLink Follower](./carelinkfollow)  
  Vedi più sotto.

<br>

## Cambiare sorgente dati {#changing-data-source}

Puoi selezionare un'altra sorgente dati senza usare la procedura guidata, dal menu delle impostazioni:

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine
:::

[G6, G7, 1 e 1+](./g6) 

::: xdripitem Dati Hardware di origine
&emsp;Dex<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Libre (con bridge)](./libreBT) 

::: xdripitem Dati Hardware di origine
&emsp;Libre Bluetooth<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Libre whole house](https://github.com/tzachi-dar/LibreAllHouse)

::: xdripitem Dati Hardware di origine
&emsp;Libre Bluetooth + wifi<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;Libre wifi<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[xDrip Sync](./xdripfollower)

::: xdripitem Dati Hardware di origine
&emsp;xDrip+ Sync Follower<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

Libre con smartwatch SWR50 modificato 

::: xdripitem Dati Hardware di origine
&emsp;LibreAlarm<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Libre 2 (solo UE), Diabox o Juggluco](./libre2patch)

::: xdripitem Dati Hardware di origine
&emsp;Libre (patched App)<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Microinfusori 640G/670G](./640_670), [Eversense](./eversense) e [Build your own app (BYODA)](./byod)

::: xdripitem Dati Hardware di origine
&emsp;Inter-app broadcast<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

Prima della release 2026.09.04 questa sorgente dati si chiamava "640G / EverSense".

[Medtrum A6/S7](./medtrum) 

::: xdripitem Dati Hardware di origine
&emsp;Medtrum A6<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Nightscout](./nightscoutfollower) 

::: xdripitem Dati Hardware di origine
&emsp;Nightscout Follower<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Dex Share](./dexshare) 

::: xdripitem Dati Hardware di origine
&emsp;Dex Share Follower<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Companion App](./companion) per G6, G7, One e CamAPS

::: xdripitem Dati Hardware di origine
&emsp;Companion App<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[SmartGuide](./smartguide)

::: xdripitem Dati Hardware di origine
&emsp;SmartGuide<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[GlucoRx/Aidex](./aidex)

::: xdripitem Dati Hardware di origine
&emsp;GlucoRx/Aidex App<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Web Follower](./webfollower) per CGM Libre 2 e Libre 3

::: xdripitem Dati Hardware di origine
&emsp;Web Follower<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[CareLink](./carelinkfollow)

::: xdripitem Dati Hardware di origine
&emsp;CareLink Follower<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

##### Disabilita Collezione {#disable-collection}

Se vuoi disattivare xDrip.

::: xdripitem Dati Hardware di origine
&emsp;Disabilita Collezione<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

<br>

::: info Nota
L'elenco `Dati Hardware di origine` contiene anche `Bluetooth Wixel`, `xBridge Wixel`, `Wifi Wixel`, `Wifi Wixel + BT Wixel` e  `Wifi Wixel + xBridge Wixel`: sono voci legacy/obsolete non trattate in questa documentazione.
:::

<br>

[*Ultima modifica 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
