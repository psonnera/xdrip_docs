---
source_hash: 87f439d0b6
source_commit: 7a18e7c
---
In questo menu sono disponibili altre opzioni.  
Se sono nascoste qui, probabilmente è perché non ti servirà modificarle tutti i giorni, oppure perché dovresti lasciarle come sono salvo indicazioni diverse.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;&ensp;Impostazioni Meno Usate  
&emsp;&emsp;&emsp;Altre opzioni
:::

##### Eseguire Collector in primo piano {#run-collector-in-foreground}

::: info Nota
Da quando è stato abbandonato il supporto ad Android 7 ([12 luglio 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.12)) questa opzione non è più disattivabile.
:::

Su Android 8.0 e successivi (la versione minima supportata) xDrip esegue sempre il collector come servizio in primo piano, per evitare che Android lo metta in sospensione. Viene quindi sempre mostrata una notifica persistente con il grafico, visibile anche sulla schermata di blocco.

Se preferisci non mostrare il grafico, l'opzione `Notifica Persistente Compatta` nello stesso menu mostra solo il valore attuale della glicemia.

::: xdripitem Notifica Persistente Compatta <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Abilita per nascondere il grafico nelle notifiche e visualizzare solo il valore attuale di glucosio.
:::

<img src="./images/M-S-LCS15a2.png" style="zoom:75%;" />

##### Modalità Sviluppatore {#engineering-mode}

Attiva funzioni potenzialmente pericolose o non testate. Non serve attivarla per riavviare un trasmettitore G5 o un vecchio G6 (quelli nuovi, chiamati Firefly, non possono essere riavviati). In realtà non hai bisogno di attivarla.

::: xdripitem Modalità Sviluppatore <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Consente di cambiare le impostazioni più pericolose: a vostro rischio e pericolo!
:::

Per attivare la Modalità Sviluppatore inserisci o pronuncia il trattamento `enable engineering mode`.

Ogni mese ti verrà ricordato che la Modalità Sviluppatore è attiva. Assicurati di averne davvero bisogno, altrimenti tienila disattivata.

<img src="./images/M-S-LCS15b3.png" style="zoom:52%;" />

##### Richiesta di Ottimizzazione della Batteria {#battery-optimization-prompt}

