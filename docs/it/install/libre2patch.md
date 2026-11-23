---
source_hash: 711cdaceb9
source_commit: 7a18e7c
---
**Questa è una sorgente dati generica per varie app, non solo per l'app del produttore modificata.**

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;Libre (patched app)
:::

Le app elencate qui sotto usano lo stesso protocollo per inviare i dati a xDrip.

::: info Nota
Le letture delle app esterne sono trattate a tutti gli effetti come dati del sensore; questo comprende i [limiti di calibrazione](../calibrate/calibrate#libre-2-patched-app).
:::

Non dovrebbe più essere necessario, ma se non vedi dati in xDrip, usa [Inizializza Sensore](../use/startsensor#followers-and-companion-apps).

<br>

#### Libre 2 UE [app modificata](../troubleshoot/libre2#patched-app) {#libre-2-eu-patched-app}

::: info App modificata
L'app modificata in sé è disponibile solo per la versione europea di Libre 2.  
Essendo un'app vecchia, è **raramente compatibile con versioni di Android successive alla 12**.
:::

<br>

#### Juggluco {#juggluco}

Se usi [Juggluco](https://www.juggluco.nl/Juggluco/index.html) puoi trasmettere i dati a xDrip attivando Send to xDrip. Per vedere le misurazioni in xDrip, Juggluco deve ricevere i dati in streaming.

<img src="./images/Juggluco.png" style="zoom:50%;" />

<br>

#### Diabox {#diabox}

Se usi una versione recente di [Diabox](https://sirius.thetaphi.de/diabox/), puoi trasmettere i dati a xDrip attivando l'opzione qui sotto:

<img src="./images/Diabox4.png" style="zoom:75%;" />

<br>

#### LinkUpConnect {#linkupconnect}

LinkUpConnect è un follower dei server del produttore: ti serve un Libre 3 per avere dati CGM nell'app.  
I dati devono essere disponibili nell'app follower del produttore.  
Attiva l'opzione `Forward to xDrip`.

<img src="./images/LinkUpConnect.png" style="zoom:75%;" />

<br>

#### Livellamento {#smoothing}

Questa sorgente dati è soggetta a un livellamento predefinito di 25 minuti. Il periodo di livellamento può essere regolato nel [menu NFC](../use/NFC#smooth-libre-3-data-when-using-xxx-method) per ridurre il ritardo generato, se il livello di rumore lo consente.

<br>

[*Ultima modifica 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
