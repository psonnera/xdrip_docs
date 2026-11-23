---
source_hash: 972ebaa79c
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Stato del sistema
:::

Stato del sistema fornisce informazioni interne sullo stato del collector di xDrip (da un sensore o come follower), oltre che sulla condivisione, sui follower e sugli smartwatch collegati direttamente.

Puoi condividere uno screenshot con il pulsante di condivisione di Android in alto a destra.

::: xdripitem <img src="../images/BDM.png" style="zoom:75%;" />Stato del sistema<span class='symbol'><img src="../images/Share.png" style="zoom:75%;" /></span>
:::

### Pagina di stato classica {#classic-status-page}

Questa pagina mostra informazioni sulla versione attualmente installata.

::: xdripitem <div style="background-color: DodgerBlue; color: white; text-align: center;">  &emsp;Classic Status Page&emsp;</div>
&emsp;Versione: a2bbca9-2024.11.26
:::

Le informazioni sulla versione ti permettono di [trovare rapidamente la release o pre-release corrispondente](https://github.com/NightscoutFoundation/xDrip/releases). Prima della data della versione vedrai la versione di build.

Qualsiasi nome di versione che mostra informazioni aggiuntive, come debug, dev, il nome di uno smartwatch, carelink, è una [versione fork](../install/download#forked-versions) di xDrip e potrebbe non contenere tutte le funzioni più recenti dell'app rilasciata (ma probabilmente qualcuna in più).

In questa pagina trovi il tipo di sorgente dati (quella che hai selezionato per ricevere i valori di glicemia).

::: xdripitem Sorgente Dati:
:::

La riga successiva mostra la dimensione del database di xDrip: la quantità di memoria che usa sul telefono.

::: xdripitem Dimensione Database:
:::

Nel caso di un sensore fisico, dopo il tipo di sorgente dati vedrai il nome del dispositivo Bluetooth effettivamente collegato a xDrip. Puoi anche vedere lo stato della connessione; tieni presente che alcuni sensori si collegano solo per poco tempo ogni 5 minuti, quindi Non connesso potrebbe non essere un vero problema.

::: xdripitem Dispositivo Bluetooth:
:::
::: xdripitem Stato della connessione:
:::
::: xdripitem Sensore attivato:
:::

Poiché questa pagina non si aggiorna automaticamente, devi toccare le frecce circolari per aggiornarla.

<img src="./images/M-SS-CS2.png" style="zoom:75%;" />

#### Riavvia Collector - Dimentica questo dispositivo {#restart-collector-forget-device}

::: xdrip <span style="background-color: white; color: black;">&ensp;RIAVVIA COLLECTOR&ensp;</span>&emsp;<span style="background-color: white; color: black;">&ensp;DIMENTICA QUESTO DISPOSITIVO&ensp;</span>
:::

Riavvia Collector riavvia il meccanismo interno di raccolta dati di xDrip. L'effetto dipende dalla sorgente dati.

Dimentica questo dispositivo ha effetto solo quando xDrip è collegato a un dispositivo tramite Bluetooth.  
Il dispositivo verrà scollegato e dovrai fare una scansione Bluetooth dal menu principale per ripristinare la connessione.

### Pagina di stato avanzata {#advanced-status-page}

La maggior parte delle sorgenti dati ha una scheda di stato avanzata. Scorri il dito sullo schermo verso sinistra per visualizzarla.

<img src="./images/M-SS.png" style="zoom:75%;" />

##### Buggy Samsung {#buggy-samsung}

Rinominato Buggy Handset perché anche altri dispositivi presentano questa non conformità.

##### Buggy Handset {#buggy-handset}

Non è un errore, indica solo che xDrip sta [correggendo](https://github.com/NightscoutFoundation/xDrip/issues/435) una non conformità ad Android di alcuni dispositivi.  
Si consiglia di [attivarlo](../use/misc#wake-workarounds) in caso di perdita di dati.

<img src="./images/M-SS-CSBSsg.png" style="zoom:75%;" />

##### Slowest wake-up {#slowest-wake-up}

Indica quando xDrip ha ricevuto i dati rispetto all'orario previsto. Qualche secondo è accettabile, ma alcuni minuti possono essere il segnale di un problema di connettività.

<img src="./images/M-SS-CSWU.png" style="zoom:75%;" />

#### G6, G7, 1 e 1+ {#g6-g7-1-and-1}

Vedi [qui](https://navid200.github.io/xDrip/docs/Connectivity-troubleshoot.html).

#### Libre Bluetooth {#libre-bluetooth}

Se usi un bridge, vedi la pagina dedicata [qui](./librebridge).

Se usi un Libre 2 direttamente (cioè senza bridge), vedi la pagina dedicata [qui](./libre2direct).

#### xDrip Sync Follower {#xdrip-sync-follower}

::: warning Lavori in corso
A luglio 2024 Google ha chiuso la [API Firebase](https://firebase.google.com/docs/cloud-messaging/migrate-v1) deprecata che xDrip usava per xDrip Sync.  
Aggiorna xDrip a una versione del [23 luglio 2024](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.07.23) o successiva.
:::

Il follower xDrip è davvero semplice da [configurare](../use/syncsetup). Se hai problemi, nella maggior parte dei casi si tratta della connessione di rete o dei servizi Google Play.  
Avere anche [Nightscout](https://nightscout.github.io/) come soluzione follower di riserva è consigliato quando risolvi problemi o segui un bambino.

<img src="./images/M-SS-xF.png" style="zoom:75%;" />

I follower si aggiungono all'elenco man mano che vengono identificati; se rimuovi un follower, potrebbe volerci un po' di tempo prima che venga effettivamente tolto dall'elenco.

Per i problemi di configurazione iniziale vedi [qui](../install/xdripfollower).

#### Nightscout Follower {#nightscout-follower}

La pagina di stato avanzata mostra l'attività durante lo scaricamento da Nightscout. Se non ci sono dati disponibili, assicurati di avere valori di glicemia attuali in Nightscout.

In caso di errore di scaricamento, se il tuo sito Nightscout viene aggiornato regolarmente dal dispositivo master e vedi errori di download NS, potrebbe trattarsi di problemi di rete. Disattiva il Wi-Fi o i dati della SIM e poi prova il contrario, per escludere questo problema.

Se non ha mai funzionato, assicurati di aver [configurato](../install/nightscoutfollower) correttamente l'URL del follower.

<img src="./images/M-SS-NF.png" style="zoom:75%;" />

Le versioni di Android più vecchie possono usare certificati scaduti e quindi impedire il funzionamento del follower Nightscout. Non c'è soluzione.

<img src="./images/M-SS-NFcert.png" style="zoom:75%;" />

<br>

[*Ultima modifica 8/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
