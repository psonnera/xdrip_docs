---
source_hash: 8a63383c39
source_commit: e9ebf28
---
Android offre molte opzioni di risparmio energetico: sono utili per aumentare l'autonomia della batteria, ma possono facilmente colpire funzioni indispensabili per un sistema CGM.

Tutte le impostazioni descritte qui sotto si trovano nelle impostazioni Android del telefono; il loro aspetto varia molto e dipende dalle personalizzazioni del produttore.

<img src="./images/AS.png" style="zoom:75%;" />

## Risparmio batteria {#battery-saver}

Quando la batteria scende sotto un certo livello, Android chiude molti servizi e impedisce a xDrip di funzionare normalmente.  Porta sempre con te un power bank per evitare questa situazione.

Durante il normale uso del telefono, assicurati che **non** sia attivo.

<img src="./images/AS-BS.png" style="zoom:75%;" />

## Risparmio batteria delle app {#apps-battery-savings}

Ogni app del telefono può essere personalizzata per quanto riguarda il risparmio della batteria. Se incontri problemi, controlla attentamente queste impostazioni. Vale anche per OOP, WatchDrip+ (se lo usi) e Bluetooth.

::: warning Aggiornamenti di Android
Gli aggiornamenti potrebbero riportare queste impostazioni ai valori predefiniti: ricontrollale sempre dopo.
:::

#### Android 10 {#android-10}

<img src="./images/AS-Apps-DO.png" style="zoom:75%;" />

#### Android 11 e superiori {#android-11-and-above}

<img src="./images/AS-Apps.png" style="zoom:75%;" />

xDrip deve funzionare senza restrizioni.

<img src="./images/AS-Apps-UR.png" style="zoom:75%;" />

### Bluetooth {#bluetooth}

Molto probabilmente troverai Bluetooth tra le app di sistema (menu a tre puntini).  
Alcuni telefoni Android non mostrano l'app Bluetooth.

<img src="./images/AS-Apps-SA.png" style="zoom:75%;" />

Bluetooth deve funzionare senza restrizioni se xDrip si collega direttamente a un sensore.

## Ottimizzazioni MIUI di Xiaomi {#xiaomi-miui-optimizations}

Le ottimizzazioni MIUI possono avere un impatto enorme (in senso negativo) sulla stabilità del sistema e sull'affidabilità di xDrip.
Se noti un aumento delle "letture mancate" con MIUI 14 (o forse con versioni MIUI precedenti), prova a disattivare le ottimizzazioni MIUI.
Questa impostazione si trova nelle \&lt;Opzioni sviluppatore\>, nascoste per impostazione predefinita. Qui sotto trovi come mostrare le \&lt;Opzioni sviluppatore\> e poi disattivare le ottimizzazioni MIUI.

### Attivare le opzioni sviluppatore {#enable-developer-options}

Per mostrare le **\&lt;Opzioni sviluppatore\>**, segui questi passaggi:

1. Apri le **\&lt;Impostazioni\>** dello smartphone.
2. Seleziona **\&lt;Info sul telefono\>**.
3. Tocca 7 volte **\&lt;Versione MIUI\>** (prima voce dell'elenco).
4. Compare il messaggio **\&lt;Ora sei uno sviluppatore.\>**.
5. Ora è visibile la voce **\&lt;Impostazioni\>** \-\> **\&lt;Impostazioni aggiuntive\>** \-\> **\&lt;Opzioni sviluppatore\>**.

### Disattivare le ottimizzazioni MIUI di Xiaomi {#disable-xiaomi-miui-optimizations}

Per disattivare le ottimizzazioni MIUI devi prima **attivare le opzioni sviluppatore**. Poi segui questi passaggi:

1. Apri le **\&lt;Impostazioni\>** dello smartphone.
2. Seleziona **\&lt;Impostazioni aggiuntive\>** \-\> **\&lt;Opzioni sviluppatore\>**.
3. **Solo per MIUI 14:** con MIUI 14 l'opzione **\&lt;Attiva ottimizzazione MIUI\>** **NON** è visibile per impostazione predefinita. Per vederla, scorri fino a **\&lt;COMPILAZIONE AUTOMATICA\>** e tocca più volte **\&lt;Ripristina valori predefiniti\>**. L'opzione comparirà.
4. **Disattiva** l'opzione **\&lt;Attiva ottimizzazione MIUI\>**!
5. Riavvia lo smartphone.

<br>

[*Ultima modifica 6/03/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2023.02.26)