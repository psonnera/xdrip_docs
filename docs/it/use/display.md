---
source_hash: d238ff7b1e
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_chart_areaspline_grey600_48dp.png" style="width:5%;" />&ensp;xDrip+ impostazioni di visualizzazione
:::

Questo menu ti permette di personalizzare molti aspetti visivi di xDrip.

::: xdripitem xDrip+ impostazioni di visualizzazione
&ensp;Personalizzazioni di visualizzazione
:::

*Nota: controlla le funzioni delle [Impostazioni grafico](#graph-settings) prima di usare le impostazioni dei colori.*

### Impostazioni colore {#color-settings}

::: xdripitem xDrip+ Impostazioni colore
  &emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_palette_grey600_48dp.png" style="width:8%;" />&ensp;Personalizzazione Colori
:::

Il grafico di esempio in alto mostra l'effetto delle modifiche.

::: xdripitem Chart di Esempio
  &emsp;<img src="./images/M-S-DS2a.png" style="zoom:75%;" />
:::

Quando modifichi un colore puoi scegliere

1. tonalità e saturazione
2. chiarezza/scurezza
3. trasparenza.

Il risultato viene mostrato a confronto con il colore originale.

Puoi riportare il colore al valore predefinito o salvarlo.

<img src="./images/M-S-DS2a2.png" style="zoom:75%;" />

##### Valori di glucosio e linee {#glucose-values-and-lines}

Puoi personalizzare il grafico principale della glicemia. I limiti alto e basso sono definiti nelle [impostazioni Unità di misura glicemia.](./settings#glucose-units)

I colori dei valori alti, nell'intervallo e bassi cambiano il grafico e le linee dei limiti nella schermata principale, nella notifica e nei grafici del widget.

::: xdrip <small><small>VALORI DI GLUCOSIO E LINEE</small></small>
Valori Glicemici Elevati<span style="float: right; width: 40px; height: 40px; background-color: #FFBB33; display: inline-block;"></span>  


Valori Glicemici nella media<span style="float: right; width: 40px; height: 40px; background-color: #33B5E6; display: inline-block;"></span>  

Valori Glicemici Bassi<span style="float: right; width: 40px; height: 40px; background-color: #C30909; display: inline-block;"></span>  

Valori Glicemici Errati<span style="float: right; width: 40px; height: 40px; background-color: #FFFFFF; display: inline-block;"></span>  

Valori Filtrati<span style="float: right; width: 40px; height: 40px; background-color: #A0A0A0; display: inline-block;"></span>  
:::

<img src="./images/M-S-DS2b2.png" style="zoom:75%;" />

I valori errati e filtrati sono visibili con i sensori che forniscono dati grezzi.

<img src="./images/M-S-DS2d2.png" style="zoom:75%;" />

##### Colori del valore di glicemia e delle frecce di tendenza {#colors-of-bg-readings-and-trend-arrows}

Puoi anche personalizzare il colore del valore di glicemia attuale e della freccia di tendenza in base ai limiti dell'intervallo.

<img src="./images/M-S-DS2b.png" style="zoom:75%;" />

::: xdrip <small><small>COLORI DEL VALORE DI GLICEMIA E FRECCIA DI TENDENZA</small></small>
Valori Glicemici Elevati<span style="float: right; width: 40px; height: 40px; background-color: #FFBB33; display: inline-block;"></span>  


Valori Glicemici nella media<span style="float: right; width: 40px; height: 40px; background-color: #FFFFFF; display: inline-block;"></span>  

Valori Glicemici Bassi<span style="float: right; width: 40px; height: 40px; background-color: #C30909; display: inline-block;"></span>  

Previsione ipo (critica)<span style="float: right; width: 40px; height: 40px; background-color: #C30909; display: inline-block;"></span>  
:::

Previsione ipo (critica) è il colore del messaggio di previsione di glicemia bassa sulla schermata principale quando la glicemia bassa è vicina.

##### Curve dei trattamenti e delle previsioni {#treatments-and-predictions-curves}

1. Insulina attiva (curva principale dei [trattamenti](./mainUI#units-of-insulin))
2. Attività dell'insulina (piccola linea tratteggiata)

::: xdrip <small><small>TERAPIA / CURVE DI PREVISIONE</small></small>
Colori Terapia<span style="float: right; width: 40px; height: 40px; background-color: #77AA00; display: inline-block;"></span>  


Colori Scuri Terapia<span style="float: right; width: 40px; height: 40px; background-color: #334400; display: inline-block;"></span>  
:::



<img src="./images/M-S-DS2e2.png" style="zoom:75%;" />

1. [Previsione](./predictions) della glicemia (grafico principale delle previsioni)
2. [Carboidrati](./mainUI#grams-of-carbs) attivi (piccola linea tratteggiata)

::: xdrip <small><small>TERAPIA / CURVE DI PREVISIONE</small></small>
Colori Previsione<span style="float: right; width: 40px; height: 40px; background-color: #AA66CC; display: inline-block;"></span>  


Colori Scuri previsione<span style="float: right; width: 40px; height: 40px; background-color: #7700AA; display: inline-block;"></span>  
:::

<img src="./images/M-S-DS2f2.png" style="zoom:75%;" />

##### Linee della media e del target {#average-and-target-lines}

1. Linea della media delle 8 ore
2. Linea della media delle 24 ore
3. Linea del target

::: xdrip <small><small>LINEE MEDIANA E DI TARGET</small></small>
Linea Media 8 ore<span style="float: right; width: 40px; height: 40px; background-color: #558800; display: inline-block;"></span>  


Linea Media 24 ore<span style="float: right; width: 40px; height: 40px; background-color: #C56F9D; display: inline-block;"></span>  

Glucosio linea di destinazione<span style="float: right; width: 40px; height: 40px; background-color: #A4A409; display: inline-block;"></span>  
:::

<img src="./images/M-S-DS2g2.png" style="zoom:75%;" />

##### Note e punti {#annotations-and-dots}

[Misure capillari (anche calibrazioni) e trattamenti.](./mainUI#treatments)

::: xdrip <small><small>NOTE E PUNTI</small></small>
Misurazioni Glicemia in Secondo Piano<span style="float: right; width: 40px; height: 40px; background-color: #FFFFFF; display: inline-block;"></span>  


Misurazioni Glicemia in Primo Piano<span style="float: right; width: 40px; height: 40px; background-color: #FF4444; display: inline-block;"></span>  

Terapia in Secondo Piano<span style="float: right; width: 40px; height: 40px; background-color: #FFFFFF; display: inline-block;"></span>  

Terapia in Primo Piano<span style="float: right; width: 40px; height: 40px; background-color: #77AA00; display: inline-block;"></span>  
:::

##### {#}

<img src="./images/M-S-DS2h2.png" style="zoom:75%;" />

##### Sfondi {#backgrounds}

Sfondi dei grafici, grafico principale

::: xdrip <small><small>SFONDI</small></small>
Diagramma Principale in secondo piano  <span style="float: right; width: 40px; height: 40px; background-color: #212121; border: 1px solid #FFFFFF; display: inline-block;"></span>  


Notifiche in secondo piano  <span style="float: right; display: inline-block; width: 40px; height: 40px; background-color: #FFFFFF; background-image: linear-gradient(45deg, #888 25%, transparent 25%, transparent 75%, #888 75%, #888), linear-gradient(45deg, #888 25%, transparent 25%, transparent 75%, #888 75%, #888); background-size: 20px 20px; background-position: 0 0, 10px 10px; border: 1px solid #000;"></span>  

Sfondo grafico Widget <span style="float: right; display: inline-block; width: 40px; height: 40px; background-color: #4C4C4C; background-image: linear-gradient(45deg, #333 25%, transparent 25%, transparent 75%, #333 75%, #333), linear-gradient(45deg, #333 25%, transparent 25%, transparent 75%, #333 75%, #333); background-size: 20px 20px; background-position: 0 0, 10px 10px; border: 1px solid #000;"></span>  
:::

Esempio: sfondo del grafico nella notifica

<img src="./images/M-S-DS2j2.png" style="zoom:75%;" />

##### Plugin e funzionalità {#plugins-and-features}

Se usi un [plugin](../calibrate/advancedcal#plugins), puoi anche visualizzare il valore di glicemia del plugin come grafico secondario.   
Deve essere attiva la visualizzazione del plugin sul grafico.

::: xdrip <small><small>PLUGIN E FUNZIONALITÀ</small></small>
Valore di glicemia del plugin secondario  <span style="float: right; width: 40px; height: 40px; background-color: #292A2B; border: 1px solid #FFFFFF; display: inline-block;"></span>  
:::
      

<img src="./images/M-S-DS2l2.png" style="zoom:75%;" />

Se hai i passi e la frequenza cardiaca da un [dispositivo indossabile](../smartwatch/smartwatch#smartwatch-sensors), puoi personalizzare i colori dei grafici. 

::: xdrip <small><small>PLUGIN E FUNZIONALITÀ</small></small>
Contapassi 1° colore <span style="float: right; display: inline-block; width: 40px; height: 40px; background-color: #CBE5DF; background-image: linear-gradient(45deg, #6B857F 25%, transparent 25%, transparent 75%, #6B857F 75%, #6B857F), linear-gradient(45deg, #6B857F 25%, transparent 25%, transparent 75%, #6B857F 75%, #6B857F); background-size: 20px 20px; background-position: 0 0, 10px 10px; border: 1px solid #000;"></span>  

Contapassi 2° colore <span style="float: right; display: inline-block; width: 40px; height: 40px; background-color: #DEF1F0; background-image: linear-gradient(45deg, #7D908F 25%, transparent 25%, transparent 75%, #7D908F 75%, #7D908F), linear-gradient(45deg, #7D908F 25%, transparent 25%, transparent 75%, #7D908F 75%, #7D908F); background-size: 20px 20px; background-position: 0 0, 10px 10px; border: 1px solid #000;"></span>  

Cardiofrequenzimetro <span style="float: right; display: inline-block; width: 40px; height: 40px; background-color: #DADCF9; background-image: linear-gradient(45deg, #707290 25%, transparent 25%, transparent 75%, #707290 75%, #707290), linear-gradient(45deg, #707290 25%, transparent 25%, transparent 75%, #707290 75%, #707290); background-size: 20px 20px; background-position: 0 0, 10px 10px; border: 1px solid #000;"></span>
:::

Nell'esempio qui sotto: 1. frequenza cardiaca e 2. contapassi.

<img src="../smartwatch/images/M-S-SW8c.png" style="zoom:75%;" />

##### Basale e SMB {#basal-and-smb}

Se riesci a visualizzare la basale ([da AAPS](#basal-information) o con [impostazione manuale](./predictions#basal-profile-editor)), puoi anche personalizzarne il colore.

::: xdrip <small><small>COLORI INSULINA</small></small>
TBR basale <span style="float: right; display: inline-block; width: 40px; height: 40px; background-color: #558AE4; background-image: linear-gradient(45deg, #3F74CE 25%, transparent 25%, transparent 75%, #3F74CE 75%, #3F74CE), linear-gradient(45deg, #3F74CE 25%, transparent 25%, transparent 75%, #3F74CE 75%, #3F74CE); background-size: 20px 20px; background-position: 0 0, 10px 10px; border: 1px solid #000;"></span>  

Icona SMB <span style="float: right; display: inline-block; width: 40px; height: 40px; background-color: #E4DF63; background-image: linear-gradient(45deg, #CEC94D 25%, transparent 25%, transparent 75%, #CEC94D 75%, #CEC94D), linear-gradient(45deg, #CEC94D 25%, transparent 25%, transparent 75%, #CEC94D 75%, #CEC94D); background-size: 20px 20px; background-position: 0 0, 10px 10px; border: 1px solid #000;"></span>  

Linea SMB <span style="float: right; display: inline-block; width: 40px; height: 40px; background-color: #7494D4; background-image: linear-gradient(45deg, #5F7FC0 25%, transparent 25%, transparent 75%, #5F7FC0 75%, #5F7FC0), linear-gradient(45deg, #5F7FC0 25%, transparent 25%, transparent 75%, #5F7FC0 75%, #5F7FC0); background-size: 20px 20px; background-position: 0 0, 10px 10px; border: 1px solid #000;"></span>
:::

<img src="./images/M-S-DS2n2.png" style="zoom:75%;" />

Gli [SMB](#smb) sono icone che alleggeriscono il grafico per i trattamenti con microboli.

<img src="./images/M-S-DS2o2.png" style="zoom:75%;" />

##### Colori luminosi {#flair-colors}

Se vuoi colorare le barre superiore e inferiore dello schermo Android, attiva i colori luminosi.

::: xdrip <small><small>COLORI LUMINOSI</small></small>
Usa colori luminosi  <span style="float: right;"><img src="../images/OFF.png" style="zoom:75%;" /></span>   


Luminosità barra di titolo superiore <span style="float: right; display: inline-block; width: 40px; height: 40px; background-color: #FFFFFF; background-image: linear-gradient(45deg, #888 25%, transparent 25%, transparent 75%, #888 75%, #888), linear-gradient(45deg, #888 25%, transparent 25%, transparent 75%, #888 75%, #888); background-size: 20px 20px; background-position: 0 0, 10px 10px; border: 1px solid #000;"></span>  

Luminosità barra inferiore tasti <span style="float: right; width: 40px; height: 40px; background-color: #000000; border: 1px solid #FFFFFF; display: inline-block;"></span>
:::

Barra del titolo superiore:

<img src="./images/M-S-DS2p2.png" style="zoom:75%;" />

Barra di navigazione inferiore:

<img src="./images/M-S-DS2p3.png" style="zoom:75%;" />

### Impostazioni Caratteri {#font-settings}

::: xdripitem Impostazioni Caratteri
&ensp;Personalizza Caratteri
:::

::: xdripitem Ingrandisci caratteri su schermi grandi<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Allarga automaticamente la dimensione dei caratteri su schermi di grande dimensione, come i tablet
:::

### Lingua {#language}

Per impostazione predefinita xDrip usa la lingua del telefono. Puoi scegliere un'altra lingua per xDrip e forzarne la visualizzazione al posto della lingua del telefono.

Per farlo: 

Seleziona la lingua in Scegli una lingua specifica.

::: xdripitem Scegli una lingua specifica
:::

<img src="./images/M-S-DS3a.png" style="zoom:75%;" />

Porta l'interruttore Forza testo inglese su ON.

::: xdripitem Forza testo inglese<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

### Liscia il rumore del sensore {#smooth-sensor-noise}

Il lisciamento mostra la curva lisciata (non modifica le letture), utile in caso di misurazioni disturbate.  
Puoi anche provare il [Lisciamento del Grafico](#graph-smoothing) per pulire il grafico.

::: xdripitem ⚠ Liscia il rumore del sensore<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Cerca di risolvere letture disturbate
:::

<img src="./images/M-S-DS4a.png" style="zoom:75%;" />

### Mostra Aiuti Interfaccia {#show-interface-hints}

Dopo la prima installazione di xDrip vedrai dei suggerimenti alla prima apertura di alcune funzioni; puoi disattivare questo comportamento o ripristinarlo.

::: xdripitem Mostra Aiuti Interfaccia<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Mostra Suggerimenti / Aiuti descrivendo le funzioni dei vari tasti ecc. Deseleziona e Riseleziona per Reset Iniziale
:::

<img src="./images/M-S-DS5a.png" style="zoom:75%;" />

### Impostazioni grafico {#graph-settings}

Puoi personalizzare la maggior parte degli elementi mostrati nel grafico principale.

::: xdripitem Impostazioni grafico
  &emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_chart_areaspline_grey600_48dp.png" style="width:8%;" />&ensp;Regola gli elementi del grafico
:::

##### Lisciamento del grafico {#graph-smoothing}

::: xdripitem Lisciamento del Grafico
:::

Il lisciamento del grafico applica un filtro di lisciamento al grafico per renderlo più facile da seguire (meno rumore).

È solo un effetto visivo e non influisce sulle letture. 

::: xdripitem Abilita <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Semplifica i grafici lisciando le irregolarità
:::

<img src="./images/M-S-DS6aa9b.png" style="zoom:76%;" />  

<img src="./images/M-S-DS6aa9c.png" style="zoom:76%;" />

::: xdripitem Visualizzazione non lisciata <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Mostra i dati non lisciati anche se il lisciamento è abilitato. Se viene utilizzato un plugin di calibrazione, i dati saranno visualizzati non levigati invece dei dati del plugin.
:::

##### Riscrivi storico {#rewrite-history}

Riscrivi Storico ammorbidisce le transizioni dopo l'aggiunta di una nuova calibrazione, per ridurre l'effetto a gradino.  
Assicurati che sia attivo anche sui follower, per evitare una visualizzazione diversa dei valori di glicemia passati. 

::: xdripitem Riscrivi Storico <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Dopo aver calibrato, regola il grafico dei dati grezzi recenti in modo da regolarlo con la nuovo valore.
:::

<img src="./images/M-S-DS6a2.png" style="zoom:75%;" />

##### Linee di range del widget {#widget-range-lines}

Puoi scegliere di visualizzare le linee dei limiti alto e basso sul widget.

::: xdripitem Linee di range del Widget <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Mostra una linea alta e bassa sul widget.
:::

<img src="./images/M-S-DS6b2.png" style="zoom:75%;" />

##### Linee del grafico principale {#main-graph-lines}

Puoi disattivare le linee verticali del tempo nel grafico principale.

::: xdripitem Mostra Griglia e Linee Temporali <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Rendi visibili le griglie temporali
:::

<img src="./images/M-S-DS6c2.png" style="zoom:75%;" />

Puoi disattivare le linee orizzontali della glicemia nel grafico principale.

::: xdripitem Mostra Griglia e Linee glicemia <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Rendi visibili le linee valori glicemia
:::

<img src="./images/M-S-DS6d2.png" style="zoom:75%;" />

##### Dati filtrati {#filtered-data}

Il grafico filtrato o lisciato aggiunge un'altra curva al grafico e può facoltativamente creare i dati mancanti.

::: xdripitem Mostra Dati Filtrati <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Utile in caso di letture mancanti o non chiare
:::

::: xdripitem Crea dati filtrati mancanti <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Crea i dati filtrati se necessario
:::

<img src="./images/M-S-DS4a.png" style="zoom:75%;" />

Per alcune sorgenti dati (come l'app LL modificata) questo mostrerà i dati grezzi non filtrati, dato che la glicemia visualizzata da xDrip è già filtrata.

<img src="./images/M-S-DS6e2.png" style="zoom:75%;" />

##### Dati grezzi {#raw-data}

Dati grezzi che xDrip può visualizzare, se disponibili.

::: xdripitem Mostra Dati Grezzi (RAW) <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

G4, G5 e G6 con batteria sostituita forniscono dati grezzi.

<img src="./images/M-S-DS6f2.png" style="zoom:75%;" />

Oggi i dati grezzi sono visibili soprattutto per i sensori Libre, ma non con questa opzione.  
Per i dati grezzi dei sensori Libre usa le [Impostazioni avanzate per Libre 2](./lesscommon#advanced-settings-for-libre-2).

##### Informazioni sulla basale {#basal-information}

Se le informazioni sulla basale sono disponibili da una sorgente esterna ([AAPS NSClient](https://androidaps.readthedocs.io/en/latest/index.html)), xDrip può visualizzarle.

In AAPS/NSClient:

- Config builder

- Synchronization - xDrip settings
- Attiva Send status line to xDrip

<img src="./images/NSClient.png" style="zoom:75%;" />

In xDrip: 

- Impostazioni - Impostazioni Meno Usate - attiva Riga di stato extra - attiva [Stato Esterno](./lesscommon#extra-status-line)
- Impostazioni - Impostazioni Inter-app - attiva [Accetta trattamenti](./interapp#receiving-from-nsclient)
- Attiva Mostra TBR basale

::: xdripitem Mostra TBR basale <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

<img src="./images/M-S-DS2n2.png" style="zoom:75%;" />

Le informazioni sulla basale vengono caricate anche su [Tidepool](./cloud#tidepool).

##### Linee del target e della media {#target-and-average-lines}

Puoi visualizzare diverse linee di riferimento sul grafico:

::: xdripitem Mostra Linea Target su Grafico <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

::: xdripitem Mostra Media recente su grafico <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

::: xdripitem Mostra Media Totale su Grafico <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

1. Linea della media delle 8 ore (recente)
2. Linea della media delle 24 ore (totale)
3. Linea del [target](./predictions#low-level-prediction)

<img src="./images/M-S-DS2g2.png" style="zoom:75%;" />

##### Tendenza Libre {#libre-trend}

[Tendenza Libre](./3dotsmenu#libre-trend) attiva un piccolo grafico disponibile nel menu a tre puntini della schermata principale.

::: xdripitem Mostra tendenza Libre <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

##### Previsioni G6 {#g6-predictions}

Predizione G6 è una funzione integrata del trasmettitore Dexcom G6, mostrata con piccoli punti grigi.

::: xdripitem Predizione G6 <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Mostra i punti di glicemia predittiva G6
:::

<img src="./images/M-S-DS6j2.png" style="zoom:75%;" />

##### SMB {#smb}

Gli SMB sono icone che alleggeriscono il grafico per i trattamenti con microboli. Toccando un SMB, la quantità di insulina compare nella riga informativa.

::: xdripitem Mostra icone microbolo <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

<img src="./images/M-S-DS6k2.png" style="zoom:75%;" />

::: xdripitem Medtrum secondario <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

Mostra i valori del sensore secondario Medtrum A6.

##### Momentum della tendenza {#trend-momentum}

::: xdripitem Mostra Curva Momentum <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

Mostra una linea rossa tratteggiata (1), il momentum, che estrapola la tendenza attuale della glicemia per prevedere ipo e iper.  
È del tutto indipendente dalle [previsioni](./predictions#use-trend-momentum) (2) e non tiene conto dei modelli dei carboidrati o dell'insulina.

<img src="./images/M-S-PS5b.png" style="zoom:75%;" />

##### Calcolo del rumore {#noise-workings}

Informazioni visive aggiuntive sul calcolo del rumore: una linea gialla di cinque punti a destra della curva.

::: xdripitem Mostra Letture Disturbate <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

<img src="./images/M-S-DS6e2.png" style="zoom:75%;" />

##### Dati recuperati {#backfilled-data}

I dati recuperati a posteriori (backfill) possono essere indicati con un punto blu vuoto.

::: xdripitem Mostra i dati ricuperati dal sensore <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

<img src="./images/M-S-DS6n2.png" style="zoom:75%;" />

##### Grafico del widget {#widget-graph}

Puoi nascondere il grafico nel [widget](./mainUI#widget) e lasciare solo il valore.

::: xdripitem Nascondi grafico widget <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

<img src="./images/M-S-DS6o2.png" style="zoom:75%;" />

Queste due opzioni sono disponibili solo per gli sviluppatori.

::: xdripitem Illustra i dati remoti <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

##### Asse Y {#y-axis}

L'asse verticale della schermata principale ha un minimo predefinito di 40 mg/dl (2,22 mmol/l) e un massimo predefinito di 250 mg/dl (13,9 mmol/l).

Puoi fissare a piacere i valori minimo e massimo dell'asse Y.

::: xdripitem Consentire
:::

Per impostazione predefinita, quando le letture sono fuori da questo intervallo, il grafico estende temporaneamente l'intervallo per renderle visibili, poi torna ai valori fissati quando quelle letture escono dallo schermo.

Se preferisci mantenere fisso l'intervallo dell'asse Y e spostare il grafico in verticale invece di espanderlo, attiva Spostamento auto asse Y.

::: xdripitem Spostamento auto asse Y <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;**Abilita:** Sposta il grafico con un asse Y fisso (minimo-massimo) per mostrare le letture fuori intervallo.  
&ensp;**Disabilita:** Espandi l'intervallo dell'asse Y per includere le letture fuori intervallo.
:::

### Numero di glucosio da Filtrata {#glucose-number-from-filtered}

Il filtraggio può ritardare le letture e non è consigliato.  
Il filtraggio è integrato nell'hardware per la [sorgente dati app Libre 2 modificata](../install/libre2patch).

::: xdripitem Numero di glucosio da Filtrata <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

<img src="./images/M-S-DS6e2.png" style="zoom:75%;" />

### Anteprima della guida automatica di bolo {#bolus-wizard-preview}

La BWP mostra l'insulina attiva (IoB) e suggerisce correzioni in base ai parametri [predittivi](./predictions) inseriti in xDrip.  
È solo un'indicazione. Assicurati di aver capito l'EULA prima di usarla.  
Non seguire mai i suggerimenti quando la glicemia cambia rapidamente.

L'anteprima della guida automatica di bolo compare solo quando sono presenti carboidrati o insulina.

::: xdripitem Mostra l'anteprima della guida automatica di bolo <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Visualizza calcoli Insulina/CHO
:::

<img src="./images/M-S-DS6s3.png" style="zoom:75%;" />

::: xdripitem Mostra sempre l'anteprima della guida automatica di bolo <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Visualizza sempre i calcoli Insulina/CHO
:::

Se forzi la visualizzazione costante della BWP, suggerirà sempre una correzione (insulina o carboidrati).

<img src="./images/M-S-DS6s2.png" style="zoom:75%;" />

### Notifiche ad alta priorità {#high-priority-notifications}

Porta il [grafico e le notifiche](./misc#run-collector-in-foreground) di xDrip in cima all'elenco; disattivandola, scendono.

Puoi disattivare Notifiche ad alta priorità se preferisci avere xDrip più in basso nell'elenco delle notifiche. Su Android 8.0 e successivi il [collector è sempre eseguito in primo piano](./misc#run-collector-in-foreground), quindi Android non metterà xDrip in sospensione.

::: xdripitem Notifiche ad alta priorità<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Mostra notifiche e grafico in alto (anche nella schermata di blocco)
:::

<img src="./images/M-S-DS2j2.png" style="zoom:75%;" />

### Notifiche pubbliche {#public-notifications}

Rende le notifiche visibili sulla schermata di blocco.

::: xdripitem Notifiche pubbliche <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

### Abilita funzionalità promemoria {#enable-reminder-features}

Attivata per impostazione predefinita: trovi i promemoria nel [menu a tre puntini](./3dotsmenu) in alto a destra nella schermata principale.

::: xdripitem Abilita funzionalità promemoria <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Mostra menu e funzionalità di promemoria 
:::

### Impostazioni Sempre Visibile {#always-on-display-settings}

Se il telefono lo supporta, xDrip può usare l'accessibilità di Android per mostrare il suo widget nella schermata sempre attiva (Always On Display).

::: xdripitem Abilita Accessibilità xDrip
&ensp;Se il telefono ha Always On Display è possibile abilitare il widget xDrip attivando il servizio di accessibilità xDrip dalla pagina Impostazioni di sistema Android.
:::

<img src="./images/M-S-DS6x2.png" style="zoom:75%;" />

<img src="./images/M-S-DS6x3.png" style="zoom:75%;" />

Su Android 16 e successivi puoi in alternativa mostrare la glicemia come chip di notifica sulla schermata di blocco / Always On Display, usando la notifica persistente invece dell'accessibilità. Questo si basa sui [canali di notifica](./alarms#notification-channels), sempre attivi su Android 8.0 e successivi.

::: xdripitem Use AOD chip style <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Display notification chip and lockscreen notification. Android 16+ only
:::

### Valore della glicemia nella schermata di blocco {#numbered-wall-on-locked-screen}

xDrip può mostrare il valore della glicemia sulla schermata di blocco del telefono.

::: xdripitem Valore della glicemia nella schermata di blocco
:::

Questo menu ti permette di personalizzare il numero visualizzato.

::: xdripitem Configurazione
Regolazioni ed anteprima
:::

Vedrai un'anteprima in tempo reale del risultato (123 ⇅)

1. Cambia la dimensione del carattere
2. Cambia la posizione verticale (o la distanza verticale tra i numeri)
3. Cambia la posizione orizzontale (o la distanza orizzontale tra i numeri)
4. Cambia il colore del numero
5. Seleziona l'immagine di sfondo
6. La schermata con il numero vera e propria

<img src="./images/M-S-DS6z2.png" style="zoom:75%;" />

Attiva la visualizzazione sulla schermata di blocco per mostrare il numero.

::: xdripitem Visualizza sulla schermata di blocco<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Mostra nella schermata di blocco. Android 7 e sopra!
:::

Per impostazione predefinita il numero sulla schermata di blocco usa gli stessi colori della glicemia bassa/nell'intervallo/alta della schermata principale. Puoi forzarlo a usare sempre un unico colore fisso.

::: xdripitem Colore testo imposto<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Abilita: Usa sempre il colore di testo selezionato.  
&ensp;Disabilita: Usa i colori della glicemia nella schermata principale (bassa / nell'intervallo / alta).
:::

::: xdrip Valore della glicemia nella schermata di blocco
Colori<span style="float: right; width: 40px; height: 40px; background-color: #FFFFFF; display: inline-block;"></span>  


Colore ombra<span style="float: right; width: 40px; height: 40px; background-color: #000000; display: inline-block;"></span>  
:::
      

Attiva e disattiva la funzione per un periodo definito della giornata. Per impostazione predefinita è attiva tutto il giorno.

::: xdripitem Accendi
Scegli l'orario di inizio visualizzazione
:::

::: xdripitem Orario spegnimento
Scegli l'orario di fine visualizzazione - setti uguale a l'inizio per averlo sempre visibile
:::

### Icona numerica nell'area di notifica {#number-icon-in-notification-area}

xDrip può mostrare la glicemia come icona numerica nell'area di notifica in alto a sinistra e nelle notifiche a discesa.

<img src="./images/M-S-DS6aa6.png" style="zoom:75%;" />

::: xdripitem Icona numerica nell'area di notifica
:::

**Prova la funzione prima di usarla, perché su alcuni telefoni può causare un crash.**

::: xdripitem Esegui test icona numerica
&ensp;Le icone numeriche bloccano alcuni telefoni! Esegui il test prima di abilitare la funzione!
:::

<img src="./images/M-S-DS6aa5.png" style="zoom:75%;" />

Durante il test il telefono vibrerà alcune volte e dovresti vedere l'icona della glicemia 123 in alto a sinistra.

<img src="./images/M-S-DS6aa7.png" style="zoom:75%;" />

Se non funziona, significa che non devi attivare la funzione.

**Una volta confermato il funzionamento** puoi attivarla.

::: xdripitem Icona numerica testata<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Quando avrai confermato che il tuo dispositivo può mostrare l'icona numerica
:::

::: xdripitem Mostra icona numerica piccola<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Mostra il valore della glicemia come icona nella barra di notifica e la schermata di blocco
:::

### Mostra xDrip all'avvio {#show-xdrip-on-boot}

Con questa opzione xDrip si apre automaticamente al riavvio del telefono.

Può essere utile attivarla se il telefono esegue aggiornamenti e riavvii automatici (sconsigliato) e xDrip non si avvia da solo al riavvio. 

::: xdripitem Mostra xDrip all'avvio <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Apri automaticamente lo schermo xDrip dopo l'avviamento del telefonino
:::

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
