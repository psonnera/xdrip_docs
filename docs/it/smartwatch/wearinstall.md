---
source_hash: 6617aa448f
source_commit: 7a18e7c
---
Trovi la documentazione di riferimento [qui](https://github.com/NightscoutFoundation/xDrip/blob/master/Documentation/WatchGuide.md).

::: info Curiosità
Puoi usare alcuni di questi metodi anche con l'app master Dexcom e con AAPS.
:::

### Prerequisiti {#prerequisites}

L'orologio deve essere compatibile con Android Wear OS e riportare il seguente logo:

<img src="https://play-lh.googleusercontent.com/WmoV-m8b6x16sDRfzebu5b2vstcyBHRrpzCj6ODoh6hGuMa9Gg39EvnOk7z3qMa0_WM=s180-rw" style="zoom:50%;" align="left"/>

Gli orologi recenti si trovano [qui](https://wearos.google.com/).  
Tutti gli smartwatch Wear OS sono direttamente compatibili con xDrip, ma le [modifiche di Google](https://www.androidpolice.com/2021/02/12/wear-os-is-making-app-sideloading-much-more-difficult/) a Wear OS ne hanno reso più complessa l'installazione.  
I successivi cambiamenti di comportamento introdotti da Samsung e da Google con Wear OS 5 l'hanno resa ancora più complicata.

### Versioni di Wear OS {#wear-os-versions}

Le vecchie versioni di Wear OS, come la 1.5 e la 1.6, sono ormai più complicate da usare con i telefoni moderni.  
Wear OS 2 e 3 sono pienamente supportati.  
Wear OS 4 e 5 possono presentare delle difficoltà.

### Wear OS 1.x {#wear-os-1x}

::: warning Android 15
Il vecchio pacchetto Android Wear 2.9 non è compatibile con Android 15.
:::

Di solito si tratta del Sony Smartwatch 3 ([SWR50](https://www.sony.com/electronics/support/other-products-xperia-smart-devices/swr50)). 

#### Metodo 1 (il più semplice) {#method-1-easiest}

1. Dissocia l'orologio dal telefono se era già associato.
2. Disinstalla Wear OS dal telefono se è installato.  
   Se hai altri orologi Android Wear collegati, potresti doverli associare di nuovo.
3. Disattiva l'aggiornamento automatico delle app di Google Play.
4. Installa [Android Wear 2.9.0.185084575 GMS](https://www.apkmirror.com/apk/google-inc/android-wear/android-wear-2-9-0-185084575-gms-release/android-wear-smartwatch-2-9-0-185084575-gms-android-apk-download/).
5. Apri Android Wear e associa l'orologio, accettando e consentendo tutto: se vuoi disattivare alcune funzioni, lo farai dopo aver completato l'installazione di xDrip.
6. Al termine dell'associazione, controlla che la versione di Google Play dell'orologio sia **superiore a 9**.  
   Settings -> About -> Versions  
   <img src="./images/M-S-SW-AW3.png" style="zoom:75%;" />  
   Se non lo è: toccala 3 volte per forzare l'aggiornamento e aspetta (anche alcune ore).  
   <img src="./images/M-S-SW-AW3a.png" style="zoom:75%;" />
7. Seleziona un quadrante xDrip nell'app Android Wear del telefono  
   <img src="./images/M-S-SW-AW1.png" style="zoom:75%;" />   
   <img src="./images/M-S-SW-AW2.png" style="zoom:75%;" /> 
8. Riattiva l'aggiornamento automatico delle app di Google Play e aggiorna manualmente a [Wear OS](https://play.google.com/store/apps/details?id=com.google.android.wearable.app).

#### Metodo 2 (con un computer) {#method-2-with-a-computer}

1. Installa [Wear OS](https://play.google.com/store/apps/details?id=com.google.android.wearable.app) e associa l'orologio al telefono.
2. Controlla che la versione dei servizi Google Play dell'orologio sia superiore a 9 (quella di fabbrica con il firmware più recente è la 8.7).  
   Settings -> About -> Versions  
   <img src="./images/M-S-SW-AW3.png" style="zoom:75%;" />   
   <img src="./images/M-S-SW-AW3a.png" style="zoom:75%;" />   
   Se lo è, hai finito: vedi sopra come selezionare un quadrante xDrip.  
   Altrimenti continua qui sotto.
3. [Scarica](https://www.apkmirror.com/apk/google-inc/google-play-services-android-wear/google-play-services-android-wear-9-8-41-release/google-play-services-9-8-41-534-130237018-android-apk-download/download/) una versione più recente dei servizi Google Play. Rinomina il file con un nome più corto, ad esempio `GPS.apk`.
4. [Installa ADB e caricalo sull'orologio](../troubleshoot/ADB).

### Wear OS 2.x e 3.x {#wear-os-2x-and-3x}

#### Metodo 1 (il più semplice) {#method-1-easiest-1}

Non sempre è possibile completare questa procedura: se non riesce, prova il Metodo 2.

1. Dissocia l'orologio dal telefono se era già associato.
2. Disinstalla Wear OS dal telefono se è installato.  
   Se hai altri orologi Android Wear collegati, potresti doverli associare di nuovo.
3. Disattiva l'aggiornamento automatico delle app di Google Play.
4. Installa una vecchia versione di Wear OS [2.51.0.398446042.gms](https://www.apkmirror.com/apk/google-inc/android-wear/android-wear-2-51-0-398446042-gms-release/wear-os-by-google-smartwatch-2-51-0-398446042-gms-android-apk-download/).
5. Apri Android Wear e associa l'orologio, accettando e consentendo tutto: se vuoi disattivare alcune funzioni, lo farai dopo aver completato l'installazione di xDrip.
6. Sull'orologio apri Settings, Apps & Notifications, App Info, System Apps e cerca Google Play Store. Seleziona Remove Upgrades (disinstalla aggiornamenti). Conferma. (Nota: l'orologio aggiornerà automaticamente l'app, quindi una volta fatto il downgrade devi essere veloce.)  
   <img src="./images/M-S-SW-AW6.png" style="zoom:65%;" />
7. Sull'orologio apri Google Play Store e scorri fino ad Apps on my Phone. Seleziona e installa xDrip.  
   <img src="./images/M-S-SW-AW7.png" style="zoom:65%;" />
8. Cambia il quadrante con uno di xDrip, con un tocco prolungato sul quadrante attuale.

#### Metodo 2 (il migliore) {#method-2-best}

**Consigliato:** segui [questo video](https://www.youtube.com/watch?v=ejrmH-JEeE0) che illustra la procedura nei dettagli.

Devi essere connesso al Wi-Fi, e così anche l'orologio.

1. Installa [Wear OS](https://play.google.com/store/apps/details?id=com.google.android.wearable.app) e associa l'orologio.
2. Installa e apri [Wear Installer 2](https://play.google.com/apps/testing/org.freepoc.wearinstaller2) sul telefono.  
   <img src="./images/M-S-SW-AW9.png" style="zoom:75%;" />
3. Attiva la modalità sviluppatore sull'orologio (istruzioni [qui](../troubleshoot/ADB#smartwatch). Solo sull'orologio, poi torna qui)
4. Attiva il debug ADB tramite Wi-Fi sull'orologio.  
   <img src="./images/M-S-SW-AW8.png" style="zoom:65%;" />
5. Annota l'indirizzo IP dell'orologio.  
   <img src="./images/M-S-SW-AW10.png" style="zoom:65%;" />
6. Apri l'app sull'orologio e copia l'indirizzo IP nell'app sul telefono.  
   Tocca `Done`  
   <img src="./images/M-S-SW-AW11.png" style="zoom:75%;" />
7. Seleziona xDrip  
   <img src="./images/M-S-SW-AW12.png" style="zoom:75%;" />  
   Wear Installer estrarrà l'apk per lo smartwatch.  
   <img src="./images/M-S-SW-AW13.png" style="zoom:75%;" />  
   Se richiesto, accetta l'autorizzazione al debug sull'orologio.  
   <img src="./images/M-S-SW-AW14.png" style="zoom:75%;" />
8. Quando è pronto, seleziona `INSTALL` e lascia lavorare l'app senza intervenire: possono servire alcuni minuti.  
   <img src="./images/M-S-SW-AW15.png" style="zoom:75%;" />
9. Osserva i messaggi durante la procedura, ma non intervenire.  
   <img src="./images/M-S-SW-AW16.png" style="zoom:75%;" />
10. Al termine, seleziona `FINISH`.  
    <img src="./images/M-S-SW-AW17.png" style="zoom:75%;" />
11. Se l'installazione di xDrip sull'orologio non è riuscita, riprova.

##### Alternative al Metodo 2 {#method-2-alternatives}

Usa [GeminiMan Wear OS Manager](https://play.google.com/store/apps/details?id=com.geminiman.wearosmanager) o [Easy Fire Tools](https://play.google.com/store/apps/details?id=de.agondev.easyfiretools) (procedura simile a quella sopra).

#### Metodo 3 (con un computer) {#method-3-with-a-computer}

1. Installa [ADB](../troubleshoot/ADB).
2. Scarica xDrip su un computer ed estrai l'APK (è un file compresso).  
   **Deve essere esattamente la stessa versione che hai sul telefono.**
3. Apri il pacchetto APK di xDrip con un programma di archiviazione, ordina per dimensione i file sotto `res` e copia il più grande (è l'apk wear incorporato, solo che non ha questo nome) nella cartella di ADB.
4. Carica l'estensione Wear di xDrip sull'orologio.

### Wear OS 5 {#wear-os-5}

Google e Samsung hanno introdotto cambiamenti importanti in Wear OS 5 e non permettono facilmente i quadranti personalizzati.

L'installazione dell'app xDrip per l'orologio va fatta con Wear Installer 2 seguendo [questo video](https://www.youtube.com/watch?v=EvTGEnPA9PY) (mostra il quadrante AAPS: la procedura è la stessa con l'APK wear di xDrip).

**Se per errore cambi il quadrante con un altro, devi ripetere la procedura qui sopra.**

### Aggiornare xDrip sull'orologio {#update-xdrip-on-your-watch}

#### Wear OS 1.x {#wear-os-1x-1}

Per forzare l'aggiornamento dell'app dell'orologio, basta sincronizzare tutte le app.  
<img src="./images/M-S-SW-AW32.png" style="zoom:75%;" />

#### Wear OS da 2.0 a 4.0 {#wear-os-20-to-40}

Dovrai disinstallare e reinstallare l'app wear ogni volta che [aggiorni](../use/update) xDrip sul telefono, per mantenere sincronizzate le due app.

A partire dal 13 aprile 2021, xDrip può aggiornare automaticamente la versione wear se hai già installato una versione compatibile (almeno la [Nightly del 13 aprile 2021](https://github.com/NightscoutFoundation/xDrip/releases/tag/2021.04.13)).

Per la versione aggiornata, le [istruzioni](https://github.com/NightscoutFoundation/xDrip/issues/1648) sono le seguenti:

- Installa sull'orologio l'ultimo componente WearOS nightly di xDrip, ad esempio con l'app Wear Installer, facendo il downgrade del Play Store o manualmente tramite adb (vedi sopra).
- Assicurati che la modalità sviluppatore e il debug adb via Wi-Fi siano attivi sull'orologio (vedi sopra: Wear OS 2 Metodo 2 passo 4)
- Vai in xDrip Prefs sull'orologio, scorri fino a `Force Update` e toccalo
- Dovrebbe verificare ADB e chiedere l'autorizzazione: seleziona `Always Allow`
- Probabilmente ti dirà che ADB non funziona perché serve l'autorizzazione
- Torna in xDrip Prefs sull'orologio e tocca di nuovo Force Update
- Questa volta dovrebbe dire che ADB è a posto e poi chiedere all'app xDrip del telefono di inviare l'ultima versione
- La versione dovrebbe essere scaricata e xDrip si installerà da solo.

Quando le versioni sono identiche non succederà granché, ma questa procedura può servire in futuro per forzare xDrip a inviare l'ultima versione; in ogni caso dovrebbe anche rilevare automaticamente i cambi di versione e aggiornarsi in background. Per divertimento puoi installare l'ultima nightly sull'orologio, poi fare il downgrade sul telefono e verificare che la procedura di aggiornamento riporti l'app dell'orologio alla versione precedente. Le informazioni sulla versione dovrebbero comparire accanto alla scritta `Force Update`.

L'idea è che non ti serva più Wear Installer o qualunque metodo tu abbia usato per la prima installazione (ad esempio adb da PC o il downgrade del Play Store), perché xDrip può aggiornarsi da solo.

#### Wear OS 5.0 {#wear-os-50}

Reinstalla il quadrante con [Wear Installer 2](#wear-os-5).

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
