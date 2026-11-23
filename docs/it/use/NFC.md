---
source_hash: 256676a54d
source_commit: 7a18e7c
---
Questo menu compare solo se è selezionata una [sorgente dati hardware Libre](../install/datasource#libre).

Se il tuo telefono ha un **chip NFC compatibile ISO 15693**, puoi usare la funzione NFC di xDrip con Libre 1/14 giorni/Pro e 2/2+ (EU).

Ricordati di attivare prima la funzione NFC nelle impostazioni di Android.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_nfc_grey600_48dp.png" style="width:5%;" />&ensp;Funzionalità Scansione NFC
:::

::: xdripitem Usa funzionalità NFC <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Consenti la scansione dei sensori quando l'app è aperta. I dati storici saranno ripristinati.
:::

Puoi mostrare l'età del sensore in fondo al grafico principale (xDrip master).

::: xdripitem Età del sensore o scadenza <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Mostra l'età del sensore nella schermata principale
:::

Per aprire automaticamente xDrip quando viene rilevato un sensore NFC dovresti **attivare** Scansiona quando non in xDrip+ (consigliato). Se più app possono scansionare dispositivi NFC, a ogni scansione ti verrà chiesto quale usare.

::: xdripitem Scansiona quando non in xDrip+ <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;La scansione NFC funzionerà anche dalla schermata di home di Android
:::

Puoi decidere come xDrip ti segnalerà che la scansione è terminata. Vibrazione e suono sono utili durante le scansioni NFC (lunghe): dovresti **attivarli** entrambi.

Durante la scansione ricorda che devi tenere il telefono sul punto dell'antenna NFC per qualche secondo per permettere una scansione corretta. Consulta la documentazione del produttore del telefono per sapere dove si trova.

::: xdripitem Vibra per indicare lo stato della scansione <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

::: xdripitem Bippa quando scansioni nell'app xDrip+ <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>

Visibile solo con la Modalità Sviluppatore attivata.
:::

La scansione più veloce è **attivata** per impostazione predefinita. Se hai problemi a scansionare i sensori, prova a disattivarla.

::: xdripitem Usa il metodo più veloce di lettura multi-blocco <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

Se hai problemi con l'NFC del telefono, prova ad **attivare** il metodo any-tag.

::: xdripitem Usa il metodo di lettura ottimizzato any-tag <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

## Avvio della connessione bluetooth con i sensori Libre2 {#starting-bluetooth-connection-with-libre2-sensors}

Questa funzione permette a xDrip di prendere il controllo della connessione Bluetooth del sensore. Sulla maggior parte dei telefoni non è compatibile con l'app del produttore (una sola app può connettersi allo stesso sensore). Alcuni utenti riferiscono di poter connettere contemporaneamente l'app del produttore e xDrip, ma non è garantito: disinstalla l'app del produttore se vuoi che xDrip sia connesso al sensore.

::: xdripitem Avvio della connessione bluetooth con i sensori Libre2
&ensp;Connettersi ai sensori Libre 2 dopo la scansione. Questo impedirà al lettore Libre e a Libre link di ricevere gli allarmi,
:::

Questa scelta comparirà quando scansioni un nuovo sensore Libre 2 solo se hai selezionato Ask me every time (chiedimelo ogni volta).

Tieni presente che Connettersi sempre ai sensori Libre 2 molto probabilmente disconnetterà qualsiasi altra app o dispositivo connesso al sensore. Se xDrip si associa correttamente, non sarà più possibile recuperare la connessione dall'altro dispositivo/app.

::: xdripitem Avvio della connessione bluetooth con i sensori Libre2
&emsp;Connettersi sempre ai sensori Libre 2<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;Ask me every time<span style="float: right;">●&emsp;</span>  
&emsp;Non connettersi mai ai sensori Libre 2<span style="float: right;">○&emsp;</span>  
:::

## Liscia i dati libre 3 quando si usa il metodo xxx {#smooth-libre-3-data-when-using-xxx-method}

::: info Nota
Lo smoothing si applica a qualsiasi app sorgente dati esterna che usa la sorgente dati `Libre2 (patched app)`.
:::

L'implementazione originale includeva un algoritmo di smoothing di 25 minuti per eliminare il rumore e rendere più sicuro il loop chiuso fai-da-te con i sensori Libre. Puoi cambiare il periodo di smoothing in 10, 15 o 25 minuti.

::: xdripitem Liscia i dati libre 3 quando si usa il metodo xxx
&ensp;Numero di minuti da prendere in considerazione quando si usano i dati librex
:::

Lo smoothing aggiunge un ritardo alla glicemia di xDrip rispetto ai dati grezzi. Il ritardo è circa la metà del periodo di smoothing. Per la tua sicurezza, imposta il ritardo in base al comportamento del sensore. Se non usi un sistema di loop chiuso fai-da-te a cui xDrip fornisce i valori glicemici, impostalo su 10 minuti.

::: xdripitem Liscia i dati libre 3 quando si usa il metodo xxx
&emsp;10 minuti<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;15 minuti<span style="float: right;">○&emsp;</span>  
&emsp;25 minuti ><span style="float: right;">●&emsp;</span>  
:::

<br>

[*Ultima modifica 15/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
