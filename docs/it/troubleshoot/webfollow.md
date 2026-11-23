---
source_hash: 8c757f2bd2
source_commit: 7a18e7c
---
# Libre Web Follower {#libre-web-follower}

## Configurazione del sistema {#system-setup}

Quando usi questa sorgente dati devi assicurarti che il sistema sia configurato correttamente con le app del produttore.

**L'app master (collegata al sensore Libre) deve caricare i dati sul [server](https://www.libreview.com/) del produttore.**  

Esci ed entra di nuovo nel server per verificare di usare le credenziali giuste.

Assicurati che sul server ci siano dati.

**L'app [follower](https://play.google.com/store/search?q=librelinkup&c=apps) del produttore deve ricevere i dati condivisi.**  

Prova a eliminare e inviare di nuovo un invito all'app follower del produttore (usando l'app master del produttore).

Prova a disinstallare e reinstallare l'app follower del produttore.

- Per accedere usa preferibilmente le credenziali dell'invito.
- Se non funziona, usa le credenziali dell'app master (server) e invia di nuovo l'invito.

<br>

## Configurazione di xDrip {#xdrip-setup}

Quando il sistema funziona con le app del produttore, puoi passare alla risoluzione dei problemi di xDrip.

1. Assicurati che la sorgente dati sia [Web follower](../install/webfollower).
2. Usa le credenziali del follower che hai invitato con l'app master del produttore.
3. Se non funziona, puoi provare a usare le credenziali del server per individuare il problema, ma fai attenzione a ridurre il rischio di blocco dell'account.

<br>

## Aggiornamenti dei server del produttore {#vendor-servers-updates}

Gli aggiornamenti del server possono rompere il meccanismo.

**Una volta che xDrip è stato corretto**, potresti doverlo reimpostare seguendo questa sequenza:

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;Web Follower
:::

Modifica il `Configuration script`

::: xdripitem Configuration Script
&ensp;This is the community helper address or keyword
:::

Aggiungi uno spazio dopo `beonlabs` e seleziona `Ok`

<img src="./images/M-S-HDS-WF-Scr.png" style="zoom:75%;" />

Modifica di nuovo il `Configuration script`, **togli lo spazio** dopo `beonlabs` e seleziona `Ok`.

Aspetta fino a un minuto che i dati vengano di nuovo visualizzati.

<br>

Se il problema persiste, installa l'app follower del produttore sullo stesso telefono e verifica che riceva i dati con le stesse credenziali.

<br>

[*Ultima modifica 8/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
