---
source_hash: b31e419e7a
source_commit: 7a18e7c
---
::: warning Calibrazione
Non fidarti mai ciecamente di un sensore di glicemia: verifica regolarmente le letture con una glicemia capillare.  
Una linea piatta (sempre lo stesso numero) **non** è mai un buon segno.
:::

### Considerazioni generali {#general-considerations}

La calibrazione è fondamentale per la precisione delle misure del CGM. Usa sempre un glucometro affidabile e mettiti nelle condizioni migliori per avere la misura capillare più precisa possibile quando calibri.

Alcuni dei prerequisiti più importanti sono:

1. **Glicemia stabile.** Non calibrare mai quando la glicemia sale o scende rapidamente.
2. **Nell'intervallo (importante per la calibrazione iniziale di Libre).** Cerca di eseguire le calibrazioni quando la glicemia è nell'intervallo normale (80-180 mg/dl o 5-10 mmol/l).
3. **Non calibrare troppo.** Meglio poche calibrazioni precise che troppe: molto probabilmente confonderesti xDrip. Per G6, G7, 1, 1+ segui le raccomandazioni del produttore.

### Algoritmo nativo e algoritmo di xDrip {#native-and-xdrip-algorithms}

xDrip può fornire i propri algoritmi di calibrazione per i sensori che inviano dati grezzi.

Con la calibrazione nativa di G6, G7, 1, 1+, xDrip non usa il proprio algoritmo ma invia i valori di calibrazione al trasmettitore, lasciando che li gestisca con il suo algoritmo proprietario.

I sensori Libre 1, 14 giorni, Pro, 2 (UE) e 2+ (UE) inviano solo dati grezzi e hanno bisogno o della calibrazione di xDrip o di un plugin di calibrazione esterno chiamato [algoritmo OOP (out of process algorithm)](../use/OOP).

L'app modificata Libre 2 usa il proprio algoritmo proprietario (anche se in una versione vecchia).

