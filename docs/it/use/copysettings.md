---
source_hash: 68f7c3719c
source_commit: 7a18e7c
---
xDrip offre un modo semplice per copiare le impostazioni da un telefono all'altro.

### Mostra impostazioni dei codici QR {#show-settings-qr-code}

Mostra impostazioni dei codici QR visualizza un codice QR che contiene le impostazioni di xDrip.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_qrcode_grey600_48dp.png" style="width:5%;" />&ensp;Mostra impostazioni dei codici QR
:::

::: xdrip Condividi impostazioni tramite il codice QR
&ensp;Utilizzare i codici QR per trasferire le impostazioni utilizzando Impostazioni-&gt; Configurazione automatica caratteristica
:::

La chiave di sicurezza di xDrip è usata per xDrip Sync: se vuoi condividere solo un codice follower (difficile da copiare a mano), usa questa opzione.

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;SOLO IMPOSTAZIONI USANDO XDRIP PLUS SECURITY KEY&emsp;</div>
:::

Se hai usato codici QR di personalizzazione per xDrip su questo telefono (G7, 1+, BlueJay, ...), puoi trasferirli direttamente su un altro telefono.

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;EXPORT KEKS KEY TO ANOTHER PHONE&emsp;</div>
:::

Le impostazioni generali e di raccolta comprendono le impostazioni generali e quelle della sorgente dati hardware.

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;VISUALIZZA IMPOSTAZIONI TRASFERIMENTO DATI E IMPOSTAZIONI GENERALI&emsp;</div>
:::

Tutte le impostazioni comprendono tutto (tranne gli allarmi: devi ricrearli a mano).

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;COPIARE TUTTE LE IMPOSTAZIONI&emsp;</div>
:::

Otterrai un codice QR da scansionare con Configurazione automatica su un altro telefono.

<img src="./images/M-S-QRe.png" style="zoom:75%;" />

### Configurazione automatica {#auto-configure}

Configurazione automatica ti permette di importare le impostazioni da un codice QR.

Assicurati che il codice QR che stai per scansionare provenga da una fonte sicura.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_qrscan.png" style="width:5%;" />&ensp;Configurazione automatica
:::

#### Camera {#camera}

::: xdripitem Camera
&ensp;Scansiona un codice QR con il tuo cellulare (consigliato)
:::

Devi autorizzare xDrip ad accedere alla fotocamera del telefono.

Puoi poi scansionare il codice QR mostrato su un altro telefono per copiare le impostazioni che hai selezionato quando l'hai visualizzato, come spiegato [sopra](#show-settings-qr-code).

<img src="./images/M-S-ACS.png" style="zoom:75%;" />

Le impostazioni attuali verranno sovrascritte: verrà mostrato un elenco da confermare.

::: xdripitem Sei sicuro?
&ensp;Importa solo le impostazioni da fonti affidabili!  
&ensp;Conferma di volere importare le impostazioni seguenti:  


&emsp;impostazione1  
&emsp;impostazione2  
&emsp;impostazione3  

&emsp;No &emsp;&emsp;&emsp;&emsp;Si
:::

Un codice QR *Copiare tutte le Impostazioni* non contiene le impostazioni stesse: xDrip le scarica dopo la tua conferma. Dalla release 2026.11.21 ti viene chiesto prima di confermare.

::: xdripitem Sei sicuro?
&ensp;Only import settings from sources you trust!  
&ensp;Please confirm to download and import all settings from this code.
:::

Potrebbe essere necessario riavviare il telefono per applicare le modifiche.

#### File immagine {#image-file}

Se il tuo telefono ha una fotocamera di scarsa qualità o non ne ha affatto, puoi caricare il codice QR da un file.

Prima devi salvare tra le tue immagini l'immagine del codice QR da scansionare.

::: xdripitem File immagine
&ensp;Puoi salvare un codice QR come un file immagine (come .png o .jpeg) sul tuo cellulare. Quindi, utilizzare questa opzione per scansionare il codice QR dal file salvato.
:::

Seleziona l'immagine che contiene il codice QR.

<img src="./images/M-S-SY3.png" style="zoom:75%;" />

Le impostazioni attuali verranno sovrascritte: verrà mostrato un elenco da confermare.

::: xdripitem Sei sicuro?
&ensp;Importa solo le impostazioni da fonti affidabili!  
&ensp;Conferma di volere importare le impostazioni seguenti:  

&emsp;impostazione1  
&emsp;impostazione2  
&emsp;impostazione3  

&emsp;No&emsp;&emsp;&emsp;&emsp;&emsp;Si  
:::

Potrebbe essere necessario riavviare il telefono per applicare le modifiche.

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
