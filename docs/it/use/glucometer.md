---
source_hash: ec52e7eb65
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_touch_app_grey600_48dp.png" style="width:5%;" />&ensp;Glucometri
:::

<br>

##### Glucometro NFC {#nfc-meter}

Se usi un glucometro Glucomen Aero con un telefono dotato di lettore NFC, puoi scansionarlo per ottenere l'ultima lettura.

::: xdripitem Usa Glucometro NFC <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Scarica le letture dal glucometro NFC quando xDrip è aperto
:::

##### Se usi un glucometro Bluetooth compatibile {#if-you-use-a-compatible-bluetooth-meter}

Per attivare Usa un glucometro Bluetooth devi prima associare un glucometro Bluetooth.  
Se il glucometro è nuovo, **assicurati di aver misurato la glicemia almeno una volta prima di provare ad associarlo**.

**<u>Non</u>** attivare per ora l'opzione del glucometro Bluetooth in xDrip.

::: xdripitem Usa un glucometro Bluetooth <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Connettersi e caricare automaticamente i dati da un glucometro compatibile come il Contour Next One
:::

Cerca il glucometro Bluetooth:

::: xdripitem Scansiona il glucometro Bluetooth
:::

Metti il glucometro in modalità di associazione e tocca scansiona nel menu Scansiona il glucometro Bluetooth.

<img src="./images/M-S-GMb.png" style="zoom:75%;" />

<img src="./images/M-S-GMc.png" style="zoom:75%;" />

Una volta associato, puoi attivare il glucometro nel menu.

::: xdripitem Usa un glucometro Bluetooth <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Connettersi e caricare automaticamente i dati da un glucometro compatibile come il Contour Next One
:::

Il tuo glucometro verrà ora mostrato qui sotto:

::: xdripitem Scansiona il glucometro Bluetooth
&ensp;Bayer HealthCare LLC AA:BB:CC:DD:EE:FF:00
:::

Puoi attivare dei suoni che indicano connessione, disconnessione e raccolta dei dati.

::: xdripitem Indicatori sonori
&ensp;Abilita questa opzione per avere avvisi sonori quando il glucometro si connette, disconnette o sincronizza i dati
:::

Puoi far sì che xDrip ti proponga di usare il risultato per calibrare il sensore connesso (se supporta la calibrazione).

::: xdripitem Usa il glucometro per calibrare <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Quando viene ricevuta una nuova misura capillare chiedi se deve essere utilizzata per calibrare
:::

Non è consigliato attivare la calibrazione automatica.

::: xdripitem Calibrazione automatica <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Calibra automaticamente utilizzando le letture di glicemia se le condizioni sembrano giuste, senza chiedere conferma (sperimentale)
:::

Quando attivi l'uso del glucometro Bluetooth, tutte le misure capillari verranno trasferite automaticamente in xDrip come [trattamenti](./mainUI#treatments).

<br>

[*Ultima modifica 4/5/2022*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2022.05.04)
