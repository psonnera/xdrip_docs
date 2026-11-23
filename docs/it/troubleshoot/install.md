---
source_hash: 92fd90f109
source_commit: 7a18e7c
---
## Il mio telefono dice che questa app è molto pericolosa {#my-phone-says-this-app-is-very-dangerous}

Le release GitHub del [repository ufficiale](https://github.com/NightscoutFoundation/xDrip/releases) sono sicure. Ignora questo messaggio.

<img src="./images/Install18.png" style="zoom:75%;" />

<br>

## Non trovo il file che ho scaricato {#i-cannot-find-the-file-i-downloaded}

Apri un file manager e guarda nella cartella Download della memoria interna del telefono: dovresti vedere un file con un nome simile a `xDrip-plus-20yymmdd-cccccccc.apk`

<br>

## Quando tocco il file .apk di xDrip si apre un elenco di file {#when-i-touch-the-xdrip-apk-it-opens-a-file-list}

Se il file xDrip-plus termina con .zip, rinominalo in .apk e riprova.

Se non c'è modo di aprirlo con il programma di installazione dei pacchetti, prova con un [APK installer](https://play.google.com/store/apps/details?id=com.apkinstaller.ApkInstaller).

<br>

## Non riesco a installare app sconosciute {#i-cannot-install-unknown-apps}

<img src="./images/Install19.png" style="zoom:75%;" />

In Impostazioni Android -> [Impostazioni di sicurezza](https://developer.android.com/distribute/marketing-tools/alternative-distribution#unknown-sources) devi consentire all'app che usi per aprire il file scaricato di installare file da origini sconosciute; se disponibile, seleziona solo questa volta.

Qui sotto l'esempio per Chrome; tu potresti usare un'altra app per aprire il file .apk di xDrip.

<img src="./images/Install20.png" style="zoom:75%;" />

<br>

## Non riesco a installare l'app {#i-cannot-install-the-app}

<img src="./images/Install23.png" style="zoom:75%;" />

Assicurati di non avere installata una versione diversa di xDrip: puoi aggiornare o riportare a una versione precedente solo app dello stesso sviluppatore. Se necessario, [reinstalla](./reinstall) xDrip per passare dalla versione ufficiale a una versione fork (e viceversa).

<br>

## **Il mio telefono dice che questa app non è sicura ed è stata creata per una versione di Android precedente** {#my-phone-says-this-app-is-unsafe-and-has-been-built-for-an-older-android-version}

Ignoralo con Altri dettagli, poi Installa comunque.

<img src="../install/images/Install01a.png" style="zoom:75%;" /> 

<br>

## xDrip ha bisogno della posizione in background {#xdrip-needs-background-location}

<img src="./images/Install21.png" style="zoom:60%;" />

Se vuoi che xDrip si colleghi a un dispositivo Bluetooth, deve avere l'[accesso alla posizione](../install/install#enable-location) permanente.

Nelle versioni di Android più recenti vai in Impostazioni Android -> Posizione -> App -> xDrip oppure Impostazioni Android -> App -> xDrip -> Posizione e verifica che sia attivo Consenti sempre.

<img src="../install/images/Install17.png" style="zoom:80%;" />

<br>

## xDrip deve essere escluso dall'ottimizzazione della batteria {#xdrip-needs-battery-optimization-whitelisting}

<img src="./images/Install22.png" style="zoom:60%;" />

xDrip non deve essere ottimizzato in alcun modo.

La posizione di questa impostazione varia a seconda della marca e della versione di Android; di solito la trovi in Impostazioni Android -> App -> xDrip -> Batteria

<img src="./images/Install22b.png" style="zoom:100%;" />

Potrebbe essere necessario riavviare il telefono per applicare queste modifiche. Se il messaggio di avviso resta, assicurati di usare una versione recente di xDrip: aggiornala se necessario.

<br>

[*Ultima modifica 28/3/2022*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2022.03.27)
