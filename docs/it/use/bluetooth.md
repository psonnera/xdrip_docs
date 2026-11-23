---
source_hash: c7d2a497a5
source_commit: 7a18e7c
---
Il gran numero di produttori di telefoni Android e le particolarità di sensori e bridge hanno reso l'affidabilità della connessione Bluetooth una delle principali difficoltà di xDrip. Questo menu contiene molte impostazioni avanzate che non possono essere standardizzate per tutti i sistemi.

::: info Configura le impostazioni Bluetooth come indicato qui sotto
:::

Si consiglia di procedere per tentativi, ma cambia una sola impostazione alla volta per non creare ulteriore confusione.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Impostazioni Meno Usate  
&ensp;&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_bluetooth_settings_grey600_48dp.png" style="width:5%;" />&ensp;Impostazioni Bluetooth
:::

#### Attiva Bluetooth {#turn-bluetooth-on}

Questa opzione fa sì che xDrip provi ad attivare il Bluetooth.

Se xDrip si connette a un dispositivo Bluetooth, Attiva Bluetooth è indispensabile.  
xDrip potrebbe non riuscire a scavalcare del tutto le impostazioni del telefono: se disattivi il Bluetooth nelle impostazioni di Android o metti il telefono in modalità aereo, potrebbe non riuscire a riattivarlo. Il Bluetooth deve essere attivato nelle impostazioni di Android se vuoi che xDrip lo usi.  

*Collector: gestione BT globale (bridge classico + OB1 Dex) — Dexcom G5/G6/G7, bridge G4/Libre*

::: xdripitem Attiva Bluetooth<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Attiva automaticamente il bluetooth se è spento quando si prova a connettersi a un dispositivo bluetooth 
:::

#### Watchdog Bluetooth {#bluetooth-watchdog}

In caso di dati mancanti per una perdita di connessione Bluetooth, puoi fare in modo che xDrip spenga e riaccenda il Bluetooth del telefono; il tempo predefinito è di 20 minuti senza dati. Puoi personalizzare questo valore.

Se vedi il messaggio **xDrip turned off Bluetooth**, probabilmente è scattato il watchdog e xDrip sta cercando di ristabilire la connessione con il sensore.

*Collector: logica di recupero globale (collector classici + sequencer) — collector Dexcom e basati su bridge*

::: xdripitem Watchdog Bluetooth<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Resetta Bluetooth (spegni e riaccendi) se non si ricevono dati in 20 minuti
:::

Quando il watchdog è attivato, puoi scegliere dopo quanto tempo senza dati deve scattare: 20 (predefinito), 15, 10 o 5 minuti.

::: xdripitem Valore timer per il watchdog Bluetooth
&ensp;Valore in minuti
:::