Va lasciata **disattivata**. xDrip deve essere [escluso dall'ottimizzazione](../install/install#authorize-background-activity) e non deve esserne soggetto. 

::: xdripitem Richiesta di Ottimizzazione della Batteria <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Con Android 6+ verifica che l'ottimizzazione della batteria sia spenta. Raccomandato
:::

##### Samsung Workarounds {#samsung-workarounds}

Rinominato Wake Workarounds perché anche altri dispositivi non sono conformi.

##### Wake Workarounds {#wake-workarounds}

Corregge una non conformità di alcuni dispositivi Android; ora è predefinito per Samsung, Xiaomi, OnePlus, Oppo e Huawei.   
Va tenuto **attivato**.

::: xdripitem Samsung Workaround <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Usa workaround per evitare il comportamento non standard a Android degli telefonini Samsung. Senza questo, di solito non si riesce a ricevere dati.
:::

Uso eccessivo Wakelocks non è necessario. Si tratta di messaggi di "risveglio" aggiuntivi che xDrip invia al dispositivo Android per impedirgli di entrare in sospensione. 

::: xdripitem Uso eccessivo Wakelocks <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Vecchi wakelocks gratuiti possono consumare la batteria, ma potrebbero essere necessari per NightWatch o Android Wear
:::

Mostra Valori Predetti (vecchio metodo) è deprecato. Usa la [simulazione predittiva](./predictions).

::: xdripitem Mostra Valori Predetti (vecchio metodo) <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Vecchio metodo - Non consigliato!
:::

Proper Ongoing è indispensabile per i dispositivi con Android 8 e successivi. Visibile solo con la Modalità Sviluppatore attivata.

::: xdripitem Proper Ongoing <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Use proper ongoing notification. Disabling this causes collector problems on Android 8+
:::

##### Algoritmo Out of Process {#out-of-process-algorithm}

L'[algoritmo Out Of Process](./OOP) permette di integrare un plugin esterno che fornisce valori glicemici simili a quelli del produttore per i sensori Libre, o che decodifica le informazioni del sensore Libre 2 EU.  
Se l'app esterna non è presente sul telefono o non fornisce le informazioni, xDrip non mostrerà la glicemia.

::: warning Attenzione
Questa opzione va attivata solo se usi un algoritmo Out Of Process versione 1 (OOP1).  
Deve essere disattivata per OOP2.
:::

::: xdripitem Algoritmo Libre OOP. <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Usa un algoritmo OOP. (Libre Bluetooth/NFC/LibreAlarm)
:::

##### OOP2 {#oop2}

OOP2 è indispensabile per gestire i dati dei sensori Libre 14 days US e Libre 2/2+ EU.

::: xdripitem Calibrazione dell'algoritmo OOP2.
&ensp;Apply xDrip calibration method on OOP2 data
:::

Puoi usare OOP2 in modi diversi:

- No calibration genera valori simili a quelli del produttore (modalità nativa) senza bisogno di calibrare. Non significa che i risultati non siano calibrati (grezzi): viene applicato un algoritmo simile a quello del produttore (come il lettore Libre 1).
- Calibrate based on raw usa i dati grezzi del sensore (senza correzione della temperatura), come per il Libre 1. Userai l'algoritmo di calibrazione di xDrip. **Impostazione predefinita.**
- Calibrate based on glucose ti permette di applicare la calibrazione di xDrip ai valori nativi. I dati grezzi vengono trasformati con l'algoritmo simile a quello del produttore e poi passati all'algoritmo di calibrazione di xDrip.

::: xdripitem Calibrazione dell'algoritmo OOP2.
&emsp;No calibration&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;○  
&emsp;Calibrate based on raw&emsp;&emsp;&emsp;●  
&emsp;Calibrate based on glucose&nbsp;&emsp;○
:::

Liscia dati Libre fa la media su 5 misure. Questo ritarda anche le letture.  
Se questa opzione non porta il miglioramento atteso, prova anche [Liscia il rumore del sensore](./display#smooth-sensor-noise).

::: xdripitem Liscia dati Libre. <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Usa una media di 5 punti per ottenere risultati Libre meno rumorosi.
:::

Recupera cronologia Libre è necessario per i bridge BluCon. Gli altri bridge recuperano i dati mancanti automaticamente.

::: xdripitem Recupera cronologia Libre <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Recupera la cronologia dal dispositivo Blukon quando si ricollega al sensore.
:::

La visualizzazione Libre a un minuto è ancora in sviluppo. xDrip mostra i valori glicemici ogni 5 minuti. Con la sorgente dati [Li3](../install/li3), quando è attivata, le letture vengono salvate ogni minuto.

::: xdripitem Libre 1-minuto <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

##### Li3 {#li3}

Le impostazioni Li3 (Account ID, Official app, Smooth Li3 readings) sono spiegate nella pagina [Li3](../install/li3#li3-settings).

##### 1-min Inter-app broadcast {#1-min-inter-app-broadcast}

::: xdripitem 1-min Inter-app broadcast <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Accept data at one-minute intervals from Inter-app broadcast. Reboot your phone for changes to take effect.
:::

Accetta letture ogni minuto invece che ogni 5 minuti dalla sorgente dati [Inter-app broadcast](../install/640_670). Riavvia il telefono dopo averla modificata. Dal [9 settembre 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.09.09) non richiede più la Modalità Sviluppatore (prima si chiamava "640G/Eversense 1-minute").

L'opzione qui sotto è sempre disattivata (in grigio) nell'app: non può essere attivata.

::: xdripitem SOLO SIMULAZIONE - NON USARE IN PRODUZIONE <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

<br>

[*Ultima modifica 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
