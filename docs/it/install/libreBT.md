---
source_hash: dc2943a1ef
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;Libre Bluetooth
:::

Sul mercato sono disponibili molti bridge da NFC a Bluetooth per i sensori Libre.

Il progetto originale è stato sviluppato da Joern: [LimiTTer](https://github.com/JoernL/LimiTTer). Ricorda questo nome, perché compare come nome predefinito del bridge quando il dispositivo effettivo non viene identificato. A meno che tu non abbia davvero un LimiTTer (o non colleghi direttamente un Libre 2), vedere questo nome significa che il tuo bridge non è collegato a xDrip.

xDrip ne supporta alcuni, per alcuni sensori.  
**Libre H e Libre 2/2+ USA/CA/AUS non sono supportati.**  
Puoi usare Diabox o Juggluco in modalità [Libre patched app](./libre2patch).

Qui sotto trovi una tabella di compatibilità dei bridge supportati; per i sensori compatibili è indicata la versione **minima** del firmware.

|   Bridge    | - Libre 1 / Pro - | - 14 giorni USA - | - Libre 2/2+ UE - |
| :---------: | :---------------: | :------------: | :---------------: |
|  MiaoMiao   |       `Sì`       |     `39*`      |       `39*`       |
| MiaoMiao 2  |       `Sì`       |      `7*`      |       `7*`        |
| MiaoMiao 3  |       `Sì`       |     `3A*`      |       `3A*`       |
|    Atom     |       `Sì`       |                |                   |

*Nota:*  
*`*` [richiede l'add-on esterno OOP](../use/OOP)*

<br>

## Impostazioni del bridge {#bridge-settings}

Se non l'hai ancora fatto, [verifica che xDrip non venga messo in sospensione](./install#make-sure-xdrip-will-not-be-put-to-sleep).

Prima di provare a collegare il bridge, verifica che le impostazioni siano corrette, per evitare disconnessioni frequenti.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Impostazioni Meno Usate  
&ensp;&emsp;Impostazioni Bluetooth  
:::

Per iniziare, usa le impostazioni indicate qui sotto.

Il Bluetooth deve essere acceso. **Attiva** `Attiva Bluetooth`.

::: xdripitem Attiva Bluetooth <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Attiva automaticamente il bluetooth se è spento quando si prova a connettersi a un dispositivo bluetooth
:::

**Attiva** il Watchdog, ma leggi le informazioni qui sotto.

::: xdripitem Watchdog Bluetooth <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Resetta Bluetooth (spegni e riaccendi) se non si ricevono dati in 20 minuti
:::

::: info Informazioni
Tieni presente che Watchdog Bluetooth spegne e riaccende il Bluetooth del telefono: questo provoca una disconnessione Bluetooth temporanea di tutti i dispositivi collegati. Potresti voler disattivare questa funzione se usi AAPS e il tuo bridge/microinfusore non recupera automaticamente la connessione Bluetooth.
:::

**Disattiva** la chiusura GATT.

::: xdripitem Chiusura GATT per scollegamento BLE <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Se il watchdog bluetooth si attiva spesso, provare a deselezionare questa opzione per vedere se aiuta
:::

Se il bridge perde la connessione e una scansione Bluetooth ti permette di recuperarla, puoi provare ad attivare `Usa scansione`. Per iniziare lasciala **disattivata**.

::: xdripitem Usa scansione <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Scansiona prima di connettersi a xBridge e Libre Bluetooth
:::

Sui telefoni Samsung e su molti telefoni cinesi **devi disattivare `Trust Auto-Connect`**! Se il telefono perde la connessione, **disattivala**.

::: xdripitem Trust Auto-Connect <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Usa e confida nella funzione di connessione automatica bluetooth di Android (sconsigliato per miaomiao)
:::

Con Android 8 e successivi puoi attivare `Usa Scansione In Background`. Se perdi la connessione, **lasciala disattivata**.

::: xdripitem Usa Scansione In Background <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Utilizza la funzione di scansione bluetooth in background Android 8+
:::

Lascia **disattivate** entrambe le opzioni qui sotto.

::: xdripitem Bluetooth Wakelocks <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Vecchi wakelocks bluetooth (possono necessitare più batteria) che potrebbero essere necessari per la ricezione dei bluetooth  
:::

::: xdripitem Resetta costantemente bluetooth <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Resetta Bluetooth spegnendolo e riaccendendolo ogni pochi minuti! Selezionare solo per prove. Potrebbe disturbare qualsiasi altra cosa usando bluetooth.
:::

Se il tuo bridge è un Transmitter_T o un Droplet, attiva questa opzione; altrimenti lasciala **disattivata**.

::: xdripitem Supporto Transmiter (PL) <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Supporto sperimentale per Transmiter_T
:::

Se hai perdite di connessione puoi **attivare** la modalità di polling. Non farà nulla di utile, se non tenere sveglio il Bluetooth del telefono.

::: xdripitem xBridge+ Modalità di Polling <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Supporto sperimentale per la funzione di polling xBridge+
:::

Se il tuo bridge è un vecchio BluCon compatibile puoi attivare questa opzione; se ricevi più richieste di abbinamento al giorno, lasciala **disattivata**.   
*Nota: solo il BluCon si abbina ad Android, gli altri bridge no.*

::: xdripitem Consenti unbonding Blucon <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Adatto solo per telefoni che supportano l'accoppiamento automatico 
:::

<br>

Riavvia il telefono per assicurarti che tutti i parametri vengano presi in considerazione.

<br>

## Collegare il bridge Bluetooth {#connect-bluetooth-bridge}

Assicurati che il bridge non sia collegato a nient'altro: nessun altro dispositivo e nessun'altra app.  
Avvia la scansione Bluetooth.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Scansione Bluetooth  
:::

Se la scansione non parte da sola, seleziona `SCANSIONE`.

<img src="../images/M-BTscan.png" style="zoom:75%;" />

Se il bridge non compare, assicurati che sia completamente carico (o che abbia una batteria nuova) e resettalo.

Quando è visibile, selezionalo.

Se il tuo bridge è un Blucon, inserisci il codice scritto sul lato. 

<img src="./images/M-BT-BK.png" style="zoom:55%;" />

Posizionalo correttamente sul sensore. Alcuni bridge hanno una tolleranza molto ridotta riguardo all'angolo e alla distanza dal sensore.

::: info Add-on esterno
Se il tuo sensore richiede un [algoritmo OOP (out of process algorithm)](../use/OOP), assicurati di installarlo adesso.
:::

<br>

Prosegui con [Inizializza Sensore](../use/startsensor#libre)

## Fermare il sensore Libre {#stop-libre-sensor}

xDrip non può fermare fisicamente un sensore Libre: si fermerà da solo dopo 14 giorni e 12 ore e continuerà a mostrare l'ultimo valore.

Tuttavia, quando cambi sensore è fortemente consigliato informare xDrip del cambio fermando il sensore.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Stop Sensore  
:::

Conferma che vuoi davvero fermare il sensore.

::: xdripitem <img src="../images/BDM.png" style="zoom:75%;" /> Arresto Sensore <span class='symbol'></span>
  &emsp;Ferma il tuo sensore solo quando pensi di rimuoverlo, altrimenti lascialo avviato!  


&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;STOP SENSORE&ensp;</span>
:::

Questo azzererà tutte le calibrazioni e permetterà a xDrip di avviare un nuovo sensore.

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
