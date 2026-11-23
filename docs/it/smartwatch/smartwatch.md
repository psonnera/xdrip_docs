---
source_hash: 3b41debaf8
source_commit: 7a18e7c
---

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_watch_grey600_48dp.png" style="width:5%;" />&ensp;Caratteristiche Collegamenti Smart Watch
:::

## Integrazione diretta in xDrip {#xdrip-direct-integration}

xDrip supporta un'ampia gamma di smartwatch.

### [Integrazione Android Wear](./wear) {#android-wear-integration}

::: xdripitem Integrazione Android Wear
:::

L'integrazione più completa la trovi sugli orologi Wear OS, perché eseguono localmente una parte dell'app xDrip.

L'estensione wear di xDrip non è più in sviluppo.

Se ti servono altri quadranti o personalizzazioni puoi usare [Tasker](https://github.com/FreDiabetics/xDrip--Tasker-Tizen-Watchface-Integration/blob/master/README.md) (ma non come collector autonomo).

### [Integrazione Pebble](./pebble) {#pebble-integration}

::: xdripitem Integrazione Pebble
:::

L'uso dello smartwatch Pebble è una tappa storica di CGM in the Cloud. Gli orologi Pebble originali sono stati dismessi nel 2016, quando Pebble è stata acquistata da Fitbit (le sue risorse sono state spostate negli archivi e su [rebble.io](https://rebble.io/)). Nel 2025 sono stati rilanciati nuovi modelli Pebble: xDrip li supporta entrambi, vedi [Integrazione Pebble](./pebble).

### [Servizio di sincronizzazione AmazFit](https://crazyinfo.de/2018/07/25/xdrip-smartwatch-widget-fuer-amazfit-pace-stratos/) {#amazfit-sync-service}

::: xdripitem Servizio di sincronizzazione AmazFit
:::

AmazFit era usato solo per i modelli Pace e Stratos.  
**Non puoi usare questa funzione con altri orologi AmazFit.**

### [BlueJay Watch](./bluejay) {#bluejay-watch}

::: xdripitem BlueJay Watch
:::

BlueJay è un compagno straordinario per il tuo sensore Dexcom, con o senza xDrip, con o senza telefono.

### [Lefun Band](https://www.lefunsmart.com/collections/smartwatches) {#lefun-band}

::: xdripitem Lefun Band
:::

L'integrazione della LeFun band è stata una prima implementazione per smartband, da usare preferibilmente in mmol/l.  
A meno che tu non abbia ancora una band LeFun W3, F3, F3S, F11 o F12, oggi non è più di alcuna utilità.

### [MiBand](./miband) {#miband}

::: xdripitem MiBand
:::

L'integrazione MiBand è il risultato dell'enorme lavoro di [Artem](https://bigdigital.home.blog/).  
Molti smartwatch e smartband sono ora supportati tramite l'app compagno WatchDrip+.

:::: info Disattiva MiBand in xDrip se usi WatchDrip+
::: xdripitem Usa MiBand <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::
::::

## Sensori dello smartwatch {#smartwatch-sensors}

xDrip può usare i sensori degli smartwatch supportati.

::: xdripitem Usa dati sensori di salute <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

xDrip può chiedere l'attivazione del sensore del battito cardiaco e puoi rendere più uniforme quel grafico.

::: xdripitem Cardiofrequenzimetro <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

Quando disponibili, puoi far raccogliere a xDrip dati sulla salute come frequenza cardiaca e passi.

Nella schermata principale compariranno due icone aggiuntive e, se attivate, le relative rappresentazioni grafiche:

1.  Un grafico blu scuro per la frequenza cardiaca
2. Una linea a nuvola azzurro chiaro per i passi

<img src="./images/M-S-SW8c.png" style="zoom:75%;" />

## Altri smartwatch {#other-smartwatches}

Altri smartwatch e dispositivi possono ricevere dati da xDrip anche se non sono integrati direttamente nell'app.

::: info
Perché xDrip invii i dati devi attivare il [web service](../use/interapp#web-service) di xDrip.
:::

### Android Wear {#android-wear}

[GlucoDataHandler](https://github.com/pachi81/GlucoDataHandler) accetta xDrip come sorgente dati. L'app è disponibile nel [Google Play store](https://play.google.com/store/apps/details?id=de.michelinside.glucodatahandler).

### Android Auto {#android-auto}

[GlucoDataAuto](https://github.com/pachi81/GlucoDataAuto) è l'estensione Android Auto di GlucoDataHandler.

### Fitbit {#fitbit}

::: warning Google sta dismettendo Sense/Ionic/Versa
Tieni presente che questi prodotti arriveranno a fine vita nel prossimo futuro.
:::

::: warning Non disponibile per gli utenti UE
Google ha [rimosso](https://support.google.com/fitbit/answer/14237121?hl=en) questa possibilità da giugno 2024. I quadranti già installati non sono interessati, ma i nuovi utenti non possono più installare quadranti personalizzati. Come soluzione alternativa devi usare una VPN.
:::

::: warning Android 9 e precedenti
Gli utenti Android con una versione inferiore alla 10 devono riportare l'app Fitbit a una versione precedente, come la 3.58, e disattivare gli aggiornamenti automatici. La trovi su [Aptoide](https://fitbit.en.aptoide.com/versions) e su altri server che ospitano apk.
:::

##### [Glance](https://gallery.fitbit.com/details/7b5d9822-7e8e-41f9-a2a7-e823548c001c) {#glance}

Ionic/Sense/Versa/Versa 2/Versa 3/Versa 4/Versa Lite

[Sito web](https://glancewatchface.com/)

##### [Sentinel](https://gallery.fitbit.com/developer/b50ac7f5-b932-441a-be18-e258b17c736b) {#sentinel}

Sentinel Elite per Sense/Versa 3  
Sentinel Pro per Ionic/Versa/Versa 2/Versa Lite

Gruppo Facebook: [Sentinel](https://www.facebook.com/groups/3185325128159614)

##### [Marclock](https://gallery.fitbit.com/details/9eacf714-5b23-40c8-9621-ded74bd9edf9) {#marclock}

Ionic/Sense/Versa/Versa 2/Versa Lite

[Istruzioni](https://github.com/cramis1/Marclock-with-CGM-weather/blob/master/README.md)

##### [Analog CGM](https://gallery.fitbit.com/details/4d7b46b1-aaba-49b4-aa10-183321014dd3) {#analog-cgm}

##### [Orbits NS](https://gallery.fitbit.com/details/44de5c81-b77c-4f90-baa8-38f3e3d28695) {#orbits-ns}

##### [Radial CGM](https://gallery.fitbit.com/details/0173730e-5381-4495-bc6e-6ec93c8df029) {#radial-cgm}

Ionic/Versa/Versa 2/Versa Lite/Versa 3/Sense

### Samsung Gear {#samsung-gear}

[G-Watch](https://play.google.com/store/apps/details?id=sk.trupici.g_watch) è il modo più semplice per farlo. Vedi la [wiki](https://github.com/trupici/G-Watch-Wear/wiki).

Puoi anche usare [Tasker](https://github.com/FreDiabetics/xDrip--Tasker-Tizen-Watchface-Integration/blob/master/README.md) per mostrare i dati di xDrip sul tuo orologio Samsung Gear.

### Garmin {#garmin}

Sono disponibili molti quadranti Garmin: verifica che il tuo modello sia supportato.

Di [Horsetooth](https://apps.garmin.com/en-US/developer/e985e9ec-bcf6-4aef-bfe9-77c1c93fc854/apps)

Di [andreas-may](https://apps.garmin.com/en-US/developer/f9420c47-810f-47ac-a7dd-9fa7b8ecd22d/apps)

Di [John_](https://apps.garmin.com/en-US/developer/b2d30711-2708-4f3a-8e83-009c16d07081/apps)

Di [Roboleo1010](https://apps.garmin.com/en-US/developer/b61690c3-5e5c-4c4e-afe9-434db16542a9/apps)

<br>

[*Ultima modifica 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
