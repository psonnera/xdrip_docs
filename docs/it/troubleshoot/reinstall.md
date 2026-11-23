---
source_hash: 59290c3e55
source_commit: 7a18e7c
---
## Disinstallare xDrip {#uninstall-xdrip}

::: warning Dati storici
Disinstallare xDrip rimuove anche tutti i dati e le impostazioni, senza possibilità di recupero.  
Assicurati di fare prima un **[backup](#backup)** del database e/o di tutte le impostazioni.  
Si consiglia di caricare i dati su [Nightscout](https://nightscout.github.io/).
:::

<br>

Di solito non dovrebbe essere necessario, ma potresti dover disinstallare xDrip per risolvere un problema, o per passare a o da una versione fork. Puoi disinstallare xDrip come qualsiasi altra app Android, con una pressione prolungata sull'icona oppure da Impostazioni Android -> App.

## Reinstallare xDrip {#reinstall-xdrip}

Segui questa sequenza:

1. Backup (in locale o nel cloud)
2. Disinstalla xDrip
3. Installa xDrip
4. Ripristino (dal backup locale o nel cloud)
5. Controlla tutte le impostazioni e ricrea i tuoi allarmi

## Backup {#backup}

Puoi fare il backup del database in locale oppure sul tuo [Google Drive](#cloud-backup).

### Backup del database {#backup-the-database}

Il database contiene tutte le letture di glicemia, i trattamenti e le note. È vivamente consigliato fare il backup del database e conservarne una copia su un altro dispositivo se vuoi tenere i dati esistenti, e come precauzione in caso di perdita del telefono, guasto, ...  
È vivamente consigliato anche il caricamento su [Nightscout](https://nightscout.github.io/).

Esportare il database [salva anche le impostazioni](../use/loadsavesettings#save-settings).

Dalla schermata principale di xDrip seleziona il menu a 3 puntini in alto a destra, Funzioni di importazione / esportazione, Esporta Database.

::: xdrip <img src="../images/3dots_menu.png" style="zoom:75%;" />
&ensp;Funzioni di importazione / esportazione ►  
&emsp;Esporta Database
:::

<br>

Il database attuale viene salvato in `/storage/emulated/0/xdrip` o `Memoria interna/xdrip`
Devi autorizzare xDrip ad accedere alla memoria del telefono.  
Puoi fare tutti i backup che la memoria può contenere.

Se sei abbastanza veloce da toccare la scritta `SHARE` prima che scompaia, puoi usare le opzioni di condivisione del telefono per inviare il database a un altro dispositivo o copiarlo in un'altra posizione.

<img src="./images/3DM-IE-ExpDB.png" style="zoom:75%;" />

Il backup si chiamerà `exportYYYYMMDD-HHMMSS.zip`, con `YYYY` l'anno corrente, `MM` il mese, `DD` il giorno e `HHMMSS` per ore, minuti e secondi. Così puoi avere più backup, ciascuno identificato da un orario univoco.

Se vuoi conservarne una copia sicura, invia il file a te stesso per email, salvalo su un cloud o copialo via USB su un computer.

È un database SQLite che puoi consultare con diversi strumenti, come [SQLite Browser](https://sqlitebrowser.org/).

<br>

## Ripristino {#restore}

Puoi ripristinare il database da una copia locale oppure dal tuo [Google Drive](#cloud-backup).

### Ripristinare le impostazioni {#restore-settings}

Al termine dell'installazione di xDrip, se è disponibile un backup, xDrip ti proporrà di ripristinarlo automaticamente.   
Seleziona RIPRISTINARE LE IMPOSTAZIONI

::: xdripitem Backup rilevato
&emsp;Sembra che tu abbia un backup delle impostazioni, vuoi provare a ripristinarlo?  


&emsp;NO&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;RIPRISTINARE LE IMPOSTAZIONI&ensp;</span>
:::

Se non vedi questo messaggio, [ripristinale manualmente](../use/loadsavesettings#load-settings).

### Ripristinare un database {#restore-a-database}

::: warning Perdita di dati
Ripristinare un database **elimina tutti i dati attuali**.  
Ripristina un database con **la stessa versione di xDrip usata per esportarlo**.  
Assicurati di fare il backup del database attuale prima di ripristinarne uno. 
:::

Al termine dell'installazione di xDrip, se è disponibile un backup del database, xDrip potrebbe proporti di ripristinarlo automaticamente.

Assicurati che sia il database che vuoi ripristinare, poi seleziona RIPRISTINA.

::: xdripitem Ripristinare il backup?
&emsp;Ripristinare il file di backup:  
&emsp;file:export20210328-085436.zip  


&emsp;NO&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;RIPRISTINA&ensp;</span>
:::

xDrip confermerà che il database è stato ripristinato correttamente.

::: xdripitem Import result
&emsp;Successfully imported database.
:::

*Nota: per sicurezza, il database attuale viene prima esportato; lo troverai nell'elenco con il nome `b4import` seguito dalla data e ora dell'importazione. Così potrai recuperarlo se necessario.*

<br>

Se vuoi ripristinare un backup specifico, dalla schermata principale di xDrip seleziona il menu a 3 puntini in alto a destra, Funzioni di importazione / esportazione, Ripristina database.

::: xdrip <img src="../images/3dots_menu.png" style="zoom:75%;" />
&ensp;Funzioni di importazione / esportazione ►  
&emsp;Ripristina database
:::

Vengono mostrate le istruzioni. Non devi spostare il file di backup se non l'hai trasferito da un altro dispositivo, e non devi decomprimerlo. Fai attenzione quando ripristini un database con una versione di xDrip diversa: si consiglia di installare la [versione di xDrip](../install/install#verify-which-version-is-installed) usata per l'esportazione prima di importare, poi potrai aggiornare xDrip.

::: xdripitem Restore Instructions
&emsp;WARNING: Database restore is rarely necessary and may cause SEVERE DATA LOSS.

Protect your data by uploading to Nightscout or Tidepool.

When switching phones, importing settings (alerts, colors, etc.) is usually sufficient. Restoring the database is typically unnecessary unless you need short-term access to historical data (for example, before a medical visit).

Instructions:

\- Place the database in the 'xdrip' folder. If it doesn't exist, perform an export once to create it.

\- Restart this restore routine.

\- Select the correct database and follow the on-screen instructions.
:::

Seleziona il database che vuoi importare; guarda la data e la dimensione (usa il file manager del telefono) per essere sicuro di scegliere quello giusto.

::: xdrip <img src="../images/BDM.png" style="zoom:75%;" />Ripristina database
export20220129-184625.zip  
export20220129-184615.zip  
b4import20220129-194141.zip
:::

Quando sei sicuro di ripristinare il backup corretto, `Ok`

::: xdripitem Confirm Import
&emsp;Do you want to import  
&emsp;'export20220129-184615.zip'?  
&emsp;This might negatively affect the data integrity of your system!  

&emsp;ANNULLA&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;OK&ensp;</span>
:::

xDrip confermerà che il database è stato ripristinato correttamente.

::: xdripitem Import result
&emsp;Successfully imported database.
:::

Se hai ripristinato il database sbagliato, ripeti semplicemente gli stessi passaggi e seleziona la versione `b4import` più recente per tornare indietro.

::: info Android 11 e successivi
C'è un problema con le versioni recenti di Android che ti costringe a ripristinare il database più volte (da 3 a 4) prima di vederne il contenuto completo.
:::

<br>

## Backup nel cloud {#cloud-backup}

Il backup nel cloud ti permette di salvare sul tuo Google Drive un file compresso che contiene sia il database sia le impostazioni.  
Per usare questa funzione devi aver effettuato l'accesso al tuo account Google.

Seleziona Backup nel Cloud.

::: xdrip <img src="../images/3dots_menu.png" style="zoom:75%;" />
&ensp;Funzioni di importazione / esportazione ►  
&emsp;Backup nel Cloud
:::

::: xdripitem Backup nel Cloud
&emsp;&emsp;Puoi utilizzare Google Drive per il backup  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Pronto
:::

Per usare questa funzione devi prima selezionare una posizione di backup.

### Selezionare la posizione di backup {#select-backup-location}

::: xdrip <span style="background-color: white; color: black;">&ensp;Seleziona dove salvare il Backup&ensp;</span>
:::

::: xdripitem Scegli il file di backup
&emsp;&emsp;Selezionare Automatico per permettere a xDrip di gestire i file nel Google Drive o selezionare un file alternativo per ripristinare da altrove.  

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;GESTISCI AUTOMATICAMENTE&ensp;</span>  

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;USA FILE ALTERNATIVO&ensp;</span>
:::

- Usa File Alternativo ti permette di selezionare una cartella e un file di backup diversi durante il **ripristino**. 
- Quando fai il **primo backup**, o quando recuperi **una reinstallazione di xDrip** sullo stesso telefono, seleziona Gestisci Automaticamente.

Devi autorizzare xDrip ad accedere al tuo account Google. xDrip salverà e recupererà solo il file di backup dal tuo Google Drive. **Nient'altro.**

<img src="./images/3DM-BR-CB3.png" style="zoom:75%;" />

Al termine, xDrip confermerà l'accesso:

<img src="./images/3DM-BR-CB4.png" style="zoom:75%;" />

xDrip creerà una nuova cartella chiamata xDrip-Backups nella radice del tuo Google Drive.

<img src="./images/3DM-BR-CB6.png" style="zoom:75%;" />

### Eseguire ora il backup {#do-backup-now}

Una volta selezionata la posizione di backup, puoi eseguire un backup. Il file di backup verrà creato sul dispositivo e poi caricato sul tuo Google Drive.

::: xdrip <span style="background-color: white; color: black;">&ensp;Esegui ora il backup&ensp;</span>
:::

<img src="./images/3DM-BR-CB5.png" style="zoom:75%;" />

Puoi controllare lo stato del backup nel cloud nella parte alta della schermata.

<img src="./images/3DM-BR-CB7.png" style="zoom:75%;" />

Puoi far eseguire il backup nel cloud automaticamente ogni giorno.  
Non attivarlo se hai un piano dati mobile limitato.

::: xdripitem <img src="../images/DIS.png" style="zoom:75%;" />&emsp;Backup automatico giornaliero
:::

### Ripristinare dal backup {#restore-from-backup}

::: xdrip <span style="background-color: white; color: black;">&ensp;Ripristino da Backup&ensp;</span>
:::

::: warning Perdita di dati
Ripristinare un database elimina tutti i dati attuali.  
Ripristina un database con **la stessa versione di xDrip usata per esportarlo**.  
Assicurati di fare il backup del database attuale prima di ripristinarne uno.
:::

::: xdripitem Sei davvero sicuro?
&emsp;Il ripristino di un backup cancellerà le impostazioni e i dati correnti con quello dal backup.  

&emsp;Sei assolutamente sicuro di voler fare questo?  

&emsp;NO&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;SI&ensp;</span>
:::

Il ripristino copia in locale il database dal cloud e sostituisce il database attuale.

Al termine, xDrip si riavvierà.

<br>

## Migrazione a un nuovo telefono {#new-phone-migration}

Esegui le operazioni seguenti:

Sul vecchio telefono:

1. [Fai il backup del database in locale](#backup-the-database) o sul tuo [Google Drive](#do-backup-now).
   - Se non userai il backup su Google cloud, invia a te stesso il backup del database o copialo su un computer.

2. Se questo vecchio telefono è collegato a un sensore o a un bridge, assicurati di [disattivare la raccolta dati](../install/datasource#changing-data-source), così non interferirà quando inizierai a usare il nuovo telefono.
3. Se questo vecchio telefono era master per dei follower xDrip Sync, [togli il ruolo di master](../use/sync#be-master-for-followers).

Sul nuovo telefono:

1. [Installa](../install/download#which-one-to-install) la [stessa versione](../install/install#verify-which-version-is-installed) di xDrip che usi sul vecchio telefono.
   - Se non hai usato il backup su Google cloud:  
     [Fai il backup del database](#backup-the-database) (serve solo a creare le cartelle corrette).  
     Copia nella cartella giusta il file del database che ti sei inviato per mail o da un computer.

2. [Ripristina il database dal backup locale](#restore-a-database) o dal tuo [Google Drive](#restore-from-backup).  
3. Se il nuovo telefono è collegato a un sensore o a un bridge, [collegalo ora](../install/datasource#sensor-selection). (La sorgente dati sarà corretta, ma dovrai ripristinare la connessione).

<br>

[*Ultima modifica 8/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
