---
source_hash: 2b688cafdf
source_commit: ea9ce3a
---
Fermare un sensore in xDrip ha funzioni molto diverse a seconda del sensore.

### G6 e 1 {#g6-and-1}

La documentazione di riferimento si trova [qui](https://navid200.github.io/xDrip/docs/Proper-connectivity.html).

### G7 e 1+ {#g7-and-1}

Questi sensori si fermano da soli dopo 10 giorni e 12 ore. Alcuni trasmettitori con firmware alternativo indicano invece una durata più lunga di 15 giorni e 12 ore; xDrip lo rileva automaticamente dal firmware del trasmettitore, non è un'impostazione che scegli tu.

<br>

### Libre {#libre}

xDrip non è in grado di fermare un sensore Libre; in realtà questo sensore non si può fermare: se non si guasta, funziona per tutta la sua durata e si ferma da solo dopo 14 giorni e 12 ore.

L'arresto del sensore in xDrip serve solo a invalidare le calibrazioni precedenti. Questa operazione è necessaria e consigliata ogni volta che sostituisci il sensore.

<br>



::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&emsp;Stop Sensore
:::

Conferma STOP SENSORE, a meno che tu non voglia solo [azzerare tutte le calibrazioni](../calibrate/calibrate#reset-all-calibrations).

::: xdripitem <img src="../images/BDM.png" style="zoom:75%;" /> Stop Sensore <span class='symbol'></span>
  &emsp;Ferma il tuo sensore solo quando pensi di rimuoverlo, altrimenti lascialo avviato!  


&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;STOP SENSORE&ensp;</span>
:::

Conferma che vuoi fermare il sensore.

::: xdripitem Sei sicuro?
  &emsp;Vuoi fermare il sensore?  


 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;NO &emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;SI&ensp;</span>
:::

Se cambi idea e il sensore non è ancora scaduto, puoi sempre ["riavviarlo"](./startsensor#libre): riprenderà la sessione in corso ed eventualmente chiederà una nuova calibrazione. xDrip non riavvia fisicamente i sensori Libre.

<br>

### Follower e app compagno {#followers-and-companion-apps}

Non ha senso fermare un sensore quando usi un'app follower.

::: warning Attenzione
L'unica eccezione è il [follower xDrip Sync, che può trasmettere il comando di avvio o arresto al sensore vero e proprio se questo è collegato direttamente allo xDrip che fa da master](./sync#accept-followers-actions).  
Non usare Avvia e Ferma sensore con un follower xDrip Sync, a meno che tu non sia certo che la persona con il telefono xDrip master sappia cosa fare con un sensore fermato!
:::

<br>

[*Ultima modifica 6/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.03)