---
source_hash: 74f3d09e63
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="./images/CrystalBall.png" style="width:5%;" />&ensp;Simulazioni predittive
:::

Le impostazioni di simulazione predittiva di xDrip sono una funzione sperimentale, non approvata in ambito medico. Assicurati di rileggere l'[EULA](../install/install#understand-what-is-xdrip) prima di attivarle. Non usarle per prendere decisioni mediche.

::: warning Attenzione
Se usi un sistema a loop chiuso non fare affidamento su queste previsioni, perché non tengono conto della modulazione della basale.
:::

::: xdripitem Simulazioni predittive
&ensp;Visualizza simulazioni matematiche basate sui dati del profilo e i log di CHO/insulina
:::

Attivando le previsioni, sul grafico principale compare la curva di previsione viola chiaro. Questa curva ti mostra come dovrebbe evolvere in teoria la tua glicemia in base all'insulina e ai carboidrati inseriti in xDrip. Maggiori dettagli sulla visualizzazione [qui](./display#treatments-and-predictions-curves).

<img src="./images/M-S-PS1a.png" style="zoom:75%;" />

xDrip può gestire più tipi di insulina. Vedi [sotto](#multiple-insulin-types).

::: xdripitem Tipi Multipli di Insulina
&ensp;Opzioni per lavorare con multipli tipi di insulina
:::

### Rapporto carboidrati e sensibilità insulinica {#carb-ratio-and-insulin-sensitivity}

::: info Importazione automatica
Se [accetti i trattamenti](./interapp#receiving-from-nsclient) da AAPS o NSClient, questi parametri e il profilo basale verranno importati automaticamente al cambio di profilo.
:::

Questi parametri sono fondamentali nella gestione del diabete e dovresti conoscerli.  
Molto probabilmente variano durante la giornata e andrebbero calcolati per ogni pasto e anche al di fuori dei pasti.  
Ognuno ha i propri parametri. Non usare quelli di altre persone.

Il rapporto carboidrati è la quantità di carboidrati coperta da 1 unità di insulina.

Ad esempio 10 significa che ogni 10 g di carboidrati richiedono 1 unità di insulina.

::: xdripitem Rapporto UI/CHO
&ensp;Grammi di carboidrati che copre 1 unità
:::

La sensibilità insulinica è il calo di glicemia che risulta da un'unità di insulina, senza carboidrati in circolo.

Ad esempio 50 (o 2,8) significa che 1 unità abbassa la glicemia di 50 mg/dl (o 2,8 mmol/l).

::: xdripitem Fattore di correzione
&ensp;Valore di abbassamento glicemia per 1 unità di insulina
:::

### Tasso di assorbimento dei carboidrati {#carb-absorbtion-rate}

Il tasso di assorbimento dei carboidrati è la velocità con cui il tuo corpo assimila i carboidrati. Vedi [qui](https://diyps.org/2014/05/29/determining-your-carbohydrate-absorption-rate-diyps-lessons-learned/) come calcolare questo parametro.

::: xdripitem Tasso di assorbimento Carb
&ensp;Modello lineare carboidrati assorbiti all'ora
:::

Toccando uno dei due menu qui sopra si apre l'editor del profilo di terapia.

<img src="./images/M-S-PS4a.png" style="zoom:75%;" />

Puoi definire i carboidrati per unità di insulina e il fattore di correzione: ricordati solo di convalidare ogni valore e di non saltare da una riga all'altra senza confermarlo. Salva quando hai finito.

<img src="./images/M-S-PS4b.png" style="zoom:75%;" />

Creerai dei blocchi per le diverse fasce orarie della giornata.  
Per creare (dividere) o eliminare un blocco, fai un tocco prolungato nella parte superiore del blocco.

  <img src="./images/M-S-PS4c.png" style="zoom:75%;" />

Toccando la barra dell'orario in cima a un blocco puoi modificarlo; la modifica si propaga anche al blocco sottostante.  
Alla fine otterrai qualcosa di simile.

<img src="./images/M-S-PS4d.png" style="zoom:75%;" />

Se necessario, puoi applicare una modifica percentuale globale a tutti i parametri con il cursore in basso.  
Ricordati di salvare.

<img src="./images/M-S-PS4e.png" style="zoom:75%;" />

### Editor Profilo Basale {#basal-profile-editor}

::: info Questa funzione è in fase di sviluppo.
Il profilo basale attuale viene importato automaticamente da NSClient quando [Accetta trattamenti](./interapp#receiving-from-nsclient) è attivato.
:::

::: xdripitem Editor Profilo Basale
&ensp;Editor grafico per profili basali del micro
:::

Puoi visualizzare e modificare il tuo profilo basale.

1. Seleziona il profilo che vuoi modificare o visualizzare
2. Esporta (non ancora funzionante)
3. Salva in locale

<img src="./images/M-S-PS4f2.png" style="zoom:78%;" />

Per modificare il profilo basale:

1.  Tocca la barra dell'ora di basale che vuoi modificare: diventerà arancione
2. Cambia il passo se necessario
3. Usa la casella con il numero positivo o la freccia verso l'alto per aumentare
4. Usa la casella con il numero negativo o la freccia verso il basso per diminuire
5. Usa set, o tocca due volte la barra, per impostare il nuovo valore

<img src="./images/M-S-PS4f3.png" style="zoom:78%;" />

### Usa momento trend {#use-trend-momentum}

Il momento del trend è indipendente dalle previsioni: è solo un'estrapolazione matematica (cioè: se la glicemia continua a seguire il suo trend, senza considerare insulina e carboidrati, dove arriverà?) dell'andamento attuale della glicemia (in salita/in discesa/stabile). Può essere usato per gli [allarmi di previsione valore basso](./alarms#forecasted-low-alert).

Il momento del trend può essere integrato nelle previsioni (consigliato).

::: xdripitem Usa momento trend
&ensp;Calcolare includendo trend glicemici
:::

Includere il trend attuale (1) può evitare variazioni brusche della previsione e può essere più vicino all'evoluzione reale (2).

<img src="./images/M-S-PS5a.png" style="zoom:75%;" />

<img src="./images/M-S-PS5b.png" style="zoom:75%;" />

<img src="./images/M-S-PS5c.png" style="zoom:75%;" />

### EULA {#eula}

Rileggi l'[EULA](../install/install#understand-what-is-xdrip) prima di usare questa funzione.

::: xdripitem Contratto di licenza con l'utente finale
&ensp;Non per uso medico - solo strumento di ricerca
:::

### Previsione di basso livello {#low-level-prediction}

Qui puoi impostare altri parametri di previsione.

::: xdripitem Valori di previsione raggiungimento LIVELLO BASSO
&ensp;Impostazioni algoritmi
:::

L'obiettivo è usato dal calcolatore del bolo. È l'obiettivo glicemico desiderato.

La [durata](https://www.diabettech.com/insulin/why-we-are-regularly-wrong-in-the-duration-of-insulin-action-dia-times-we-use-and-why-it-matters/) dell'insulina dipende dal tipo di insulina. Per applicare una modifica del valore bisogna riavviare xDrip (o il telefono).

Il valore glicemico obiettivo è quello usato per calcolare le correzioni suggerite.

::: xdripitem Obiettivo di glicemia predefinito
&ensp;100 / 5.6
:::

La durata dell'insulina è un parametro da discutere con il tuo diabetologo. Con i sistemi a loop chiuso questo valore sarà molto più alto. Ricorda comunque che le previsioni di xDrip danno il meglio con le iniezioni multiple giornaliere, non con i microinfusori.

::: xdripitem Durata insulina ore
&ensp;3
:::

I parametri del fegato sono stati introdotti per tenere conto della reazione del glicogeno epatico alle ipoglicemie, ma non sono facili da caratterizzare e vanno lasciati ai valori predefiniti.

::: xdripitem Rapporto Sensibilità Fegato di Default
&ensp;2
:::

::: xdripitem Impatto fegato massimo (0-1) - Non modificare
&ensp;0.8
:::

### Tipi multipli di insulina {#multiple-insulin-types}

::: xdripitem Tipi Multipli di Insulina
:::

Seleziona i tipi di insulina che usi.

Puoi selezionare fino a tre tipi di insulina e poi decidere quale usare per la basale e quale per il bolo.

::: xdripitem Edita Profilo della Terapia
abilitare almeno uno e massimo di tre profili  
&ensp;☐&emsp;FIASP (ultra-fast acting)  
&ensp;☐&emsp;Afrezza (ultra-fast acting)  
&ensp;☐&emsp;Apidra (ultra-fast acting)  
&ensp;☐&emsp;Novorapid (fast acting)  
&ensp;☐&emsp;Humalog (fast acting)  
&ensp;☐&emsp;Lispro (fast acting)  
&ensp;☐&emsp;Actrapid (short acting)  
&ensp;☐&emsp;Insulatard (NPH)  
&ensp;☐&emsp;Toujeo (long acting)  
&ensp;☐&emsp;Lantus (long acting)  
&ensp;☐&emsp;Levemir (long acting)  
&ensp;☐&emsp;Basaglar (long acting)  
&ensp;☐&emsp;Tresiba (ultra-long acting) 
:::

Nella parte inferiore della finestra, seleziona quale insulina verrà usata per la basale (ad azione lenta) e quale per il bolo (ad azione rapida):

::: xdripitem scegliere il profilo di basale dell’insulina.
:::

::: xdripitem scegliere il profilo di bolo di insulina. utilizzato anche per micro e penna...
:::

Al termine, salva le tue scelte.

::: xdripitem <span style="background-color: grey; color: white;"> &ensp;ANNULLA&ensp;</span> &emsp;<span style="background-color: grey; color: white;"> &ensp;RESET&ensp;</span>  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: grey; color: white;"> &ensp;SALVA&ensp;</span>  &emsp;
:::

Se aggiungi più tipi di insulina, quando usi i [trattamenti](./mainUI#treatments) ti verrà chiesto di selezionare quella che usi per quel trattamento.

<img src="./images/M-S-PS2b3.png" style="zoom:75%;" />

Puoi aggiungere l'insulina basale alla visualizzazione e integrarla nel calcolo.  
Non è consigliato, perché nella terapia multiniettiva l'insulina basale serve solo a mantenere costante la glicemia di fondo.  
Usa le [note](./mainUI#treatment-notes) per registrare le iniezioni di basale.

I diversi tipi di insulina vengono mostrati allo stesso modo sul grafico principale.

::: xdripitem Usa Attività Basale
&ensp;Tracciare l'attività basale sul grafico e incorporare nel modello predittivo
:::

<img src="./images/M-S-PS2c2.png" style="zoom:75%;" />

<br>

[*Ultima modifica 15/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
