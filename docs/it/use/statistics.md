---
source_hash: cf4c58239c
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_chart_areaspline_grey600_48dp.png" style="width:5%;" /> Statistiche
:::

La schermata Statistiche offre 3 visualizzazioni statistiche di base che puoi configurare per diversi periodi di tempo.

1. Per prima cosa seleziona il periodo su cui calcolare le statistiche: oggi, ieri, ultimi 7, 30 o 90 giorni.
2. Puoi visualizzare il grafico a schermo intero (toccalo di nuovo per uscire dalla modalità a schermo intero).
3. Puoi condividere la schermata come screenshot.

<img src="./images/M-STA1.png" style="zoom:75%;" />

<br>

La prima schermata mostra i tuoi numeri.

<img src="./images/M-STA2.png" style="zoom:75%;" />

La percentuale nel range è calcolata usando i valori basso e alto definiti in Menu - Unità di Misura Glicemia.  
I numeri assoluti contano le misure nel range, sopra e sotto.  
La glicemia mediana è il valore centrale dei tuoi dati: lo stesso numero di misure sta sopra e sotto.  
La glicemia media è la media aritmetica di tutte le misure.  
L'HbA1c stimata è solo un calcolo matematico basato sulla glicemia media, convertito in mmol/mol o in percentuale.  
La StdDev, o deviazione standard, è il risultato di un calcolo matematico. Mostra la dispersione della tua glicemia.  
La SD relativa (CV) è la StdDev divisa per la media e mostra anch'essa la dispersione delle tue misure.  
GVI e PGS sono parametri introdotti da Dexcom, vedi [qui](https://web.archive.org/web/20160523152519/http://www.healthline.com/diabetesmine/a-new-view-of-glycemic-variability-how-long-is-your-line). 

Guarda [qui](https://diatribe.org/understanding-average-glucose-standard-deviation-cv-and-blood-sugar-variability) per la spiegazione di questi parametri, e ricorda che si basano sulle misure e dipendono dalla loro qualità. Misure sbagliate (imprecise) daranno statistiche sbagliate, che dipenda dalla precisione del sensore o dalle tue calibrazioni.

Puoi scegliere quali di questi valori mostrare. Tocca il menu (⋮) in alto a destra e seleziona `Parameters`, poi spunta o togli la spunta a: Numeri assoluti, Glicemia Mediana, HbA1c stimata, STD relativa, GVI, PGS, Deviazione Standard.

<br>

Scorri verso sinistra per vedere una rappresentazione grafica della percentuale nel range.  
Il verde è nel range, il giallo sopra e il rosso sotto l'obiettivo.

<img src="./images/M-STA3.png" style="zoom:75%;" />

<br>

Scorri di nuovo per vedere il grafico dei percentili.

<img src="./images/M-STA4.png" style="zoom:75%;" />

Ruota lo schermo per una visualizzazione migliore.

<img src="./images/M-STA5.png" style="zoom:50%;" />

<br>

[*Ultima modifica 6/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.03)
