---
source_hash: 03b49989fb
source_commit: e9ebf28
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;Libre Bluetooth
:::

### Libre 2 Direct {#libre-2-direct}

Questa pagina descrive come attivare la connessione Bluetooth diretta tra il sensore e xDrip, senza bisogno di un bridge.

#### Prerequisiti {#prerequisites}

Il telefono su cui hai installato xDrip ha un lettore NFC.

Se l'app del produttore è installata sullo stesso telefono che usi per xDrip, **l'hai disinstallata**.  
Se è installata su un altro telefono o usi il lettore Bluetooth, hai allontanato questi dispositivi, o li hai schermati, in modo che non interferiscano.

#### Prima configurazione {#setting-up-for-the-first-time}

(Clicca [Inizializza Sensore](#starting-libre-2-sensors) per i sensori successivi).

::: info Sono supportati solo i modelli di sensore Libre 2/2+ europei
Devi installare l'[ultima versione dell'app OOP2](../use/OOP#oop2).
:::


La documentazione di riferimento di Libre 2 si trova [qui](https://www.minimallooper.com/post/how-to-setup-freestyle-libre-2-and-oop2-to-use-a-native-bluetooth-connection-in-xdrip), ma non è più aggiornata.

<br>

::: warning Attenzione
**Disinstalla tutte le app collegate al sensore e scherma il lettore prima di provare a collegarlo a xDrip.**  
Se colleghi il sensore direttamente a xDrip perderai definitivamente gli allarmi dell'app del produttore o del lettore, senza possibilità di recuperarli.  
Se non sei sicuro che funzioni, usa un sensore a fine vita per provare il sistema.  
Come per i bridge Libre, il successo e l'affidabilità variano a seconda del telefono.  
Collegare il sensore a xDrip annulla la garanzia del produttore sulla funzione Bluetooth del sensore.
:::

#### Configurare xDrip {#setup-xdrip}

Come scorciatoia, puoi scansionare il codice QR qui sotto per caricare le impostazioni necessarie per Libre 2/2+ diretto con la funzione [Configurazione automatica](../use/copysettings#auto-configure) di xDrip. Se stai consultando la documentazione dal telefono su cui installi xDrip, salva prima le immagini e poi caricale con la funzione "File immagine" della configurazione automatica.

Impostano la **[calibrazione disattivata](../use/misc#oop2), consigliata per il primo utilizzo**. Se invece vuoi la calibrazione, [segui queste istruzioni](./libre2direct-calib). L'elenco completo delle impostazioni importate è [qui](./libre2direct-qr-settings).

Codici QR - Clicca sull'immagine per ingrandirla

Senza calibrazione             |  Con calibrazione
:-------------------------:|:-------------------------:
[<img src="./images/qr_libre2direct-nocalib-30.png" style="zoom:50%;" />](./libre2direct-qr-settings) | [<img src="./images/qr_libre2direct-calib-30.png" style="zoom:50%;" />](./libre2direct-calib)

Se hai usato i codici QR, puoi passare direttamente ad [Avviare i sensori Libre 2](#starting-libre-2-sensors)

#### Configurare l'NFC {#configure-nfc}

Configura l'NFC esattamente [come qui](../use/NFC).

#### Avviare i sensori Libre 2 {#starting-libre-2-sensors}

Applica fisicamente il sensore Libre 2/2+ e avvialo con il lettore oppure con LibreLink. Annota l'ora in cui il sensore sarà pronto. Se usi lo stesso telefono di xDrip, disattiva LibreLink sul telefono. Scansionandolo dovresti vedere i valori di glicemia. Ora attendi 60 minuti, finché il sensore ha terminato il riscaldamento e si è autocalibrato.

#### Collegarsi al sensore {#connect-to-the-sensor}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Stop Sensore  
:::

Se a xDrip è collegato un sensore precedente, ferma il vecchio sensore.

Scansiona il sensore con l'NFC di xDrip e verifica di vedere i messaggi "Scansione in corso.." e poi "Scansionato OK!".

::: info Nota
Tieni il telefono fermo durante la scansione del sensore e non muoverlo: ci vuole più tempo rispetto alla lettura che fai di solito con l'app del produttore.  
Ricorda che devi attendere un minuto tra due scansioni NFC consecutive.
:::

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Inizializza Sensore  
:::

Avvia il sensore in xDrip. Quando ti viene chiesto di inserire l'ora in cui hai avviato fisicamente il sensore, non indicare un'ora precedente a quella reale, per evitare valori incoerenti.

Attendi 60 secondi e scansiona di nuovo con xDrip. In questo modo il sensore viene aggiunto come dispositivo BT da cui xDrip riceverà le letture. Dovresti vedere la notifica NUOVO SENSOR AVVIATO. Se hai impostato "Nessuna calibrazione", dovresti vedere subito la prima lettura. Se hai impostato la calibrazione, dovresti trovarti nella schermata "Sto raccogliendo le prime letture".
Ora dovrai attendere tra 3 e 15 minuti per ricevere 3 letture, poi verrà mostrata la richiesta **Calibrare il sensore?**, a meno che tu non abbia selezionato "Nessuna calibrazione" nelle [impostazioni OOP2](../use/misc#oop2).
Dopo aver inserito i dati di calibrazione, il sensore Libre 2/2+ dovrebbe essere associato a xDrip e fornire letture ogni 5 minuti.

Puoi verificare che tutto funzioni confrontando con "Come dovrebbe apparire" [qui](../troubleshoot/libre2direct#what-it-should-look-like)

Se hai difficoltà a ricevere dati direttamente dal sensore, scansionalo ogni 5 minuti con l'NFC di xDrip fino ad arrivare alla richiesta di calibrazione (vale se hai selezionato l'[opzione di calibrazione](../use/misc#oop2) con OOP2).

<br>

#### **Problemi?** {#problems}

Consulta la pagina di [risoluzione problemi](../troubleshoot/libre2direct).

<br>

[*Ultima modifica 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)

