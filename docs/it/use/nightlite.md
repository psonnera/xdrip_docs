---
source_hash: 12ee29c8aa
source_commit: 7a18e7c
---
NightLite è un servizio follower leggero e compatibile con Nightscout. È un'alternativa più semplice alla gestione di un tuo sito Nightscout quando ti serve solo condividere la glicemia con i follower.

xDrip è il **master** (carica i tuoi dati). L'[app NightLite per iOS](https://apps.apple.com/us/app/nightlite/id6759909591) (un fork di Nightguard, di Richard Lander) è il **follower** e mostra i tuoi dati su iPhone, iPad, Apple Watch o Mac.

::: info Curiosità
xDrip invia solo le ultime 12 ore di letture glicemiche (con tendenza e delta) e i trattamenti, aggiornati a ogni nuova lettura (circa ogni 5 minuti).
:::

### Prerequisiti {#prerequisites}

- xDrip su una [nightly](../install/download#pre-release) recente (minimo [1 marzo 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.03.01)).
- Un URL NightLite per il tuo account. Contiene la tua chiave di sicurezza ed è l'unica cosa che devi inserire: xDrip ne ricava il codice QR per i follower.
- Per il follower: un iPhone o iPad (iOS 15+), Apple Watch (watchOS 9.1+) o Mac (macOS 12 con M1 o successivo) con l'[app NightLite](https://apps.apple.com/us/app/nightlite/id6759909591).

::: warning Attenzione
NightLite non può essere usato mentre xDrip funziona come [follower Nightscout](../install/nightscoutfollower). Funziona solo quando xDrip è la tua sorgente dati principale.
:::

### Configura il master (xDrip) {#setup-the-master-xdrip}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_cloud_upload_grey600_48dp.png" style="width:5%;" />&ensp;Caricamento nel Cloud  
&ensp;&emsp;NightLite
:::

Inserisci il tuo URL NightLite:

::: xdripitem NightLite URL
&ensp;Typically entered by scanning QR code from dashboard  
&ensp;This contains your security key - do not disclose it
:::

Poi attiva il caricamento:

::: xdripitem Upload to NightLite<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Whether to upload to the remote service
:::

::: warning Attenzione
L'URL NightLite contiene la tua chiave di sicurezza. Chiunque lo possieda può accedere ai tuoi dati, quindi non condividerlo.
:::

### Collega un follower {#connect-a-follower}

Una volta attivato il caricamento, xDrip può mostrare un codice QR che contiene tutta la tua configurazione. È questo che il follower scansiona: non c'è nulla da digitare sul dispositivo follower.

::: xdripitem Mostra Codice QR
&ensp;Codice a barre da scansionare per configurare i follower
:::

1. Installa l'[app NightLite](https://apps.apple.com/us/app/nightlite/id6759909591) sul dispositivo follower.
2. Sul telefono master, tocca **Mostra Codice QR**. xDrip mostra il codice QR `NightLite configuration`.
3. Nelle preferenze dell'app NightLite, tocca l'icona di scansione accanto al campo dell'URL Nightscout e scansiona il codice QR dallo schermo del master.

<img src="./images/M-S-NL4.png" style="zoom:33%;" />

::: info Nota
Il servizio NightLite può inviare notifiche a xDrip e, se necessario, interrompere il caricamento da remoto.
:::

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
