---
source_hash: 3b41debaf8
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_watch_grey600_48dp.png" style="width:5%;" />&ensp;Options montre intelligente
:::

## Intégration directe dans xDrip {#xdrip-direct-integration}

xDrip prend en charge une large gamme de montres connectées.

### [Intégration Wear OS](./wear) {#android-wear-integration}

::: xdripitem Intégration Wear OS
:::

C'est avec les montres Wear OS que l'intégration est la plus complète, car elles exécutent localement une partie de l'application xDrip.

L'extension Wear de xDrip n'est plus développée.

Si vous avez besoin de plus de cadrans ou de personnalisations, vous pouvez utiliser [Tasker](https://github.com/FreDiabetics/xDrip--Tasker-Tizen-Watchface-Integration/blob/master/README.md) (mais pas comme collecteur autonome).

### [Intégration Pebble](./pebble) {#pebble-integration}

::: xdripitem Intégration Pebble
:::

L'utilisation de la montre Pebble est une étape historique du CGM dans le Cloud. Pebble a été rachetée par Fitbit en 2016 et ses ressources ont été déplacées vers des archives et vers [rebble.io](https://rebble.io/).

Vous devez télécharger l'application de la montre depuis [APKMirror](https://www.apkmirror.com/apk/pebble-technology-corp/pebble/pebble-4-4-2-1405-62d45d7d7-endframe-release/pebble-4-4-2-1405-62d45d7d7-endframe-android-apk-download/).

### [Service de synchronisation AmazFit](https://crazyinfo.de/2018/07/25/xdrip-smartwatch-widget-fuer-amazfit-pace-stratos/) {#amazfit-sync-service}

::: xdripitem Service de synchronisation AmazFit
:::

AmazFit n'était utilisé que pour les modèles Pace et Stratos.  
**Vous ne pouvez pas utiliser cette fonction avec d'autres montres AmazFit.**

### [BlueJay Watch](./bluejay) {#bluejay-watch}

::: xdripitem BlueJay Watch
:::

BlueJay est un formidable compagnon pour votre capteur Dexcom, avec ou sans xDrip, avec ou sans téléphone.

### [Bracelet Lefun](https://www.lefunsmart.com/collections/smartwatches) {#lefun-band}

::: xdripitem Bracelet Lefun
:::

L'intégration du bracelet LeFun a été l'une des premières pour les bracelets connectés ; elle s'utilise de préférence en mmol/l.  
À moins que vous ne possédiez encore un bracelet LeFun W3, F3, F3S, F11 ou F12, elle n'a plus aucune utilité aujourd'hui.

### [MiBand](./miband) {#miband}

::: xdripitem MiBand
:::

L'intégration MiBand est le fruit de l'énorme travail d'[Artem](https://bigdigital.home.blog/).  
De nombreuses montres et bracelets connectés sont désormais pris en charge grâce à l'application compagnon WatchDrip+.

:::: info Désactivez MiBand dans xDrip si vous utilisez WatchDrip+
::: xdripitem Use MiBand <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::
::::

## Capteurs des montres connectées {#smartwatch-sensors}

xDrip peut utiliser les capteurs des montres connectées compatibles.

::: xdripitem Utiliser les données de santé <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

xDrip peut demander l'activation du capteur de fréquence cardiaque, et vous pouvez lisser ce graphique.

::: xdripitem Capteur de fréquence cardiaque <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

Lorsque c'est possible, vous pouvez laisser xDrip collecter des données de santé comme la fréquence cardiaque et les pas.

Deux icônes supplémentaires apparaîtront sur l'écran principal et, si elles sont activées, des représentations graphiques :

1.  Un graphique bleu foncé pour la fréquence cardiaque
2. Une ligne en nuage cyan clair pour les pas

<img src="./images/M-S-SW8c.png" style="zoom:75%;" />

## Autres montres connectées {#other-smartwatches}

D'autres montres et appareils peuvent recevoir les données de xDrip même s'ils ne sont pas directement intégrés à l'application.

::: info
Pour que xDrip envoie les données, vous devez activer le [service web](../use/interapp#web-service) de xDrip.
:::

### Android Wear {#android-wear}

[GlucoDataHandler](https://github.com/pachi81/GlucoDataHandler) accepte xDrip comme source de données. L'application est disponible sur le [Google Play Store](https://play.google.com/store/apps/details?id=de.michelinside.glucodatahandler).

### Android Auto {#android-auto}

[GlucoDataAuto](https://github.com/pachi81/GlucoDataAuto) est l'extension Android Auto de GlucoDataHandler.

### Fitbit {#fitbit}

::: warning Google arrête Sense/Ionic/Versa
Tenez compte du fait que ces produits arriveront en fin de vie dans un avenir proche.
:::

::: warning Indisponible pour les utilisateurs de l'UE
Google a [supprimé](https://support.google.com/fitbit/answer/14237121?hl=en) cette possibilité depuis juin 2024. Les cadrans déjà installés ne sont pas concernés, mais les nouveaux utilisateurs ne peuvent plus installer de cadrans personnalisés. Vous devez utiliser un VPN pour contourner le problème.
:::

::: warning Android 9 et versions antérieures
Les utilisateurs d'Android dans une version inférieure à 10 doivent rétrograder l'application Fitbit vers une version précédente, comme la 3.58, et désactiver les mises à jour automatiques. Vous la trouverez sur [Aptoide](https://fitbit.en.aptoide.com/versions) et d'autres serveurs d'hébergement d'apk.
:::

##### [Glance](https://gallery.fitbit.com/details/7b5d9822-7e8e-41f9-a2a7-e823548c001c) {#glance}

Ionic/Sense/Versa/Versa 2/Versa 3/Versa 4/Versa Lite

[Site web](https://glancewatchface.com/)

##### [Sentinel](https://gallery.fitbit.com/developer/b50ac7f5-b932-441a-be18-e258b17c736b) {#sentinel}

Sentinel Elite pour Sense/Versa 3  
Sentinel Pro pour Ionic/Versa/Versa 2/Versa Lite

Groupe Facebook : [Sentinel](https://www.facebook.com/groups/3185325128159614)

##### [Marclock](https://gallery.fitbit.com/details/9eacf714-5b23-40c8-9621-ded74bd9edf9) {#marclock}

Ionic/Sense/Versa/Versa 2/Versa Lite

[Instructions](https://github.com/cramis1/Marclock-with-CGM-weather/blob/master/README.md)

##### [Analog CGM](https://gallery.fitbit.com/details/4d7b46b1-aaba-49b4-aa10-183321014dd3) {#analog-cgm}

##### [Orbits NS](https://gallery.fitbit.com/details/44de5c81-b77c-4f90-baa8-38f3e3d28695) {#orbits-ns}

##### [Radial CGM](https://gallery.fitbit.com/details/0173730e-5381-4495-bc6e-6ec93c8df029) {#radial-cgm}

Ionic/Versa/Versa 2/Versa Lite/Versa 3/Sense

### Samsung Gear {#samsung-gear}

[G-Watch](https://play.google.com/store/apps/details?id=sk.trupici.g_watch) est le moyen le plus simple d'y parvenir. Consultez le [wiki](https://github.com/trupici/G-Watch-Wear/wiki).

Vous pouvez aussi utiliser [Tasker](https://github.com/FreDiabetics/xDrip--Tasker-Tizen-Watchface-Integration/blob/master/README.md) pour afficher les données de xDrip sur votre montre Samsung Gear.

### Garmin {#garmin}

De nombreux cadrans Garmin sont disponibles ; vérifiez que votre modèle est pris en charge.

Par [Horsetooth](https://apps.garmin.com/en-US/developer/e985e9ec-bcf6-4aef-bfe9-77c1c93fc854/apps)

Par [andreas-may](https://apps.garmin.com/en-US/developer/f9420c47-810f-47ac-a7dd-9fa7b8ecd22d/apps)

Par [John_](https://apps.garmin.com/en-US/developer/b2d30711-2708-4f3a-8e83-009c16d07081/apps)

Par [Roboleo1010](https://apps.garmin.com/en-US/developer/b61690c3-5e5c-4c4e-afe9-434db16542a9/apps)

<br>

[*Dernière modification le 8/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