| Sensore                          | Calibrazione xDrip              | Calibrazione nativa |
| ------------------------------- | ------------------------------- | ------------------ |
| G6 con batteria sostituita                  | Disponibile                       | Disponibile          |
| G6, G7, 1, 1+                   | Non disponibile                   | Obbligatoria          |
| Libre 1                         | Obbligatoria                       | OOP1 (obsoleto)    |
| Libre 2 UE app modificata          | Scostamento limitato (vedi sotto)      | Per costruzione          |
| Libre 2/2+ UE, Libre 14 giorni USA | [Facoltativa](../use/OOP#oop2) | OOP2               |

##### App modificata Libre 2 {#libre-2-patched-app}

Con l'app modificata puoi calibrare, ma la correzione viene applicata come scostamento (offset) con valori massimi tra -40 mg/dl e +20 mg/dL [-2,2 mmol/l e +1,1 mmol/l]. Le calibrazioni che non rispettano questi criteri vengono **ignorate**.

### Impostazioni di calibrazione di xDrip {#xdrip-calibration-settings}

::: warning Solo calibrazione xDrip
Le informazioni qui sotto riguardano la calibrazione di xDrip.  
Per la modalità nativa di G6/G7/1/1+ vedi [qui](https://navid200.github.io/xDrip/docs/Dexcom_page.html).
:::

Prima di calibrare controlla le tue [impostazioni](./advancedcal).

Una cosa che conviene attivare sono le [tabelle dati](../use/lesscommon#show-data-tables) nel menu principale. Ti aiuteranno davvero a capire quando qualcosa va storto.

### Prima calibrazione {#first-calibration}

Se il tuo sensore richiede calibrazioni, dopo averlo collegato a xDrip e aver ricevuto tre valori dovresti vedere questa richiesta:

::: xdripitem Calibrare il sensore?
&emsp;Abbiamo alcune letture!  


&ensp;Ci servirà il valore della prima misura capillare.  

&ensp;Pronto per calibrare ora?  

&emsp;NO&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;CALIBRA&ensp;</span>
:::

I due valori di calibrazione iniziali sono un'eredità del G4. Se vuoi usarli correttamente, esegui due misure diverse (due strisce): è l'approccio consigliato. Se di solito inserisci lo stesso valore, puoi renderlo predefinito [qui](./advancedcal#calibrations).

::: xdrip ☰&emsp;Calibrazione iniziale
&emsp;<u>Inserisci Primo Valore Glicemia</u>  
&emsp;<u>Inserisci Secondo Valore Glicemia</u>  

&emsp;<small>Per iniziare, si prega di effettuare due test della Glicemia e inserire i valori qui!</small>    
:::

Se usi la calibrazione nativa, il valore viene inviato al trasmettitore per l'elaborazione.

Se usi la calibrazione di xDrip, questo valore viene elaborato 10 minuti dopo, per compensare tutti i ritardi fisiologici e chimici della misura del CGM: **per questo è estremamente importante calibrare con glicemia stabile**.

Vediamo graficamente cosa succede nella schermata principale:

1. Prima lettura (riportata al valore di calibrazione)
2. Seconda lettura (riportata al valore di calibrazione)
3. Non ancora visibile, ma è la terza lettura: il valore effettivo al momento della calibrazione
4. Lettura successiva tra 5 minuti
5. Lettura successiva tra 10 minuti e punto di calibrazione (che verrà usato tra 10 minuti)

<img src="./images/CAL03.png" />

Se la glicemia è rimasta stabile in questo periodo, dovresti vederla passare per il punto di calibrazione.

<img src="./images/CAL04.png" />

Nella tabella dati di calibrazione vedrai nuove voci che corrispondono alle misure di glicemia grezza usate per definire la calibrazione:

1. È il valore che hai inserito (convertito in mg/dl se necessario)
2. Stesso valore, ma nell'unità che usi con xDrip (qui in mg/dl, ma comparirà anche in mmol/l)
3. Glicemia grezza del sensore
4. Pendenza e intercetta calcolate
5. Data e ora effettive della calibrazione (cioè l'ora reale + 10 minuti) e data e ora della glicemia grezza corrispondente
6. Per una calibrazione ci sono due serie di misure di dati grezzi: una più bassa, una più alta

<img src="./images/CAL05.png" style="zoom:75%;"  />

Il grafico di calibrazione sarà ora più o meno così.  
A seconda della differenza tra i campioni di sangue e della variabilità della glicemia attuale, la pendenza potrebbe non essere esattamente 1.

<img src="./images/CAL06.png" style="zoom:75%;"  />

### Calibrazioni successive {#successive-calibrations}

Per sicurezza controllerai regolarmente la tua glicemia reale, almeno una volta al giorno, perché non puoi fidarti ciecamente di un sensore. Inserisci queste glicemie capillari come [trattamenti](../use/mainUI#treatments).  
Perché i valori di glicemia non varino troppo rapidamente, non dovresti calibrare quando in quel momento hai carboidrati o insulina attivi.

::: info Frequenza
A meno che il tuo sensore non lo richieda espressamente, non calibrare sistematicamente ogni volta che fai una glicemia capillare.  
Per i sensori Libre, non è necessario calibrare se la differenza è inferiore al 15%.
:::

**Non calibrare troppo**: puoi fare tutte le glicemie capillari che vuoi e inserirle come trattamenti in xDrip, ma aggiungi calibrazioni con particolare attenzione.

Nel grafico di calibrazione vedrai i punti di calibrazione attivi in blu e quelli vecchi o non validi in grigio.

<img src="./images/CAL15.png" style="zoom:75%;"  />

Se, con glicemia stabile, confrontando il valore di xDrip 10 minuti dopo la glicemia capillare, vedi che il valore è troppo diverso, aggiungerai un altro punto di calibrazione.

Poiché l'andamento della glicemia è spesso difficile da prevedere, puoi usare un trucco:

- Verifica che Usa i valori di glicemia dei trattamenti non sia impostato su Never Use Them in [Calibrazione avanzata](./advancedcal).
- Inserisci la glicemia capillare come trattamento.

<img src="./images/CAL07.png" style="zoom:75%;"  />

- Attendi 10 minuti e valuta se sarebbe stato un buon momento per calibrare (glicemia abbastanza stabile).

<img src="./images/CAL08.png" style="zoom:75%;"  />

- Se lo era, tocca il trattamento (la nuova glicemia capillare, punto quadrato bianco sul grafico) e trasformalo in una calibrazione.

::: xdripitem Azione su misura capillare

&emsp;Che cosa vorresti fare?  

  &emsp;NIENTE&emsp;CANCELLA&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;CALIBRA&ensp;</span>
:::

Ora hai un altro punto di calibrazione.

<img src="./images/CAL09.png" style="zoom:75%;"  />

### Disattivare una calibrazione {#disable-a-calibration}

Può succedere che un punto di calibrazione sia chiaramente sbagliato e che tu voglia eliminarlo.

Apri la Tabella dati di calibrazione e **tieni premuta** la calibrazione che vuoi disattivare.

<img src="./images/CAL10.png" style="zoom:75%;"  />

::: xdripitem Disable this calibration?
Flagged calibrations will no longer have an effect.  

&emsp;&emsp;&emsp;NO&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;SI&ensp;</span>
:::

Comparirà in rosso e non verrà più usata nel calcolo.

<img src="./images/CAL11.png" style="zoom:75%;"  />

### Azzerare tutte le calibrazioni {#reset-all-calibrations}

Questo metodo vale solo per i sensori che supportano la calibrazione di xDrip.

**Non usarlo per i sensori solo a calibrazione nativa (G6 nuovi, G7, 1, 1+ ecc.).**

Quando diventa chiaro che le calibrazioni attuali sono sbagliate, o se non hai dati dopo aver calibrato, il modo più rapido per ripartire da zero con la calibrazione (Calibrazione iniziale) è azzerare tutte le calibrazioni.

Dal menu principale, Stop Sensore.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Stop Sensore  
:::

**Non fermare il sensore**: azzera solo tutte le calibrazioni.

::: xdripitem <img src="../images/BDM.png" style="zoom:75%;" /> Arresto Sensore <span class='symbol'></span>
  &emsp;Ferma il tuo sensore solo quando pensi di rimuoverlo, altrimenti lascialo avviato!  

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;NON FERMARE, RESETTA SOLO TUTTE LE CALIBRAZIONI&ensp;</span>
:::

::: xdripitem Sei sicuro?
  &emsp;Eliminare e resettare le calibrazioni per questo sensore?  

 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;NO &emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;SI&ensp;</span>
:::

xDrip ti riporterà alla [calibrazione iniziale](#first-calibration). Assicurati di eseguire questa operazione con glicemia stabile, nell'intervallo.

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