::: info Nota
Tieni presente che l'attivazione del watchdog Bluetooth provoca una disconnessione Bluetooth temporanea di tutti i dispositivi connessi. Potresti voler disattivare questa funzione se usi AAPS e il tuo bridge/microinfusore non recupera automaticamente la connessione Bluetooth.  
Nota che il collector Dexcom (G5/G6/G7/ONE/ONE+/Stelo) ha un proprio watchdog Bluetooth, sempre attivo e non controllato da questa impostazione (l'impostazione Dex Bluetooth Watchdog è stata rimossa nella versione [2026.04.22](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.04.22)).
:::

#### Chiusura GATT per scollegamento BLE {#close-gatt-on-ble-disconnect}

Quando questa opzione è attivata, xDrip esegue una disconnessione completa seguita da una riconnessione del dispositivo Bluetooth (chiusura del collegamento, rilevamento e connessione) quando la connessione si perde. Poiché questo potrebbe non essere efficace, si consiglia di lasciarla **disattivata**, così che il dispositivo resti in memoria e xDrip provi solo a riconnettersi a un dispositivo BLE già noto.

*Collector: collector bridge classico (`DexCollectionService`) — bridge G4/Libre, BlueReader/Atom/Tomato*

::: xdripitem Chiusura GATT per scollegamento BLE<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Se il watchdog bluetooth si attiva spesso, provare a deselezionare questa opzione per vedere se aiuta
:::

#### Usa scansione {#use-scanning}

Usa scansione esegue l'equivalente di Scansione Bluetooth dal menu principale per cercare di recuperare una connessione persa. Con i telefoni più recenti non è sempre efficace. Lasciala inizialmente **disattivata**, a meno che non si dimostri utile.

*Collector: collector bridge classico (`DexCollectionService`) — bridge G4/Libre, BluKon*

::: xdripitem Usa scansione<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Scansiona prima di connettersi a xBridge e Libre Bluetooth
:::

#### Use BLE manager {#use-ble-manager}

Usa un sistema di gestione BLE più moderno. Lascialo **disattivato**, a meno che tu non stia risolvendo un problema di connessione e ti sia stato consigliato di provarlo.

*Collector: collector bridge classico (`DexCollectionService`) — dispositivi basati su bridge*

::: xdripitem Use BLE manager<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Use a more modern BLE manager system
:::

#### Trust Auto-Connect {#trust-auto-connect}

Trust Auto-Connect dipende molto dal telefono. È **attivato** per impostazione predefinita. Se hai un Samsung, Xiaomi, OnePlus, Oppo, Huawei o Realme probabilmente dovresti disattivarlo. Se perdi spesso la connessione e non riesci a recuperarla, prova a disattivarlo.

*Collector: collector bridge classico + collector OB1 Dex — Dexcom G5/G6/G7, dispositivi bridge*

::: xdripitem Trust Auto-Connect<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Usa e confida nella funzione di connessione automatica bluetooth di Android (sconsigliato per miaomiao)
:::

#### Usa Scansione In Background {#use-background-scan}

Usa Scansione In Background è una funzione delle versioni più recenti di Android, **attivata** per impostazione predefinita. Se perdi regolarmente la connessione, prova a disattivarla.

*Collector: collector con sequencer/scansione in background (Android O+) — soprattutto collector Dexcom/BLE*

::: xdripitem Usa Scansione In Background<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Utilizza la funzione di scansione bluetooth in background Android 8+
:::

#### Companion Bluetooth {#companion-bluetooth}

Companion Bluetooth permette all'app di funzionare insieme all'app master Dex connessa al sensore.

*Collector: listener compagno BlueTails — trasmettitori Dexcom in configurazioni companion/sniffer*

::: xdripitem Companion Bluetooth<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Use Bluetooth with companion app data source
:::

#### Bluetooth Wakelocks {#bluetooth-wakelocks}

I Bluetooth wakelock non sono consigliati e vanno lasciati **disattivati**.

*Collector: collector classico + percorsi di callback BLE — soprattutto collector basati su bridge*

::: xdripitem Bluetooth Wakelocks<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Vecchi wakelocks bluetooth (possono necessitare più batteria) che potrebbero essere necessari per la ricezione dei bluetooth  
:::

#### xBridge+ Modalità di Polling {#xbridge-polling-mode}

xBridge+ Modalità di Polling permette a xDrip di inviare richieste al bridge. Anche se non ha alcun effetto con altri dispositivi Bluetooth, puoi attivarla se perdi spesso la connessione, perché terrà comunque il Bluetooth del telefono occupato a tentare di connettersi.

*Collector: collector bridge classico (`DexCollectionService`) — xBridge e hardware simile*

::: xdripitem xBridge+ Modalità di Polling<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Supporto sperimentale per la funzione di polling xBridge+
:::

#### Usa sempre i servizi BT in modalità discover {#always-discover-services}

Attivato per impostazione predefinita. Visibile solo con la Modalità Sviluppatore attivata.

*Collector: collector bridge classico (`DexCollectionService`) — dispositivi BLE basati su bridge*

::: xdripitem Usa sempre i servizi BT in modalità discover<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Verifica servizi Bluetooth ad ogni connessione
:::

#### Use GATT refresh {#use-gatt-refresh}

Indica se usare il meccanismo di refresh GATT di basso livello. Attivato per impostazione predefinita. Visibile solo con la Modalità Sviluppatore attivata.

*Collector: collector OB1 Dex, collector di tipo JamBase — Dexcom G5/G6/G7, Medtrum*

::: xdripitem Use GATT refresh<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Whether to use the low level gatt refresh mechanism
:::

#### Consenti unbonding Blucon {#allow-blucon-unbonding}

Consenti unbonding Blucon è utile solo se usi un bridge BluCon, perché gli altri non creano un'associazione (bonding) con il telefono. Se ricevi spesso richieste di associazione con questo bridge, disattivalo.

*Collector: percorso bridge BluKon/Libre — configurazioni BluKon e bridge Libre affini*

::: xdripitem Consenti unbonding Blucon<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Adatto solo per telefoni che supportano l'accoppiamento automatico
:::

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
