---
source_hash: 3c220d5612
source_commit: 7a18e7c
---
### Preparare il dispositivo per il debug {#prepare-your-device-for-debug}

Questo passaggio è obbligatorio per collegarlo tramite ADB con un collegamento fisico. Se il tuo dispositivo non ha un connettore USB fisico devi usare ADB tramite Wi-Fi (documentazione in arrivo).

Se vuoi fare il debug di uno smartphone, passa direttamente a [questa sezione](#smartphone).

#### Smartwatch {#smartwatch}

1. Attiva le Opzioni sviluppatore  
   Impostazioni -> Info -> Versioni -> Numero build  
   Tocca 7 volte il numero di build finché l'orologio non mostra "sei uno sviluppatore".   
   <img src="../smartwatch/images/M-S-SW-AW4.png" style="zoom:75%;" />  
2. Impostazioni -> Opzioni sviluppatore -> Debug ADB  
   Attiva il Debug ADB  
   <img src="../smartwatch/images/M-S-SW-AW5.png" style="zoom:75%;" />

#### Smartphone {#smartphone}

1. Attiva le Opzioni sviluppatore  
   Impostazioni -> Info -> Software -> Numero build  
   Tocca 7 volte il numero di build finché il telefono non mostra "sei uno sviluppatore".   
   <img src="./images/ADB5.png" style="zoom:75%;" />  
2. Impostazioni -> Opzioni sviluppatore -> Debug USB  
   Attiva il Debug ADB  
   <img src="./images/ADB6.png" style="zoom:75%;" />

### Installare ADB su un computer Windows {#install-adb-on-a-windows-computer}

1. Scarica [Android Debug Bridge](https://developer.android.com/studio/releases/platform-tools#downloads) sul computer.  
   `1` Apri la cartella Download  
   `2` Apri il file che hai scaricato  
   `3` Seleziona tutti i file  
   `4` Copiali nella cartella `5` adb che hai creato in C:

   <img src="./images/ADB0.png" />

2. Apri una nuova finestra del prompt dei comandi (`Start -> Run - > cmd`) con privilegi di amministratore.  
   <img src="./images/ADB1.png" />

### Installare un'app con ADB in Windows {#sideload-an-app-with-adb-in-windows}

1. Collega il dispositivo (orologio/telefono) al computer con un cavo USB e sblocca lo schermo.
2. Digita `cd \adb`  
   <img src="./images/ADB2.png" />
3. Digita `adb devices`  
   <img src="./images/ADB3.png" />
4. Guarda il dispositivo collegato e autorizza il debug, sempre.  
   <img src="./images/ADB10.png" style="zoom:75%;" />  
   <img src="./images/ADB9.png" style="zoom:75%;" />
5. Digita di nuovo `adb devices`  
     Ora dovresti vedere il tuo dispositivo nell'elenco.  
   <img src="./images/ADB4.png" />
6. Copia il file che vuoi installare nella cartella C:\ADB (chiamiamolo per esempio `myapplication.apk`; se il nome contiene spazi rinominalo con qualcosa di breve e semplice, come `oop.apk` o `xdrip.apk`).
7. Digita il comando `adb install -r myapplication.apk` e attendi il completamento (sostituisci `myapplication` con il nome della tua app).
8. Ora l'app dovrebbe essere presente sul dispositivo.

### Installare ADB su un Mac {#install-adb-on-a-mac}

1. Scarica [Android Debug Bridge](https://developer.android.com/studio/releases/platform-tools#downloads) sul computer.  
   `1` Apri la cartella Download nel Finder  
   `2` Fai clic con il tasto destro sulla cartella platform tools  
   `3` Seleziona Nuovo terminale nella cartella

<img src="./images/ADB7.png" />

### Installare un'app con ADB in macOS {#sideload-an-app-with-adb-in-ios}

1. Collega il dispositivo (orologio/telefono) al computer con un cavo USB e sblocca lo schermo.

2. Digita `./adb devices`  
   <img src="./images/ADB8.png" />

3. Guarda il dispositivo collegato e autorizza il debug, sempre.    
   <img src="./images/ADB10.png" style="zoom:75%;" />  
   <img src="./images/ADB9.png" style="zoom:75%;" />

4. Digita di nuovo `./adb devices`  
     Ora dovresti vedere il tuo dispositivo nell'elenco.  

5. Copia il file che vuoi installare nella cartella platform tools (chiamiamolo per esempio `myapplication.apk`; se il nome contiene spazi rinominalo con qualcosa di breve e semplice, come `oop.apk` o `xdrip.apk`).

6. Digita il comando `./adb install -r myapplication.apk` e attendi il completamento (sostituisci `myapplication` con il nome della tua app).

7. Ora l'app dovrebbe essere presente sul dispositivo.


### INSTALL_FAILED_VERSION_DOWNGRADE {#install_failed_version_downgrade}

Probabilmente significa che l'app è già presente sul dispositivo in una versione più recente.

Prova a trovarla e a disinstallarla.

Se non c'è modo di disinstallarla, prova a installarla con l'opzione di downgrade:

(Windows)	`adb install -r -d myapplication.apk`

(Mac)	`./adb install -r -d myapplication.apk`

<br>

[*Ultima modifica 4/8/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.08.02)
