---
source_hash: 5e151bd537
source_commit: 7a18e7c
---

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;Dex Share Follower
:::

### Prerequisiti {#prerequisites}

Perché xDrip riceva i dati dai server Share, ti servono:

1. un nome utente che **non sia un numero di telefono**: crea un [account dipendente](https://www.dexcom.com/faqs/how-do-i-create-a-dependent-account) per ottenerne uno. Una volta creato il nuovo account dipendente, assicurati di aver effettuato l'accesso con questo account nelle app Dexcom e ricrea tutti i follower
2. la condivisione attivata nell'app Dex collegata al sensore
3. l'invito accettato nell'app Dex follower (dopo puoi disinstallarla)

<img src="./images/M-S-HDS-DexSh1.png" style="zoom:75%;" />

Inserisci le credenziali che usi per accedere a Clarity.

::: xdripitem Share Username
&ensp;Login username for Dex Share Following
:::

::: xdripitem Share Password
&ensp;Login password for Dex Share following
:::

Attiva US Servers solo se il tuo account è negli Stati Uniti.

::: xdripitem US Servers
&ensp;Your account and follower app are from the USA
:::

::: warning Blocco dell'account
Lasciare xDrip con una password sbagliata bloccherà il tuo account.  
Per uscire dal blocco dell'account, elimina le credenziali, [disattiva la raccolta dati di xDrip](./datasource#changing-data-source) e attendi 15/20 minuti.  
xDrip e qualsiasi altra app di terze parti che tenti di collegarsi con una password sbagliata manterranno il blocco.
:::

Se non vedi dati e non compare alcun messaggio di errore, potrebbe essere necessario [Inizializza Sensore](../use/startsensor#followers-and-companion-apps).

<br>

[*Ultima modifica 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
