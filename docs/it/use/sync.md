---
source_hash: 8ff0f07a91
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;Impostazioni xDrip+ Sync
:::

::: warning Vecchio xDrip Sync
A luglio 2024 Google ha chiuso la [Firebase API](https://firebase.google.com/docs/cloud-messaging/migrate-v1) deprecata che xDrip usava per xDrip Sync.  
Aggiorna xDrip a una versione successiva al [23 luglio 2024](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.07.23) per usare il metodo Sync legacy.  
Si consiglia di aggiornare xDrip all'ultima release.
:::

::: warning Attenzione
I [Google Play services](https://play.google.com/store/apps/details?id=com.google.android.gms) sono indispensabili per usare questa funzione. Assicurati che siano presenti, attivati e non soggetti all'ottimizzazione della batteria.
:::

xDrip offre un meccanismo esclusivo di sincronizzazione in tempo reale tra dispositivi Android, che rende la condivisione di glicemia e trattamenti il più semplice possibile.

La chiave di sicurezza sottostante può essere personalizzata invece di usare la chiave dell'account Google (non modificabile).

::: xdripitem Sincronizza usando la Chiave di Sicurezza <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;La Chiave è usata al posto dell'account Google
:::

##### Chiave di sicurezza del Gruppo per sincronizzazione {#handset-group-security-sync-key}

All'installazione di xDrip viene creata una chiave unica (sarà diversa se reinstalli xDrip), che deve coincidere su tutti i dispositivi che usano xDrip Sync. Anche se puoi personalizzare questa chiave scegliendone una tua (lettere e numeri), di solito la lascerai come è stata generata.

::: xdripitem Chiave di sicurezza del Gruppo per sincronizzazione
&ensp;Chiave di gruppo per sincronizzazione telefoni
:::

##### Imposta come Telefono Principale (MASTER) per tel. secondari (FOLLOWER) {#be-master-for-followers}

Il dispositivo che riceve i dati glicemici dal sensore sarà il master, tutti gli altri saranno follower.  
Un solo master può usare la stessa chiave di sicurezza. Se vengono rilevati due master, l'ultimo arrivato verrà disattivato e tornerà follower.

::: xdripitem Imposta come Telefono Principale (MASTER) per tel. secondari (FOLLOWER) <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Questo telefono invierà i dati ad apparecchi Secondari
:::

##### Accetta le azioni dei follower {#accept-followers-actions}

Puoi configurare il telefono master per ricevere e accettare trattamenti e calibrazioni dai follower. Fai estrema attenzione con questa funzione se usi le calibrazioni automatiche. Ricorda anche che l'avvio e l'arresto del sensore possono essere inviati dai follower e accettati dal master.

::: xdripitem Accetta le azioni dei follower <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Trattamenti e calibrazioni mandati dei follower saranno accettati
:::

##### Usa xDrip Cloud {#use-xdrip-cloud}

Dopo che Google ha chiuso a luglio 2024 la [Firebase API](https://firebase.google.com/docs/cloud-messaging/migrate-v1) deprecata usata per xDrip Sync, è stato sviluppato un nuovo metodo di condivisione.

::: warning Deve essere impostato allo stesso modo su tutti i telefoni
Master e follower. O è attivo su tutti, o è disattivato su tutti.
:::

::: xdripitem Usa xDrip Cloud <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Usa i nuovi server cloud xDrip+. Master e follower devono avere entrambi questa impostazione selezionata.  
:::

Se xDrip consuma troppa batteria quando usa i dati mobili della SIM, puoi provare ad attivare questa opzione.

::: xdripitem Risparmia energia <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Riduce l'utilizzo della batteria dei dati di rete con l'elaborazione in batch escludendo dati inutili  
:::

##### Whole house {#whole-house}

Basandosi sul progetto [Parakeet](https://github.com/jamorham/wixel-xDrip), più dispositivi **master** possono creare una rete che copre tutta la casa.  
Se usi sensori Libre puoi usare anche questa funzione: vedi [qui](https://github.com/tzachi-dar/LibreAllHouse) come creare la tua rete per tutta la casa.

::: xdripitem Whole House <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Partecipa a una rete di casa intera (LibreAllHouse)
:::

::: xdripitem Libre copertura Casa Intera <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Questo telefono sarà un collector in una rete di copertura casa completa
:::

##### Sospensione allarmi a distanza {#remote-snoozing}

La sospensione a distanza permette di propagare la richiesta di sospensione a tutto il gruppo. Sia il master sia i follower possono sospendere gli allarmi. Usala con cautela.

::: xdripitem Invia sospensione allarme a tutti <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Le sospensione allarme avranno effetto su tutti i telefoni del gruppo se questa impostazione è abilitata su ognuno di loro
:::

::: xdripitem Conferma invio sospensione allarme <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Messaggio di conferma a l'invio di ogni sospensione allarme a distanza
:::

::: xdripitem Accetta sospensione allarme a distanza <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Consenti a tutti i telefoni di sospendere a distanza gli allarmi su questo telefono
:::

::: xdripitem Il nome del WiFi deve essere identico <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Accetta solo se il nome della rete WiFi remota inizia con le stesse lettere e somiglia molto a la nostra
:::

##### Trasmissione Locale {#local-broadcast}

Trasmissione Locale invia o accetta sospensioni verso/da altre app (non xDrip) installate sullo stesso telefono, indipendentemente dalla sospensione a distanza tra telefoni xDrip.

::: xdripitem Trasmissione Locale <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Invia silenziamento ad altre applicazioni su questo telefono
:::

::: xdripitem Accetta Trasmissione Locale <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Accetta silenziamenti da altre applicazioni su questo telefono
:::

##### Disattivare la sincronizzazione {#disable-sync}

Disattivare tutte le funzioni di sincronizzazione blocca completamente la condivisione. Quando la riattivi potrebbe essere necessario riavviare il telefono.

Puoi usare questa opzione in caso di malfunzionamento totale di Sync o quando usi un telefono senza Google Play Services.

::: xdripitem Disattivare tutte le funzioni di sincronizzazione <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Opzione Modifica Programma Temporanea, si ferma completamente tutta la sincronizzazione. Potrebbe essere necessario riavviare il sistema dopo essere stato riattivato. Usare con cautela!
:::

### Sincronizzazione nel deserto {#desert-sync}

Sincronizzazione nel deserto permette di usare xDrip Sync senza internet né copertura dati del telefono.

::: xdripitem Sincronizzazione nel deserto
<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xxhdpi/desert_sync.png" style="width:5%;" />&ensp;Follower fuori rete dati
:::

Sincronizzazione nel deserto ti permette di condividere i dati tra il master xDrip e i follower quando internet non è disponibile. Può succedere quando viaggi fuori dalla copertura telefonica o su una intranet locale (senza accesso a internet).

Attiva la sincronizzazione nel deserto su tutti i dispositivi.

::: xdripitem Sincronizzazione nel deserto <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Attivata sincronizzazione locale (non internet)
:::

Se conosci l'indirizzo IP del master (vale per le intranet locali), inseriscilo qui.  
Trovi l'IP del master nelle impostazioni Android del telefono - Informazioni sul telefono - Indirizzo IP.

::: xdripitem Indirizzo IP del Master
:::

Ora mostra il codice QR delle impostazioni del master e scansionalo sui follower con [Configurazione automatica](./copysettings#auto-configure).

::: xdripitem Mostra Codice QR
Codice a barre da scansionare per configurare i follower
:::

Se vuoi proteggere la connessione (intranet locali e wifi pubblici) puoi attivare https.

::: xdripitem Usa HTTPS <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Aggiungi un altro livello di crittografia per reti condivise, per esempio wifi pubblici
:::

Se non hai dati mobili né Wi-Fi, metti il telefono master in modalità hotspot Wi-Fi e connetti i follower tramite tethering. La distanza massima tra i dispositivi sarà limitata. Questo peserà anche molto sulla batteria del master: assicurati di avere a disposizione un power bank di riserva.  
Quando usi il tethering devi attivare un [servizio web](./interapp#web-service) sul master. Assicurati che il secret sia identico sul master e sui follower.

Controlla in Stato del sistema che tutto si connetta correttamente.

<img src="./images/M-S-SY8d2.png" style="zoom:75%;" />

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
