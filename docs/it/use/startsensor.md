---
source_hash: ec23b1baed
source_commit: ea9ce3a
---
Avviare un sensore in xDrip ha funzioni molto diverse a seconda del sensore.

### G6 e 1 {#g6-and-1}

La documentazione di riferimento si trova [qui](https://navid200.github.io/xDrip/docs/Proper-connectivity.html).

### G7 e 1+ {#g7-and-1}

Il sensore si avvia automaticamente nel momento in cui viene inserito. Non devi avviarlo in xDrip.

<br>

### Libre {#libre}

Nota: questa sezione NON vale per Libre 2/2+ (UE) collegato a xDrip senza bridge. In quel caso, consulta le istruzioni di [Libre 2 Direct](../install/libre2#starting-libre-2-sensors)

xDrip non è in grado di avviare un sensore Libre, né di fermarlo (in realtà questo sensore non si può fermare: se non si guasta, funziona per tutta la sua durata e si ferma da solo dopo 14 giorni e 12 ore; i sensori Libre 3 durano 15 giorni).

Per avviare il sensore devi usare il lettore o l'app del produttore; anche alcune app di terze parti come Glimp-S ed eDropletNFC possono avviare il sensore Libre 1. Juggluco può avviare i sensori Libre 2 e 3.

L'avvio del sensore in xDrip serve solo a tenere traccia della sua durata e a garantire che le calibrazioni siano aggiornate. Questa operazione è necessaria e consigliata ogni volta che sostituisci il sensore.

<br>

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&emsp;Inizializza Sensore 
:::

Conferma INIZIALIZZA SENSORE

::: xdrip <img src="../images/BDM.png" style="zoom:75%;" />Inizializza Nuovo Sensore
Non premere avviare sensore prima che il sensore sia inserito e il trasmettitore connesso.  

&emsp;&emsp;&emsp;&emsp;<span style="background-color: grey; color: white; align: center;">  &ensp;INIZIALIZZA SENSORE&ensp;</span>
:::

Se hai inserito il sensore oggi (cioè non avviato o avviato da poco), rispondi SI, OGGI

::: xdripitem L'hai inserito oggi?
Abbiamo bisogno di sapere quando il sensore è stato inserito per migliorare l'accuratezza del calcolo.  

<span style="color: cyan; float: right;">NON OGGI&emsp;&emsp;SI, OGGI&emsp;</span>
:::

Se hai risposto oggi, seleziona l'ora in cui hai avviato fisicamente il sensore trascinando l'indicatore blu sull'ora corretta. Con la visualizzazione a 12 ore, tocca `am` o`pm`. Con la visualizzazione a 24 ore, rilascia l'ora corretta sull'anello interno o esterno. Tocca OK.

<img src="../install/images/M-StaSHour.png" style="zoom:75%;" />

Trascina l'indicatore blu dei minuti sul valore corretto e tocca `OK`.

<img src="../install/images/M-StaSMin.png" style="zoom:75%;" />

Il sensore appena avviato continuerà il riscaldamento se è stato avviato da meno di un'ora.

::: warning Attenzione
**Anche se xDrip proverà a leggere un sensore durante la fase di riscaldamento, i valori possono essere da inaffidabili a incoerenti e non vanno usati.**
:::

<img src="../install/images/LibreWarmup.png" style="zoom:70%;" />

Se usi [OOP1](./OOP#oop1) o [OOP2](./OOP#oop2) senza calibrazione, la glicemia verrà mostrata subito, senza bisogno della calibrazione iniziale.

Se usi un sensore già avviato, riceverai una richiesta di calibrazione entro 15 minuti.

Se vedi una freccia viola, potresti aver sbagliato la data e l'ora di avvio del sensore: i dati di glicemia sono disponibili ma non vengono mostrati durante il riscaldamento di 1 ora.

<img src="../install/images/PurpleArrow.png" style="zoom:70%;" />

<br>

Ora xDrip attenderà le letture e aggiornerà l'avanzamento. Resta su questa schermata. Le letture arrivano a 5 minuti l'una dall'altra, quindi dovrebbero bastare meno di 20 minuti.

::: xdripitem Sto raccogliendo le prime letture
&ensp;✔ Raccolta dati in esecuzione  
&ensp;⧖  Ricezione dati dal collector MiaoMiao  
&emsp;&nbsp;Ho ricevuto alcuni dati recenti  
&emsp;&nbsp;Ho ricevuto abbastanza dati per calibrare  
&ensp;***No data received yet***  
:::
Se come sorgente dati compare LimiTTer e non stai usando un vero [LimiTTer](https://github.com/JoernL/LimiTTer), il tuo bridge non è collegato correttamente.

<img src="../install/images/M-SS-LimiTTer.png" style="zoom:70%;" />

L'indicazione ***No data received yet*** diventerà ***Need 3 recent readings***. Se non arriva nessun dato, [controlla i parametri](../install/libreBT#bridge-settings).

::: xdripitem Sto raccogliendo le prime letture
&ensp;✔ Raccolta dati in esecuzione  
&ensp;✔ Ricezione dati dal collector MiaoMiao  
&ensp;✔ Ho ricevuto alcuni dati recenti  
&ensp;⧖ Ho ricevuto abbastanza dati per calibrare  
&ensp;***Need 3 recent readings, got only 1 so far***  
&ensp;Next reading expected in 1 minute 
:::

Quando sono state ricevute abbastanza letture, compare la richiesta di calibrazione. Per saperne di più sulla calibrazione, vedi [qui](../calibrate/101).

Se la tua glicemia è nell'intervallo normale (per un sensore nuovo è consigliata la parte bassa dell'intervallo normale) ed è stabile da almeno 10 minuti, senza carboidrati né insulina attivi, puoi calibrare.

Se la tua glicemia varia rapidamente o non è nell'intervallo normale, non è consigliato calibrare adesso. 

::: xdrip Calibrare il sensore?
Abbiamo alcune letture!  
Ci servirà il valore della prima misura capillare.  
Pronto per calibrare ora?
:::

Per la prima calibrazione possono essere richieste due letture; puoi usarne una sola se sei sicuro che sia valida. Inserisci semplicemente due volte lo stesso valore. Puoi impostare un solo valore come predefinito [disattivando la doppia calibrazione](../calibrate/advancedcal#calibrations).

La glicemia dovrebbe comparire nel grafico principale.

<br>

### Follower e app compagno {#followers-and-companion-apps}

A volte è necessario "avviare" una sessione del sensore in xDrip per ricevere le letture.

Avviare o fermare un sensore in xDrip, quando si usa una sorgente follower o un'app compagno, non ha alcun effetto sul sensore.

::: warning Attenzione
L'unica eccezione è il [follower xDrip Sync, che può trasmettere il comando di avvio o arresto al sensore vero e proprio se questo è collegato direttamente allo xDrip che fa da master](./sync#accept-followers-actions).  
Non usare Avvia e Ferma sensore con un follower xDrip Sync, a meno che tu non sia certo che la persona con il telefono xDrip master sappia cosa fare con un sensore fermato!
:::

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&emsp;Inizializza Sensore 
:::

Conferma INIZIALIZZA SENSORE

::: xdrip <img src="../images/BDM.png" style="zoom:75%;" />Inizializza Nuovo Sensore
Non premere avviare sensore prima che il sensore sia inserito e il trasmettitore connesso.  

&emsp;&emsp;&emsp;&emsp;<span style="background-color: grey; color: white; align: center;">  &ensp;INIZIALIZZA SENSORE&ensp;</span>
:::

Rispondi NON OGGI

::: xdripitem L'hai inserito oggi?
Abbiamo bisogno di sapere quando il sensore è stato inserito per migliorare l'accuratezza del calcolo.  

<span style="color: cyan; float: right;">NON OGGI&emsp;&emsp;SI, OGGI&emsp;</span>
:::

xDrip dovrebbe ricevere le letture con la misurazione successiva.

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)