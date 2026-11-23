---
source_hash: d8b53e5b65
source_commit: 7a18e7c
---
Questo menu contiene alcune impostazioni e meccanismi importanti per la calibrazione.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;"/>
&ensp;Impostazioni  
&emsp;Impostazioni Meno Usate  
&emsp;&ensp;Calibrazione avanzata
:::

##### Usa i valori di glicemia dei trattamenti {#use-treatment-bg-values}

Puoi decidere di usare i [trattamenti](../use/mainUI#treatments) di glicemia (glicemie capillari) come calibrazioni.

::: xdripitem Usa i valori di glicemia dei trattamenti
&ensp;Scegli se calibrare con il valore di glicemia aggiunto come trattamento  
:::

::: warning Attenzione
Usare sempre i trattamenti come calibrazioni **non è consigliato**.
:::

La modalità automatica ti propone di usare il trattamento come calibrazione solo se xDrip rileva che le condizioni attuali sono buone per calibrare (ad esempio glicemia stabile da 20 minuti, poco rumore).

::: xdripitem Usa i valori di glicemia dei trattamenti
&emsp;Automatic mode (best)<span style="float: right;">●&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;Ask me every time<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;Never use them<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;Always use them<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp; 
:::

Potrebbe anche proporti di attivare la calibrazione automatica.  

**Non è consigliato usare questa funzione con i sensori G6/G7/1/1+.**

::: xdripitem Abilita la calibrazione automatica
&emsp;Le glicemie capillare effettuate durante periodi stabili possono essere utilizzate automaticamente per ricalibrare dopo 20 minuti. Questo dovrebbe essere il modo più preciso per calibrare  


&ensp;Attivare questa funzionalità?  

&emsp;<span style="background-color: white; color: black;">&ensp;NO&ensp;</span>&emsp;&emsp;&emsp;&emsp;SI, ABILITA
:::

Ask me every time (chiedimi ogni volta) fa esattamente questo ogni volta che inserisci un trattamento di glicemia.

::: xdripitem Usare questa capillare per calibrare?
&emsp;Vuoi usare questa glicemia capillare per calibrare?  
:::

Never use them (non usarli mai) non li usa mai per calibrare (e ti impedisce di trasformare un [trattamento](../use/mainUI#treatments) in una calibrazione).

##### Calibrazione automatica {#automatic-calibration}

Si consiglia di **disattivarla con i sensori G6/G7/1/1+**.

La calibrazione automatica accetta un trattamento come calibrazione se soddisfa la condizione di un andamento piatto per 20 minuti.

::: xdripitem Calibrazione automatica <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Calibra automaticamente utilizzando le letture di glicemia se le condizioni sembrano giuste, senza chiedere conferma (sperimentale)  
:::

### Plugin {#plugins}

In xDrip sono disponibili dei plugin di calibrazione, ma la maggior parte non viene più usata. Se attivato, un plugin agisce al posto della calibrazione standard di xDrip. L'idea era di offrire una scelta personalizzabile dell'algoritmo di calibrazione, ma non è mai stata implementata del tutto. In generale, per ragioni di sicurezza, un sensore che ha bisogno di un plugin per essere calibrato andrebbe sostituito.

::: warning **SICUREZZA**
**I meccanismi di sicurezza della calibrazione non si applicano ai plugin. Usare un plugin per aggirare un errore di calibrazione è pericoloso.**
:::

::: xdripitem Plugin di calibrazione
&ensp;Plugin di calibrazione secondaria sperimentale  
:::

::: warning Estensione Wear
I plugin non sono implementati del tutto in Wear. Potresti vedere valori diversi sullo smartwatch.
:::

::: xdripitem Plugin di calibrazione
&emsp;None  
&emsp;Datricsae  
&emsp;Fixed slope - **NON USARE**  
&emsp;xDrip   
&emsp;Last7Ua
:::

**`None`**: per impostazione predefinita viene usato l'algoritmo di xDrip. **Consigliato**

**`Datricsae`** era molto usato da chi aveva problemi con l'algoritmo predefinito di xDrip. Richiede 8 punti di calibrazione (se sono meno di 4 viene usato l'algoritmo originale di xDrip) e ha limiti di pendenza tra 0,5 e 1,7. Il suo punto di forza principale è eliminare i valori anomali (punti di calibrazione sbagliati) che cadono troppo lontano dalla retta di calibrazione. Dopo il filtraggio, se il numero di punti di calibrazione scende sotto 4 o la pendenza è fuori dai limiti, viene usato l'algoritmo classico di xDrip.  
Fai attenzione: calibrazioni rumorose possono portare a risultati incoerenti.

<img src="./images/M-S-LCS-AC3d.png" style="zoom:75%;" />

**`Fixed slope`** è un plugin vuoto che restituisce una pendenza di 1,08 e un'intercetta di -5. **Non usarlo per la glicemia reale.**

**`xDrip Original`** era l'equivalente in forma di plugin dell'algoritmo di xDrip. Non fa nulla di diverso dall'algoritmo di xDrip. **Usarlo non porta alcun vantaggio.**

**`Last 7 unweighted`** è stato un primo tentativo di migliorare l'algoritmo originale. Richiede almeno 4 calibrazioni (usa al massimo le ultime 7; sotto le 4 viene usato l'algoritmo attuale di xDrip). **Non consigliato.**

::: xdripitem Grafico dei valori Plugin <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Mostra i risultati della glicemia dal plugin sul grafico principale  
:::

Attivalo se vuoi che xDrip tracci i risultati ottenuti con il plugin.

<img src="../use/images/M-S-DS2l2.png" style="zoom:75%;" />

::: xdripitem Usa un Plugin Glucosio <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;La visualizzazione del valore di glicemia principale proviene dal plugin!  
:::

Attivalo se vuoi che il valore principale della glicemia provenga dai risultati del plugin. Comparirà una P cerchiata.

<img src="./images/M-S-LCS-AC5a.png" style="zoom:75%;" />

::: xdripitem Ignorare TUTTI i Plugin <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;La visualizzazione del valore di glicemia principale proviene dal plugin!  
:::

Non implementato.

### Calibrazioni {#calibrations}

::: xdripitem Calibrazione doppia <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Richiedi una seconda calibrazione capillare iniziale facoltativa  
:::

Se per la calibrazione iniziale non esegui davvero due glicemie capillari distinte, disattivala.

La Modalità di calibrazione Vecchia Scuola ripristina l'intervallo originale, più stretto, di pendenze consentite nell'algoritmo di calibrazione classico di xDrip (prima del 2017), rendendo più probabili le pendenze predefinite. È visibile solo con la Modalità Sviluppatore attivata.

::: xdripitem Modalità di calibrazione Vecchia Scuola <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Intervallo originale (più stretto) di fattori consentiti nell'algoritmo di calibrazione classico xDrip (pre-2017). Preferire quelli predefiniti perché più probabili! (solo modalità ingegneristica)
:::

::: xdripitem Calibrazioni poco frequente <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Se necessario, usa calibrazioni più vecchie, es.: se le calibrazioni vengono fatte raramente.  
:::

Le calibrazioni troppo vecchie vengono ignorate: se calibri raramente e vuoi che le misure di calibrazione più vecchie pesino sulla curva di calibrazione attuale, attiva questa opzione. 

### Specifico per Libre {#libre-specific}

##### Calibrazione non linear per Libre {#non-fixed-libre-slopes}

::: xdripitem Calibrazione non linear per Libre <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Abilitare per permettere la calibrazione non lineare (pendenze variabile) per il sensore Libre  
:::

I sensori Libre possono essere difficili da calibrare. Se non riesci a ottenere precisione su tutto l'intervallo o non calibri mai nell'intervallo alto, disattiva questa opzione e rendi la pendenza uguale a 1. È consigliato ai principianti.

**Per sicurezza, calibra sempre con glicemia stabile nella parte bassa dell'intervallo normale.**

::: xdripitem Check Libre Serial <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Automatically stop if Libre Serial changes unexpectedly  
:::

Trasferire le calibrazioni dal vecchio sensore a quello nuovo è pericoloso. **Lascia questa opzione attivata.**

### Ignora il controllo di qualità {#bypass-quality-check}

::: xdripitem Ignora il controllo di qualità <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Consenti la calibrazione iniziale anche se non disponiamo di dati abbastanza validi. Attenzione potrebbe causare una calibrazione imprecisa!  
:::

Durante le misure preliminari per la prima calibrazione sono necessarie 3 misure valide. Se mancano o non rispettano i valori di sicurezza, xDrip attende. Attivando questa opzione la calibrazione è consentita senza controllo. **Non consigliato.**

::: xdripitem Sto raccogliendo le prime letture
&ensp;✔ Raccolta dati in esecuzione  
&ensp;✔ Ricezione dati dal collector  
&ensp;✔ Ho ricevuto alcuni dati recenti  
&ensp;⧖ Ho ricevuto abbastanza dati per calibrare  
&ensp;**Need 3 recent readings, got only one so far**  
&ensp;Next reading expected in 1 minute 
:::

<br>

[*Ultima modifica 15/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
