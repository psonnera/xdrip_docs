---
source_hash: 59d10a9889
source_commit: 7a18e7c
---
### Blucon {#blucon}

Non puoi aggiornare né riportare a una versione precedente il firmware di questi dispositivi.  
Per conoscere la versione attuale del firmware devi installare l'[app del produttore](https://www.ambrosiasys.com/our-products/blucon/): la trovi nella sezione Informazioni...

<img src="./images/BluKon_FW.png" style="zoom:55%;" />

Le versioni di firmware più vecchie supportano Libre 1.  
Per Libre 14 giorni USA e Libre 2 ti serve un dispositivo recente con firmware almeno 4.2 e un algoritmo Out Of Process (OOP).

**I firmware più recenti, dalla 8.6 in su, non supportano xDrip.**

### MiaoMiao {#miaomiao}

Il firmware consigliato è:

| Dispositivo | Firmware |
| ---------- | -------- |
| MiaoMiao   | 39       |
| MiaoMiao 2 | 7        |
| MiaoMiao 3 | il più recente |

Per aggiornare il firmware devi prima usare [Dimentica questo dispositivo](./systemstatus#restart-collector-forget-device) in Stato del sistema di xDrip.

Installa l'[app del produttore](http://tomato.cool/), che aggiornerà automaticamente il firmware del tuo miaomiao.

Una volta aggiornato, disinstalla l'app, resetta il dispositivo e usa [Scansione Bluetooth](../install/libreBT#connect-bluetooth-bridge) in xDrip per ricollegarlo.

<br>

[*Ultima modifica 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
