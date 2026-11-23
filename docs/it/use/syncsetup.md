---
source_hash: 2d97e8913b
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;Impostazioni xDrip+ Sync
:::

::: warning Vecchio xDrip Sync
A luglio 2024 Google ha chiuso la [Firebase API](https://firebase.google.com/docs/cloud-messaging/migrate-v1) deprecata che xDrip usava per xDrip Sync.  
Aggiorna xDrip a una versione successiva al [23 luglio 2024](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.07.23) per usare il metodo Sync legacy.  
Si consiglia di aggiornare xDrip almeno all'ultima release.
:::

xDrip offre un meccanismo esclusivo di sincronizzazione in tempo reale tra dispositivi Android, che rende la condivisione di glicemia e trattamenti il più semplice possibile.

<br>

[Qui il video di riferimento originale](https://www.youtube.com/watch?v=LcgjfbYcWkE).

### Prerequisiti {#prerequisites}

::: warning Attenzione
I [Google Play services](https://play.google.com/store/apps/details?id=com.google.android.gms) sono indispensabili per usare questa funzione. Assicurati che siano presenti, attivati e non soggetti all'ottimizzazione della batteria.
:::

Il telefono master di xDrip è il dispositivo che riceve effettivamente le letture glicemiche direttamente da un sensore, un bridge o un'app.  
Rendere master di xDrip Sync un dispositivo follower serve a poco, a meno che il follower non possa usare la stessa sorgente dati.

Il master deve ricevere i dati in modo affidabile. Se il follower non ha dati, verifica sempre prima il master.

## Configura il master {#setup-master}

Rendi master il telefono con la sorgente dati principale (attiva la casella):

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;Impostazioni xDrip+ Sync  


&emsp;&emsp;&emsp;&emsp;**Imposta come Telefono Principale (MASTER) per tel. secondari (FOLLOWER) <span class='symbol' style="float: right;"><img src="../images/EN.png" style="zoom:75%;" />&emsp;&emsp;</span>**
:::

<br>

### Copia la chiave di sincronizzazione {#copy-the-sync-key}

#### Opzione 1 (consigliata) {#option-1-recommended}

Sul telefono master mostra il codice QR della chiave di sincronizzazione:

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_qrcode_grey600_48dp.png" style="width:5%;" />&ensp;Mostra impostazioni dei codici QR  
<div style="background-color: gray; color: white; text-align: center;">  &emsp;SOLO IMPOSTAZIONI USANDO XDRIP PLUS SECURITY KEY&emsp;</div>
:::

Per il momento lascia il telefono master su questa schermata.

<img src="./images/M-S-QRe.png" style="zoom:75%;" />

##### Opzione 1 bis (il telefono follower non riesce a leggere il codice QR) {#option-1-bis-follower-phone-cannot-read-the-qr-code}

Fai uno screenshot del codice QR e invialo al telefono follower (MMS, WhatsApp, caricamento su Google Cloud, ...).

#### Opzione 2 (complicata) {#option-2-complicated}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;Impostazioni xDrip+ Sync  

&emsp;&emsp;&emsp;&emsp;**Chiave di sicurezza del Gruppo per sincronizzazione**
:::

<img src="./images/M-S-SY2.png" style="zoom:75%;" />

<br>

## Configura il follower {#setup-follower}

Rendi follower tutti gli altri telefoni (disattiva la casella):

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;Impostazioni xDrip+ Sync  


&emsp;&emsp;&emsp;&emsp;**Imposta come Telefono Principale (MASTER) per tel. secondari (FOLLOWER) <span class='symbol' style="float: right;"><img src="../images/DIS.png" style="zoom:75%;" />&emsp;&emsp;</span>**
:::

<br>

Imposta la sorgente dati del follower:

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;xDrip Sync Follower
:::

Maggiori informazioni sulla sorgente dati [xDrip Sync Follower](../install/xdripfollower).

<br>

::: warning Usa xDrip Cloud deve essere impostato allo stesso modo su tutti i telefoni
Master e follower. O è attivo su tutti, o è disattivato su tutti.
:::

::: xdripitem Usa xDrip Cloud
&ensp;Usa i nuovi server cloud xDrip+. Master e follower devono avere entrambi questa impostazione selezionata.  
:::

Si consiglia di attivare [Usa xDrip Cloud](./sync#use-xdrip-cloud) su tutti i dispositivi, perché è il metodo più a prova di futuro.

### Copia la chiave di sincronizzazione dal master {#copy-the-sync-key-from-the-master}

#### Opzione 1 (consigliata) {#option-1-recommended-1}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_qrscan.png" style="width:5%;" />&ensp;Configurazione automatica  
&emsp;&emsp;&emsp;Camera
:::

Devi autorizzare xDrip ad accedere alla fotocamera del telefono.  
Scansiona il codice QR mostrato sul telefono master.

<img src="./images/M-S-ACS.png" style="zoom:75%;" />

Ti verrà chiesto di confermare che vuoi importare queste impostazioni (assicurati di importare impostazioni sicure).

::: xdripitem Sei sicuro?
&ensp;Importa solo le impostazioni da fonti affidabili!  
&ensp;Conferma di volere importare le impostazioni seguenti:  

&ensp;impostazione1  
&ensp;impostazione2  
&ensp;impostazione3  

No&emsp;&emsp;<span style="background-color: gray; color: white; text-align: center;">&ensp;Si&ensp;</span>     
:::

#### Opzione 1 bis (il telefono follower non riesce a leggere il codice QR) {#option-1-bis-follower-phone-cannot-read-the-qr-code-1}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_qrscan.png" style="width:5%;" />&ensp;Configurazione automatica  
&emsp;&emsp;&emsp;File immagine
:::

Seleziona l'immagine che contiene il codice QR.

<img src="./images/M-S-SY3.png" style="zoom:75%;" />

::: xdripitem Sei sicuro?
&ensp;Importa solo le impostazioni da fonti affidabili!  
&ensp;Conferma di volere importare le impostazioni seguenti:   

&ensp;impostazione1  
&ensp;impostazione2  
&ensp;impostazione3  

No&emsp;&emsp;<span style="background-color: gray; color: white; text-align: center;">&ensp;Si&ensp;</span>  
:::

#### Opzione 2 (complicata) {#option-2-complicated-1}

Modifica il campo della chiave e digita **esattamente** la stessa chiave del master.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;Impostazioni xDrip+ Sync  

&emsp;&emsp;&emsp;&emsp;**Chiave di sicurezza del Gruppo per sincronizzazione**
:::

<img src="./images/M-S-SY2.png" style="zoom:75%;" />

<br>

## Azioni dei follower {#follower-actions}

Per impostazione predefinita i follower possono inviare al master trattamenti, calibrazioni e persino l'avvio o l'arresto del sensore.  
Se vuoi impedirlo, disattiva [Accetta le azioni dei follower](./sync#accept-followers-actions) sul master.

## Verifica {#verify}

Per verificare che il follower riceva i dati, controlla lo [Stato del sistema](../troubleshoot/systemstatus#xdrip-sync-follower) sul telefono follower.

<br>

[*Ultima modifica 21/07/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.19)
