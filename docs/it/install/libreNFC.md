---
source_hash: 9c60a43392
source_commit: 7a18e7c
---
Oggi quasi tutti i telefoni supportano la scansione NFC. Se il tuo la supporta, puoi scansionare il tuo sensore Libre 1, 14 giorni USA, Libre 2/2+ (UE) e Libre Pro con xDrip oltre che con LibreLink, l'app del produttore. Nota che la scansione NFC di xDrip **non può** avviare un sensore: solo LibreLink (o il lettore) può farlo. 

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;LibreAlarm
:::

## Sorgenti dati supportate {#supported-data-sources}

Per accedere al menu NFC devi selezionare una delle sorgenti dati Libre.

Se userai xDrip solo per scansionare il sensore, scegli LibreAlarm.

::: info Nota
Se attivi il supporto alla scansione NFC di xDrip, disattiva qualsiasi altra app che tenti di leggere dispositivi NFC, per evitare conflitti. Questo vale soprattutto per l'app Libre del produttore.
:::

#### Configurare NFC {#configure-nfc}

Configura NFC esattamente [così](../use/NFC).

## Sensori supportati {#supported-sensors}

Solo Libre 1 e Pro sono supportati nativamente da xDrip per le letture NFC. Per scansionare un Libre 14 giorni USA o un Libre 2 europeo, devi installare sul telefono un [algoritmo OOP (Out of Process Algorithm)](../use/OOP).

| - Libre 1 / Pro - | - 14 giorni USA - | - Libre 2/2+ UE - |
| :---------------: | :------------: | :------------: |
|       `Sì`       |     `OOP2`      |     `OOP2`      |

::: info Intervallo minimo di scansione
Attendi almeno 60 secondi tra due scansioni NFC.
:::

<br>

Prosegui con [Inizializza Sensore](../use/startsensor#libre), ricordando che dovrai scansionare il sensore per ottenere le prime letture.

<br>



<br>

[*Ultima modifica 6/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
