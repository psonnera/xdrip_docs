---
source_hash: 874eaebd13
source_commit: 7a18e7c
---
Puoi aggiornare xDrip installando un'altra versione sopra quella attuale senza disinstallarla, nello stesso modo in cui l'hai [installato](../install/download) la prima volta.

Puoi anche usare il meccanismo di aggiornamento interno di xDrip.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_briefcase_download_grey600_48dp.png" style="width:5%;" />&ensp;xDrip+ Impostazioni di aggiornamento
:::

Le impostazioni di aggiornamento ti permettono di scegliere quali versioni di xDrip ti vengono proposte come aggiornamenti.

::: warning NON DISINSTALLARE xDRIP+
Puoi passare a una versione più recente o più vecchia di xDrip semplicemente installandola sopra quella attuale.  
Disinstallare xDrip può causare una perdita di dati completa e irrecuperabile se non hai fatto un [backup](../troubleshoot/reinstall#reinstall-xdrip).
:::

Solo le versioni ufficiali di xDrip possono usare questa funzione.  
Se hai installato una [versione fork](../install/download#forked-versions), solo il suo autore può fornire gli aggiornamenti. 

::: info Nota
L'aggiornamento di xDrip è del tutto trasparente e non richiede alcuna azione particolare sul sensore in uso.  
Le tue impostazioni verranno mantenute, a meno che un'impostazione specifica non abbia subito una modifica importante.  
Per precauzione è meglio tenere d'occhio xDrip se hai selezionato una release alpha o nightly.
:::

Dovresti attivare il controllo automatico degli aggiornamenti.

::: xdripitem Controllo Aggiornamento automatico <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Ricevi un avviso di nuove uscite app  
:::

Se lo lasci disattivato, xDrip ti ricorderà di aggiornare ogni 60 giorni.

::: xdripitem Raga...
&ensp;Hai il controllo di aggiornamenti disattivato!  
&ensp;Stiamo cercando di correggere i bug e di aggiungere nuove funzionalità a xDrip+.  
&ensp;Ogni 60 giorni questo promemoria ti chiederà di attivare il controllo degli aggiornamenti.  
:::

Ci sono tre canali di aggiornamento:

- Stable: versioni rilasciate che hanno dimostrato stabilità e affidabilità
- Beta: versioni candidate a diventare release stabili
- Alpha: versioni in sviluppo

Un quarto compare solo dopo aver selezionato Alpha (vedi [sotto](#getting-the-nightlies-on-automatic-update)):

- Nightly: prototipi per i test

Le versioni più testate non includono le funzioni e le correzioni più recenti.

Le versioni meno testate possono contenere bug, ma includono anche le funzioni e le correzioni più recenti.

::: xdripitem Aggiorna Canale
&ensp;Scegli Trasmissione Stable, Beta o Alpha
:::

::: xdripitem Aggiorna Canale
&ensp;Stable - tried and tested versions  
&ensp;Beta - new features but not fully tested  
&ensp;Alpha - versions for early testing  
&ensp;Nightly - untested raw code - experts only!
:::

### Ricevere le nightly con l'aggiornamento automatico {#getting-the-nightlies-on-automatic-update}

Il canale Nightly è nascosto finché non hai selezionato Alpha almeno una volta.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_briefcase_download_grey600_48dp.png" style="width:5%;" />&ensp;xDrip+ Impostazioni di aggiornamento  
&ensp;&emsp;Aggiorna Canale
:::

1. Apri Aggiorna Canale. Se Nightly è nell'elenco, selezionalo e hai finito.
2. Se Nightly non è nell'elenco, seleziona Alpha, torna alla schermata principale di xDrip, poi apri di nuovo xDrip+ Impostazioni di aggiornamento e Aggiorna Canale. Ora Nightly è visibile: selezionalo.

::: warning Nightly è il canale meno testato
Le build Nightly contengono il codice più recente e meno testato. Sono le prime a ricevere le nuove funzioni, ma anche quelle in cui di solito emergono i bug. Tieni d'occhio xDrip dopo ogni aggiornamento e sii pronto a [tornare indietro](#downgrade) installando sopra una release più vecchia.
:::

I controlli degli aggiornamenti avvengono circa ogni 24 ore. Per controllare subito, usa [Verifica versione aggiornata](./3dotsmenu#check-for-updated-version) nel menu a 3 puntini.

Nel [repository ufficiale](https://github.com/NightscoutFoundation/xDrip/releases) puoi riconoscere l'ultima release dall'etichetta Latest.    
Puoi scaricare l'ultima release [qui](https://xdrip-plus-updates.appspot.com/stable/xdrip-plus-latest.apk).  
Tutte le altre hanno l'etichetta Pre-release.

<img src="./images/M-S-US2b.png" style="zoom:75%;" />

Le funzioni di segnalazione non sono più usate. Se hai bisogno di supporto usa le [discussioni](https://github.com/NightscoutFoundation/xDrip/discussions) o [Facebook](https://www.facebook.com/groups/xDripG5).

::: xdripitem Segnalazione automatica Crash
:::

::: xdripitem Attiva telemetria
:::

Il feedback non è più usato. Usalo solo per i complimenti.

::: xdripitem Invia Feedback
:::

### Aggiornamento {#update}

Puoi aggiornare xDrip installando un'altra versione sopra quella attuale senza disinstallarla, nello stesso modo in cui l'hai [installato](../install/download) la prima volta.

Puoi anche usare il meccanismo di aggiornamento interno di xDrip.

Le notifiche di aggiornamento disponibile scattano in base al canale selezionato.  
Se hai disattivato il controllo automatico degli aggiornamenti, puoi richiedere un controllo manuale dal [menu a 3 puntini](./3dotsmenu#check-for-updated-version).

1. Viene mostrato il canale di aggiornamento attuale
2. Versione attuale e versione più recente (disponibile)
3. Scaricalo ora! avvia il download dell'aggiornamento; al termine del download Android ti chiederà l'autorizzazione all'installazione.
4. Puoi disattivare gli aggiornamenti automatici. Ha lo stesso effetto del pulsante di controllo automatico degli aggiornamenti visto sopra.
5. Se non usi il downloader interno, il dispositivo userà l'app predefinita per scaricare i file da internet.
6. Esci senza fare nulla.

<img src="./images/M-S-US5.png" style="zoom:75%;" />

Se selezioni il downloader interno vedrai una barra di avanzamento e, al termine, l'installazione partirà automaticamente.

<img src="./images/M-S-US6.png" style="zoom:75%;" />

Se non hai selezionato il downloader interno, il telefono scaricherà il pacchetto da [GitHub](https://github.com/NightscoutFoundation/xDrip/releases) e avvierà l'installazione al termine.

Non dovrebbero servire nuove autorizzazioni.

 <img src="./images/M-S-US6a.png" style="zoom:75%;" />

Dopo l'aggiornamento puoi verificare la versione attuale in [Stato del sistema](../troubleshoot/systemstatus).

### Tornare a una versione precedente {#downgrade}

Non serve disinstallare xDrip per tornare a una versione più vecchia (a meno che tu non stia [passando dalla versione ufficiale a una fork](../troubleshoot/reinstall) o viceversa): installa semplicemente la versione che vuoi sopra quella attuale, [come hai fatto alla prima installazione](../install/download).

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
