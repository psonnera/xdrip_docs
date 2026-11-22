---
source_hash: 932cfecc51
source_commit: 298bb92
---
## Quale installare? {#which-one-to-install}

xDrip non è disponibile sul Google Play Store. Trovi tutte le release su [Github](https://github.com/NightscoutFoundation/xDrip/releases).  
Per installare xDrip hai due scelte principali: l'**ultima release** (Latest release) o una **Pre-release**.

::: info Nota
Se hai già xDrip installato sul telefono, non devi disinstallarlo prima di installare un aggiornamento.  
Se usi una versione fork e vuoi passare a una release ufficiale di xDrip, o viceversa, segui [questa procedura](../troubleshoot/reinstall).
:::

::: info Più installazioni di xDrip
Se devi installare più di un xDrip sullo stesso telefono, ti serve una [variante](#variants).
:::

### Ultima release {#latest-release}

L'ultima release (Latest release) è una versione stabile di xDrip. Non ha tutte le funzioni più recenti, ma ha una stabilità comprovata e non soffre di bug gravi. È una versione sicura con cui iniziare, a meno che non ti serva una funzione specifica (controlla il [changelog](../changelog)).

Puoi scaricarla da [qui](https://xdrip-plus-updates.appspot.com/stable/xdrip-plus-latest.apk) o con questo codice QR:

<img src="https://jamorham.github.io/images/download-xdrip-plus-qr-code-120.png" />

La trovi anche nel [repository principale](https://github.com/NightscoutFoundation/xDrip) selezionando Latest.

<img src="./images/GitHubReleaseLatest.png" style="zoom:50%;" />

<br>

#### Avviso al download {#download-warning}

xDrip scaricato da [https://github.com/NightscoutFoundation/xDrip/releases](https://github.com/NightscoutFoundation/xDrip/releases) è sicuro.

<img src="./images/Install46.png" style="zoom:75%;" />

<br>

Una volta scaricato, [passa all'installazione di xDrip](./install)

<br>

### Pre-release {#pre-release}

Le pre-release includono gli sviluppi più recenti di xDrip, come traduzioni, nuove funzioni e correzioni di bug. E potrebbero anche contenere qualche bug... Resta comunque la versione da usare per beneficiare dei miglioramenti più recenti.

Tutte le versioni di xDrip sono disponibili [qui](https://github.com/NightscoutFoundation/xDrip/releases).

Espandi gli asset (Assets) e seleziona il file `.apk`. Lo troverai nella cartella `Downloads` del telefono.

<img src="./images/GitHubReleaseAssets.png" style="zoom:50%;" />

::: info Nota
**Non** usare i link di Facebook per scaricare xDrip, ma **copia e incolla il link** in un browser (come Chrome).
:::

<br>

#### Avviso al download {#download-warning-1}

xDrip scaricato da [https://github.com/NightscoutFoundation/xDrip/releases](https://github.com/NightscoutFoundation/xDrip/releases) è sicuro.

<img src="./images/Install46.png" style="zoom:75%;" />

<br>

Una volta scaricato, [passa all'installazione di xDrip](./install)

<br>

## Versioni fork {#forked-versions}

Alcuni sviluppatori aggiungono funzioni e personalizzazioni che non sono disponibili nelle pre-release ufficiali, finché l'autore non crea una Pull Request in xDrip e questa viene integrata nel progetto principale.

::: warning Aggiornare le versioni fork
Puoi usare queste versioni, ma devi sapere che potrebbero essere supportate solo dal loro autore.  
**Gli aggiornamenti automatici di xDrip non funzionano con le versioni fork.**  
Tieni anche presente che non puoi installare una versione fork se sul telefono hai installata una versione ufficiale:  
dovrai prima [disinstallarla](../troubleshoot/reinstall).  
Lo stesso vale nel senso opposto (da fork a ufficiale).
:::

<br>

## Varianti {#variants}

Vengono rilasciate regolarmente quattro varianti, che permettono di installare fino a 5 xDrip sul telefono. Può essere particolarmente utile per seguire più persone contemporaneamente.

::: warning Attenzione
È sconsigliato usare una variante collegata al tuo sensore: usa solo la release principale.  
Usa le varianti solo come follower.  
Alcune prime versioni di xDrip perdevano valori quando si usava AAPS/NSClient. Usa le varianti più recenti.
:::

Puoi scaricare le varianti [qui](https://drive.google.com/drive/folders/0B6mvYVNVC-fOWkxnVF80dlFabjQ?resourcekey=0-ebguuiPuB1wUI9Rp2zjMNg).

Ordinale per ultima modifica e scegli la variante da scaricare.

<img src="./images/Variant.png" style="zoom:90%;" />

Le varianti sono incluse anche come asset accanto all'apk normale nell'ultima release su [GitHub](https://github.com/NightscoutFoundation/xDrip/releases).

<img src="./images/GitHubReleaseLatest.png" style="zoom:50%;" />

Una volta scaricata una variante, procedi come per una normale installazione di xDrip.

**Le varianti non si aggiornano automaticamente.** Devi scaricare e installare gli aggiornamenti sopra la versione attuale della variante (non serve disinstallarla): assicurati solo di selezionare la stessa variante (da 1 a 4).

<br>

[*Ultima modifica 3/2/2023*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2023.02.26)
