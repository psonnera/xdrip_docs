---
source_hash: 498f98f131
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_watch_grey600_48dp.png" style="width:5%;" />&ensp;Caratteristiche Collegamenti Smart Watch  
&emsp;  BlueJay Watch
:::

Puoi acquistare il tuo orologio BlueJay [qui: <img src="./images/M-S-SW-BJ1.png" style="zoom:100%;" />](https://bluejay.website/) 

Il [BlueJay U3](https://bluejay.website/shop) è il modello attuale ed è già disponibile. Esegue il pacchetto xDrip completo su Android e si collega direttamente ai sensori G6, G7 e Dexcom ONE/ONE+.

I modelli precedenti X2, GTS, U1 e U2 **non sono più in vendita**. Le loro istruzioni di configurazione restano qui sotto per chi li possiede già.  
Riferimenti dei modelli precedenti: [GTS](https://bluejay.website/shop/product/bluejay-gts-26) (autonomo o con xDrip), [U1](https://bluejay.website/shop/product/bluejay-u1-27) e [U2](https://bluejay.website/shop/product/bluejay-u2-28).

::: info Condivisione della glicemia
I BlueJay X2/GTS sono solo Bluetooth e non possono condividere i dati della glicemia se non sono collegati a xDrip sul telefono.  
Gli U1/U2/U3 eseguono xDrip completo e possono anche ritrasmettere le letture a un telefono o ad altri follower tramite Bluetooth (xDrip Link) o internet (xDrip Sync).
:::

Gli orologi BlueJay sono compagni potenti per i sensori G6, G7 e 1/1+. Si collegano direttamente al trasmettitore, ma devi conoscerne i limiti.

##### G6/G7 e 1/1+ {#g6g7-and-11}

Questi trasmettitori hanno due slot Bluetooth: phone (telefono) e non-phone (non telefono).  
Puoi configurare gli slot secondo la tabella qui sotto. Al trasmettitore possono essere collegati contemporaneamente solo due dispositivi, ciascuno su uno slot diverso.  
Per impostazione predefinita BlueJay usa lo slot non-phone. Vedi [qui per il GTS](#run-collector) come modificare questa impostazione.

U1, U2 e U3 devono essere collegati per primi al sensore. Una volta collegati, puoi attivare anche la seconda connessione e l'orologio sceglierà automaticamente lo slot libero.

| App del produttore  | Ricevitore              | Microinfusore collegato                   | Orologio BlueJay                          |
| ------------------- | ----------------------- | ----------------------------------------- | ----------------------------------------- |
| Non utilizzabile    | Non utilizzabile        | Non utilizzabile                          | Slot non-phone **xDrip usa lo slot phone** |
| **Usa lo slot phone** | Non utilizzabile      | Non utilizzabile                          | Slot non-phone                            |
| Non utilizzabile    | **Usa lo slot non-phone** | Non utilizzabile                        | Slot phone                                |
| Non utilizzabile    | Non utilizzabile        | t:slim, Omnipod 5 **usano gli slot non-phone** | Slot phone                           |
| Non utilizzabile    | Non utilizzabile        | CamAPS, DBLG1 **usano lo slot phone**     | Slot non-phone                            |

*Nota: per impostazione predefinita xDrip usa lo slot phone; lo slot non-phone richiede l'Engineering mode*

## BlueJay U3 {#bluejay-u3}

L'U3 esegue Android completo e il core di xDrip direttamente sull'orologio. Lo configuri sull'orologio e, se vuoi, puoi ritrasmettere le letture al telefono.

### Comandi dell'U3 {#u3-controls}

L'U3 ha due pulsanti fisici: un pulsante **sinistro** (arancione) e un pulsante **destro**. Sugli U1/U2 il comando a destra era una corona; sull'U3 in quella posizione c'è la fotocamera.

- Premi uno qualsiasi dei due pulsanti per riattivare lo schermo.  
- Il pulsante **destro** spegne lo schermo.  
- Il pulsante **sinistro** torna indietro.  
- Tieni premuto il pulsante di accensione per il menu Shutdown / Reboot / SOS, poi scorri verso destra l'opzione che vuoi.

### Ricevere le letture sull'U3 {#get-readings-on-the-u3}

Imposta l'identificativo del sensore in xDrip sull'orologio, esattamente come faresti su un telefono: vai in Impostazioni &ensp;›&ensp; Dati Hardware di origine &ensp;›&ensp; DexcomG5/G6/G7.

- **G6**: inserisci l'**ID del trasmettitore (TXID)**.  
- **G7 / Dexcom ONE+**: inserisci il **codice di accoppiamento a 4 cifre**.

Con un sensore nuovo, imposta prima l'ID o il codice sull'orologio e lascia che riceva le letture prima di impostarlo in qualsiasi app del telefono. Con un sensore già in funzione e collegato a un'app del telefono, disattiva temporaneamente l'app del telefono (spegnila, disattiva il Bluetooth o allontanati), collega l'orologio, poi riattiva l'app del telefono quando l'orologio riceve le letture.

### Slot del trasmettitore {#transmitter-slot}

Per impostazione predefinita l'U3 usa lo **slot non-phone**. Consulta la [tabella degli slot qui sopra](#g6g7-and-11) per scegliere lo slot giusto. Per spostare l'orologio sullo **slot phone**, scansiona il codice QR corrispondente in:

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Configurazione automatica
:::

Evita di cambiare ripetutamente il dispositivo su uno slot: il sensore potrebbe bloccarsi. Lo slot è una configurazione fissa, non uno scambio a caldo.

::: warning Aggiornamento canale phone per il G7
Se l'orologio smette di ricevere le letture del **G7**, applica l'aggiornamento software dell'orologio: sull'orologio apri **Impostazioni Android › Software Upgrade**, con il Wi-Fi connesso e in carica (batteria > 25%), cerca gli aggiornamenti e installali.  
Dopo puoi passare l'orologio sul canale phone scansionando il codice QR mostrato in xDrip **Impostazioni › Configurazione automatica**, poi riavvia l'orologio.  
Con questo metodo **l'orologio e un'app del telefono non possono entrambi** ricevere le letture direttamente dal sensore: disattiva il collector dell'app del telefono se il collector è l'orologio.
:::

### Posticipare un allarme di xDrip {#snooze-an-xdrip-alarm}

Tieni premuto il **pulsante sinistro arancione** finché l'orologio non vibra.

### Ritrasmettere le letture al telefono o ai follower {#relay-readings-to-your-phone-or-followers}

Quando l'orologio è il collector, puoi comunque fornire i dati al telefono e ad altri dispositivi:

- **xDrip Link**: orologio ↔ telefono tramite Bluetooth quando sono nel raggio d'azione. Sull'orologio apri l'app **xDrip Link**, attivala e scansiona il suo codice QR in xDrip sul telefono, **Impostazioni › Configurazione automatica**. Le impostazioni BlueJay inserite sul telefono (compresi TXID e codice di accoppiamento) vengono copiate sull'orologio. Se il telefono non deve collegarsi direttamente al sensore, imposta [Run Phone Collector](#run-phone-collector) su **Off** sul telefono.  
- **xDrip Sync**: ritrasmette le letture via internet (Wi-Fi/4G) da un master a uno o più follower, anche da orologio a orologio e da telefono a orologio.

::: info Funzioni dell'orologio non legate a xDrip
L'inserimento della SIM, il Wi-Fi, la fotocamera, i quadranti, i cinturini, le pellicole protettive, l'account Google, le chiamate, il GPS, le chiamate SOS, la musica e l'aggiornamento software dell'orologio sono documentati dal produttore. Vedi le [Top Tips / FAQ](https://bluejay.website/faq) di BlueJay.
:::

## Modelli precedenti: X2 / GTS {#legacy-models-x2-gts}

I passaggi seguenti riguardano i vecchi orologi X2 e GTS, che non sono più in vendita.

### Associare l'orologio a xDrip (X2 e GTS) {#pair-your-watch-to-xdrip-x2-and-gts}

1 - Assicurati che l'orologio sia carico prima di iniziare.

2 - Attiva BlueJay e disattiva il collector dell'orologio.  

::: xdripitem BlueJay Watch <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Run Collector <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

3 - Se hai un BlueJay GTS, passa al punto 6.  
Se hai un BlueJay X2, dovrebbe mostrare un codice QR sullo schermo.  
<img src="./images/M-S-SW-BJc5.png" style="zoom:40%;" />  
Se lo vedi, passa al punto 7.

4 - Avvia BlueJay Panel e fai la scansione.  

::: xdripitem Launch BlueJay Panel
:::
<img src="./images/M-S-SW-BJc1.png" style="zoom:76%;" />  
Quando l'orologio viene rilevato dovresti vedere il suo indirizzo MAC. Selezionalo.  
<img src="./images/M-S-SW-BJc2.png" style="zoom:66%;" /><br>  
Se xDrip non trova l'orologio, prova a riavviare il telefono e riprova. Se ancora non lo trovi, puoi inserire manualmente qui l'indirizzo MAC dell'orologio   

::: xdripitem BlueJay Advanced Settings
&ensp;BlueJay Mac
:::

Ora il codice QR dovrebbe comparire sull'orologio; se lo vedi, passa al punto 7.

5 - Se il codice QR non è comparso sull'orologio, seleziona QR e riprova.  
<img src="./images/M-S-SW-BJc4.png" style="zoom:76%;" />  
Se ancora non vedi il codice QR, prova REBOOT, poi [contatta](https://bluejay.website/contactus) il produttore per assistenza o chiedi aiuto [qui](https://gitter.im/jamorham/BlueJay).

6 - Sul GTS segui questa sequenza di menu per mostrare il codice QR:  
Settings Menu -> Admin Menu -> Show QR Code  
<img src="./images/M-S-SW-BJc6.png" style="zoom:76%;" /> 

7 - In xDrip scansiona il codice QR dell'orologio  

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Configurazione automatica    
:::
Devi autorizzare xDrip ad accedere alla fotocamera del telefono.  
Scansiona il codice QR mostrato sull'orologio.  
<img src="./images/M-S-SW-BJc7.png" style="zoom:50%;" />

Configura l'orologio come follower e dovresti vedere la tua glicemia entro pochi minuti.

::: xdripitem BlueJay Watch <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Run Collector <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Invia Letture <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

Controlla lo [Stato del sistema](../troubleshoot/systemstatus) per verificare che l'orologio sia associato correttamente. Scorri fino alla scheda di stato avanzato BlueJay.  

<img src="./images/M-S-SW-BJc8.png" style="zoom:66%;" />

Se il core di xDrip non è installato, installalo ora.

### Installare il core di xDrip {#install-the-xdrip-core}

::: warning Metti l'orologio in carica durante l'installazione del core
:::

In Stato del sistema di xDrip, stato avanzato BlueJay, tocca la riga rossa xDrip Core: Not Installed.

<img src="./images/M-S-SW-BJd1.png" style="zoom:71%;" />

Seleziona OK per aggiornare l'orologio.

<img src="./images/M-S-SW-BJd2.png" style="zoom:79%;" />

Controlla poi lo Stato del sistema: dovresti vedere il core installato.

<img src="./images/M-S-SW-BJd3.png" style="zoom:66%;" />

### Run collector {#run-collector}

Run collector significa che userai l'orologio senza dover necessariamente avere il telefono con te.

Se usi un modello X2, devi configurare l'orologio con xDrip.  
Per il GTS puoi farlo direttamente dal [menu](https://bluejay.website/gts-menu-top) dell'orologio, senza usare xDrip.

Per usare l'orologio con xDrip devi avere un trasmettitore collegato direttamente a xDrip, con i dati della glicemia attualmente visualizzati in xDrip.

Definisci quale slot si collegherà al trasmettitore. Consulta la tabella [qui sopra](#g6g7-and-11) per configurare gli slot.

::: xdripitem BlueJay Advanced Settings
:::

##### Run Phone Collector {#run-phone-collector}

::: xdripitem Run Phone Collector <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Also run the standard collector on this phone. Only turn this off if you don't want this phone itself to be connecting to the transmitter.
:::

Attiva o disattiva la connessione di xDrip al trasmettitore (tramite lo slot phone).

##### BlueJay uses Phone Slot {#bluejay-uses-phone-slot}

::: xdripitem BlueJay uses Phone Slot <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;This allows the BlueJay to occupy the phone slot on the transmitter. Select this if you want another non-phone device to be able to connect to the transmitter and you are not using a phone to connect to the transmitter.
:::

Per impostazione predefinita BlueJay usa lo slot non-phone. Con questa opzione puoi fargli usare lo slot phone, ma devi allora disattivare Run Phone Collector qui sopra.

Una volta configurati gli slot, puoi attivare l'orologio come dispositivo collector autonomo.

::: xdripitem BlueJay Watch <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Run Collector <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

Vedrai allora che xDrip sul telefono non è più collegato al trasmettitore: lo è BlueJay.  
Quando l'orologio è nel raggio d'azione Bluetooth, il telefono dovrebbe ricevere la glicemia da BlueJay.

<img src="./images/M-S-SW-BJe4.png" style="zoom:66%;" />

## BlueJay GTS {#bluejay-gts}

Il GTS non ha bisogno di xDrip per essere configurato, ma se vuoi farlo i passaggi qui sopra valgono anche per lui.

Guarda il video [qui](https://www.youtube.com/watch?v=JM5cw-xVAZk) per una visita guidata.

Guarda qui [come](https://www.youtube.com/watch?v=6YpjuZe2c_Q) collegarti al trasmettitore.

## BlueJay U1/U2 (modelli precedenti) {#bluejay-u1u2-legacy}

Gli U1 e U2 non sono più in vendita ma eseguono lo stesso pacchetto xDrip completo dell'U3, quindi vale la [configurazione dell'U3](#bluejay-u3) qui sopra. Consulta le [Top Tips / FAQ](https://bluejay.website/faq) del produttore per i consigli sugli orologi della serie U.

<br>

[*Ultima modifica 18/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
