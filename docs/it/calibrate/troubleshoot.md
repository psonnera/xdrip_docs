---
source_hash: 54556a9422
source_commit: 7a18e7c
---
### Algoritmo nativo {#native-algorithm}

Se usi xDrip con l'algoritmo nativo di un G6, G7, 1, 1+ o Stelo, vedi [qui](https://navid200.github.io/xDrip/docs/Dexcom_page.html).

### Algoritmo di xDrip {#xdrip-algorithm}

Attiva le [tabelle dati](../use/lesscommon#show-data-tables) per avere più informazioni.

#### Nessun dato dopo la calibrazione iniziale {#no-data-after-initial-calibration}

<img src="./images/CAL16.png" style="zoom:75%;"  />

Se hai verificato di avere la connessione con il sensore/bridge e dopo la calibrazione iniziale non compare alcun dato, potrebbe essere perché stai calibrando troppo in alto e l'intercetta calcolata supera il limite di sicurezza. [Azzera](./calibrate#reset-all-calibrations) tutte le calibrazioni e riprova con glicemia stabile nella parte bassa dell'intervallo.

#### Nessun dato dopo aver aggiunto una nuova calibrazione {#no-data-after-adding-a-new-calibration}

<img src="./images/CAL18.png" style="zoom:75%;"  />

Probabilmente hai portato le calibrazioni oltre i limiti di sicurezza. Controlla la Tabella dati di calibrazione e, se necessario, [disattiva](./calibrate#disable-a-calibration) la calibrazione responsabile.

Un sensore che richiede un'intercetta positiva elevata potrebbe non essere sicuro. Se ritieni che il sensore sia ancora affidabile, [azzera](./calibrate#reset-all-calibrations) tutte le calibrazioni e riprova con glicemia stabile nella parte bassa dell'intervallo.

#### La nuova calibrazione viene ignorata {#new-calibration-is-ignored}

<img src="./images/CAL19.png" style="zoom:75%;"  />

Controlla la Tabella dati di calibrazione: molto probabilmente vedrai le tue calibrazioni in rosso, perché sono disattivate per ragioni di sicurezza.

Molto probabilmente il sensore non è più affidabile. Se ritieni che lo sia, [azzera](./calibrate#reset-all-calibrations) tutte le calibrazioni e riprova con glicemia stabile nella parte bassa dell'intervallo.

#### Intercetta o pendenza oltre il limite di sicurezza {#intercept-or-slope-above-safety-limit}

::: warning Sicurezza
I limiti che ti impediscono di calibrare sono pensati per la tua sicurezza.  
**Non puoi fare affidamento su un sistema che non è in grado di rilevare l'ipoglicemia.**
:::

Apri la Tabella dati di calibrazione e controlla l'ultima calibrazione.

<img src="./images/CAL17.png" style="zoom:75%;"  />

::: warning L'intercetta massima consentita è 39
Un'intercetta superiore a 39 mg/dl impedisce la visualizzazione della glicemia per ragioni di sicurezza.
:::

I limiti di pendenza dipendono dal sensore:

| Sensore                                    | Pendenza minima | Pendenza massima |
| ------------------------------------------ | ------------- | ------------- |
| G5 o G6 con algoritmo non nativo (3 o più calibrazioni) | 0,7           | 1,6           |
| G5 o G6 con algoritmo non nativo (esattamente 2 calibrazioni) | 0,75          | 1,5           |
| Libre (sorgente di dati grezzi, Calibrazione non linear per Libre attivata) | 0,5           | 1,6           |
| Libre (sorgente di dati grezzi, pendenza fissa predefinita) | 1 (fissa)     | 1 (fissa)     |
| Libre 2 app modificata                       | 1 (fissa)     | 1 (fissa)     |

Poiché i limiti di sicurezza di pendenza e intercetta impediscono a xDrip di avere un'intercetta troppo alta, le calibrazioni che porterebbero a questa situazione vengono ignorate.

Nell'esempio qui sotto vedi che la linea arancione è quella che meglio corrisponde alle calibrazioni; tuttavia, per sicurezza xDrip userà quella rossa, perché la sua intercetta è sicura. Puoi vedere il valore dell'intercetta del plugin, che rispecchia ciò che corrisponderebbe meglio alle calibrazioni.

<img src="./images/CAL20.png" style="zoom:75%;"  />

<br>

[*Ultima modifica 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)