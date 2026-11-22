---
source_hash: 3c47ed9511
source_commit: ea9ce3a
---
### Scopri l'interfaccia utente {#meet-the-user-interface}

Benvenuto in xDrip!

<img src="./images/UI-basic.png" style="zoom:50%;" />

Se hai appena configurato xDrip, inizia con le personalizzazioni di base:

1. [Imposta l'unità con cui visualizzare la glicemia](./settings)
2. [Aggiungi gli allarmi](./alarms)
3. Se colleghi xDrip a un sensore, [condividi i dati con un altro telefono con xDrip](./syncsetup)
4. Visualizza xDrip sul telefono quando [lo schermo è bloccato](./display#numbered-wall-on-locked-screen)
5. Aggiungi un [widget](#widget) alla schermata Home del telefono
6. Aggiungi uno [smartwatch](../smartwatch/smartwatch)
7. Condividi i dati con il tuo diabetologo tramite [Tidepool](https://www.tidepool.org/): se hai un account Tidepool, basta [configurare xDrip](./cloud#tidepool)
8. Carica i tuoi dati su [Nightscout](https://nightscout.github.io/) (consigliato)

### Indicazioni di base {#basic-indications}

Quando xDrip riceve i dati vedrai queste indicazioni predefinite.

<img src="./images/UI-indications.png" style="zoom:75%;" />

1. Quanto tempo fa è stata ricevuta la lettura e qual è la differenza di glicemia rispetto al valore precedente.
2. L'ultimo valore di glicemia misurato.
3. La tendenza rispetto alla misura precedente.

##### Freccia di tendenza {#trend-arrow}

::: info Nota
La freccia indica la tendenza rispetto alla misura precedente; altre app CGM usano un algoritmo per questa indicazione e il risultato potrebbe non coincidere.  
In caso di letture mancanti, la freccia potrebbe indicare un aumento o un calo rapido: confrontala sempre con l'indicazione in `1`.
:::

Puoi personalizzare le informazioni mostrate in `1` con le [Impostazioni grafico](./display#graph-settings).

Puoi [personalizzare l'aspetto della freccia di tendenza](#blood-drop-menu) ma non il suo comportamento (userà sempre la differenza con la lettura precedente).

Ecco come appare la freccia di tendenza classica, che tiene conto della differenza tra la lettura di glicemia precedente e quella attuale.

| Differenza di glicemia (precedente e attuale)                |                                                           |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| Variazione al massimo di +/- 5 mg/dL (0,28 mmol/L)           | <img src="./images/ArrowFlat.png" style="zoom:75%;" />   |
| Variazione superiore alla precedente e inferiore a +/- 10 mg/dL (0,56 mmol/L) | <img src="./images/ArrowUpDn.png" style="zoom:75%;" />   |
| Variazione superiore alla precedente e inferiore a +/- 17,5 mg/dL (0,97 mmol/L) | <img src="./images/ArrowUpDn+.png" style="zoom:75%;" />  |
| Variazione superiore alla precedente                         | <img src="./images/ArrowUpDn++.png" style="zoom:75%;" /> |



### Trattamenti {#treatments}

Puoi registrare i trattamenti con l'icona della siringa.

<img src="./images/UI-Treat.png" style="zoom:75%;" />

Aggiungi uno o più elementi al trattamento.

#### Misura capillare {#blood-test}

Viene visualizzata nell'unità selezionata in xDrip.

<img src="./images/UI-Treat1.png" style="zoom:75%;" />

#### Grammi di carboidrati {#grams-of-carbs}

<img src="./images/UI-Treat2.png" style="zoom:75%;" />

#### Unità di insulina {#units-of-insulin}

::: info Nota
Se hai attivato i [tipi di insulina multipli](./predictions#multiple-insulin-types), seleziona anche il tipo di insulina per questo trattamento.
:::

<img src="./images/UI-Treat3.png" style="zoom:75%;" />

#### Ora {#time}

E infine l'ora del trattamento (se non è adesso), nel formato 24 ore, con o senza separatore.

::: info Nota
Puoi selezionare un orario del trattamento da 23 ore nel passato fino a 1 ora nel futuro.
:::

<img src="./images/UI-Treat4.png" style="zoom:75%;" />

I trattamenti sono validi quando compare il segno di spunta verde nell'angolo in alto a destra. Toccalo per confermare i dati inseriti.

<img src="./images/UI-Treat6.png" style="zoom:75%;" />

Viene mostrato un riepilogo. Tocca l'icona verde `+` per confermare o l'icona rossa `x` per annullare.

<img src="./images/UI-Treat5.png" style="zoom:75%;" />

Una volta fatto, sul grafico compariranno nuovi simboli.

Unità e carboidrati appaiono così:

<img src="./images/UI-Treat7.png" style="zoom:75%;" />

E le misure capillari così (nota che il simbolo è quadrato, a differenza delle [calibrazioni](../calibrate/calibrate) che sono rotonde):

<img src="./images/UI-Treat8.png" style="zoom:75%;" />

#### Modificare ed eliminare {#edit-and-delete}

Quando sono visibili, puoi eliminare i trattamenti così:

- Tocca il trattamento e guarda in fondo allo schermo: tocca Aggiungi nota 

<div style="background-color: black; color: white; text-align: left;">  &emsp;18:45 Trattamento&emsp;<span style="color: cyan; float: right;">AGGIUNGI NOTA&emsp;</span></div>

oppure Misura capillare.

<div style="background-color: black; color: white; text-align: left;">  &emsp;10:06 85 mg/dl&emsp;<span style="color: cyan; float: right;">MISURA CAPILLARE&emsp;</span></div>

- Puoi inserire una nota o toccare CANCELLA per eliminare la voce. Vale per misure capillari, carboidrati e insulina.

::: xdripitem Note di Terapia
<span style="color: cyan;">_____________________________________________________________________________________</span>  
<small>Inserimento vocale di default dal prossimo</small> ☐  


<span style="color: cyan; float: left;">CANCELLA&emsp;</span><span style="color: cyan; float: right;">ANNULLA&emsp;FATTO&emsp;</span>
:::

Nota che se tocchi una misura capillare e la modifichi, puoi anche convertirla in calibrazione con CALIBRA. È possibile se non hai selezionato **Never use them** (non usarle mai) in [Calibrazione avanzata](../calibrate/advancedcal).

::: xdripitem Azione su misura capillare
Che cosa vorresti fare?  


<span style="color: cyan; float: left;">NIENTE&emsp;</span><span style="color: cyan; float: right;">CANCELLA&emsp;CALIBRA&emsp;</span>
:::

##### Trattamenti vocali {#spoken-treatments}

Puoi usare l'icona del microfono per inserire a voce i trattamenti o i comandi avanzati.

Un tocco prolungato sull'icona del microfono ti permette di scrivere i [comandi avanzati](./spokencommands).

### Note di terapia {#treatment-notes}

Indipendentemente dai trattamenti, puoi inserire delle note.

<img src="./images/UI-Note.png" style="zoom:75%;" />

Inserisci il commento che vuoi (ad esempio le unità di insulina lenta), oppure usa l'icona del microfono per dettare la nota.

::: xdripitem Note di Terapia
<span style="color: cyan;">_____________________________________________________________________________________</span>  
<small>Inserimento vocale di default dal prossimo</small> ☐  


<span style="color: cyan; float: left;">CANCELLA&emsp;</span><span style="color: cyan; float: right;">ANNULLA&emsp;FATTO&emsp;</span>
:::



Verranno aggiunte al grafico così:

<img src="./images/UI-Note2.png" style="zoom:75%;" />

Toccandole puoi modificarle o eliminarle.

### Annulla e Ripeti {#undo-and-redo}

1. Annulla torna indietro passo per passo tra simulazioni di trattamenti, calibrazioni e note. Dopo 30 minuti si nasconde di nuovo.
2. Ripeti va avanti passo per passo tra simulazioni di trattamenti, calibrazioni e note. Dopo 30 minuti si nasconde di nuovo.

<img src="./images/UI-UndoRedo.png" style="zoom:77%;" />

### [Menu principale](./hamburger) {#main-menu}

Chiamato anche menu hamburger o menu a scomparsa, è il menu principale in cui trovi o aggiungi le azioni più comuni, oltre a tutte le impostazioni e personalizzazioni.

<img src="../images/hamburger_menu.png" style="zoom:75%;" />

### Menu goccia di sangue {#blood-drop-menu}

Con un tocco prolungato nell'area centrale tra il menu principale e il menu a tre puntini, apri un altro menu per personalizzare l'interfaccia utente.

<img src="../images/UImenu.png" style="zoom:75%;" />

##### Pulsante Assistente Sorgente {#source-wizard-button}

Mostra il pulsante che ti guida nella scelta della sorgente dati, come descritto [qui](../install/datasource).

::: xdripitem <span style="background-color: grey; color: white;">  &emsp;&emsp;AVVIA CONFIGURAZIONE GUIDATA&emsp;</span>
:::

##### Mostrare Tasti Periodo {#show-time-buttons}

Aggiunge una riga di quattro preimpostazioni per l'intervallo di tempo del grafico principale: 24, 12, 6 e 3 ore.  
Con una pressione prolungata su un pulsante del periodo puoi bloccare la vista su quel periodo.

::: xdripitem <span style="background-color: grey; color: white;"> &ensp;24 ORE&ensp;</span> &emsp;<span style="background-color: grey; color: white;"> &ensp;12 ORE&ensp;</span>  &emsp;<span style="background-color: grey; color: white;"> &ensp;6 ORE&ensp;</span>  &emsp;<span style="background-color: grey; color: white;"> &ensp;3 ORE&ensp;</span>
:::

##### Usa Sempre Periodo Fisso {#locked-time-period-always-used}

Imposta come predefinito l'ultimo periodo di visualizzazione modificato.

##### Mostra Anteprima Grafico {#show-chart-preview}

Attiva o disattiva il piccolo grafico delle 24 ore nella parte bassa dello schermo.

<img src="./images/UI-ChartPreview.png" style="zoom:75%;" />

##### Mostra Stato Collettore {#show-collector-status}

Mostra sotto il grafico principale i messaggi informativi sullo stato del collector.

<img src="./images/UI-CollStatus.png" style="zoom:75%;" />

##### Mostra Scadenza Sensore {#show-sensor-expiry}

Mostra sotto il grafico principale il tempo rimanente prima della scadenza del sensore.

<img src="./images/UI-SensorExpiry.png" style="zoom:75%;" />

##### Mostra Freccia Di Tendenza Grafica {#show-graphical-trend-arrow}

Aggiunge un'opzione che ti permette di scegliere altri stili di freccia.

Usa la chiave inglese <img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_wrench_grey600_48dp.png" style="width:3%;" /> e il menu a tendina ▼ per selezionarli.  
Le frecce colorate includono un cursore della tonalità per cambiare colore. 

L'angolo delle frecce di tendenza grafiche dipende dalla differenza della lettura rispetto al valore precedente (5 minuti) e non solo piatto/45/90 gradi come le frecce classiche.

<img src="./images/UI-GraphicArrow.png" style="zoom:90%;" />

### [Menu a tre puntini](./3dotsmenu) {#three-dots-menu}

Questo menu contiene alcune scorciatoie alle impostazioni e altre funzioni specifiche.

<img src="../images/3dots_menu.png" style="zoom:75%;" />

### Widget {#widget}

Se il tuo telefono supporta i widget, fai un tocco prolungato su un'area vuota della schermata Home e seleziona Widget.  
Scorri le app finché trovi xDrip. 

<img src="./images/Widget1.png" style="zoom:75%;" />

Tieni il dito sul widget e trascinalo nella posizione in cui vuoi visualizzarlo.

<img src="./images/Widget2.png" style="zoom:75%;" />

Puoi ridimensionarlo con i punti blu.

<img src="./images/Widget3.png" style="zoom:75%;" />

E dargli la dimensione che preferisci. Poi puoi personalizzarne i colori e l'aspetto dei contenuti nelle [impostazioni di visualizzazione](./display).

<img src="./images/Widget4.png" style="zoom:75%;" />

### Salvaschermo {#screensaver}

Se il tuo telefono supporta questa funzione, puoi attivare xDrip come salvaschermo nelle Impostazioni di Android.

<img src="./images/ScreenSaver1.png" style="zoom:75%;" />

Quando metti il telefono in carica, mostrerà un piccolo grafico e il valore della glicemia.

<img src="./images/ScreenSaver2.png" style="zoom:75%;" />

<br>

[*Ultima modifica 15/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
