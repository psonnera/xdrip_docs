---
source_hash: 47eb878cea
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_watch_grey600_48dp.png" style="width:5%;" />&ensp;Caratteristiche Collegamenti Smart Watch  
&emsp;  MiBand
:::

La release ufficiale di xDrip supporta MiBand 2, 3, 4 e la trasmissione a [WatchDrip+](https://bigdigital.home.blog/2022/06/16/watchdrip-a-new-application-for-xdrip-watch-integration) per le altre smartband.

::: info Prerequisito
Assicurati di avere le letture della glicemia in xDrip prima di provare a vederle sull'orologio.  
Se xDrip non riceve le letture sul telefono, non verranno mostrate sull'orologio.
:::

## Installazione {#install}

### Ottenere una chiave di autenticazione {#obtain-an-authentication-key}

#### Se hai già associato l'orologio all'app del produttore {#if-you-already-paired-your-watch-with-the-vendor-app}

- Dissocia l'orologio.
- Disinstalla MiFit o Zepp, o qualunque app tu abbia usato per collegare l'orologio.

- **Elimina i vecchi file della chiave** (usa un file manager sul telefono) nella cartella `freemyband` della memoria del telefono.  
  Consigliato se non riesci a far collegare xDrip all'orologio.  
  *Nota: il nome qui sotto è un esempio*

<img src="./images/MiBand1.png" style="zoom:75%;" />

#### Installa l'app modificata adatta al tuo orologio {#install-the-patched-app-matching-your-watch}

Vai su [https://www.freemyband.com/](https://www.freemyband.com/)

Scarica e installa [Zepp](https://www.freemyband.com/2019/08/amazfit-gtr-auth-key.html) per gli orologi Amazfit.  
(oppure)  
Scarica e installa [MiFit](https://www.freemyband.com/2019/08/mi-band-4-auth-key.html) per le smartband Xiaomi.

Accedi con email e password. Crea un account se necessario.

Associa la smartband.

Attiva la visibilità dell'orologio. Se non trovi questa opzione, verifica di aver impostato un'età di almeno 18 anni.

Controlla che sia stato creato un file della chiave nella cartella `freemyband` della memoria del telefono.

Puoi disinstallare l'app modificata, ma non è obbligatorio. Se vuoi installare l'app originale, accedi con lo stesso account email.

## Senza WatchDrip+ {#not-using-watchdrip}

::: info Solo MiBand 2, 3 e 4
:::

### Configurare xDrip {#setup-xdrip}

Attiva la funzione MiBand. Tieni l'orologio vicino al telefono finché non viene rilevato.

::: xdripitem Usa MiBand <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

<img src="./images/M-S-SW-MB-I1.png" style="zoom:80%;" />

L'indirizzo MAC dovrebbe compilarsi automaticamente.

::: xdripitem Indirizzo MAC (FF:EE:DD:CC:BB:AA)
&ensp;Lascia vuoto per la ricerca automatica
:::

**Se non succede** (caso anomalo)**:**   
Elimina i file nella cartella `freemyband`.  
Apri l'app modificata dell'orologio.  
Riprova: disattiva e riattiva la funzione MiBand.

Puoi anche provare a inserire manualmente l'indirizzo MAC dell'orologio. Lo trovi nel nome del file nella cartella `freemyband`.  
Ad esempio, se il nome è `mibandFFEEDDCCBBAA.txt`, l'indirizzo MAC corrispondente sarà `FF:EE:DD:CC:BB:AA`.

<img src="./images/M-S-SW-MB-I2.png" style="zoom:75%;" />

Tieni d'occhio i messaggi a comparsa: durante l'autenticazione dello smartwatch dovresti vedere quanto segue:

<img src="./images/M-S-SW-MB-I3.png" style="zoom:75%;" />

Se l'autorizzazione non riesce, elimina i file nella cartella `freemyband` e apri l'app modificata per rigenerarli.

<img src="./images/M-S-SW-MB-I4.png" style="zoom:75%;" />

Se xDrip non riesce a ottenere automaticamente la chiave di autenticazione, puoi provare a inserirla manualmente. La trovi aprendo il file in modifica.

<img src="./images/M-S-SW-MB-I5.png" style="zoom:75%;" />

Prima di inserire la chiave manualmente, assicurati che l'orologio sia collegato e corrisponda all'indirizzo MAC.

::: xdripitem Chiave di autenticazione
&ensp;Imposta la chiave di autenticazione per MiBand4 (Per ottenere la chiave di autenticazione, segui le istruzioni su [https://www.freemyband.com](https://www.freemyband.com/2019/08/mi-band-4-auth-key.html))
:::

Una volta collegato e autenticato l'orologio, attiva Invia Letture. Aspetta il valore successivo in xDrip: il quadrante dovrebbe aggiornarsi.

::: xdripitem Invia Letture <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Data dell'orologio aggiustata per visualizzare i valori di glicemia. Meglio mmol/l - consultare la documentazione 
:::

Per forzare l'aggiornamento dell'orologio, puoi inviare una lettura manualmente. Osserva bene i messaggi a comparsa.

::: xdripitem Aggiorna la glicemia manualmente
:::

Se hai problemi a visualizzare il grafico, prova a disattivare i valori MTU elevati.

::: xdripitem Disable high MTU values <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

### Funzioni {#features}

::: xdripitem Usa MiBand <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Sincronizza i dati con fitness band MiBand
:::

Puoi attivare e disattivare l'integrazione MiBand con l'interruttore principale. Durante la risoluzione dei problemi non esitare a spegnerlo e riaccenderlo per riavviarla.

::: xdripitem Indirizzo MAC
&ensp;Lascia vuoto per la ricerca automatica
:::

L'indirizzo MAC dell'orologio dovrebbe essere rilevato automaticamente quando il campo è lasciato vuoto. Puoi modificarlo manualmente e scrivere i 6 valori esadecimali a due cifre del tuo orologio, separati da due punti.

::: xdripitem Chiave di autenticazione
&ensp;Imposta la chiave di autenticazione per MiBand4 (Per ottenere la chiave di autenticazione, segui le istruzioni su [https://www.freemyband.com](https://www.freemyband.com/2019/08/mi-band-4-auth-key.html))
:::

Quando viene trovato un indirizzo MAC valido, vedrai anche il campo della chiave. Se non viene compilato automaticamente, puoi inserire manualmente la chiave di autenticazione di 32 caratteri.

::: xdripitem Invia Letture <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Data dell'orologio aggiustata per visualizzare i valori di glicemia. Meglio mmol/l - consultare la documentazione 
:::

Devi attivare questa opzione perché le letture vengano inviate all'orologio.

::: xdripitem Vibra alle letture <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Invia Allarmi <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Invia le notifiche per gli allarmi di glicemia alla Band
:::

::: xdripitem Invia Chiamate <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Invia notifiche di chiamata alla band (Android 6+)
:::

Puoi attivare varie opzioni per far vibrare l'orologio a ogni lettura, ricevere gli allarmi o ricevere le notifiche come chiamate telefoniche.

::: xdripitem Aggiorna la glicemia manualmente
:::

Puoi forzare l'aggiornamento del quadrante con Aggiorna la glicemia manualmente.

::: xdripitem Schermate MiBand / Caratteristiche
:::

In questo menu sono disponibili altre personalizzazioni.

::: xdripitem Allow to use custom watchface <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

Con queste funzioni puoi creare il tuo quadrante e modificare l'immagine di sfondo.  
Lasciale disattivate a meno che tu non abbia preparato correttamente i file necessari nella cartella xdrip del telefono.

Per consigli ed esempi guarda [qui](https://github.com/twinko).

::: xdripitem Disable high MTU values <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

Disable high MTU values (disattiva i valori MTU elevati) può essere usato in caso di problemi di visualizzazione del quadrante.

## Con WatchDrip+ {#using-watchdrip}

### Installa [WatchDrip+](https://bigdigital.home.blog/2022/06/16/watchdrip-a-new-application-for-xdrip-watch-integration/) {#install-watchdrip}

:::: info Disattiva MiBand in xDrip se usi WatchDrip+
::: xdripitem Usa MiBand <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::
::::

### Configurare xDrip {#setup-xdrip-1}

Attiva Servizio di Trasmissione API in Impostazioni -> Impostazioni Inter-app

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_open_in_app_grey600_48dp.png" style="width:5%;" />&ensp;Impostazioni Inter-app
:::

::: xdripitem Servizio di Trasmissione API <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Abilita la comunicazione tra xDrip e applicazioni terze parti utilizzando la nuova API
:::

<br>

[*Ultima modifica 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
