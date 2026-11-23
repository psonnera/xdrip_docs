---
source_hash: a4207f8d58
source_commit: 7a18e7c
---
Trovi la documentazione di riferimento [qui](https://github.com/NightscoutFoundation/xDrip/blob/master/Documentation/WatchGuide.md).

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_watch_grey600_48dp.png" style="width:5%;" />&ensp;Caratteristiche Collegamenti Smart Watch  
&emsp;  Integrazione Android Wear
:::

Dopo aver installato xDrip sull'orologio associato al telefono, puoi attivare Wear.  
xDrip comunicherà allora con una sua versione ridotta presente sull'orologio.

::: xdripitem Integrazione Android Wear <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Inviare dati a Android Watchface Wear.
:::

Con alcune combinazioni di sensore e smartwatch, xDrip può essere usato direttamente dall'orologio, senza bisogno del telefono. Vedi più avanti per maggiori informazioni.

L'attivazione di Wear permette all'orologio di subentrare al telefono quando xDrip sul telefono perde la connessione con il sensore o il bridge.

::: xdripitem Abilita Indossare G5 Collection Service <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Collegare indossare per G5 quando il telefono è out-of-range
:::

La forzatura di Wear obbliga l'orologio a fare da dispositivo principale collegato al sensore o al bridge, anche se il telefono è vicino (consigliato).

::: xdripitem Forza Indossare servizio G5 Collection <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Telefono Force per l'uso Indossare G5 Collection Service
:::

Disabilita letture da Wear per batteria scarica fa sì che l'orologio lasci la connessione al sensore o al bridge, restituendola al telefono, quando il livello della sua batteria è troppo basso.

::: xdripitem Disabilita letture da Wear per batteria scarica <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Disabilita collezione forzata da Wear per allarme batteria smartwatch scarica
:::

Disabilita lettura forzata da smartwatch per assenza letture fa sì che l'orologio lasci la connessione al sensore o al bridge, restituendola al telefono, dopo un certo periodo senza letture, definito nel menu qui sotto.

::: xdripitem Disabilita lettura forzata da smartwatch per assenza letture <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
Disabilita la lettura forzata da Wear dopo minuti di letture mancante dallo smartwatch  
:::

Usa solo lo smartwatch può essere attivato se hai configurato l'orologio una volta ma non userai il telefono per collegarti al sensore o al bridge.

::: xdripitem Usa solo lo smartwatch <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Se pensi di utilizzare solo lo smartwatch in collector e mai il tuo telefono.
:::

Se hai più smartwatch Android Wear con xDrip, puoi scegliere quale farà da collector. Gli altri mostreranno solo i dati di xDrip.

::: xdripitem Dispositivo G5 esecuzione Collection Service
:::

::: info Cambio di orologio
Quando passi da un orologio all'altro, xDrip potrebbe non riuscire a comunicare le sue intenzioni a entrambi se uno è spento. Se vuoi cambiare l'orologio che raccoglie i dati, forza il collector in xDrip e forza il collector anche nel menu xDrip Prefs dell'orologio.
:::

Sincronizza log Wear è una funzione molto utile per la risoluzione problemi: aggiunge i log dell'orologio al [registro eventi](../use/3dotsmenu#events-log) di xDrip, con un prefisso che indica che l'attività riguarda l'orologio. Il prefisso predefinito è `wear`, ma puoi personalizzarlo. Ti consigliamo di lasciarla attiva.

::: xdripitem Sincronizza log Wear <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Invia eventi Wear in visualizzazione logs
:::

Visualizzazione Trattamenti aggiunge i simboli dei trattamenti sul grafico dell'orologio.

::: xdripitem Visualizzazione Trattamenti <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Visualizzare trattamenti nel grafico
:::

## Modalità collector autonomo {#standalone-collector-mode}

L'estensione Wear di xDrip contiene anche la parte di xDrip che si collega ad alcuni sensori: puoi quindi far lavorare l'orologio al posto del telefono e fargli gestire la comunicazione e le letture, senza avere il telefono vicino.

Questa funzione non è disponibile per tutti i sensori, vedi la tabella qui sotto:

| Sensore                      | Wear 1.x | Wear 2.x | Wear 3+ |
| ---------------------------- | -------- | -------- | ------- |
| G5/G6/1                      | Sì       | Limitato* | No      |
| G7/1+                        | No       | No       | No      |
| Libre 1 con bridge           | Sì       | Sì       |         |
| Libre 14 days US con bridge  | Sì**     | Sì**     |         |
| Libre 2/2+ EU senza bridge   | No       | No       |         |
| Libre 2/2+ EU con bridge     | Sì**     | Sì**     |         |

***Limitato\*:*** Sulla maggior parte degli smartwatch Android Wear sono presenti alcuni bug che impediscono il corretto funzionamento con G5/G6. Nel migliore dei casi avrai una lettura ogni 10 minuti. Alcuni orologi possono essere [modificati](https://github.com/NightscoutFoundation/xDrip/wiki/Patching-Android-Wear-devices-for-use-with-the-G5) per ottenere letture ogni 5 minuti.

::: info Perché il mio orologio non riesce a raccogliere da solo i dati di un G5/G6?
La maggior parte degli orologi Android Wear esce di fabbrica con bug nel firmware Bluetooth che interrompono il ciclo di connessione del G5/G6: l'orologio perde letture o ne riceve solo una ogni 10 minuti. L'unica soluzione trovata è stata modificare il firmware dell'orologio stesso: sbloccare il bootloader e installare una patch tramite una recovery personalizzata. Questo fa decadere la garanzia ed esiste solo per pochi orologi datati (Asus Zenwatch 2/3, Huawei Watch e Watch 2, LG G Watch, Polar M600). La spiegazione completa, l'elenco degli orologi supportati e i "care pack" da scaricare si trovano nella pagina wiki [Patching Android Wear devices for use with the G5](https://github.com/NightscoutFoundation/xDrip/wiki/Patching-Android-Wear-devices-for-use-with-the-G5). Se il tuo orologio non è nell'elenco, non può raccogliere direttamente i dati di un G5/G6: usalo invece come display del telefono.
:::

***Sì\*\*:*** Ti serve un telefono funzionante con [OOP1](../use/OOP) o [OOP2](../use/OOP#oop2) e devi anche [caricare](../troubleshoot/ADB#smartwatch) la stessa app OOP sull'orologio. Alcuni bridge potrebbero non essere compatibili.

### Prerequisiti {#prerequisites}

La funzione è disponibile per le combinazioni di sensore e orologio descritte sopra.

L'estensione di xDrip è installata sull'orologio con la stessa versione presente sul telefono.

La connettività di xDrip sul telefono è buona (cioè i parametri Bluetooth sono impostati correttamente).

xDrip sull'orologio deve essere autorizzato ad accedere alla posizione.  
<img src="./images/M-S-SW-AW33.png" style="zoom:75%;" />

### Sequenza consigliata {#recommended-sequence}

Primo tentativo o ripristino dopo un errore:

1 - In xDrip sul telefono: disattiva la forzatura del collector, poi la raccolta, poi Wear, in questo ordine.  

::: xdripitem Forza Indossare servizio G5 Collection <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

::: xdripitem Abilita Indossare G5 Collection Service <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

::: xdripitem Integrazione Android Wear <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

2 - Attiva i log di Wear.  

::: xdripitem Sincronizza log Wear <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Invia eventi Wear in visualizzazione logs
:::

3 - Riavvia lo smartwatch. Aspetta che sia completamente avviato.

4 - Sul telefono attiva solo Wear.  

::: xdripitem Integrazione Android Wear <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

5 - Aspetta che il grafico di xDrip sia completamente visualizzato sull'orologio (attendere una nuova misurazione non guasta).

6 - Tieni telefono, orologio e sensore vicini e attiva prima la raccolta, poi la forzatura del collector.  

::: xdripitem Abilita Indossare G5 Collection Service <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

::: xdripitem Forza Indossare servizio G5 Collection <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

7 - L'associazione richiede di solito 10 minuti: apri il registro eventi di xDrip sul telefono e aspetta gli eventi che iniziano con `wear`.  
<img src="./images/M-S-SW-AW31.png" style="zoom:75%;" />

8 - Se tutto è andato bene, l'orologio dovrebbe ora essere in modalità autonoma.

##### Se l'orologio non si collega al bridge: {#if-the-watch-doesnt-connect-to-the-bridge}

- Nel menu xDrip Prefs dell'orologio, spunta Force Collector.  
  <img src="./images/M-S-SW-AW-ST3b.png" style="zoom:75%;" />
- Dal menu a 3 puntini del quadrante xDrip, scegli Restart Collector.  
  <img src="./images/M-S-SW-AW-3DM.png" style="zoom:75%;" />
- Nelle impostazioni Bluetooth dell'orologio, trova il bridge e fai finta di associarlo (non puoi associare il Miaomiao all'orologio, ma l'orologio proverà a stabilire un collegamento). Dopo il fallimento dell'associazione, aspetta 10 minuti che compaiano le letture.
- Se le letture non compaiono, disattiva Force Collector e ripeti la sequenza.

## Condivisione dei dati in modalità autonoma {#sharing-data-in-standalone-mode}

Se vuoi che l'orologio condivida i dati (xDrip Sync, Nightscout, ...), deve essere collegato al telefono e il telefono deve essere connesso a internet.

Questo non significa che debbano trovarsi nello stesso posto, ma l'orologio non condivide direttamente i dati: li invia al telefono, ed è il telefono a condividerli. Se l'orologio è connesso a internet tramite Wi-Fi o una SIM con piano dati, dovrà inviarli al telefono (anch'esso connesso a internet) e sarà il telefono a condividere i dati. Finché sono entrambi connessi a internet, non serve che siano vicini.

<img src="./images/M-S-SW-AW-XP24.png" style="zoom:75%;" />

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
