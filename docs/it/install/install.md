---
source_hash: 4b874be737
source_commit: 0bbdbd2
---
Una volta scaricato, installa l'apk di xDrip.

<img src="./images/InstallConfirm.png" style="zoom:50%;" />

Nelle versioni recenti di Android vedrai un avviso di Google Play Protect che indica che l'app non è sicura perché è stata creata per versioni precedenti di Android. Ignoralo con Altri dettagli e poi Installa comunque.

<img src="./images/PlayProtectWarning.png" style="zoom:50%;" />

**Devi [autorizzare l'installazione di app da origini sconosciute](https://developer.android.com/distribute/marketing-tools/alternative-distribution#unknown-sources) nelle impostazioni di sicurezza di Android.**  
Le versioni ufficiali di xDrip sono prive di virus e malware: essendo open source e controllate dallo sviluppatore principale, la loro distribuzione è sicura se le scarichi da GitHub.

<img src="./images/AllowUnknownSources.png" style="zoom:50%;" />

Tocca `Impostazioni` e poi attiva `Consenti da questa fonte`.

<img src="./images/AllowFromThisSource.png" style="zoom:50%;" />

Una volta installato, apri xDrip.

<img src="./images/Install03.png" style="zoom:75%;" />

### Capire cos'è xDrip {#understand-what-is-xdrip}

::: warning **Leggi** l'avviso importante
:::

::: xdrip <img src="./images/ImportantWarning.png" style="zoom:50%;" />
<img src="./images/WarningAgree.png" style="zoom:50%;" />  
Do NOT use or rely on this software or any associated materials for any medical purpose or decision.  
Do NOT rely on this system for any real-time alarms or time critical data.  
Do NOT use or rely on this system for treatment decisions or use as a substitute for professional healthcare judgement.  
All software and materials have been provided for informational purposes only as a proof of concept to assist possibilities for further research.  
No claims at all are made about fitness for any purpose and everything is provided **AS IS**. Any part of the system can fail at any time.  
Always seek the advice of a qualified healthcare professional for any medical questions.  
Always follow your glucose-sensor or other device manufacturers' instructions when using any equipment; do not discontinue use of accompanying reader or receiver, other than as advised by your doctor.  
This software is not associated with or endorsed by any equipment manufacturer and all trademarks are those of their respective owners.  
Your use of this software is entirely at your own risk.  
No charge has been made by the developers for the use of this software.  
This is an open-source project which has been created by volunteers. The source code is published free and open-source for you to inspect and evaluate.  
By using this software and/or website you agree that you are over 18 years of age and have read, understood and agree to all of the above.
:::

<br>

**Leggi** l'EULA.  

::: warning Assicurati di averla compresa del tutto prima di salvare.
:::

::: xdrip <img src="./images/EULA.png" style="zoom:50%;" />
xDrip MUST NOT BE USED TO MAKE MEDICAL DECISIONS.  
IT IS A RESEARCH TOOL ONLY AND IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  
THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  
SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
:::



<br>

### Autorizzare l'attività in background {#authorize-background-activity}

xDrip deve avere il diritto di funzionare in background: deve essere escluso dall'ottimizzazione della batteria. È essenziale per un corretto funzionamento. L'app dovrebbe chiederti di concedere questa autorizzazione. Se non lo fa, o se devi verificarlo in seguito, controllalo in `Impostazioni` - `App` - `xDrip` del telefono. Consulta il manuale del telefono, perché dipende dalla versione di Android e dal produttore.

::: xdripitem Consentire il permesso
&emsp;xDrip+ ha bisogno di essere autorizzato in background per funzionare correttamente  

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;Ok&ensp;</span>
:::

<img src="./images/AllowRunInBackground.png" style="zoom:75%;" />

*Nota: da Android 12 in poi non vedrai più la parola **whitelisting** (lista bianca).*

Maggiori informazioni [qui](../troubleshoot/savings#apps-battery-savings).

<br>

### Autorizzare le notifiche {#authorize-notifications}

xDrip deve accedere alle notifiche del telefono per funzionare come previsto.

<img src="./images/Install47.png" style="zoom:75%;" />

<br>

## Verificare quale versione è installata {#verify-which-version-is-installed}

Tocca il tasto indietro del telefono finché non torni alla schermata principale. Seleziona il menu hamburger in alto a sinistra, poi `Stato del sistema`.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;  Stato del sistema
:::

La versione attuale è indicata dopo `Versione`. Nell'esempio qui sotto, 28 gennaio 2022.

<img src="../images/M-SS-Ver.png" style="zoom:75%;" />

Nelle versioni più recenti la trovi in tutte le pagine dello stato del sistema.

<img src="../images/M-SS-Ver2.png" style="zoom:76%;" />

Vedi [qui](../use/update) per aggiornare o tornare a una versione precedente.

<br>

## Assicurarsi che xDrip non venga messo in sospensione {#make-sure-xdrip-will-not-be-put-to-sleep}

Queste sono le impostazioni predefinite, ma assicurati comunque che siano esattamente come mostrato qui sotto. Ogni volta che il telefono si aggiorna, torna a controllarle: disattiva e riattiva le caselle che devono essere attive per forzare le impostazioni.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Impostazioni Meno Usate  
&ensp;&emsp;Altre opzioni  
&ensp;&emsp;&emsp;Eseguire Collector in primo piano
:::

Da quando il supporto di Android 7 è stato ritirato ([12 luglio 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.12)), il collector funziona sempre in primo piano su Android 8.0 e superiori: non c'è più un interruttore per questa opzione. Il grafico della notifica persistente nella tendina del telefono è essenziale per mantenere attiva l'app ed è sempre visualizzato.

::: xdripitem Notifica Persistente Compatta <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Abilita per nascondere il grafico nelle notifiche e visualizzare solo il valore attuale di glucosio.
:::

Se preferisci non mostrare il grafico nella notifica persistente, attiva `Notifica Persistente Compatta` per mostrare solo il valore attuale di glucosio.

::: xdripitem Richiesta di Ottimizzazione della Batteria <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Con Android 6+ verifica che l'ottimizzazione della batteria sia spenta. Raccomandato
:::

`Richiesta di Ottimizzazione della Batteria` deve essere **disattivata**, perché durante l'installazione dovresti aver accettato l'[esclusione dall'ottimizzazione della batteria](#authorize-background-activity). In caso contrario, escludi xDrip dall'ottimizzazione della batteria nelle impostazioni di Android.

::: xdripitem Samsung Workaround <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Usa workaround per evitare il comportamento non standard a Android degli telefonini Samsung. Senza questo, di solito non si riesce a ricevere dati.
:::

In origine "Samsung workaround", questa opzione corregge il mancato rispetto delle specifiche Android da parte di alcuni produttori. Con alcuni smartphone si attiva automaticamente. Consigliata.

### Attivare la localizzazione {#enable-location}

Nelle versioni più recenti di Android (dalla 6 in poi), la localizzazione è [obbligatoria](https://developer.android.com/training/location/permissions) per consentire la connessione Bluetooth Low Energy.  
Se userai xDrip con un sensore o un bridge Bluetooth, **devi** attivare la localizzazione (Impostazioni Android -> [Posizione](https://support.google.com/android/answer/3467281)) e autorizzare xDrip ad accedervi. Consulta il manuale del telefono, perché dipende dalla versione di Android e dal produttore.

Assicurati di selezionare Consenti sempre nelle impostazioni.

<img src="./images/Install17a.png" style="zoom:75%;" />

<img src="./images/Install17.png" style="zoom:75%;" />

<br>

Passa alla [selezione della sorgente dati](./datasource)

<br>

[*Ultima modifica 18/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.15)
