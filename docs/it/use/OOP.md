---
source_hash: bb1a1f1faf
source_commit: 7a18e7c
---
Gli algoritmi Out of process sono app esterne che si occupano di un'elaborazione dei dati non fornita direttamente da xDrip.

Oggi sono usati solo per i sensori Libre e i bridge.

Esistono due famiglie di algoritmi Out Of Process (OOP):

### OOP1 {#oop1}

<img src="./images/OOP_1.png" style="zoom:75%;" />

::: warning SOLO versioni di Android vecchie
La versione massima di Android supportata è la 9.  
È stato segnalato che alcuni telefoni con Android 10 e successivi funzionano con OOP1new/OOP1us.
:::

| Versione OOP                                | Data versione | Sensori supportati       | Dimensione file |
| ------------------------------------------- | ------------- | ------------------------ | --------------- |
| OOP1 (2bb9458)                              | 2018-08-26    | Libre                    | 17.1MB          |
| OOP1new (fa218ef)                           | 2019-11-22    | Libre, Libre 2 EU        | 25.3MB          |
| OOP1us (e901151) - **non usare: usa OOP2**  | 2019-09-13    | Libre 14 days US (vecchio) | 27.8MB        |

OOP1 fornisce letture simili a quelle del lettore del produttore, senza calibrazione. Ti serve un [bridge compatibile](../install/libreBT), se ne usi uno. OOP1 si applica anche ai risultati delle scansioni NFC.

::: warning Nessuna calibrazione possibile
Con OOP1 le calibrazioni vengono ignorate.  
È una funzione di sicurezza, perché xDrip non può verificare la plausibilità dei dati forniti da OOP1.
:::

Sono disponibili due versioni: [Libre 1 e Libre 2 EU](https://drive.google.com/open?id=13ERWcSVSFMLy9rhpbv5rArFrnDuAzriM) oppure [Libre 14 Days US](https://drive.google.com/open?id=172whZZYTyE_ZEuN0T-zhdMKhucy6jP-a). 
*Nota: devi aver effettuato l'accesso al tuo account Google per aprire i link qui sopra*

Quando usi OOP1, l'algoritmo Out Of Process deve essere [attivato](./misc#out-of-process-algorithm).

### OOP2 {#oop2}

<img src="./images/OOP_2.png" style="zoom:75%;" />

OOP2 fornisce la decodifica per i sensori Libre 14 days US e Libre 2 EU, sia in connessione diretta (solo Libre 2 EU) sia tramite un [bridge compatibile](../install/libreBT).

::: info La calibrazione è facoltativa
Puoi calibrare a partire dai dati grezzi, non calibrare oppure aggiungere una calibrazione ai dati nativi.  
Consulta le [impostazioni OOP2](./misc#oop2).
:::

**Usa solo l'app OOP2 più recente con la versione più recente di xDrip.**

**<u><big>[→ Scarica qui l'ultima OOP2. ←](https://drive.google.com/file/d/1106h2s12b3Ev9gKCTU2G75q8h9ChHjcz/view?usp=sharing)</big></u>**

*Nota: devi aver effettuato l'accesso al tuo account Google per aprire il link qui sopra.* 

::: warning Attenzione
Quando usi OOP2, *Out Of process Libre Algorithm* (OOP1) deve essere [disattivato in xDrip](./misc#out-of-process-algorithm).
:::

| Versione OOP                         | Data versione  | Sensori supportati                                 | Dimensione file |
| ------------------------------------ | -------------- | -------------------------------------------------- | --------------- |
| OOP2 (70129ac) - **non usare**       | 2021-12-04     | Libre 2 EU                                         | 2.63MB          |
| OOP2new (93e5cac) - **non usare**    | 2020-12-08     | Libre 14 days US, Libre 2 EU                       | 2.65MB          |
| OOP2 1.2 (8a0ee8f) - **non usare**   | 2022-06-10     | Libre 14 days US (vecchio), Libre 2 EU             | 2.66MB          |
| OOP2_e6 (6de6678) - **non usare**    | 2023-01-10     | Libre 14 days US (nuovo), Libre 2 EU               | 2.66MB          |
| OOP2_more (27da3f5)                  | 2023-05-25     | Libre 14 days US (nuovo), Libre 2 EU (nuovo)       | 2.66MB          |
| OOP2_c6_09_31 (27da3f5)              | 2024-05-31     | Libre 14 days US, Libre 2/2+ EU                    | 2.7MB           |
| OOP2-7f0e31 (27da3f5)                | 2025-06-12     | Libre 14 days US, Libre 2/2+ EU                    | 2.73MB          |
| **OOP2-21_9_25 (05d1989)**           | **2025-09-21** | **Libre 14 days US, Libre 2/2+ EU**                | **2.73MB**      |

### Rilevamento automatico {#auto-detection}

Alcune versioni più vecchie di xDrip rilevano la presenza o la necessità dell'algoritmo out of process.

Attivalo <u>solo</u> per OOP1.  
**Non attivarlo per OOP2**. Se l'hai attivato per errore, [disattiva](./misc#out-of-process-algorithm) OOP1.

<img src="./images/OOP_AD.png" style="zoom:75%;" />

### Impostazioni {#settings}

Use service corrisponde ad accendere o spegnere l'app OOP. Se vuoi usarla, deve essere attivato.

<img src="./images/OOP_UI1.png" style="zoom:75%;" />

Foreground service è un'aggiunta che riduce la probabilità che il telefono metta l'app in sospensione. Non impedisce però a Google Play Protect di fermarla.  
Attivalo se hai perdite di dati (**consigliato**).

<img src="./images/OOP_UI2.png" style="zoom:75%;" />

Direct intent può essere attivato se il tuo smartwatch Wear OS autonomo lo richiede (serve un bridge).

<img src="./images/OOP_UI4.png" style="zoom:75%;" />

Puoi selezionare l'intervallo con cui OOP verifica di essere disponibile.  
Se hai perdite di dati puoi ridurre l'intervallo. Più breve è l'intervallo, maggiore sarà il consumo di batteria.

<img src="./images/OOP_UI3.png" style="zoom:75%;" />

<br>

[*Ultima modifica 15/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
