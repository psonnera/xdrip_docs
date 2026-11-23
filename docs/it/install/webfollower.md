---
source_hash: 05ada65eb5
source_commit: 7a18e7c
---
::: warning Soggetto a interruzioni
Poiché il produttore non ha pubblicato un'API, gli aggiornamenti del server e del protocollo renderanno inutilizzabile questa sorgente dati.  
**In caso di problemi usa l'[ultima pre-release](./download#pre-release).**
:::

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;Web Follower
:::

<br>

### Prerequisiti {#prerequisites}

1. Installa l'app LibreLink o Libre 3, accedi o crea un account (obbligatorio) e assicurati che mostri le letture in tempo reale del sensore
2. Invita un follower  
   <img src="./images/M-S-HDS-WF3.png" style="zoom:76%;" />
3. Nell'email di invito, tocca il link al Play Store per installare l'[app follower](https://play.google.com/store/apps/details?id=org.nativescript.LibreLinkUp)  
   Crea un altro account per l'app follower.

::: warning Rischio di blocco dell'account
**Non** usare le credenziali del tuo account principale!
:::

Assicurati di ricevere le letture.   
Poi puoi disinstallare l'app follower. Potrebbe essere necessario reinstallarla per autenticare di nuovo il follower se i dati smettono di comparire in xDrip.

### Configurare il web follower di xDrip {#configure-xdrip-web-follower}

::: xdripitem Web Follower Settings
&ensp;Configuration options for web follower data source
:::

Non cambiare il nome dello script di configurazione: è `beonlabs`

::: xdripitem Configuration Script
&ensp;This is the community helper address or keyword
:::

Inserisci le credenziali che hai usato nell'app follower.

::: xdripitem Service logon user name
&ensp;This is your registered user name or email address with the service
:::

::: xdripitem Service logon password
&ensp;This is your registered password with the service
:::

Non attivare un server proxy a meno che tu non sappia perché vuoi farlo.

::: xdripitem Use proxy server (advanced) <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

<br>

Se non vedi dati e non compare alcun messaggio di errore, potrebbe essere necessario [Inizializza Sensore](../use/startsensor#followers-and-companion-apps).

Se necessario, consulta la pagina di [risoluzione problemi](../troubleshoot/webfollow).

<br>

[*Ultima modifica 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
