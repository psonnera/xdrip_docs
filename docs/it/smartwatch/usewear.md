---
source_hash: f17272d683
source_commit: 7a18e7c
---
Trovi la documentazione di riferimento [qui](https://github.com/NightscoutFoundation/xDrip/blob/master/Documentation/WatchGuide.md).

## Scoprire l'estensione Wear {#discover-wear-extension}

xDrip mette a disposizione quattro quadranti nativi.

|                           XDrip                            |                      XDrip(BigChart)                       |
| :--------------------------------------------------------: | :--------------------------------------------------------: |
| <img src="./images/M-S-SW-AW-W1.png" style="zoom:75%;" /> | <img src="./images/M-S-SW-AW-W2.png" style="zoom:75%;" /> |
|                      **XDrip(Large)**                      |                     **XDrip(Circle)**                      |
| <img src="./images/M-S-SW-AW-W3.png" style="zoom:75%;" /> | <img src="./images/M-S-SW-AW-W4.png" style="zoom:75%;" /> |

I quadranti con grafico hanno alcuni elementi in comune con la schermata principale di xDrip.

1. L'ultimo valore di glicemia misurato.  
   La differenza di glicemia rispetto al valore precedente ricevuto.  
   La tendenza rispetto alla misurazione precedente.
2. Una riga di stato.
3. Un grafico della glicemia.

 <img src="./images/M-S-SW-AW-SC1.png" style="zoom:75%;" />

Un doppio tocco sul grafico cambia la scala temporale.

<img src="./images/M-S-SW-AW-SC2.png" style="zoom:75%;" />

Poiché l'estensione Wear di xDrip contiene una parte del codice dell'app, troverai sull'orologio alcune voci di menu di xDrip. Le trovi tra le app dell'orologio; alcune sono accessibili anche dal grafico tramite il menu a tre puntini presente su tutti i quadranti.

<img src="./images/M-S-SW-AW-3DM.png" style="zoom:75%;" />

### xDrip Prefs. {#xdrip-prefs}

Questo menu contiene le opzioni di visualizzazione del quadrante.  
Quando l'orologio è configurato come collector autonomo, sono visibili altre voci. Vedi più avanti.

<img src="./images/M-S-SW-AW-XP.png" style="zoom:75%;" />

Il tema scuro mostra uno sfondo nero con testo e grafico bianchi. Disattivandolo ottieni il contrario: sfondo bianco con testo e grafico scuri.

<img src="./images/M-S-SW-AW-XP3.png" style="zoom:75%;" />

Refresh on change aggiorna il quadrante a ogni cambiamento dei dati (minimo 5 minuti). Se lo disattivi, l'orologio aggiornerà il quadrante ogni minuto (consumerà più batteria).

<img src="./images/M-S-SW-AW-XP4.png" style="zoom:75%;" />

Show treatment aggiunge i punti dei trattamenti sui quadranti con grafico.

<img src="./images/M-S-SW-AW-XP5.png" style="zoom:75%;" />

Il formato 24 ore forza la visualizzazione dell'ora in questo formato.

<img src="./images/M-S-SW-AW-XP6.png" style="zoom:75%;" />

Show date mostra anche la data sul quadrante.

<img src="./images/M-S-SW-AW-XP7.png" style="zoom:75%;" />

Se l'orologio è configurato per usare la propria lingua, puoi forzarlo a usare le impostazioni del telefono.

<img src="./images/M-S-SW-AW-XP8.png" style="zoom:75%;" />

I toast sono messaggi a comparsa: puoi attivarli e ottenere informazioni aggiuntive toccando i passi e lo stato sull'orologio.

<img src="./images/M-S-SW-AW-XP9.png" style="zoom:75%;" />

Se l'orologio lo supporta e hai autorizzato xDrip Prefs. ad accedere ai dati dei sensori dell'orologio, avrai il contapassi sul quadrante e potrai visualizzare i [dati dei passi](../use/display) in xDrip sul telefono.

<img src="./images/M-S-SW-AW-XP10.png" style="zoom:75%;" />

Se l'orologio lo supporta e hai autorizzato xDrip Prefs. ad accedere ai dati dei sensori dell'orologio, avrai la frequenza cardiaca sul quadrante e potrai visualizzare i [dati della frequenza cardiaca](../use/display) in xDrip sul telefono.

<img src="./images/M-S-SW-AW-XP11.png" style="zoom:75%;" />

Se usi un sistema open source a circuito chiuso (come AAPS) che trasmette i dati a xDrip, puoi aggiungere lo stato del loop alla riga di stato.

<img src="./images/M-S-SW-AW-XP12.png" style="zoom:75%;" />

Per impostazione predefinita il quadrante mostra la batteria del dispositivo che raccoglie i dati come `uploader` o `wear`. È una definizione storica che non aggiunge nulla se non usi xDrip come master: non mostrerà il livello di batteria del telefono master né quello di un eventuale bridge, ma solo la batteria del tuo telefono e dell'orologio.

<img src="./images/M-S-SW-AW-XP13.png" style="zoom:75%;" />

Ti permette di mostrare le schede (avvisi) con uno sfondo uniforme per migliorarne la leggibilità.

<img src="./images/M-S-SW-AW-XP14.png" style="zoom:75%;" />

Puoi cambiare la dimensione del carattere della riga di stato: 10 o 12 punti.

<img src="./images/M-S-SW-AW-XP15.png" style="zoom:75%;" />

Puoi cambiare l'intervallo di tempo del grafico, come con il doppio tocco.

<img src="./images/M-S-SW-AW-XP16.png" style="zoom:75%;" />

In questo menu trovi le personalizzazioni del quadrante circolare.

<img src="./images/M-S-SW-AW-XP17.png" style="zoom:75%;" />

Colore per i valori bassi.

<img src="./images/M-S-SW-AW-XP18.png" style="zoom:75%;" />

Su xDrip e xDrip Large, cambia il colore del divisore (riga di stato) per adattarlo allo sfondo.

<img src="./images/M-S-SW-AW-XP19.png" style="zoom:75%;" />

Force update è disponibile sugli orologi Wear 2.0 e successivi, se disponibile per la versione attuale e attivato come spiegato [qui](./wearinstall#wear-os-2x-and-3x).

<img src="./images/M-S-SW-AW-XP20.png" style="zoom:75%;" />

Demigod è disponibile per gli [orologi modificati](https://github.com/NightscoutFoundation/xDrip/wiki/Patching-Android-Wear-devices-for-use-with-the-G5).

<img src="./images/M-S-SW-AW-XP21.png" style="zoom:75%;" />

### Keypad Treatment {#keypad-treatment}

Keypad Treatment è identico all'[icona della siringa](../use/mainUI#treatments) di xDrip.

<img src="./images/M-S-SW-AW-KT.png" style="zoom:75%;" />

<img src="./images/M-S-SW-AW-XP22.png" style="zoom:75%;" />

### Spoken treatment {#spoken-treatment}

Spoken treatment (trattamento vocale) è identico a quello di xDrip.

<img src="./images/M-S-SW-AW-ST.png" style="zoom:75%;" />

<img src="./images/M-S-SW-AW-XP23.png" style="zoom:75%;" />

### Snooze Alert {#snooze-alert}

Non tutti gli avvisi e gli allarmi sono disponibili sull'orologio.

<img src="./images/M-S-SW-AW-SA.png" style="zoom:75%;" />

Su Wear 1.x, gli allarmi e gli avvisi che rimandano all'apertura sul telefono indicano che devi posticiparli dall'app xDrip del telefono.

<img src="./images/M-S-SW-AW-SA2.png" style="zoom:75%;" />

Su Wear 2.x e successivi, gli avvisi possono comparire come notifiche: dovrai aprire manualmente l'app di sospensione degli allarmi sul telefono o posticiparli dall'app xDrip del telefono.

<img src="./images/M-S-SW-AW-SA3.png" style="zoom:75%;" />

## [Modalità collector autonomo](./wear#standalone-collector-mode) {#standalone-collector-mode}

Il menu xDrip Prefs. conterrà informazioni aggiuntive riprese da xDrip sul telefono quando i due sono collegati.

#### Convalida {#validation}

Un meccanismo di convalida garantisce che entrambi usino le stesse impostazioni. Se l'orologio non accetta la modifica delle impostazioni inviata da xDrip, queste verranno modificate automaticamente per corrispondere alle impostazioni dell'orologio quando i due sono collegati.

1. Le impostazioni vengono modificate sul telefono
2. Le modifiche vengono inviate all'orologio, quando è collegato
3. L'orologio prova ad applicare le modifiche alle impostazioni
4. Le impostazioni dell'orologio vengono rimandate al telefono (modificate o no)
5. Le impostazioni del telefono vengono aggiornate per riflettere quelle dell'orologio, quando è collegato

<img src="./images/M-S-SW-AW-XP1.png" style="zoom:75%;" />

Funziona anche nell'altro senso. Se le impostazioni dell'orologio vengono modificate, saranno inviate al telefono quando è collegato. xDrip sul telefono convaliderà le modifiche e le rimanderà all'orologio come conferma.

1. Le impostazioni vengono modificate sull'orologio
2. Le modifiche vengono inviate al telefono, quando è collegato
3. xDrip sul telefono convalida le modifiche alle impostazioni
4. Le impostazioni del telefono vengono rimandate all'orologio (convalidate o no)
5. Le impostazioni dell'orologio vengono aggiornate per riflettere quelle del telefono, quando è collegato

<img src="./images/M-S-SW-AW-XP2.png" style="zoom:75%;" />

#### xDrip Prefs. {#xdrip-prefs-1}

Quando il collector autonomo è attivo, trovi altre voci nel menu.

BT collector mostra quale collector della sorgente dati hardware è impostato in xDrip sul telefono.

<img src="./images/M-S-SW-AW-ST1.png" style="zoom:75%;" />

Enable collector corrisponde all'impostazione in [Integrazione Wear](./wear#standalone-collector-mode).

<img src="./images/M-S-SW-AW-ST2.png" style="zoom:75%;" />

Lo stesso vale per Force collector. Se l'orologio non è collegato al telefono e hai perso la connessione al sensore, puoi attivarlo per forzare un tentativo di riconnessione.

<img src="./images/M-S-SW-AW-ST3.png" style="zoom:75%;" />

In modalità collector autonomo puoi usare (alcuni) avvisi locali dell'orologio. Verranno posticipati sull'orologio.

<img src="./images/M-S-SW-AW-ST4.png" style="zoom:75%;" />

Compreso l'avviso di glicemia alta persistente.

<img src="./images/M-S-SW-AW-ST5.png" style="zoom:75%;" />

Se l'orologio ha un altoparlante, può anche far suonare gli allarmi.

<img src="./images/M-S-SW-AW-ST6.png" style="zoom:75%;" />

Se ti colleghi a un G5 o G6, troverai altre impostazioni.

<img src="./images/M-S-SW-AW-ST8.png" style="zoom:75%;" />

Sono la copia delle impostazioni del telefono G5/G6 Debug Settings - Old G5 Collector Settings.

<img src="./images/M-S-SW-AW-ST9.png" style="zoom:75%;" />

<img src="./images/M-S-SW-AW-ST10.png" style="zoom:75%;" />

<img src="./images/M-S-SW-AW-ST11.png" style="zoom:75%;" />

<img src="./images/M-S-SW-AW-ST12.png" style="zoom:75%;" />

Force screen on garantisce che l'orologio sia completamente attivo durante la scansione.

<img src="./images/M-S-SW-AW-ST13.png" style="zoom:75%;" />

<br>

[*Ultima modifica 28/3/2022*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2022.03.27)
