---
source_hash: 6cdbd15c0c
source_commit: 7a18e7c
---
::: info Libre 2 UE
xDrip supporta solo la versione europea di Libre 2.  
Se vuoi usare un Libre 2 di un'altra area geografica, puoi far inviare i dati a xDrip da [un'altra app](../install/libre2patch).
:::

<br>

## App patchata {#patched-app}

In Europa puoi creare la tua app patchata in conformità con la direttiva 2009/24/CE art. 6 (l'applicazione può variare da paese a paese). La Germania ha un'eccezione nel capitolo 6 dell'EULA dell'app del produttore.  
La distribuzione dell'app patchata non è autorizzata.

Trovi le spiegazioni su come generare l'app cercando `xDrip-Patch` su [GitHub](https://github.com/search).

Il sensore attuale deve essere avviato con l'app patchata perché l'app possa collegarsi.  
Il Bluetooth del telefono deve essere attivato e i prerequisiti dell'app soddisfatti **prima** di avviare il sensore. Se hai avviato un sensore senza i prerequisiti corretti, potresti non riuscire ad attivare gli allarmi e quindi a ricevere dati.

xDrip riceverà automaticamente i dati dall'app patchata usando la sorgente dati hardware specifica [Libre2 (patched App)](../install/libre2patch).

#### Verificare la connessione {#check-connection}

L'app patchata deve essere collegata al sensore perché xDrip possa riceverne i dati. Di solito, quando non lo è, vedi un punto esclamativo in alto a sinistra.

<img src="./images/LLnotconnected.png" style="zoom:75%;" />

Se il sistema funzionava correttamente e questo è successo all'improvviso, prova a riavviare il telefono, a metterlo in modalità aereo, a spegnere e riaccendere il Bluetooth per vedere se la connessione si ripristina.

Scansionare il sensore può essere una buona idea. Se il sensore non fornisce dati dopo la scansione, potrebbe essere difettoso.

Aprire il menu può darti informazioni sui prerequisiti mancanti perché l'app si colleghi al sensore.

#### Prerequisiti per la connessione {#prerequisites-to-connection}

- Il servizio di localizzazione di Android deve essere consentito, **Sempre**. Consenti sempre l'app patchata (esempio qui sotto per xDrip)  
  <img src="../install/images/Install17.png" style="zoom:80%;" />
- Il telefono deve essere impostato su [data, ora e fuso orario automatici](../install/prerequisites#phone-time-accuracy)
- Almeno uno dei tre allarmi **deve essere attivato** nell'app patchata
- Il Bluetooth deve essere **acceso**
- Sveglie e promemoria (suoni) devono essere **autorizzati** (Impostazioni Android - App)
- Le notifiche devono essere **autorizzate** (Impostazioni Android - App)
- Le notifiche sulla schermata di blocco devono essere **autorizzate** (Impostazioni Android - App)

<br>

## Connessione diretta {#direct-connection}

Quando provi per la prima volta a collegare xDrip direttamente a un sensore Libre 2 e non sei sicuro di riuscire a far funzionare il sistema, è vivamente consigliato farlo l'ultimo giorno del sensore attuale.  
xDrip non rompe il sensore, impedisce solo all'app del produttore o al lettore di ricevere gli allarmi; se fai affidamento su questi, potresti ritrovarti con un sensore che si comporta come un Libre 1.

Trovi altre informazioni su Libre 2 direct [qui](./libre2direct)

#### Prerequisiti {#prerequisites}

Il dispositivo con cui hai avviato il sensore deve essere schermato (forno a microonde, spento) per evitare che interferisca con il processo di associazione di xDrip. Mostrerà l'icona di connessione persa.

<img src="./images/FLnotconnected.png" style="zoom:75%;" />

Se hai installato xDrip sullo stesso telefono con cui hai avviato e scansionato il sensore, si consiglia di disinstallare l'app del produttore, perché ti impedirà di collegarti al Bluetooth del sensore e interferirà con le scansioni NFC. Puoi reinstallare l'app quando xDrip è collegato al sensore; ovviamente non avrà più gli allarmi del sensore.

Se non vuoi rimuovere l'app del produttore, devi disattivarne l'autorizzazione alla posizione nelle impostazioni di Android.  
**xDrip deve essere autorizzato, sempre.  
L'app del produttore NON deve essere autorizzata, mai.**

Nota che se tieni l'app del produttore sul telefono, ogni volta che scansioni il sensore con NFC dovrai scegliere tra questa e xDrip. Questo può generare errori di lettura in xDrip.

#### Errori di scansione del sensore {#sensor-scan-errors}

Assicurati di aver [configurato](../install/libreNFC#configure-nfc) correttamente l'NFC di xDrip.  
Con xDrip la scansione richiede più tempo. Una volta trovata la posizione corretta dell'antenna NFC del telefono, mettiti nel punto giusto e resta fermo.  
Non puoi fare una scansione prima che siano passati 30 secondi dalla precedente.

#### Impossibile collegarsi al sensore {#cannot-connect-to-the-sensor}

Verifica che [OOP2](../use/OOP#oop2) sia installato, attiva [nessuna calibrazione](../use/misc#oop2), [ferma il sensore](../use/stopsensor#libre) e ricomincia da [qui](../install/libre2#connect-to-the-sensor).

Scansiona ripetutamente ogni 2 minuti per 10 minuti, poi lascia stare il sistema per 20 minuti.

Dopo scansioni ripetute dovresti vedere dei valori in xDrip.  
Dovresti vedere dei valori anche nell'app OOP2.

<img src="./images/OOP2values.png" style="zoom:74%;" />

Se non vedi valori dopo la scansione:

- Verifica di **NON** aver attivato [OOP1](../use/misc#out-of-process-algorithm) per errore
- Assicurati che xDrip abbia l'[accesso alla posizione autorizzato](../install/install#enable-location), **sempre**
- Riavvia il telefono e riprova

<br>

Se necessario, consulta la pagina di [risoluzione problemi](./librebridge).

<br>

[*Ultima modifica 18/06/2023*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2023.06.15)
