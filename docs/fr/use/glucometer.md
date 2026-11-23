---
source_hash: ec52e7eb65
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_touch_app_grey600_48dp.png" style="width:5%;" />&ensp;Lecteurs de Glycémie
:::

<br>

##### Lecteur NFC {#nfc-meter}

Si vous utilisez un lecteur Glucomen Aero avec un téléphone équipé d'un lecteur NFC, vous pouvez le scanner pour récupérer la dernière mesure.

::: xdripitem Utiliser le lecteur NFC <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Télécharger les enregistrements de glucose à partir du lecteur NFC lorsque xDrip est ouvert
:::

##### Si vous utilisez un lecteur Bluetooth compatible {#if-you-use-a-compatible-bluetooth-meter}

Pour pouvoir activer Utiliser un lecteur Bluetooth, vous devez d'abord appairer un lecteur Bluetooth.  
S'il s'agit d'un lecteur neuf, **assurez-vous d'avoir mesuré votre glycémie au moins une fois avant d'essayer de l'appairer**.

**<u>N'activez pas</u>** encore l'option de lecteur Bluetooth dans xDrip.

::: xdripitem Utiliser un lecteur Bluetooth <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Automatiquement connecter et extraire des données d'un lecteur de glycémie compatible standard comme le Contour Next One
:::

Recherche du lecteur Bluetooth :

::: xdripitem Scanner pour trouver un lecteur Bluetooth
:::

Mettez votre lecteur en mode appairage et appuyez sur Balayage dans le menu Scanner pour trouver un lecteur Bluetooth.

<img src="./images/M-S-GMb.png" style="zoom:75%;" />

<img src="./images/M-S-GMc.png" style="zoom:75%;" />

Une fois l'appairage effectué, vous pouvez activer le lecteur dans le menu.

::: xdripitem Utiliser un lecteur Bluetooth <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Automatiquement connecter et extraire des données d'un lecteur de glycémie compatible standard comme le Contour Next One
:::

Votre lecteur s'affiche maintenant en dessous :

::: xdripitem Scanner pour trouver un lecteur Bluetooth
&ensp;Bayer HealthCare LLC AA:BB:CC:DD:EE:FF:00
:::

Vous pouvez activer des sons pour signaler la connexion, la déconnexion et la récupération des données.

::: xdripitem Indicateurs d’effets sonores
&ensp;Cocher pour jouer des effets sonores lorsque le compteur se connecte, se déconnecte ou synchronise les données
:::

xDrip peut vous proposer d'utiliser le résultat pour étalonner votre capteur connecté (s'il accepte l'étalonnage).

::: xdripitem Utiliser Meter pour les Calibrations <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Lorsqu'une nouvelle glycémie est reçue, demander si elle doit être utilisée pour calibrer
:::

Il n'est pas recommandé d'activer l'étalonnage automatique.

::: xdripitem Calibration automatique <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Calibrer en utilisant de nouvelles lectures de glycémie si les conditions semblent correctes sans demander confirmation (expérimental)
:::

Lorsque vous activez l'utilisation du lecteur Bluetooth, toutes les glycémies capillaires sont automatiquement transférées dans xDrip en tant que [traitements](./mainUI#treatments).

<br>

[*Dernière modification le 4/5/2022*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2022.05.04)
