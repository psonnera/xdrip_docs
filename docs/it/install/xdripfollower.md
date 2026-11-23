---
source_hash: 5d88c762ae
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;xDrip Sync Follower
:::

::: warning Vecchio xDrip Sync
A luglio 2024 Google ha chiuso la [Firebase API](https://firebase.google.com/docs/cloud-messaging/migrate-v1) deprecata che xDrip usava per xDrip Sync.  
Aggiorna xDrip a una versione successiva al [23 luglio 2024](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.07.23) per usare il metodo Sync legacy.  
Si consiglia di aggiornare xDrip almeno all'ultima release.
:::

Seleziona questa sorgente dati se hai configurato un dispositivo con xDrip come master e hai deciso che quest'altro dispositivo sarà il follower.  
Il dispositivo master è di solito quello che riceve la glicemia dal sensore.  
Un follower replica in tempo reale le letture del dispositivo master (a parte la latenza della rete).

Non c'è praticamente alcun limite al numero di dispositivi xDrip follower.

Vedi [qui](../use/syncsetup) come configurare xDrip Sync follower. 

<br>

[*Ultima modifica 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
