---
source_hash: 29d4533605
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;CareLink Follower
:::

<br>

::: warning Attenzione
I server CareLink sono soggetti a frequenti modifiche che possono rendere inutilizzabile la funzione.  
**In caso di problemi usa l'[ultima pre-release](./download#pre-release).**  
Valuta di usare [Companion App](./companion) sul telefono master e xDrip [Sync](./xdripfollower) o Nightscout per condividere i dati.  
L'autenticazione dell'app CarePartner è valida per 1 settimana: anche se xDrip non riesce a collegarsi a CareLink per qualche giorno (ad esempio per mancanza di connessione a internet), potrà rinnovare l'accesso (aggiornare il token) automaticamente in background quando riesce di nuovo a collegarsi a CareLink, senza dover accedere di nuovo manualmente con il browser. Anche a questo processo di autenticazione si applica la restrizione sull'account utente:   
**per xDrip va usato un account follower dedicato: non puoi usare lo stesso follower per altre app o altri telefoni.**
:::

<br>

Funziona anche con un CGM Simplera autonomo (usato senza un microinfusore collegato) che carica i dati su CareLink.

Seleziona il paese in cui hai registrato il tuo utente CareLink.

::: xdripitem Paese CareLink
&ensp;Seleziona il tuo paese CareLink.
:::

Imposta il nome utente del paziente se usi un account care partner con più pazienti.

::: xdripitem Nome Utente Paziente CareLink
&ensp;Nome utente paziente CareLink (opzionale)
:::

xDrip aprirà il sito di autenticazione CareLink: inserisci le tue credenziali per accedere.  

::: xdripitem Login
&ensp;Accedi con il browser
:::

Il periodo di grazia è un tempo di attesa aggiuntivo dopo la ricezione dell'ultima lettura + 5 minuti.  
Serve a evitare il blocco da parte del server se xDrip invia richieste troppo frequenti.

::: xdripitem Periodo di grazia
&ensp;Periodo di tolleranza per la richiesta di dati in secondi
:::

L'intervallo di richiesta dei dati mancanti è un tempo di attesa aggiuntivo dopo la ricezione dell'ultima lettura + 5 minuti + periodo di grazia.  
Serve a evitare il blocco da parte del server se xDrip invia richieste troppo frequenti.

::: xdripitem Intervallo richiesta dati mancanti
&ensp;Intervallo di richieste dopo dati mancanti, in minuti
:::

<br>

#### Trattamenti {#treatments}

Puoi scaricare i trattamenti e ricevere le notifiche.

::: xdripitem Glicemia capillare <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Scarica misure capillare da CareLink  
:::

::: xdripitem Boli <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Scarica boli da CareLink
:::

::: xdripitem Pasti <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Scarica pasti da CareLink
:::

::: xdripitem Notifiche <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Scarica le notifiche da CareLink
:::

<br>

#### Riga di stato {#status-line}

Lo stato del sensore e lo stato del microinfusore possono essere attivati nell'opzione [Riga di stato extra](../use/lesscommon#extra-status-line).

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;&ensp;Impostazioni Meno Usate  
&emsp;&emsp;Riga di stato extra
:::

::: xdripitem Stato Esterno <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Mostra lo stato di altre applicazioni come AndroidAPS
:::

::: xdripitem Stato del micro <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Mostra informazioni sullo stato del micro se disponibile
:::

Le informazioni del microinfusore (stato, basale) sono <u>visibili solo</u> nella riga di stato e **non possono essere caricate su Nightscout/Tidepool**.

<img src="./images/M-S-HDS-CF6.png" style="zoom:75%;" />

<br>

Se non vedi dati e non compare alcun messaggio di errore, potrebbe essere necessario [Inizializza Sensore](../use/startsensor#followers-and-companion-apps).

[*Ultima modifica 6/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.03)
